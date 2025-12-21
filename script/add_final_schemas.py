#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
添加最后5种发票类型schemas
"""

import json

def load_existing_api():
    with open('发票查验接口.apifox.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def create_used_vehicle_sales_invoice_schema():
    """二手车销售发票 (15, 88)"""
    return {
        "name": "二手车销售统一发票数据",
        "displayName": "",
        "id": "#/definitions/223576038",
        "description": "包含发票类型: 15-二手车销售统一发票, 88-纸质发票（二手车销售统一发票）",
        "schema": {
            "jsonSchema": {
                "type": "object",
                "properties": {
                    "invoice_code": {"type": "string", "title": "发票代码", "maxLength": 12},
                    "invoice_no": {"type": "string", "title": "发票号码", "maxLength": 20},
                    "invoice_date": {"type": "string", "title": "开票日期", "maxLength": 19},
                    "sale_date": {"type": "string", "title": "销售日期", "maxLength": 19},
                    "vehicle_type": {"type": "string", "title": "车辆类型", "maxLength": 50},
                    "license_plate_no": {"type": "string", "title": "车牌照号", "maxLength": 20},
                    "registration_no": {"type": "string", "title": "登记证号", "maxLength": 50},
                    "vehicle_identification_no": {"type": "string", "title": "车辆识别代号/车架号码", "maxLength": 50},
                    "transfer_date": {"type": "string", "title": "转入日期", "maxLength": 19},
                    "buyer_name": {"type": "string", "title": "买方单位/个人", "maxLength": 300},
                    "buyer_id_type": {"type": "string", "title": "买方证件类型", "maxLength": 20},
                    "buyer_id_no": {"type": "string", "title": "买方证件号码/组织机构代码", "maxLength": 50},
                    "buyer_address": {"type": "string", "title": "买方单位/个人住址", "maxLength": 300},
                    "buyer_phone": {"type": "string", "title": "买方电话", "maxLength": 60},
                    "saler_name": {"type": "string", "title": "卖方单位/个人", "maxLength": 300},
                    "saler_id_type": {"type": "string", "title": "卖方证件类型", "maxLength": 20},
                    "saler_id_no": {"type": "string", "title": "卖方证件号码/组织机构代码", "maxLength": 50},
                    "saler_address": {"type": "string", "title": "卖方单位/个人住址", "maxLength": 300},
                    "saler_phone": {"type": "string", "title": "卖方电话", "maxLength": 60},
                    "vehicle_price_total": {"type": "number", "title": "车价合计", "description": "DECIMAL 18,2"},
                    "market_name": {"type": "string", "title": "二手车市场名称", "maxLength": 300},
                    "market_tax_no": {"type": "string", "title": "二手车市场纳税人识别号", "maxLength": 20},
                    "market_address": {"type": "string", "title": "二手车市场地址", "maxLength": 300},
                    "market_bank_account": {"type": "string", "title": "二手车市场开户行、账号", "maxLength": 300}
                },
                "required": ["invoice_code", "invoice_no", "invoice_date", "vehicle_identification_no", "market_tax_no"],
                "x-apifox-orders": ["invoice_code", "invoice_no", "invoice_date", "sale_date", "vehicle_type", "license_plate_no", "registration_no", "vehicle_identification_no", "transfer_date", "buyer_name", "buyer_id_type", "buyer_id_no", "buyer_address", "buyer_phone", "saler_name", "saler_id_type", "saler_id_no", "saler_address", "saler_phone", "vehicle_price_total", "market_name", "market_tax_no", "market_address", "market_bank_account"]
            }
        }
    }

def create_aviation_eticket_schema():
    """航空运输客票 (61)"""
    return {
        "name": "航空运输客票电子行程单数据",
        "displayName": "",
        "id": "#/definitions/223576039",
        "description": "包含发票类型: 61-电子发票（航空运输客票电子行程单）",
        "schema": {
            "jsonSchema": {
                "type": "object",
                "properties": {
                    "invoice_no": {"type": "string", "title": "发票号码", "maxLength": 20},
                    "issue_date": {"type": "string", "title": "填开日期", "maxLength": 19},
                    "passenger_name": {"type": "string", "title": "旅客姓名", "maxLength": 100},
                    "passenger_id_no": {"type": "string", "title": "旅客身份证号码", "maxLength": 50},
                    "carrier": {"type": "string", "title": "承运人", "maxLength": 300},
                    "flight_no": {"type": "string", "title": "航班号", "maxLength": 50},
                    "seat_class": {"type": "string", "title": "座位等级", "maxLength": 50},
                    "departure": {"type": "string", "title": "出发地", "maxLength": 100},
                    "destination": {"type": "string", "title": "目的地", "maxLength": 100},
                    "travel_date": {"type": "string", "title": "乘机日期", "maxLength": 19},
                    "travel_time": {"type": "string", "title": "乘机时间", "maxLength": 10},
                    "fare": {"type": "number", "title": "票价", "description": "DECIMAL 18,2"},
                    "fuel_surcharge": {"type": "number", "title": "燃油附加费", "description": "DECIMAL 18,2"},
                    "airport_construction_fee": {"type": "number", "title": "民航发展基金", "description": "DECIMAL 18,2"},
                    "other_tax": {"type": "number", "title": "其他税费", "description": "DECIMAL 18,2"},
                    "total_amount": {"type": "number", "title": "合计金额", "description": "DECIMAL 18,2"},
                    "insurance_premium": {"type": "number", "title": "保险费", "description": "DECIMAL 18,2"},
                    "agent_code": {"type": "string", "title": "销售单位代号", "maxLength": 50},
                    "agent_name": {"type": "string", "title": "填开单位", "maxLength": 300},
                    "remark": {"type": "string", "title": "备注", "maxLength": 450}
                },
                "required": ["invoice_no", "issue_date", "passenger_name", "flight_no"],
                "x-apifox-orders": ["invoice_no", "issue_date", "passenger_name", "passenger_id_no", "carrier", "flight_no", "seat_class", "departure", "destination", "travel_date", "travel_time", "fare", "fuel_surcharge", "airport_construction_fee", "other_tax", "total_amount", "insurance_premium", "agent_code", "agent_name", "remark"]
            }
        }
    }

def create_railway_eticket_schema():
    """铁路电子客票 (51)"""
    return {
        "name": "铁路电子客票数据",
        "displayName": "",
        "id": "#/definitions/223576040",
        "description": "包含发票类型: 51-电子发票（铁路电子客票）",
        "schema": {
            "jsonSchema": {
                "type": "object",
                "properties": {
                    "invoice_no": {"type": "string", "title": "发票号码", "maxLength": 20},
                    "issue_date": {"type": "string", "title": "开票日期", "maxLength": 19},
                    "passenger_name": {"type": "string", "title": "旅客姓名", "maxLength": 100},
                    "passenger_id_no": {"type": "string", "title": "旅客身份证号码", "maxLength": 50},
                    "train_no": {"type": "string", "title": "车次", "maxLength": 50},
                    "seat_type": {"type": "string", "title": "席别", "maxLength": 50},
                    "seat_no": {"type": "string", "title": "座位号", "maxLength": 20},
                    "departure_station": {"type": "string", "title": "出发站", "maxLength": 100},
                    "arrival_station": {"type": "string", "title": "到达站", "maxLength": 100},
                    "departure_date": {"type": "string", "title": "开车日期", "maxLength": 19},
                    "departure_time": {"type": "string", "title": "开车时间", "maxLength": 10},
                    "fare": {"type": "number", "title": "票价", "description": "DECIMAL 18,2"},
                    "tax_rate": {"type": "number", "title": "税率", "description": "DECIMAL 6,6"},
                    "tax_amount": {"type": "number", "title": "税额", "description": "DECIMAL 18,2"},
                    "ticket_type": {"type": "string", "title": "票种", "maxLength": 50},
                    "saler_name": {"type": "string", "title": "销售方名称", "maxLength": 300},
                    "saler_tax_no": {"type": "string", "title": "销售方纳税人识别号", "maxLength": 20},
                    "remark": {"type": "string", "title": "备注", "maxLength": 450}
                },
                "required": ["invoice_no", "issue_date", "passenger_name", "train_no", "saler_tax_no"],
                "x-apifox-orders": ["invoice_no", "issue_date", "passenger_name", "passenger_id_no", "train_no", "seat_type", "seat_no", "departure_station", "arrival_station", "departure_date", "departure_time", "fare", "tax_rate", "tax_amount", "ticket_type", "saler_name", "saler_tax_no", "remark"]
            }
        }
    }

def create_digital_vehicle_sales_invoice_schema():
    """数字化电子机动车销售发票 (83)"""
    return {
        "name": "数字化电子发票-机动车销售统一发票数据",
        "displayName": "",
        "id": "#/definitions/223576041",
        "description": "包含发票类型: 83-机动车销售电子统一发票",
        "schema": {
            "jsonSchema": {
                "type": "object",
                "properties": {
                    "invoice_no": {"type": "string", "title": "发票号码", "maxLength": 20},
                    "paper_invoice_code": {"type": "string", "title": "纸质发票代码", "maxLength": 12},
                    "paper_invoice_no": {"type": "string", "title": "纸质发票号码", "maxLength": 20},
                    "invoice_date": {"type": "string", "title": "开票日期", "maxLength": 19},
                    "vehicle_type": {"type": "string", "title": "车辆类型", "maxLength": 50},
                    "product_model": {"type": "string", "title": "厂牌型号", "maxLength": 100},
                    "origin_place": {"type": "string", "title": "产地", "maxLength": 100},
                    "certificate_no": {"type": "string", "title": "合格证号", "maxLength": 50},
                    "engine_no": {"type": "string", "title": "发动机号码", "maxLength": 50},
                    "vehicle_identification_no": {"type": "string", "title": "车辆识别代号", "maxLength": 50},
                    "buyer_name": {"type": "string", "title": "购买方名称", "maxLength": 300},
                    "buyer_tax_no": {"type": "string", "title": "购买方纳税人识别号", "maxLength": 20},
                    "saler_name": {"type": "string", "title": "销售方名称", "maxLength": 300},
                    "saler_tax_no": {"type": "string", "title": "销售方纳税人识别号", "maxLength": 20},
                    "amount": {"type": "number", "title": "不含税价", "description": "DECIMAL 18,2"},
                    "tax_rate": {"type": "number", "title": "税率", "description": "DECIMAL 6,6"},
                    "tax_amount": {"type": "number", "title": "税额", "description": "DECIMAL 18,2"},
                    "total_amount": {"type": "number", "title": "价税合计", "description": "DECIMAL 18,2"},
                    "remark": {"type": "string", "title": "备注", "maxLength": 450}
                },
                "required": ["invoice_no", "invoice_date", "vehicle_identification_no", "saler_tax_no"],
                "x-apifox-orders": ["invoice_no", "paper_invoice_code", "paper_invoice_no", "invoice_date", "vehicle_type", "product_model", "origin_place", "certificate_no", "engine_no", "vehicle_identification_no", "buyer_name", "buyer_tax_no", "saler_name", "saler_tax_no", "amount", "tax_rate", "tax_amount", "total_amount", "remark"]
            }
        }
    }

def create_digital_used_vehicle_sales_invoice_schema():
    """数字化电子二手车销售发票 (84)"""
    return {
        "name": "数字化电子发票-二手车销售统一发票数据",
        "displayName": "",
        "id": "#/definitions/223576042",
        "description": "包含发票类型: 84-二手车销售电子统一发票",
        "schema": {
            "jsonSchema": {
                "type": "object",
                "properties": {
                    "invoice_no": {"type": "string", "title": "发票号码", "maxLength": 20},
                    "paper_invoice_code": {"type": "string", "title": "纸质发票代码", "maxLength": 12},
                    "paper_invoice_no": {"type": "string", "title": "纸质发票号码", "maxLength": 20},
                    "invoice_date": {"type": "string", "title": "开票日期", "maxLength": 19},
                    "special_element_type_code": {
                        "type": "string",
                        "title": "特定要素类型代码",
                        "enum": ["51", "52"],
                        "x-apifox-enum": [
                            {"value": "51", "name": "正向开具", "description": ""},
                            {"value": "52", "name": "反向开具", "description": ""}
                        ]
                    },
                    "vehicle_type": {"type": "string", "title": "车辆类型", "maxLength": 50},
                    "license_plate_no": {"type": "string", "title": "车牌照号", "maxLength": 20},
                    "vehicle_identification_no": {"type": "string", "title": "车辆识别代号", "maxLength": 50},
                    "buyer_name": {"type": "string", "title": "买方名称", "maxLength": 300},
                    "buyer_tax_no": {"type": "string", "title": "买方纳税人识别号", "maxLength": 20},
                    "saler_name": {"type": "string", "title": "卖方名称", "maxLength": 300},
                    "saler_tax_no": {"type": "string", "title": "卖方纳税人识别号", "maxLength": 20},
                    "vehicle_price_total": {"type": "number", "title": "车价合计", "description": "DECIMAL 18,2"},
                    "market_name": {"type": "string", "title": "二手车市场名称", "maxLength": 300},
                    "market_tax_no": {"type": "string", "title": "二手车市场纳税人识别号", "maxLength": 20},
                    "market_address": {"type": "string", "title": "二手车市场地址", "maxLength": 300},
                    "remark": {"type": "string", "title": "备注", "maxLength": 450}
                },
                "required": ["invoice_no", "invoice_date", "vehicle_identification_no", "market_tax_no"],
                "x-apifox-orders": ["invoice_no", "paper_invoice_code", "paper_invoice_no", "invoice_date", "special_element_type_code", "vehicle_type", "license_plate_no", "vehicle_identification_no", "buyer_name", "buyer_tax_no", "saler_name", "saler_tax_no", "vehicle_price_total", "market_name", "market_tax_no", "market_address", "remark"]
            }
        }
    }

def add_final_schemas(api_doc):
    """添加最后5种schemas"""
    for schema_root in api_doc["schemaCollection"]:
        for item in schema_root.get("items", []):
            if item.get("name") == "ISV发票查验数据类型":
                item["items"].extend([
                    create_used_vehicle_sales_invoice_schema(),
                    create_aviation_eticket_schema(),
                    create_railway_eticket_schema(),
                    create_digital_vehicle_sales_invoice_schema(),
                    create_digital_used_vehicle_sales_invoice_schema()
                ])
                print(f"✓ 已添加5种新发票类型schemas")
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
                            verification_data["oneOf"].extend([
                                {"$ref": "#/definitions/223576038"},  # 二手车销售
                                {"$ref": "#/definitions/223576039"},  # 航空客票
                                {"$ref": "#/definitions/223576040"},  # 铁路客票
                                {"$ref": "#/definitions/223576041"},  # 数字化机动车
                                {"$ref": "#/definitions/223576042"}   # 数字化二手车
                            ])
                            print(f"✓ 已更新API响应的oneOf引用，当前包含 {len(verification_data['oneOf'])} 种发票类型")
    
    return api_doc

def main():
    print("开始添加最后5种发票类型schemas...")
    api_doc = load_existing_api()
    print("✓ 已加载现有API定义")
    
    api_doc = add_final_schemas(api_doc)
    
    output_path = "发票查验接口.apifox.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(api_doc, f, ensure_ascii=False, indent=2)
    
    print(f"✓ 完成！已更新文件: {output_path}")
    print(f"\n🎉 全部10种发票类型已完成！")
    print(f"\n完整列表：")
    print(f"  1. 数字化电子发票-增值税发票 (81, 82, 85, 86)")
    print(f"  2. 标准增值税发票 (01, 02, 04, 08, 10)")
    print(f"  3. 增值税普通发票（卷式）(11)")
    print(f"  4. 增值税普通发票（通行费）(14)")
    print(f"  5. 机动车销售统一发票 (03, 87)")
    print(f"  6. 二手车销售统一发票 (15, 88)")
    print(f"  7. 航空运输客票电子行程单 (61)")
    print(f"  8. 铁路电子客票 (51)")
    print(f"  9. 数字化电子发票-机动车 (83)")
    print(f"  10. 数字化电子发票-二手车 (84)")

if __name__ == "__main__":
    main()
