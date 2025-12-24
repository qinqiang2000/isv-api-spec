#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
统一API规范文件中不一致的字段命名
"""

import json
import copy
from typing import Dict, Any, Set

class FieldUnifier:
    def __init__(self, json_file: str):
        self.json_file = json_file
        self.data = None
        self.changes_count = 0

        # 不应该重命名的路径（元数据字段）
        self.skip_paths = {
            'id',  # Apifox的元数据ID
            'serverId', 'moduleId', 'parentId',
            'folderId', 'projectId'
        }

        # 字段统一规则：旧名称 -> 新名称（标准名称）
        # 基于语义清晰性、完整性和行业标准选择
        self.field_mapping = {
            # 发票相关
            'invoice_no': 'invoice_number',  # 发票号码 - 使用完整形式
            'paper_invoice_code': 'invoice_code',  # 改回来，invoice_code在纸质发票中更标准
            'invoice_date': 'issue_date',  # 开票日期 - issue_date更标准
            'invoice_copy_type': 'paper_invoice_type',  # 数电纸质发票类型

            # 地点相关
            'origin': 'origin_place',  # 产地 - 更明确
            'departure': 'start_place',  # 出发地 - 统一使用start/end
            'arrival_location': 'end_place',  # 到达地 - 与start_place对应
            'destination': 'end_place',  # 到达地 - 统一
            'departure_location': 'start_place',  # 起运地 - 统一

            # 人员相关
            'traveler': 'passenger_name',  # 出行人 - passenger更专业

            # 税务相关
            'agent_seller_name': 'proxy_seller_name',  # 代开发票真实销售方名称
            'agent_seller_tax_no': 'proxy_seller_tax_no',  # 代开发票真实销售方识别号
            'seller_tax_no': 'tin',  # 纳税人识别号 - TIN是标准缩写
            'buyer_identifier': 'buyer_tax_no',  # 购买方税号
            'commodity_tax_classification_code': 'tax_classification_code',  # 税收分类编码

            # 车辆相关
            'model': 'product_model',  # 厂牌型号
            'certificate_no': 'compliance_no',  # 合格证号
            'tonnage': 'vehicle_weight',  # 吨位
            'car_brand_no': 'license_plate_number',  # 车牌号
            'register_no': 'vehicle_plate_or_vessel_registration_no',  # 车牌号/船舶登记号
            'vehicle_type': 'vehicle_type_code',  # 车辆类型代码
            'chassis_no': 'identify_no',  # 车辆识别代号
            'license_plate': 'transport_tool_plate_no',  # 运输工具牌号
            'passenger_capacity': 'vehicle_capacity',  # 限乘人数

            # 商品相关
            'goods_code': 'product_code',  # 商品编码
            'business_no': 'inspection_no',  # 商检单号
            'spec_model': 'specification',  # 规格型号
            'num': 'quantity',  # 数量
            'item_name': 'name',  # 货物名称
            'detail_sequence_no': 'sequence_no',  # 货物明细序号
            'cargo_name': 'transport_goods',  # 运输货物名称

            # 金额相关
            'amount_with_tax': 'total_amount',  # 价税合计
            'actual_transaction_amount': 'actual_turnover',  # 实际成交含税金额
            'deduction': 'deduction_amount',  # 扣除额

            # 证件相关
            'id_card_number': 'id_no',  # 证件号码
            'import_certificate_no': 'import_no',  # 进口证明书号

            # 房产相关
            'estate_id': 'property_certificate_number',  # 房屋产权证书号
            'land_tax_no': 'land_value_tax_project_no',  # 土地增值税项目编号
            'end_lease_date': 'lease_end_date',  # 租赁期止
            'start_lease_date': 'lease_start_date',  # 租赁期起
            'simple_address': 'construction_service_location',  # 建筑服务发生地
            'building_name': 'construction_project_name',  # 建筑项目名称

            # 车船税相关（在vehicle_vessel_tax上下文中）
            'insurance_no': 'insurance_policy_no',  # 保险单号

            # 联系方式
            'agent_phone': 'agent_telephone',  # 经办人联系电话
            'buyer_phone': 'buyer_fixed_telephone',  # 购买方电话

            # 其他
            'payee_organization': 'payee_unit',  # 收款单位
            'sms_code': 'verification_code',  # 验证码
            'tax_payment_voucher_no': 'taxation_voucher',  # 完税凭证号码
            'account_status': 'status',  # 当前状态
            'cross_city_sign': 'cross_city_flag',  # 跨地市标志
            'is_cross_city': 'cross_city_flag',  # 跨地市标志
            'approved_price': 'approved_tax_price',  # 核定计税价格
        }

    def load_json(self):
        """加载JSON文件"""
        print(f"正在加载 {self.json_file}...")
        with open(self.json_file, 'r', encoding='utf-8') as f:
            self.data = json.load(f)
        print("✓ 文件加载成功")

    def should_rename(self, key: str, parent_key: str = "") -> bool:
        """判断是否应该重命名此字段"""
        # 跳过元数据字段
        if key in self.skip_paths:
            return False

        # 跳过特定父级下的字段（如parameters中的id）
        metadata_parents = {'preProcessors', 'postProcessors', 'parameters',
                          'headers', 'responses', 'cases', 'api', 'items',
                          'apiCollection', 'schemaCollection', 'servers'}

        # 如果父级是元数据相关的，并且key是id，则跳过
        if key == 'id' and parent_key in metadata_parents:
            return False

        return True

    def rename_key_in_dict(self, obj: Any, parent_key: str = "", context: str = "") -> Any:
        """递归重命名字典中的key"""
        if isinstance(obj, dict):
            new_obj = {}
            for key, value in obj.items():
                # 检查是否需要重命名
                new_key = key

                # 只在jsonSchema、properties等数据结构中重命名
                in_data_context = any(x in context for x in [
                    'jsonSchema', 'properties', 'items', 'schema',
                    'requestBody', 'response'
                ])

                if (key in self.field_mapping and
                    self.should_rename(key, parent_key) and
                    in_data_context):
                    new_key = self.field_mapping[key]
                    if new_key != key:
                        self.changes_count += 1
                        # 简化输出路径
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
        print("\n开始统一字段命名...")
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
    print("API字段统一化工具")
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
    print("字段统一化完成！")
    print(f"原始文件已备份至：{backup_file}")
    print("=" * 60 + "\n")

if __name__ == '__main__':
    main()
