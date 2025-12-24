#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
提取 issue_type 到独立Schema并建立引用
"""

import json
from datetime import datetime

def find_item_by_name(items, target_name):
    """查找指定名称的item"""
    for item in items:
        if isinstance(item, dict):
            if item.get('name') == target_name:
                return item
            if 'items' in item:
                result = find_item_by_name(item['items'], target_name)
                if result:
                    return result
    return None

def create_issue_type_schema():
    """创建独立的issue_type Schema定义"""
    # 生成一个新的ID
    schema_id = f"#/definitions/issue_type_enum"

    schema = {
        "name": "开具类型（代开标识）",
        "displayName": "",
        "id": schema_id,
        "description": "发票开具类型枚举，用于标识发票是自开、代开还是代办退税",
        "schema": {
            "jsonSchema": {
                "type": "string",
                "title": "开具类型（代开标识）",
                "enum": ["1", "2", "3"],
                "maxLength": 1,
                "x-apifox-enum": [
                    {
                        "value": "1",
                        "name": "自开",
                        "description": ""
                    },
                    {
                        "value": "2",
                        "name": "代开",
                        "description": ""
                    },
                    {
                        "value": "3",
                        "name": "代办退税",
                        "description": ""
                    }
                ]
            }
        }
    }

    return schema

def main():
    print("\n" + "=" * 80)
    print("提取 issue_type 到独立Schema")
    print("=" * 80 + "\n")

    # 加载文件
    with open('ISV_glossary_1224.apifox.json', 'r', encoding='utf-8') as f:
        data = json.load(f)

    # 备份
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    backup_file = f'ISV_glossary_1224.apifox_backup_{timestamp}.json'
    with open(backup_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    print(f"✓ 已创建备份：{backup_file}")

    if 'schemaCollection' not in data:
        print("❌ 未找到 schemaCollection")
        return

    # 1. 在"公用代码"下添加新的Schema
    for collection in data['schemaCollection']:
        if 'items' in collection:
            common_code = find_item_by_name(collection['items'], '公用代码')
            if common_code and 'items' in common_code:
                # 检查是否已存在
                existing = find_item_by_name(common_code['items'], '开具类型（代开标识）')
                if existing:
                    print("⚠️  '开具类型（代开标识）' Schema已存在，将更新")
                    # 更新现有的
                    existing.update(create_issue_type_schema())
                else:
                    # 添加新的
                    new_schema = create_issue_type_schema()
                    common_code['items'].append(new_schema)
                    print("✓ 已在'公用代码'下创建新Schema：开具类型（代开标识）")
                break

    # 2. 修改3个发票Schema，让它们引用这个新Schema
    schemas_to_update = [
        ('机动车销售统一发票数据', 'invoice_type'),
        ('二手车销售统一发票数据', 'invoice_type'),
        ('增值税发票数据', 'issue_type')
    ]

    for collection in data['schemaCollection']:
        if 'items' in collection:
            for schema_name, old_field_name in schemas_to_update:
                schema = find_item_by_name(collection['items'], schema_name)
                if schema and 'schema' in schema and 'jsonSchema' in schema['schema']:
                    props = schema['schema']['jsonSchema'].get('properties', {})

                    # 如果存在旧字段（invoice_type 或 issue_type）
                    if old_field_name in props:
                        # 移除旧字段
                        old_field = props.pop(old_field_name)

                        # 添加新字段 issue_type，引用独立Schema
                        props['issue_type'] = {
                            "$ref": "#/definitions/issue_type_enum"
                        }

                        # 更新 x-apifox-orders（字段顺序）
                        orders = schema['schema']['jsonSchema'].get('x-apifox-orders', [])
                        if old_field_name in orders and old_field_name != 'issue_type':
                            idx = orders.index(old_field_name)
                            orders[idx] = 'issue_type'
                        elif 'issue_type' not in orders:
                            # 如果orders中没有，添加到末尾
                            orders.append('issue_type')

                        print(f"✓ 已修改 {schema_name}：{old_field_name} -> issue_type (引用)")

    # 保存文件
    with open('ISV_glossary_1224.apifox.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print("\n✓ 修改完成！")
    print("\n" + "=" * 80)
    print("总结：")
    print("  1. 在'公用代码'下创建了独立Schema：开具类型（代开标识）")
    print("  2. 机动车销售统一发票数据：invoice_type -> issue_type (引用)")
    print("  3. 二手车销售统一发票数据：invoice_type -> issue_type (引用)")
    print("  4. 增值税发票数据：issue_type -> issue_type (引用)")
    print("=" * 80 + "\n")

if __name__ == '__main__':
    main()
