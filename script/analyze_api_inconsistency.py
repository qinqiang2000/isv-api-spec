#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
分析Apifox API规范文件中字段的不一致性
"""

import json
from collections import defaultdict
from typing import Dict, List, Set, Tuple, Optional
import re

class FieldInfo:
    """字段信息"""
    def __init__(self, key: str, title: str, field_type: str, enum: List = None,
                 location: str = "", format_str: str = "", description: str = ""):
        self.key = key
        self.title = title
        self.field_type = field_type
        self.enum = enum or []
        self.location = location
        self.format_str = format_str
        self.description = description

    def get_format_description(self) -> str:
        """获取格式描述（类型+format+枚举）"""
        # 处理field_type可能是list或str的情况
        if isinstance(self.field_type, list):
            type_str = ','.join(self.field_type)
        else:
            type_str = str(self.field_type)

        parts = [type_str]
        if self.format_str:
            parts.append(f"format:{self.format_str}")
        if self.enum:
            enum_str = ', '.join([str(e) for e in self.enum[:3]])
            if len(self.enum) > 3:
                enum_str += f'... (共{len(self.enum)}个)'
            parts.append(f"enum:[{enum_str}]")
        return ' | '.join(parts)

class APIAnalyzer:
    def __init__(self, json_file: str):
        self.json_file = json_file
        self.fields_by_title = defaultdict(list)  # title -> [FieldInfo]
        self.schema_definitions = {}  # ref_id -> schema_object
        self.data = None

    def load_json(self) -> dict:
        """加载JSON文件"""
        with open(self.json_file, 'r', encoding='utf-8') as f:
            return json.load(f)

    def load_schema_definitions(self):
        """加载所有schema定义到字典中"""
        if 'schemaCollection' not in self.data:
            return

        def traverse_schemas(items):
            for item in items:
                if isinstance(item, dict):
                    # 如果有schema定义
                    if 'id' in item and 'schema' in item and isinstance(item['id'], str) and item['id'].startswith('#/definitions/'):
                        self.schema_definitions[item['id']] = item['schema']

                    # 递归处理子项
                    if 'items' in item:
                        traverse_schemas(item['items'])

        for collection in self.data['schemaCollection']:
            if 'items' in collection:
                traverse_schemas(collection['items'])

        print(f"  加载了 {len(self.schema_definitions)} 个schema定义")

    def resolve_ref(self, ref_str: str) -> Optional[dict]:
        """解析$ref引用"""
        if ref_str in self.schema_definitions:
            return self.schema_definitions[ref_str]
        return None

    def extract_fields_from_schema(self, schema: dict, location: str, visited: Set[str] = None):
        """从schema中提取字段信息"""
        if not isinstance(schema, dict):
            return

        if visited is None:
            visited = set()

        # 处理$ref引用
        if '$ref' in schema:
            ref = schema['$ref']
            if ref in visited:
                return  # 避免循环引用
            visited.add(ref)

            resolved = self.resolve_ref(ref)
            if resolved:
                # 查找jsonSchema
                if 'jsonSchema' in resolved:
                    self.extract_fields_from_schema(resolved['jsonSchema'], location, visited)
                else:
                    self.extract_fields_from_schema(resolved, location, visited)
            return

        # 处理jsonSchema包装
        if 'jsonSchema' in schema:
            self.extract_fields_from_schema(schema['jsonSchema'], location, visited)
            return

        # 处理x-apifox-refs（Apifox特有的引用格式）
        if 'x-apifox-refs' in schema and 'properties' in schema:
            refs = schema['x-apifox-refs']
            for key, ref_info in refs.items():
                if '$ref' in ref_info:
                    ref = ref_info['$ref']
                    if ref not in visited:
                        visited.add(ref)
                        resolved = self.resolve_ref(ref)
                        if resolved and 'jsonSchema' in resolved:
                            self.extract_fields_from_schema(
                                resolved['jsonSchema'],
                                location,
                                visited
                            )

        # 处理properties
        if 'properties' in schema:
            for key, prop in schema['properties'].items():
                if isinstance(prop, dict):
                    # 处理$ref
                    if '$ref' in prop:
                        ref = prop['$ref']
                        if ref not in visited:
                            visited.add(ref)
                            resolved = self.resolve_ref(ref)
                            if resolved and 'jsonSchema' in resolved:
                                self.extract_fields_from_schema(
                                    resolved['jsonSchema'],
                                    f"{location}.{key}",
                                    visited
                                )
                        continue

                    title = prop.get('title', prop.get('description', ''))
                    field_type = prop.get('type', 'unknown')
                    enum = prop.get('enum', [])
                    format_str = prop.get('format', '')
                    description = prop.get('description', '')

                    if title:  # 只记录有title的字段
                        field_info = FieldInfo(
                            key=key,
                            title=title,
                            field_type=field_type,
                            enum=enum,
                            location=location,
                            format_str=format_str,
                            description=description
                        )
                        self.fields_by_title[title].append(field_info)

                    # 递归处理嵌套对象
                    if field_type == 'object' and 'properties' in prop:
                        self.extract_fields_from_schema(prop, f"{location}.{key}", visited)
                    elif field_type == 'array' and 'items' in prop:
                        self.extract_fields_from_schema(prop['items'], f"{location}.{key}[]", visited)

        # 处理items（数组类型）
        if 'items' in schema and isinstance(schema['items'], dict):
            self.extract_fields_from_schema(schema['items'], location, visited)

        # 处理allOf, anyOf, oneOf
        for combine_key in ['allOf', 'anyOf', 'oneOf']:
            if combine_key in schema and isinstance(schema[combine_key], list):
                for sub_schema in schema[combine_key]:
                    self.extract_fields_from_schema(sub_schema, location, visited)

    def extract_fields_from_api(self, api: dict, api_path: str):
        """从API定义中提取字段"""
        # 处理请求参数（parameters是dict，包含header, query, path等）
        if 'parameters' in api and isinstance(api['parameters'], dict):
            for param_type, params in api['parameters'].items():
                if isinstance(params, list):
                    for param in params:
                        if isinstance(param, dict):
                            name = param.get('name', '')
                            description = param.get('description', '')
                            # title可能在description或title字段中
                            title = description or param.get('title', '')

                            # 获取类型信息
                            field_type = param.get('type', 'unknown')
                            if 'schema' in param and isinstance(param['schema'], dict):
                                field_type = param['schema'].get('type', field_type)

                            enum = param.get('enum', [])
                            if 'schema' in param and isinstance(param['schema'], dict):
                                enum = param['schema'].get('enum', enum)

                            format_str = param.get('format', '')
                            if 'schema' in param and isinstance(param['schema'], dict):
                                format_str = param['schema'].get('format', format_str)

                            if title:
                                field_info = FieldInfo(
                                    key=name,
                                    title=title,
                                    field_type=field_type,
                                    enum=enum,
                                    location=f"{api_path}[{param_type}]",
                                    format_str=format_str,
                                    description=description
                                )
                                self.fields_by_title[title].append(field_info)

        # 处理请求体
        if 'requestBody' in api:
            request_body = api['requestBody']
            if 'jsonSchema' in request_body:
                self.extract_fields_from_schema(
                    request_body['jsonSchema'],
                    f"{api_path}[request]"
                )

        # 处理响应
        if 'responses' in api and isinstance(api['responses'], list):
            for response in api['responses']:
                if isinstance(response, dict):
                    status = response.get('code', response.get('name', 'unknown'))
                    if 'jsonSchema' in response:
                        self.extract_fields_from_schema(
                            response['jsonSchema'],
                            f"{api_path}[response:{status}]"
                        )

    def traverse_api_collection(self, items: list, parent_path: str = ""):
        """遍历API集合"""
        for item in items:
            if not isinstance(item, dict):
                continue

            name = item.get('name', 'unnamed')
            current_path = f"{parent_path}/{name}" if parent_path else name

            # 如果是文件夹，递归处理
            if 'items' in item and 'api' not in item:
                self.traverse_api_collection(item['items'], current_path)

            # 如果是API，提取字段
            if 'api' in item:
                api = item['api']
                method = api.get('method', 'GET').upper()
                path = api.get('path', '')
                api_path = f"{method} {path}"
                self.extract_fields_from_api(api, api_path)

    def analyze(self):
        """执行分析"""
        print("正在加载JSON文件...")
        self.data = self.load_json()

        print("正在加载schema定义...")
        self.load_schema_definitions()

        print("正在提取字段信息...")
        # 遍历API集合
        if 'apiCollection' in self.data:
            self.traverse_api_collection(self.data['apiCollection'])

        # 遍历schemaCollection中的所有schema
        if 'schemaCollection' in self.data:
            def extract_from_schema_items(items, path="Schema"):
                for item in items:
                    if isinstance(item, dict):
                        name = item.get('name', 'unnamed')
                        if 'schema' in item:
                            schema_path = f"{path}/{name}"
                            if 'jsonSchema' in item['schema']:
                                self.extract_fields_from_schema(
                                    item['schema']['jsonSchema'],
                                    schema_path
                                )
                        if 'items' in item:
                            extract_from_schema_items(item['items'], f"{path}/{name}")

            for collection in self.data['schemaCollection']:
                if 'items' in collection:
                    extract_from_schema_items(collection['items'])

        print(f"  共提取到 {len(self.fields_by_title)} 个不同的字段名称")

    def find_inconsistencies(self) -> List[Dict]:
        """查找不一致的字段"""
        inconsistencies = []

        for title, field_list in self.fields_by_title.items():
            if len(field_list) < 2:
                continue  # 只出现一次的字段不需要比较

            # 收集所有不同的key、title、format
            keys = set(f.key for f in field_list)
            titles_set = set(f.title for f in field_list)
            formats = set(f.get_format_description() for f in field_list)

            # 如果存在差异
            if len(keys) > 1 or len(titles_set) > 1 or len(formats) > 1:
                # 收集所有位置
                locations = list(set(f.location for f in field_list))

                inconsistency = {
                    '字段名': title,
                    '差异的endpoint/schema': locations,
                    'key的差异': sorted(list(keys)) if len(keys) > 1 else [],
                    'title的差异': sorted(list(titles_set)) if len(titles_set) > 1 else [],
                    '格式的差异': sorted(list(formats)) if len(formats) > 1 else []
                }
                inconsistencies.append(inconsistency)

        # 按字段名排序
        inconsistencies.sort(key=lambda x: x['字段名'])
        return inconsistencies

    def generate_report(self, inconsistencies: List[Dict], output_file: str):
        """生成报告"""
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# API字段不一致性报告\n\n")
            f.write(f"**生成时间**: {self.get_current_time()}\n\n")
            f.write(f"**分析文件**: {self.json_file}\n\n")
            f.write(f"**发现问题**: 共发现 {len(inconsistencies)} 个字段存在不一致性\n\n")

            if not inconsistencies:
                f.write("✅ 未发现字段不一致问题。\n")
                return

            f.write("---\n\n")
            f.write("## 不一致字段列表\n\n")

            for idx, item in enumerate(inconsistencies, 1):
                f.write(f"### {idx}. {item['字段名']}\n\n")

                # 出现位置
                f.write("**出现位置**:\n")
                for loc in item['差异的endpoint/schema']:
                    f.write(f"- {loc}\n")
                f.write("\n")

                # key的差异
                if item['key的差异']:
                    f.write("**key的差异**:\n")
                    for key in item['key的差异']:
                        f.write(f"- `{key}`\n")
                    f.write("\n")

                # title的差异
                if item['title的差异']:
                    f.write("**title的差异**:\n")
                    for title in item['title的差异']:
                        f.write(f"- {title}\n")
                    f.write("\n")

                # 格式的差异
                if item['格式的差异']:
                    f.write("**格式的差异**:\n")
                    for fmt in item['格式的差异']:
                        f.write(f"- {fmt}\n")
                    f.write("\n")

                f.write("---\n\n")

            # 添加表格视图
            f.write("\n## 表格视图\n\n")
            f.write("| 字段名（中文） | 差异的endpoint/schema | key的差异 | title的差异 | 格式的差异 |\n")
            f.write("|---------------|---------------------|-----------|------------|----------|\n")

            for item in inconsistencies:
                field_name = item['字段名']
                locations_count = len(item['差异的endpoint/schema'])
                locations = f"{locations_count}个位置"

                key_diff = ', '.join(item['key的差异']) if item['key的差异'] else ''
                title_diff = '有差异' if item['title的差异'] else ''
                format_diff = '有差异' if item['格式的差异'] else ''

                f.write(f"| {field_name} | {locations} | {key_diff} | {title_diff} | {format_diff} |\n")

    @staticmethod
    def get_current_time() -> str:
        """获取当前时间"""
        from datetime import datetime
        return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def main():
    analyzer = APIAnalyzer('ISV_glossary_1224.apifox.json')

    print("\n=== 开始分析API规范 ===\n")
    analyzer.analyze()

    print("\n正在查找不一致性...")
    inconsistencies = analyzer.find_inconsistencies()

    print(f"✓ 发现 {len(inconsistencies)} 个字段存在不一致性\n")

    print("正在生成报告...")
    output_file = '字段不一致报告.md'
    analyzer.generate_report(inconsistencies, output_file)

    print(f"✓ 报告已生成：{output_file}\n")
    print("=== 分析完成 ===\n")

if __name__ == '__main__':
    main()
