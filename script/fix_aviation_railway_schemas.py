#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
修复航空运输客票和铁路电子客票的schema定义
根据文档添加完整的"货物信息"和"特定要素"结构
"""

import json

def create_complete_aviation_eticket_schema():
    """航空运输客票 (61) - 完整版本，包含货物信息和特定要素"""
    return {
        "name": "航空运输客票电子行程单数据",
        "displayName": "",
        "id": "#/definitions/223576039",
        "description": "包含发票类型: 61-电子发票（航空运输客票电子行程单）",
        "schema": {
            "jsonSchema": {
                "type": "object",
                "properties": {
                    # 基本字段（35个字段）
                    "invoice_no": {"type": "string", "title": "发票号码", "maxLength": 20},
                    "is_paper_invoice": {"type": "string", "title": "是否为纸质发票", "maxLength": 1},
                    "invoice_date": {"type": "string", "title": "开票日期", "description": "YYYY-MM-DD HH:mm:ss", "maxLength": 19},
                    "original_blue_invoice_no": {"type": "string", "title": "开具红字发票对应的蓝字发票号码", "maxLength": 30},
                    "invoice_category_code": {"type": "string", "title": "发票票种代码", "maxLength": 2},
                    "special_element_type_code": {"type": "string", "title": "特定要素类型代码", "maxLength": 2},
                    "buyer_tax_no": {"type": "string", "title": "购买方纳税人识别号", "maxLength": 20},
                    "buyer_name": {"type": "string", "title": "购买方名称", "maxLength": 300},
                    "buyer_address": {"type": "string", "title": "购买方地址", "maxLength": 300},
                    "buyer_phone": {"type": "string", "title": "购买方联系电话", "maxLength": 60},
                    "seller_tax_no": {"type": "string", "title": "销售方纳税人识别号", "maxLength": 20},
                    "seller_name": {"type": "string", "title": "销售方名称", "maxLength": 300},
                    "seller_address": {"type": "string", "title": "销售方地址", "maxLength": 300},
                    "seller_phone": {"type": "string", "title": "销售方联系电话", "maxLength": 60},
                    "buyer_agent_name": {"type": "string", "title": "购买方经办人", "maxLength": 150},
                    "agent_id_no": {"type": "string", "title": "经办人身份证件号码", "maxLength": 30},
                    "agent_phone": {"type": "string", "title": "经办人联系电话", "maxLength": 60},
                    "issuer": {"type": "string", "title": "开票人", "maxLength": 300},
                    "payee": {"type": "string", "title": "收款人", "maxLength": 300},
                    "remitter": {"type": "string", "title": "付汇人", "maxLength": 300},
                    "amount_with_tax": {"type": "number", "title": "价税合计", "description": "DECIMAL 18,2"},
                    "amount_with_tax_in_words": {"type": "string", "title": "价税合计（大写）", "maxLength": 100},
                    "settlement_method_code": {"type": "string", "title": "结算方式代码", "maxLength": 2},
                    "total_amount": {"type": "number", "title": "合计金额（合计不含税金额）", "description": "DECIMAL 18,2"},
                    "total_tax_amount": {"type": "number", "title": "合计税额", "description": "DECIMAL 18,2"},
                    "issuer_real_name_auth_location": {"type": "string", "title": "开票人实人认证地址信息", "maxLength": 100},
                    "mobile_invoice_location": {"type": "string", "title": "手机开票地址信息", "maxLength": 100},
                    "contract_no": {"type": "string", "title": "合同编号", "maxLength": 60},
                    "tax_obligation_occurrence_time": {"type": "string", "title": "纳税义务发生时间", "description": "YYYY-MM-DD HH:MI:SS", "maxLength": 17},
                    "agent_id_type_code": {"type": "string", "title": "经办人身份证件种类", "maxLength": 30},
                    "is_blue_invoice": {"type": "string", "title": "是否蓝字发票标志", "enum": ["Y", "N"], "maxLength": 1},
                    "vat_immediate_refund_code": {"type": "string", "title": "增值税即征即退代码", "maxLength": 2},
                    "remark": {"type": "string", "title": "备注", "maxLength": 300},
                    "goods_quantity": {"type": "number", "title": "商品数量", "description": "DECIMAL 18,4"},
                    "export_tax_refund_type_code": {"type": "string", "title": "出口退税类代码", "maxLength": 2},

                    # 货物信息数组
                    "items": {
                        "type": "array",
                        "title": "货物信息",
                        "items": {
                            "type": "object",
                            "properties": {
                                "sequence_no": {"type": "integer", "title": "序号"},
                                "item_name": {"type": "string", "title": "项目名称", "maxLength": 600},
                                "goods_or_service_name": {"type": "string", "title": "货物或应税劳务、服务名称", "maxLength": 300},
                                "item_short_name": {"type": "string", "title": "商品服务简称", "maxLength": 120},
                                "tax_classification_code": {"type": "string", "title": "商品和服务税收分类合并编码", "maxLength": 19},
                                "amount": {"type": "number", "title": "金额", "description": "DECIMAL 18,2"},
                                "tax_rate": {"type": "number", "title": "税率", "description": "DECIMAL 16,6"},
                                "tax_amount": {"type": "number", "title": "税额", "description": "DECIMAL 18,6"},
                                "deduction_amount": {"type": "number", "title": "扣除额", "description": "DECIMAL 18,2"}
                            },
                            "required": ["sequence_no", "tax_classification_code", "amount", "tax_rate", "tax_amount"]
                        }
                    },

                    # 民航行程单电子发票特定要素
                    "flight_specific_elements": {
                        "type": "object",
                        "title": "民航行程单电子发票特定要素",
                        "properties": {
                            "invoice_no": {"type": "string", "title": "发票号码", "maxLength": 30},
                            "domestic_international_flag": {"type": "string", "title": "国内国际标识", "maxLength": 1},
                            "gp_no": {"type": "string", "title": "GP单号", "maxLength": 20},
                            "is_blue_invoice": {"type": "string", "title": "是否蓝字发票标志", "enum": ["Y", "N"], "maxLength": 1},
                            "passenger_name": {"type": "string", "title": "姓名", "maxLength": 49},
                            "id_no": {"type": "string", "title": "证件号码", "maxLength": 30},
                            "endorsement": {"type": "string", "title": "签注", "maxLength": 200},
                            "eticket_no": {"type": "string", "title": "电子客票号码", "maxLength": 30},
                            "verification_code": {"type": "string", "title": "验证码", "maxLength": 20},
                            "tips": {"type": "string", "title": "提示信息", "maxLength": 100},
                            "insurance_fee": {"type": "string", "title": "保险费", "maxLength": 20},
                            "sales_outlet_code": {"type": "string", "title": "销售网点代号", "maxLength": 20},
                            "issuing_unit": {"type": "string", "title": "填开单位", "maxLength": 300},
                            "invoice_date": {"type": "string", "title": "开票日期"},
                            "seller_name": {"type": "string", "title": "销售方名称", "maxLength": 300},
                            "seller_tax_no": {"type": "string", "title": "销售方纳税人识别号", "maxLength": 20},
                            "buyer_name": {"type": "string", "title": "购买方名称", "maxLength": 300},
                            "buyer_tax_no": {"type": "string", "title": "购买方纳税人识别号", "maxLength": 20},

                            # 特定要素明细数组
                            "flight_segment_details": {
                                "type": "array",
                                "title": "特定要素明细",
                                "items": {
                                    "type": "object",
                                    "properties": {
                                        "departure_station": {"type": "string", "title": "始发站", "maxLength": 50},
                                        "destination_station": {"type": "string", "title": "目的站", "maxLength": 50},
                                        "segment": {"type": "integer", "title": "航段"},
                                        "carrier": {"type": "string", "title": "承运人", "maxLength": 20},
                                        "flight_no": {"type": "string", "title": "航班号", "maxLength": 20},
                                        "seat_class": {"type": "string", "title": "座位等级", "maxLength": 20},
                                        "carrier_date": {"type": "string", "title": "承运日期", "description": "YYYYYMMDD", "maxLength": 8},
                                        "takeoff_time": {"type": "string", "title": "起飞时间", "description": "YYYY-MM-DD HH:MI:SS", "maxLength": 17},
                                        "ticket_class_category": {"type": "string", "title": "客票级别/客票类别", "maxLength": 20},
                                        "ticket_effective_date": {"type": "string", "title": "客票生效日期", "description": "YYYYYMMDD", "maxLength": 8},
                                        "valid_until_date": {"type": "string", "title": "有效截止日期", "description": "YYYYYMMDD", "maxLength": 8},
                                        "free_baggage_allowance": {"type": "string", "title": "免费行李额", "maxLength": 20}
                                    }
                                }
                            }
                        },
                        "required": ["invoice_no", "is_blue_invoice", "invoice_date", "seller_name", "seller_tax_no", "buyer_name"]
                    }
                },
                "required": ["invoice_no", "is_paper_invoice", "invoice_date", "invoice_category_code", "seller_tax_no", "seller_name", "buyer_name", "is_blue_invoice"],
                "x-apifox-orders": [
                    "invoice_no", "is_paper_invoice", "invoice_date", "original_blue_invoice_no",
                    "invoice_category_code", "special_element_type_code", "buyer_tax_no", "buyer_name",
                    "buyer_address", "buyer_phone", "seller_tax_no", "seller_name", "seller_address",
                    "seller_phone", "buyer_agent_name", "agent_id_no", "agent_phone", "issuer",
                    "payee", "remitter", "amount_with_tax", "amount_with_tax_in_words",
                    "settlement_method_code", "total_amount", "total_tax_amount",
                    "issuer_real_name_auth_location", "mobile_invoice_location", "contract_no",
                    "tax_obligation_occurrence_time", "agent_id_type_code", "is_blue_invoice",
                    "vat_immediate_refund_code", "remark", "goods_quantity", "export_tax_refund_type_code",
                    "items", "flight_specific_elements"
                ],
                "title": "航空运输客票电子行程单数据",
                "description": "包含发票类型: 61-电子发票（航空运输客票电子行程单）"
            }
        }
    }

def create_complete_railway_eticket_schema():
    """铁路电子客票 (51) - 完整版本，包含货物信息和特定要素"""
    return {
        "name": "铁路电子客票数据",
        "displayName": "",
        "id": "#/definitions/223576040",
        "description": "包含发票类型: 51-电子发票（铁路电子客票）",
        "schema": {
            "jsonSchema": {
                "type": "object",
                "properties": {
                    # 基本字段（35个字段）
                    "invoice_no": {"type": "string", "title": "发票号码", "maxLength": 20},
                    "is_paper_invoice": {"type": "string", "title": "是否为纸质发票", "maxLength": 1},
                    "invoice_date": {"type": "string", "title": "开票日期", "description": "YYYY-MM-DD HH:mm:ss", "maxLength": 19},
                    "original_blue_invoice_no": {"type": "string", "title": "开具红字发票对应的蓝字发票号码", "maxLength": 30},
                    "invoice_category_code": {"type": "string", "title": "发票票种代码", "maxLength": 2},
                    "special_element_type_code": {"type": "string", "title": "特定要素类型代码", "maxLength": 2},
                    "buyer_tax_no": {"type": "string", "title": "购买方纳税人识别号", "maxLength": 20},
                    "buyer_name": {"type": "string", "title": "购买方名称", "maxLength": 300},
                    "buyer_address": {"type": "string", "title": "购买方地址", "maxLength": 300},
                    "buyer_phone": {"type": "string", "title": "购买方联系电话", "maxLength": 60},
                    "seller_tax_no": {"type": "string", "title": "销售方纳税人识别号", "maxLength": 20},
                    "seller_name": {"type": "string", "title": "销售方名称", "maxLength": 300},
                    "seller_address": {"type": "string", "title": "销售方地址", "maxLength": 300},
                    "seller_phone": {"type": "string", "title": "销售方联系电话", "maxLength": 60},
                    "buyer_agent_name": {"type": "string", "title": "购买方经办人", "maxLength": 150},
                    "agent_id_no": {"type": "string", "title": "经办人身份证件号码", "maxLength": 30},
                    "agent_phone": {"type": "string", "title": "经办人联系电话", "maxLength": 60},
                    "issuer": {"type": "string", "title": "开票人", "maxLength": 300},
                    "payee": {"type": "string", "title": "收款人", "maxLength": 300},
                    "remitter": {"type": "string", "title": "付汇人", "maxLength": 300},
                    "amount_with_tax": {"type": "number", "title": "价税合计", "description": "DECIMAL 18,2"},
                    "amount_with_tax_in_words": {"type": "string", "title": "价税合计（大写）", "maxLength": 100},
                    "settlement_method_code": {"type": "string", "title": "结算方式代码", "maxLength": 2},
                    "total_amount": {"type": "number", "title": "合计金额（合计不含税金额）", "description": "DECIMAL 18,2"},
                    "total_tax_amount": {"type": "number", "title": "合计税额", "description": "DECIMAL 18,2"},
                    "issuer_real_name_auth_location": {"type": "string", "title": "开票人实人认证地址信息", "maxLength": 100},
                    "mobile_invoice_location": {"type": "string", "title": "手机开票地址信息", "maxLength": 100},
                    "contract_no": {"type": "string", "title": "合同编号", "maxLength": 60},
                    "tax_obligation_occurrence_time": {"type": "string", "title": "纳税义务发生时间", "description": "YYYY-MM-DD HH:MI:SS", "maxLength": 17},
                    "agent_id_type_code": {"type": "string", "title": "经办人身份证件种类", "maxLength": 30},
                    "is_blue_invoice": {"type": "string", "title": "是否蓝字发票标志", "enum": ["Y", "N"], "maxLength": 1},
                    "vat_immediate_refund_code": {"type": "string", "title": "增值税即征即退代码", "maxLength": 2},
                    "remark": {"type": "string", "title": "备注", "maxLength": 300},
                    "goods_quantity": {"type": "number", "title": "商品数量", "description": "DECIMAL 18,4"},
                    "export_tax_refund_type_code": {"type": "string", "title": "出口退税类代码", "maxLength": 2},

                    # 货物信息数组
                    "items": {
                        "type": "array",
                        "title": "货物信息",
                        "items": {
                            "type": "object",
                            "properties": {
                                "sequence_no": {"type": "integer", "title": "序号"},
                                "item_name": {"type": "string", "title": "项目名称", "maxLength": 600},
                                "goods_or_service_name": {"type": "string", "title": "货物或应税劳务、服务名称", "maxLength": 300},
                                "item_short_name": {"type": "string", "title": "商品服务简称", "maxLength": 120},
                                "tax_classification_code": {"type": "string", "title": "商品和服务税收分类合并编码", "maxLength": 19},
                                "amount": {"type": "number", "title": "金额", "description": "DECIMAL 18,2"},
                                "tax_rate": {"type": "number", "title": "税率", "description": "DECIMAL 16,6"},
                                "tax_amount": {"type": "number", "title": "税额", "description": "DECIMAL 18,6"},
                                "deduction_amount": {"type": "number", "title": "扣除额", "description": "DECIMAL 18,2"}
                            },
                            "required": ["sequence_no", "tax_classification_code", "amount", "tax_rate", "tax_amount"]
                        }
                    },

                    # 铁路电子客票特定要素
                    "railway_specific_elements": {
                        "type": "object",
                        "title": "铁路电子客票特定要素",
                        "properties": {
                            "invoice_no": {"type": "string", "title": "发票号码", "maxLength": 30},
                            "invoice_date": {"type": "string", "title": "开票日期"},
                            "business_type_name": {"type": "string", "title": "业务类型名称", "maxLength": 300},
                            "departure_station": {"type": "string", "title": "出发站", "maxLength": 60},
                            "departure_station_pinyin": {"type": "string", "title": "出发站拼音", "maxLength": 60},
                            "arrival_station": {"type": "string", "title": "到达站", "maxLength": 60},
                            "arrival_station_pinyin": {"type": "string", "title": "到达站拼音", "maxLength": 60},
                            "train_no": {"type": "string", "title": "乘车车次", "maxLength": 20},
                            "travel_date": {"type": "string", "title": "日期"},
                            "departure_time": {"type": "string", "title": "出发时间", "maxLength": 5},
                            "railway_eticket_type_name": {"type": "string", "title": "铁路电子客票票种名称", "maxLength": 60},
                            "air_condition_flag": {"type": "string", "title": "空调特征", "maxLength": 20},
                            "seat_class": {"type": "string", "title": "席别", "maxLength": 20},
                            "carriage": {"type": "string", "title": "车厢", "maxLength": 20},
                            "seat_no": {"type": "string", "title": "席位", "maxLength": 60},
                            "payment_amount": {"type": "number", "title": "支付金额", "description": "DECIMAL 18,2"},
                            "refunded_amount": {"type": "number", "title": "已退金额", "description": "DECIMAL 18,2"},
                            "original_fare": {"type": "number", "title": "原票票价", "description": "DECIMAL 18,2"},
                            "original_departure_station": {"type": "string", "title": "原票出发站", "maxLength": 60},
                            "original_arrival_station": {"type": "string", "title": "原票到达站", "maxLength": 60},
                            "eticket_no": {"type": "string", "title": "电子客票号", "maxLength": 30},
                            "id_no": {"type": "string", "title": "证件号码", "maxLength": 30},
                            "passenger_name": {"type": "string", "title": "姓名", "maxLength": 150},
                            "railway_discount_type": {"type": "string", "title": "铁路客票优惠类型", "maxLength": 30},
                            "original_invoice_no": {"type": "string", "title": "原发票号码", "maxLength": 30}
                        },
                        "required": ["invoice_no", "invoice_date", "business_type_name", "payment_amount"]
                    }
                },
                "required": ["invoice_no", "is_paper_invoice", "invoice_date", "invoice_category_code", "seller_tax_no", "seller_name", "buyer_name", "is_blue_invoice"],
                "x-apifox-orders": [
                    "invoice_no", "is_paper_invoice", "invoice_date", "original_blue_invoice_no",
                    "invoice_category_code", "special_element_type_code", "buyer_tax_no", "buyer_name",
                    "buyer_address", "buyer_phone", "seller_tax_no", "seller_name", "seller_address",
                    "seller_phone", "buyer_agent_name", "agent_id_no", "agent_phone", "issuer",
                    "payee", "remitter", "amount_with_tax", "amount_with_tax_in_words",
                    "settlement_method_code", "total_amount", "total_tax_amount",
                    "issuer_real_name_auth_location", "mobile_invoice_location", "contract_no",
                    "tax_obligation_occurrence_time", "agent_id_type_code", "is_blue_invoice",
                    "vat_immediate_refund_code", "remark", "goods_quantity", "export_tax_refund_type_code",
                    "items", "railway_specific_elements"
                ],
                "title": "铁路电子客票数据",
                "description": "包含发票类型: 51-电子发票（铁路电子客票）"
            }
        }
    }

def fix_schemas(json_file):
    """修复JSON文件中的两个schema定义"""
    with open(json_file, 'r', encoding='utf-8') as f:
        api_doc = json.load(f)

    # 找到schemas并替换
    for schema_root in api_doc["schemaCollection"]:
        for item in schema_root.get("items", []):
            if item.get("name") == "ISV发票查验数据类型":
                schemas = item["items"]

                # 找到并替换航空运输客票
                for i, schema in enumerate(schemas):
                    if schema.get("id") == "#/definitions/223576039":
                        schemas[i] = create_complete_aviation_eticket_schema()
                        print("✓ 已替换航空运输客票电子行程单数据定义")
                    elif schema.get("id") == "#/definitions/223576040":
                        schemas[i] = create_complete_railway_eticket_schema()
                        print("✓ 已替换铁路电子客票数据定义")

                break

    # 保存修改后的文件
    with open(json_file, 'w', encoding='utf-8') as f:
        json.dump(api_doc, f, ensure_ascii=False, indent=2)

    print(f"\n✓ 已更新文件: {json_file}")

if __name__ == "__main__":
    fix_schemas("/Users/qinqiang02/colab/codespace/api_spec/isv/invoice_verification.apifox.json")
    print("\n🎉 修复完成！两个schema定义现在包含完整的货物信息和特定要素结构。")
