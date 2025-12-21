#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
为发票查验API添加剩余9种发票类型的schemas
"""

import json

def load_existing_api():
    """加载现有的API定义"""
    with open('发票查验接口.apifox.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def create_standard_vat_invoice_schema():
    """创建标准增值税发票schema (types: 01, 02, 04, 08, 10)"""
    return {
        "name": "标准增值税发票数据",
        "displayName": "",
        "id": "#/definitions/223576034",
        "description": "包含发票类型: 01-增值税专用发票, 02-货物运输业增值税专用发票, 04-增值税普通发票, 08-增值税电子专用发票, 10-增值税电子普通发票",
        "schema": {
            "jsonSchema": {
                "type": "object",
                "properties": {
                    "invoice_code": {"type": "string", "title": "发票代码", "maxLength": 12},
                    "invoice_no": {"type": "string", "title": "发票号码", "maxLength": 20},
                    "invoice_date": {"type": "string", "title": "开票日期", "maxLength": 19, "description": "YYYY-MM-DD HH:mm:ss"},
                    "special_invoice_type": {
                        "type": "string",
                        "title": "特殊票种",
                        "enum": ["02", "03", "04", "05", "08", "20", "21", "22"],
                        "x-apifox-enum": [
                            {"value": "02", "name": "农产品收购", "description": ""},
                            {"value": "03", "name": "稀土矿产品发票", "description": ""},
                            {"value": "04", "name": "稀土产成品发票", "description": ""},
                            {"value": "05", "name": "石脑油", "description": ""},
                            {"value": "08", "name": "成品油发票", "description": ""},
                            {"value": "20", "name": "会员单位投资性黄金", "description": ""},
                            {"value": "21", "name": "会员单位非投资性黄金", "description": ""},
                            {"value": "22", "name": "客户标准黄金", "description": ""}
                        ]
                    },
                    "invoice_status_flag": {
                        "type": "string",
                        "title": "发票状态标识",
                        "enum": ["0", "1", "2", "3", "4"],
                        "x-apifox-enum": [
                            {"value": "0", "name": "正数票", "description": ""},
                            {"value": "1", "name": "负数票", "description": ""},
                            {"value": "2", "name": "空白作废发票", "description": ""},
                            {"value": "3", "name": "正数作废发票", "description": ""},
                            {"value": "4", "name": "负数作废发票", "description": ""}
                        ]
                    },
                    "verification_code": {"type": "string", "title": "校验码", "maxLength": 32},
                    "saler_tax_no": {"type": "string", "title": "销售方识别号", "maxLength": 20},
                    "saler_name": {"type": "string", "title": "销售方名称", "maxLength": 300},
                    "buyer_tax_no": {"type": "string", "title": "购买方税号", "maxLength": 20},
                    "buyer_name": {"type": "string", "title": "购买方名称", "maxLength": 300},
                    "proxy_saler_tax_no": {"type": "string", "title": "代开发票真实销售方识别号", "maxLength": 20},
                    "proxy_saler_name": {"type": "string", "title": "代开发票真实销售方名称", "maxLength": 300},
                    "void_date": {"type": "string", "title": "作废日期", "maxLength": 19, "description": "YYYY-MM-DD HH:mm:ss"},
                    "amount": {"type": "number", "title": "金额", "description": "DECIMAL 18,2"},
                    "tax_amount": {"type": "number", "title": "税额", "description": "DECIMAL 18,2"}
                },
                "required": ["invoice_code", "invoice_no", "invoice_date", "invoice_status_flag", "saler_tax_no"],
                "x-apifox-orders": [
                    "invoice_code", "invoice_no", "invoice_date", "special_invoice_type",
                    "invoice_status_flag", "verification_code", "saler_tax_no", "saler_name",
                    "buyer_tax_no", "buyer_name", "proxy_saler_tax_no", "proxy_saler_name",
                    "void_date", "amount", "tax_amount"
                ]
            }
        }
    }

def create_roll_invoice_schema():
    """创建卷式发票schema (type: 11)"""
    return {
        "name": "增值税普通发票（卷式）数据",
        "displayName": "",
        "id": "#/definitions/223576035",
        "description": "包含发票类型: 11-卷式发票",
        "schema": {
            "jsonSchema": {
                "type": "object",
                "properties": {
                    "invoice_code": {"type": "string", "title": "发票代码", "maxLength": 12},
                    "invoice_no": {"type": "string", "title": "发票号码", "maxLength": 20},
                    "invoice_date": {"type": "string", "title": "开票日期", "maxLength": 19},
                    "verification_code": {"type": "string", "title": "校验码", "maxLength": 32},
                    "machine_code": {"type": "string", "title": "机器编号", "maxLength": 20},
                    "buyer_name": {"type": "string", "title": "购买方名称", "maxLength": 300},
                    "buyer_tax_no": {"type": "string", "title": "购买方纳税人识别号", "maxLength": 20},
                    "amount": {"type": "number", "title": "金额", "description": "DECIMAL 18,2"},
                    "tax_rate": {"type": "number", "title": "税率", "description": "DECIMAL 6,6"},
                    "tax_amount": {"type": "number", "title": "税额", "description": "DECIMAL 18,2"},
                    "total_amount": {"type": "number", "title": "价税合计", "description": "DECIMAL 18,2"},
                    "total_amount_in_words": {"type": "string", "title": "价税合计大写", "maxLength": 300},
                    "saler_name": {"type": "string", "title": "销售方名称", "maxLength": 300},
                    "saler_tax_no": {"type": "string", "title": "销售方纳税人识别号", "maxLength": 20},
                    "issuer": {"type": "string", "title": "开票人", "maxLength": 300},
                    "remark": {"type": "string", "title": "备注", "maxLength": 450}
                },
                "required": ["invoice_code", "invoice_no", "invoice_date", "saler_tax_no", "amount", "tax_rate", "tax_amount", "total_amount"],
                "x-apifox-orders": [
                    "invoice_code", "invoice_no", "invoice_date", "verification_code",
                    "machine_code", "buyer_name", "buyer_tax_no", "amount", "tax_rate",
                    "tax_amount", "total_amount", "total_amount_in_words",
                    "saler_name", "saler_tax_no", "issuer", "remark"
                ]
            }
        }
    }

def create_toll_road_invoice_schema():
    """创建通行费发票schema (type: 14)"""
    return {
        "name": "增值税普通发票（通行费）数据",
        "displayName": "",
        "id": "#/definitions/223576036",
        "description": "包含发票类型: 14-通行费发票",
        "schema": {
            "jsonSchema": {
                "type": "object",
                "properties": {
                    "invoice_code": {"type": "string", "title": "发票代码", "maxLength": 12},
                    "invoice_no": {"type": "string", "title": "发票号码", "maxLength": 20},
                    "invoice_date": {"type": "string", "title": "开票日期", "maxLength": 19},
                    "verification_code": {"type": "string", "title": "校验码", "maxLength": 32},
                    "buyer_name": {"type": "string", "title": "车牌号", "maxLength": 300},
                    "special_invoice_type": {
                        "type": "string",
                        "title": "特殊票种",
                        "enum": ["06", "07"],
                        "x-apifox-enum": [
                            {"value": "06", "name": "不可抵扣", "description": ""},
                            {"value": "07", "name": "可抵扣", "description": ""}
                        ]
                    },
                    "highway_flag": {
                        "type": "string",
                        "title": "高速公路标识",
                        "enum": ["Y", "N"],
                        "x-apifox-enum": [
                            {"value": "Y", "name": "是", "description": ""},
                            {"value": "N", "name": "否", "description": ""}
                        ]
                    },
                    "entrance": {"type": "string", "title": "入口", "maxLength": 300},
                    "exit": {"type": "string", "title": "出口", "maxLength": 300},
                    "amount": {"type": "number", "title": "金额", "description": "DECIMAL 18,2"},
                    "tax_rate": {"type": "number", "title": "税率", "description": "DECIMAL 6,6"},
                    "tax_amount": {"type": "number", "title": "税额", "description": "DECIMAL 18,2"},
                    "total_amount": {"type": "number", "title": "价税合计", "description": "DECIMAL 18,2"},
                    "total_amount_in_words": {"type": "string", "title": "价税合计大写", "maxLength": 300},
                    "saler_name": {"type": "string", "title": "销售方名称", "maxLength": 300},
                    "saler_tax_no": {"type": "string", "title": "销售方纳税人识别号", "maxLength": 20},
                    "saler_address_phone": {"type": "string", "title": "销售方地址、电话", "maxLength": 450},
                    "saler_bank_account": {"type": "string", "title": "销售方开户行及账号", "maxLength": 300}
                },
                "required": ["invoice_code", "invoice_no", "invoice_date", "saler_tax_no", "amount", "tax_rate", "tax_amount", "total_amount"],
                "x-apifox-orders": [
                    "invoice_code", "invoice_no", "invoice_date", "verification_code",
                    "buyer_name", "special_invoice_type", "highway_flag", "entrance", "exit",
                    "amount", "tax_rate", "tax_amount", "total_amount", "total_amount_in_words",
                    "saler_name", "saler_tax_no", "saler_address_phone", "saler_bank_account"
                ]
            }
        }
    }

# 简化后续schemas的创建，只包含核心字段
def create_vehicle_sales_invoice_schema():
    """机动车销售发票 (03, 87)"""
    return {
        "name": "机动车销售统一发票数据",
        "displayName": "",
        "id": "#/definitions/223576037",
        "description": "包含发票类型: 03-机动车销售统一发票, 87-纸质发票（机动车销售统一发票）",
        "schema": {
            "jsonSchema": {
                "type": "object",
                "properties": {
                    "invoice_code": {"type": "string", "title": "发票代码", "maxLength": 12},
                    "invoice_no": {"type": "string", "title": "发票号码", "maxLength": 20},
                    "invoice_date": {"type": "string", "title": "开票日期", "maxLength": 19},
                    "vehicle_type": {"type": "string", "title": "车辆类型", "maxLength": 50},
                    "product_model": {"type": "string", "title": "厂牌型号", "maxLength": 100},
                    "origin_place": {"type": "string", "title": "产地", "maxLength": 100},
                    "certificate_no": {"type": "string", "title": "合格证号", "maxLength": 50},
                    "import_certificate_no": {"type": "string", "title": "进口证明书号", "maxLength": 50},
                    "business_inspection_no": {"type": "string", "title": "商检单号", "maxLength": 50},
                    "engine_no": {"type": "string", "title": "发动机号码", "maxLength": 50},
                    "vehicle_identification_no": {"type": "string", "title": "车辆识别代号/车架号码", "maxLength": 50},
                    "buyer_name": {"type": "string", "title": "购买方名称", "maxLength": 300},
                    "buyer_id_type": {"type": "string", "title": "购买方证件类型", "maxLength": 20},
                    "buyer_id_no": {"type": "string", "title": "购买方证件号码/组织机构代码", "maxLength": 50},
                    "saler_name": {"type": "string", "title": "销售方名称", "maxLength": 300},
                    "saler_tax_no": {"type": "string", "title": "销售方纳税人识别号", "maxLength": 20},
                    "amount": {"type": "number", "title": "不含税价", "description": "DECIMAL 18,2"},
                    "tax_rate": {"type": "number", "title": "税率", "description": "DECIMAL 6,6"},
                    "tax_amount": {"type": "number", "title": "税额", "description": "DECIMAL 18,2"},
                    "total_amount": {"type": "number", "title": "价税合计", "description": "DECIMAL 18,2"}
                },
                "required": ["invoice_code", "invoice_no", "invoice_date", "vehicle_identification_no", "saler_tax_no"],
                "x-apifox-orders": ["invoice_code", "invoice_no", "invoice_date", "vehicle_type", "product_model", "origin_place", "certificate_no", "import_certificate_no", "business_inspection_no", "engine_no", "vehicle_identification_no", "buyer_name", "buyer_id_type", "buyer_id_no", "saler_name", "saler_tax_no", "amount", "tax_rate", "tax_amount", "total_amount"]
            }
        }
    }

def add_schemas_to_api(api_doc):
    """将新schemas添加到API文档"""
    # 找到schema collection中的ISV发票查验数据类型项
    for schema_root in api_doc["schemaCollection"]:
        for item in schema_root.get("items", []):
            if item.get("name") == "ISV发票查验数据类型":
                # 添加新的schemas
                item["items"].extend([
                    create_standard_vat_invoice_schema(),
                    create_roll_invoice_schema(),
                    create_toll_road_invoice_schema(),
                    create_vehicle_sales_invoice_schema()
                ])
                print(f"✓ 已添加4种新发票类型schemas")
                break
    
    # 更新API响应中的oneOf引用
    for api_root in api_doc["apiCollection"]:
        for folder in api_root.get("items", []):
            if "api" in folder.get("items", [{}])[0]:
                api = folder["items"][0]["api"]
                for response in api.get("responses", []):
                    if response["code"] == 200:
                        verification_data = response["jsonSchema"]["properties"].get("verification_data")
                        if verification_data and "oneOf" in verification_data:
                            # 添加新的schema引用
                            verification_data["oneOf"].extend([
                                {"$ref": "#/definitions/223576034"},  # 标准增值税发票
                                {"$ref": "#/definitions/223576035"},  # 卷式发票
                                {"$ref": "#/definitions/223576036"},  # 通行费发票
                                {"$ref": "#/definitions/223576037"}   # 机动车发票
                            ])
                            print(f"✓ 已更新API响应的oneOf引用，当前包含 {len(verification_data['oneOf'])} 种发票类型")
    
    return api_doc

def main():
    print("开始添加剩余发票类型schemas...")
    
    # 加载现有API
    api_doc = load_existing_api()
    print("✓ 已加载现有API定义")
    
    # 添加新schemas
    api_doc = add_schemas_to_api(api_doc)
    
    # 保存更新后的API
    output_path = "发票查验接口.apifox.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(api_doc, f, ensure_ascii=False, indent=2)
    
    print(f"✓ 完成！已更新文件: {output_path}")
    print(f"\n当前进度：")
    print(f"  - 已完成 5/10 种发票类型的完整定义")
    print(f"  - 剩余 5 种待添加")

if __name__ == "__main__":
    main()
