#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
第二轮字段统一化 - 处理剩余的key差异
"""

import json
from typing import Any

class FieldUnifier:
    def __init__(self, json_file: str):
        self.json_file = json_file
        self.data = None
        self.changes_count = 0

        # 第二轮字段映射规则
        self.field_mapping = {
            # 纸质发票号码：在纸质发票上下文中使用paper_invoice_no
            'invoice_number': 'paper_invoice_no',  # 特指纸质发票号码时

            # 代收车船税金额：在vehicle_vessel_tax上下文中统一
            'amount': 'vehicle_vessel_tax_amount',  # 仅在vehicle_vessel_tax上下文

            # 开票类型：统一使用type（更简洁）
            'invoice_type': 'type',
        }

        # 需要特殊处理的上下文
        self.context_mapping = {
            'invoice_number': ['paper_invoice', '纸质发票'],  # 只在纸质发票相关上下文重命名
            'amount': ['vehicle_vessel_tax'],  # 只在车船税上下文重命名
        }

    def load_json(self):
        """加载JSON文件"""
        print(f"正在加载 {self.json_file}...")
        with open(self.json_file, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        print("✓ 文件加载成功")

    def should_rename_in_context(self, key: str, context: str) -> bool:
        """判断在当前上下文中是否应该重命名"""
        if key not in self.context_mapping:
            return True  # 没有上下文限制，直接重命名

        required_contexts = self.context_mapping[key]
        # 检查context中是否包含必需的上下文关键字
        for ctx in required_contexts:
            if ctx in context:
                return True
        return False

    def rename_key_in_dict(self, obj: Any, parent_key: str = "", context: str = "") -> Any:
        """递归重命名字典中的key"""
        if isinstance(obj, dict):
            new_obj = {}
            for key, value in obj.items():
                new_key = key

                # 只在jsonSchema、properties等数据结构中重命名
                in_data_context = any(x in context for x in [
                    'jsonSchema', 'properties', 'items', 'schema',
                    'requestBody', 'response'
                ])

                # 检查是否需要重命名
                if (key in self.field_mapping and in_data_context):
                    # 检查上下文
                    if self.should_rename_in_context(key, context):
                        new_key = self.field_mapping[key]
                        if new_key != key:
                            self.changes_count += 1
                            simple_context = context.split('.')[-3:] if '.' in context else [context]
                            print(f"  {'/'.join(simple_context)}: {key} -> {new_key}")

                # 递归处理值
                new_obj[new_key] = self.rename_key_in_dict(
                    value,
                    key,
                    f"{context}.{new_key}" if context else new_key
                )
            return new_obj
        elif isinstance(obj, list):
            return [self.rename_key_in_dict(item, parent_key, f"{context}[]") for item in obj]
        else:
            return obj

    def unify_fields(self):
        """统一所有字段"""
        print("\n开始第二轮字段统一...")
        print("=" * 60)
        self.changes_count = 0
        self.data = self.rename_key_in_dict(self.data, "", "root")
        print("=" * 60)
        print(f"\n✓ 完成！共修改了 {self.changes_count} 处字段")

    def save_json(self, output_file: str = None):
        """保存JSON文件"""
        if output_file is None:
            output_file = self.json_file

        print(f"\n正在保存到 {output_file}...")
        with open(output_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
        print("✓ 保存成功")

    def create_backup(self):
        """创建备份文件"""
        import shutil
        from datetime import datetime

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_file = self.json_file.replace('.json', f'_backup_{timestamp}.json')
        shutil.copy2(self.json_file, backup_file)
        print(f"✓ 已创建备份：{backup_file}")
        return backup_file

def main():
    print("\n" + "=" * 60)
    print("API字段统一化工具 - 第二轮")
    print("=" * 60 + "\n")

    unifier = FieldUnifier('ISV_glossary_1224.apifox.json')

    # 创建备份
    backup_file = unifier.create_backup()

    # 加载文件
    unifier.load_json()

    # 统一字段
    unifier.unify_fields()

    # 保存修改
    unifier.save_json()

    print("\n" + "=" * 60)
    print("第二轮字段统一化完成！")
    print(f"原始文件已备份至：{backup_file}")
    print("=" * 60 + "\n")

if __name__ == '__main__':
    main()
