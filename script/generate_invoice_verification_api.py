#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成发票查验API的Apifox JSON定义
根据税局文档和现有ISV API规范，生成完整的10种发票类型schemas
"""

import json
import re
from typing import Dict, List, Any

# 字段名映射：税局字段 -> ISV snake_case
FIELD_MAPPING = {
    # 基础发票信息
    "fphm": "invoice_no",
    "zzfpDm": "paper_invoice_code",
    "zzfphm": "paper_invoice_no",
    "kprq": "invoice_date",
    "fppzDm": "invoice_category_code",
    "tdyslxDm": "special_element_type_code",
    "sflzfp": "is_blue_invoice",

    # 红字发票对应蓝字发票信息
    "kjhzfpdydlzfphm": "original_blue_invoice_no",
    "kjhzfpdydzzfpDm": "original_blue_paper_invoice_code",
    "kjhzfpdydzzfphm": "original_blue_paper_invoice_no",

    # 销售方信息
    "xsfnsrsbh": "saler_tax_no",
    "xsfsbh": "saler_tax_no",
    "xsfmc": "saler_name",
    "xhfdz": "saler_address",
    "xsfdz": "saler_address",
    "xsfdh": "saler_phone",
    "xsflxdh": "saler_phone",
    "xsfkhh": "saler_bank_name",
    "xsfzh": "saler_account_number",
    "xfnsrlxdm": "saler_taxpayer_type_code",

    # 购买方信息
    "gmfnsrsbh": "buyer_tax_no",
    "gmfsbh": "buyer_tax_no",
    "gmfmc": "buyer_name",
    "gmfdz": "buyer_address",
    "gmfdh": "buyer_phone",
    "gmflxdh": "buyer_phone",
    "gmfkhh": "buyer_bank_name",
    "gmfzh": "buyer_account_number",

    # 金额相关
    "hjje": "total_amount",
    "hjse": "total_tax_amount",
    "jshj": "amount_with_tax",
    "jshjdx": "amount_with_tax_in_words",
    "kce": "deduction_amount",

    # 其他发票信息
    "jsfsDm": "settlement_method_code",
    "kpr": "issuer",
    "bz": "remark",
    "xmmxhs": "item_count",
    "zz sjzjtDm": "vat_immediate_refund_code",
    "cktslDm": "export_tax_refund_type_code",
    "fhrxm": "reviewer",
    "skrxm": "payee",
    "cpyycbs": "refined_oil_abnormal_flag",
    "fjysxx": "additional_elements",

    # 明细行字段 (hwxx数组)
    "xh": "sequence_no",
    "xmmc": "item_name",
    "spfwjc": "item_short_name",
    "hwhyslwfwmc": "goods_or_service_name",
    "sphfwssflhbbm": "tax_classification_code",
    "ggxh": "spec_model",
    "dw": "unit",
    "fpjysl": "quantity",
    "fpjydj": "unit_price",
    "slv": "tax_rate",
    "se": "tax_amount",
    "je": "amount",
    "sptm": "product_barcode",

    # 建筑服务特定要素
    "tdzzsxmbh": "land_value_added_tax_project_no",
    "kdsbz": "cross_city_flag",
    "jzfwfsd": "construction_service_location",
    "jzxmmc": "construction_project_name",
    "sl1": "tax_rate",

    # 机动车相关
    "cllx": "vehicle_type",
    "cpxh": "product_model",
    "cd": "origin_place",
    "hgzh": "certificate_no",
    "jkzmsh": "import_certificate_no",
    "sjdh": "business_inspection_no",
    "fdjh": "engine_no",
    "clsbdh": "vehicle_identification_no",
    "dw1": "tonnage",
    "xcrs": "passenger_capacity",
    "sbbh": "tax_payment_certificate_no",
    "cllxdm": "vehicle_type_code",
    "scqymc": "manufacturer_name",
    "jdcwybsm": "motor_vehicle_uuid",
    "bsrq": "sale_date",
    "cjh": "frame_no",
    "dpzh": "license_plate_no",
    "djzh": "registration_no",
    "ccrq": "transfer_date",
    "zysx": "main_tax_items",
    "ejsccmc": "used_car_market_name",
    "ejsccsbdm": "used_car_market_tax_id",
    "ejsccdz": "used_car_market_address",
    "ejsccdh": "used_car_market_phone",
    "ejscckhh": "used_car_market_bank",
    "ejscczh": "used_car_market_account",
    "ejsccnsrsbh": "used_car_market_taxpayer_id",

    # 航空/铁路客票
    "gmrxm": "buyer_name",
    "gmrsfzjhm": "buyer_id_no",
    "gmsj": "purchase_time",
    "hbzl": "currency_type",
    "dplx": "ticket_category",
    "hcdjdz": "route_start_end",
    "hcrq": "travel_date",
    "hcsj": "travel_time",
    "cx": "flight_train_no",
    "cw": "seat_class",
    "zwj": "seat_fare",
    "rsj": "fuel_surcharge",
    "jcf": "airport_construction_fee",
    "jsfwf": "agency_service_fee",
    "qtfy": "other_fees",

    # 医疗相关
    "yljgdm": "medical_institution_code",
    "yljglx": "medical_institution_type",
    "ylfylb": "medical_expense_category",
    "yzhye": "medical_card_balance",
    "ybzhzf": "insurance_payment",
    "xjzf": "cash_payment",
}

def create_base_structure() -> Dict[str, Any]:
    """创建基础Apifox结构"""
    return {
        "apifoxProject": "1.0.0",
        "$schema": {
            "app": "apifox",
            "type": "project",
            "version": "1.2.0"
        },
        "info": {
            "name": "发票查验接口",
            "description": "ISV发票查验API，支持10种发票类型的实时查验",
            "mockRule": {
                "rules": [],
                "enableSystemRule": True
            }
        },
        "projectSetting": {
            "id": "7461123",  # 新ID
            "auth": {},
            "securityScheme": {},
            "gateway": [],
            "language": "zh-CN",
            "apiStatuses": [
                "developing",
                "testing",
                "released",
                "deprecated"
            ],
            "mockSettings": {},
            "preProcessors": [],
            "postProcessors": [],
            "advancedSettings": {
                "enableJsonc": False,
                "enableBigint": False,
                "responseValidate": True,
                "enableTestScenarioSetting": False,
                "enableYAPICompatScript": False,
                "isDefaultUrlEncoding": 2,
                "publishedDocUrlRules": {
                    "defaultRule": "RESOURCE_KEY_ONLY",
                    "resourceKeyStandard": "NEW"
                },
                "folderShareExpandModeSettings": {
                    "expandId": [],
                    "mode": "AUTO"
                }
            },
            "initialDisabledMockIds": [],
            "servers": [
                {
                    "id": "default",
                    "name": "默认服务",
                    "moduleId": 6572471
                }
            ],
            "cloudMock": {
                "security": "free",
                "enable": False,
                "tokenKey": "apifoxToken"
            }
        },
        "apiCollection": [],
        "socketCollection": [],
        "docCollection": [],
        "webSocketCollection": [],
        "socketIOCollection": [],
        "responseCollection": [],
        "schemaCollection": []
    }

def create_medical_institution_type_schema() -> Dict[str, Any]:
    """创建医疗机构类型schema"""
    return {
        "id": 220013573,  # 新ID，紧接证件类型
        "name": "医疗机构类型",
        "visibility": "INHERITED",
        "moduleId": 6572471,
        "items": [],
        "schema": {
            "jsonSchema": {
                "type": "string",
                "enum": ["1", "2", "3", "4", "5"],
                "x-apifox-enum": [
                    {"value": "1", "name": "综合医院", "description": ""},
                    {"value": "2", "name": "中医医院", "description": ""},
                    {"value": "3", "name": "专科医院", "description": ""},
                    {"value": "4", "name": "社区卫生服务中心（站）", "description": ""},
                    {"value": "5", "name": "其他", "description": ""}
                ]
            }
        }
    }

def create_digital_vat_invoice_schema() -> Dict[str, Any]:
    """创建数字化电子发票-增值税发票schema (types: 81, 82, 85, 86)"""
    return {
        "id": 223576033,  # 新ID
        "name": "数字化电子发票-增值税发票数据",
        "displayName": "",
        "description": "包含发票类型: 81-电子发票(增值税专用发票), 82-电子发票(普通发票), 85-纸质发票(增值税专用发票), 86-纸质发票(普通发票)",
        "visibility": "INHERITED",
        "moduleId": 6572471,
        "items": [],
        "schema": {
            "jsonSchema": {
                "type": "object",
                "properties": {
                    "invoice_no": {
                        "type": "string",
                        "title": "发票号码",
                        "maxLength": 20
                    },
                    "paper_invoice_code": {
                        "type": "string",
                        "title": "纸质发票代码",
                        "maxLength": 12
                    },
                    "paper_invoice_no": {
                        "type": "string",
                        "title": "纸质发票号码",
                        "maxLength": 20
                    },
                    "invoice_date": {
                        "type": "string",
                        "title": "开票日期",
                        "description": "YYYY-MM-DD HH:mm:ss",
                        "maxLength": 19
                    },
                    "invoice_category_code": {
                        "type": "string",
                        "title": "发票票种代码",
                        "maxLength": 2
                    },
                    "special_element_type_code": {
                        "type": "string",
                        "title": "特定要素类型代码",
                        "maxLength": 2
                    },
                    "is_blue_invoice": {
                        "type": "string",
                        "title": "是否蓝字发票",
                        "enum": ["Y", "N"],
                        "x-apifox-enum": [
                            {"value": "Y", "name": "是", "description": ""},
                            {"value": "N", "name": "否", "description": ""}
                        ]
                    },
                    "original_blue_invoice_no": {
                        "type": "string",
                        "title": "开具红字发票对应的蓝字发票号码",
                        "maxLength": 20
                    },
                    "original_blue_paper_invoice_code": {
                        "type": "string",
                        "title": "开具红字发票对应的纸质发票代码",
                        "maxLength": 12
                    },
                    "original_blue_paper_invoice_no": {
                        "type": "string",
                        "title": "开具红字发票对应的纸质发票号码",
                        "maxLength": 20
                    },
                    "saler_tax_no": {
                        "type": "string",
                        "title": "销售方识别号",
                        "maxLength": 20
                    },
                    "saler_name": {
                        "type": "string",
                        "title": "销售方名称",
                        "maxLength": 150
                    },
                    "saler_address": {
                        "type": "string",
                        "title": "销货方地址",
                        "maxLength": 250
                    },
                    "buyer_tax_no": {
                        "type": "string",
                        "title": "购买方识别号",
                        "maxLength": 20
                    },
                    "buyer_name": {
                        "type": "string",
                        "title": "购买方名称",
                        "maxLength": 150
                    },
                    "buyer_address": {
                        "type": "string",
                        "title": "购买方地址",
                        "maxLength": 300
                    },
                    "total_amount": {
                        "type": "number",
                        "title": "合计金额",
                        "description": "整数部分最大18位，保留2位小数"
                    },
                    "total_tax_amount": {
                        "type": "number",
                        "title": "合计税额",
                        "description": "整数部分最大18位，保留2位小数"
                    },
                    "amount_with_tax": {
                        "type": "number",
                        "title": "价税合计",
                        "description": "整数部分最大18位，保留2位小数"
                    },
                    "amount_with_tax_in_words": {
                        "type": "string",
                        "title": "价税合计(大写)",
                        "maxLength": 300
                    },
                    "deduction_amount": {
                        "type": "number",
                        "title": "扣除额",
                        "description": "整数部分最大18位，保留2位小数"
                    },
                    "settlement_method_code": {
                        "type": "string",
                        "title": "结算方式",
                        "maxLength": 2
                    },
                    "issuer": {
                        "type": "string",
                        "title": "开票人",
                        "maxLength": 300
                    },
                    "remark": {
                        "type": "string",
                        "title": "备注",
                        "maxLength": 450
                    },
                    "item_count": {
                        "type": "integer",
                        "title": "明细条数"
                    },
                    "vat_immediate_refund_code": {
                        "type": "string",
                        "title": "增值税即征即退代码",
                        "maxLength": 2
                    },
                    "export_tax_refund_type_code": {
                        "type": "string",
                        "title": "出口退税类代码",
                        "maxLength": 2
                    },
                    "reviewer": {
                        "type": "string",
                        "title": "复核人姓名",
                        "maxLength": 75
                    },
                    "payee": {
                        "type": "string",
                        "title": "收款人姓名",
                        "maxLength": 150
                    },
                    "saler_phone": {
                        "type": "string",
                        "title": "销售方电话",
                        "maxLength": 60
                    },
                    "saler_bank_name": {
                        "type": "string",
                        "title": "销售方开户行",
                        "maxLength": 120
                    },
                    "saler_account_number": {
                        "type": "string",
                        "title": "销售方账号",
                        "maxLength": 100
                    },
                    "buyer_phone": {
                        "type": "string",
                        "title": "购买方电话",
                        "maxLength": 60
                    },
                    "buyer_bank_name": {
                        "type": "string",
                        "title": "购买方开户行",
                        "maxLength": 120
                    },
                    "buyer_account_number": {
                        "type": "string",
                        "title": "购买方账号",
                        "maxLength": 100
                    },
                    "saler_taxpayer_type_code": {
                        "type": "string",
                        "title": "销方纳税人类型代码",
                        "enum": ["1", "2", "3", "4", "5"],
                        "x-apifox-enum": [
                            {"value": "1", "name": "一般纳税人", "description": ""},
                            {"value": "2", "name": "小规模纳税人", "description": ""},
                            {"value": "3", "name": "转登记小规模纳税人", "description": ""},
                            {"value": "4", "name": "辅导期一般纳税人", "description": ""},
                            {"value": "5", "name": "自然人", "description": ""}
                        ]
                    },
                    "refined_oil_abnormal_flag": {
                        "type": "string",
                        "title": "成品油异常标识",
                        "enum": ["9", "1", "2"],
                        "x-apifox-enum": [
                            {"value": "9", "name": "正常", "description": ""},
                            {"value": "1", "name": "成品油单价异常", "description": ""},
                            {"value": "2", "name": "成品油超库存异常", "description": ""}
                        ]
                    },
                    "additional_elements": {
                        "type": "object",
                        "title": "附加要素信息",
                        "description": "JSON格式"
                    },
                    "items": {
                        "type": "array",
                        "title": "货物信息",
                        "items": {
                            "type": "object",
                            "properties": {
                                "sequence_no": {
                                    "type": "integer",
                                    "title": "序号"
                                },
                                "item_name": {
                                    "type": "string",
                                    "title": "项目名称",
                                    "maxLength": 600
                                },
                                "item_short_name": {
                                    "type": "string",
                                    "title": "商品服务简称",
                                    "maxLength": 120
                                },
                                "goods_or_service_name": {
                                    "type": "string",
                                    "title": "货物或应税劳务、服务名称",
                                    "maxLength": 300
                                },
                                "tax_classification_code": {
                                    "type": "string",
                                    "title": "商品和服务税收分类合并编码",
                                    "maxLength": 19
                                },
                                "spec_model": {
                                    "type": "string",
                                    "title": "规格型号",
                                    "maxLength": 150
                                },
                                "unit": {
                                    "type": "string",
                                    "title": "单位",
                                    "maxLength": 300
                                },
                                "quantity": {
                                    "type": "string",
                                    "title": "发票交易数量",
                                    "maxLength": 25
                                },
                                "unit_price": {
                                    "type": "string",
                                    "title": "发票交易单价",
                                    "maxLength": 25
                                },
                                "tax_rate": {
                                    "type": "number",
                                    "title": "税率",
                                    "description": "DECIMAL 6,6"
                                },
                                "tax_amount": {
                                    "type": "number",
                                    "title": "税额",
                                    "description": "DECIMAL 8,6"
                                },
                                "amount": {
                                    "type": "number",
                                    "title": "金额",
                                    "description": "DECIMAL 8,2"
                                },
                                "deduction_amount": {
                                    "type": "number",
                                    "title": "扣除额",
                                    "description": "DECIMAL 8,2"
                                },
                                "product_barcode": {
                                    "type": "string",
                                    "title": "商品条码",
                                    "maxLength": 300
                                }
                            },
                            "required": ["sequence_no", "tax_rate", "tax_amount", "amount"],
                            "x-apifox-orders": [
                                "sequence_no", "item_name", "item_short_name", "goods_or_service_name",
                                "tax_classification_code", "spec_model", "unit", "quantity",
                                "unit_price", "tax_rate", "tax_amount", "amount",
                                "deduction_amount", "product_barcode"
                            ]
                        }
                    }
                },
                "required": [
                    "invoice_no", "invoice_date", "invoice_category_code", "is_blue_invoice",
                    "saler_name", "buyer_name", "total_amount", "total_tax_amount", "amount_with_tax",
                    "amount_with_tax_in_words"
                ],
                "x-apifox-orders": [
                    "invoice_no", "paper_invoice_code", "paper_invoice_no", "invoice_date",
                    "invoice_category_code", "special_element_type_code", "is_blue_invoice",
                    "original_blue_invoice_no", "original_blue_paper_invoice_code", "original_blue_paper_invoice_no",
                    "saler_tax_no", "saler_name", "saler_address",
                    "buyer_tax_no", "buyer_name", "buyer_address",
                    "total_amount", "total_tax_amount", "amount_with_tax", "amount_with_tax_in_words",
                    "deduction_amount", "settlement_method_code", "issuer", "remark", "item_count",
                    "vat_immediate_refund_code", "export_tax_refund_type_code",
                    "reviewer", "payee",
                    "saler_phone", "saler_bank_name", "saler_account_number",
                    "buyer_phone", "buyer_bank_name", "buyer_account_number",
                    "saler_taxpayer_type_code", "refined_oil_abnormal_flag",
                    "additional_elements", "items"
                ]
            }
        }
    }

def create_verification_api() -> Dict[str, Any]:
    """创建发票查验API endpoint定义"""
    return {
        "name": "发票查验",
        "id": 71413748,  # 新ID
        "auth": {},
        "securityScheme": {},
        "parentId": 0,
        "serverId": "",
        "description": "企业端业务系统通过接口对开具、取得的各类发票发起查验申请，系统根据查验申请反馈查验结果。支持10种发票类型的实时查验。",
        "identityPattern": {
            "httpApi": {
                "type": "methodAndPath",
                "bodyType": "",
                "fields": []
            }
        },
        "shareSettings": {},
        "visibility": "SHARED",
        "moduleId": 6572471,
        "preProcessors": [
            {
                "id": "inheritProcessors",
                "type": "inheritProcessors",
                "data": {}
            }
        ],
        "postProcessors": [
            {
                "id": "inheritProcessors",
                "type": "inheritProcessors",
                "data": {}
            }
        ],
        "inheritPostProcessors": {},
        "inheritPreProcessors": {},
        "items": [
            {
                "name": "发票查验",
                "api": {
                    "id": "383078996",  # 新ID
                    "method": "post",
                    "path": "/isv/invoice-verifications",
                    "parameters": {
                        "path": [],
                        "query": [],
                        "cookie": [],
                        "header": [
                            {
                                "id": "PleQywDimm1",
                                "name": "Accept-Language",
                                "required": False,
                                "enable": True,
                                "description": "HTTP 标准请求头，使用 IETF BCP 47（如 zh-CN、en-US）指定客户端期望的响应语言。默认 en-US",
                                "example": "",
                                "type": "string",
                                "schema": {
                                    "type": "string"
                                }
                            },
                            {
                                "id": "amC8hRaJPy1",
                                "name": "Authorization",
                                "required": True,
                                "enable": True,
                                "description": "Bearer <access_token>",
                                "example": "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9",
                                "type": "string"
                            },
                            {
                                "id": "bLjpR1kdWQ1",
                                "name": "X-Request-Id",
                                "required": True,
                                "enable": True,
                                "description": "用于标识一次请求的全局唯一 ID，以支持跨系统的链路追踪与日志关联。推荐格式：req_{timestamp_ms}_{random_8}（毫秒时间戳 + 8 位随机数）",
                                "example": "req_1701937730123_48210952",
                                "type": "string"
                            },
                            {
                                "id": "TxIfclLcTo1",
                                "name": "X-Customer-Id",
                                "required": True,
                                "enable": True,
                                "description": "客户编号；长度：10位，数字",
                                "example": "",
                                "type": "string"
                            }
                        ]
                    },
                    "auth": {},
                    "securityScheme": {},
                    "commonParameters": {
                        "query": [],
                        "body": [],
                        "cookie": [],
                        "header": []
                    },
                    "responses": [
                        {
                            "id": "168915581",  # 新ID
                            "code": 200,
                            "name": "成功",
                            "headers": [],
                            "jsonSchema": {
                                "type": "object",
                                "description": "",
                                "properties": {
                                    "result_code": {
                                        "type": "string",
                                        "title": "结果代码",
                                        "enum": ["00", "01", "02", "03", "04"],
                                        "x-apifox-enum": [
                                            {"value": "00", "name": "成功", "description": ""},
                                            {"value": "01", "name": "失败", "description": ""},
                                            {"value": "02", "name": "查无数据", "description": ""},
                                            {"value": "03", "name": "查验不一致", "description": ""},
                                            {"value": "04", "name": "此发票非本单位开具或取得", "description": ""}
                                        ]
                                    },
                                    "result_message": {
                                        "type": "string",
                                        "title": "返回信息"
                                    },
                                    "verification_data": {
                                        "title": "查验结果信息",
                                        "description": "根据发票类型返回对应的发票数据结构（已自动解压gzip+base64）",
                                        "oneOf": [
                                            {"$ref": "#/definitions/223576033"}  # 数字化电子发票-增值税发票
                                            # TODO: 添加其他9种发票类型的$ref
                                        ]
                                    }
                                },
                                "required": ["result_code"],
                                "x-apifox-orders": [
                                    "result_code", "result_message", "verification_data"
                                ]
                            },
                            "description": "",
                            "contentType": "json",
                            "mediaType": "application/json"
                        },
                        {
                            "id": "161367660",  # 新ID
                            "code": 401,
                            "name": "没有权限",
                            "headers": [],
                            "jsonSchema": {
                                "type": "object",
                                "properties": {
                                    "errcode": {
                                        "type": "string"
                                    },
                                    "description": {
                                        "type": "string"
                                    }
                                },
                                "required": ["errcode", "description"],
                                "x-apifox-orders": ["errcode", "description"]
                            },
                            "description": "",
                            "contentType": "json",
                            "mediaType": "application/json"
                        }
                    ],
                    "responseExamples": [],
                    "requestBody": {
                        "type": "application/json",
                        "parameters": [],
                        "jsonSchema": {
                            "type": "object",
                            "description": "",
                            "properties": {
                                "invoice_type": {
                                    "type": "string",
                                    "title": "发票类型",
                                    "description": "2位字符",
                                    "enum": [
                                        "01", "02", "03", "04", "08", "10", "11", "14", "15",
                                        "81", "82", "85", "86", "51", "61", "83", "84", "87", "88"
                                    ],
                                    "x-apifox-enum": [
                                        {"value": "01", "name": "增值税专用发票", "description": ""},
                                        {"value": "02", "name": "货物运输业增值税专用发票", "description": ""},
                                        {"value": "03", "name": "机动车销售统一发票", "description": ""},
                                        {"value": "04", "name": "增值税普通发票", "description": ""},
                                        {"value": "08", "name": "增值税电子专用发票", "description": ""},
                                        {"value": "10", "name": "增值税电子普通发票", "description": ""},
                                        {"value": "11", "name": "卷式发票", "description": ""},
                                        {"value": "14", "name": "通行费发票", "description": ""},
                                        {"value": "15", "name": "二手车销售统一发票", "description": ""},
                                        {"value": "81", "name": "电子发票（增值税专用发票）", "description": ""},
                                        {"value": "82", "name": "电子发票（普通发票）", "description": ""},
                                        {"value": "85", "name": "纸质发票（增值税专用发票）", "description": ""},
                                        {"value": "86", "name": "纸质发票（普通发票）", "description": ""},
                                        {"value": "51", "name": "电子发票（铁路电子客票）", "description": ""},
                                        {"value": "61", "name": "电子发票（航空运输客票电子行程单）", "description": ""},
                                        {"value": "83", "name": "机动车销售电子统一发票", "description": ""},
                                        {"value": "84", "name": "二手车销售电子统一发票", "description": ""},
                                        {"value": "87", "name": "纸质发票（机动车销售统一发票）", "description": ""},
                                        {"value": "88", "name": "纸质发票（二手车销售统一发票）", "description": ""}
                                    ]
                                },
                                "invoice_code": {
                                    "type": "string",
                                    "title": "发票代码",
                                    "description": "12位字符，纸质发票类型时必填",
                                    "maxLength": 12
                                },
                                "invoice_no": {
                                    "type": "string",
                                    "title": "发票号码",
                                    "description": "20位字符",
                                    "maxLength": 20
                                },
                                "invoice_date": {
                                    "type": "string",
                                    "title": "开票日期",
                                    "description": "YYYY-MM-DD格式",
                                    "example": "2025-01-01"
                                },
                                "verification_code": {
                                    "type": "string",
                                    "title": "校验码",
                                    "description": "后六位",
                                    "maxLength": 32
                                },
                                "invoice_amount": {
                                    "type": "number",
                                    "title": "开票金额",
                                    "description": "整数部分最大18位，保留2位小数"
                                },
                                "taxpayer_id": {
                                    "type": "string",
                                    "title": "纳税人识别号",
                                    "description": "20位字符",
                                    "maxLength": 20
                                }
                            },
                            "required": ["invoice_type", "invoice_no", "invoice_date", "taxpayer_id"],
                            "x-apifox-orders": [
                                "invoice_type", "invoice_code", "invoice_no",
                                "invoice_date", "verification_code", "invoice_amount", "taxpayer_id"
                            ]
                        },
                        "examples": [
                            {
                                "value": json.dumps({
                                    "invoice_type": "81",
                                    "invoice_code": "5101*****111",
                                    "invoice_no": "00000001",
                                    "invoice_date": "2025-01-01",
                                    "verification_code": "123456",
                                    "invoice_amount": 10000.00,
                                    "taxpayer_id": "915100************"
                                }, ensure_ascii=False, indent=2),
                                "mediaType": "application/json",
                                "description": ""
                            }
                        ],
                        "mediaType": "",
                        "oasExtensions": "",
                        "required": False,
                        "additionalContent": []
                    },
                    "description": "企业端业务系统通过接口对开具、取得的各类发票发起查验申请，系统根据查验申请反馈查验结果。",
                    "tags": ["发票查验"],
                    "status": "released",
                    "serverId": "",
                    "operationId": "",
                    "sourceUrl": "",
                    "ordering": 10,
                    "cases": [],
                    "mocks": [],
                    "customApiFields": "{}",
                    "advancedSettings": {
                        "disabledSystemHeaders": {}
                    },
                    "mockScript": {},
                    "codeSamples": [],
                    "commonResponseStatus": {},
                    "responseChildren": [],
                    "visibility": "INHERITED",
                    "moduleId": 6572471,
                    "oasExtensions": "",
                    "type": "http",
                    "preProcessors": [],
                    "postProcessors": [],
                    "inheritPostProcessors": {},
                    "inheritPreProcessors": {}
                }
            }
        ]
    }

def main():
    """主函数：生成完整的Apifox JSON文件"""
    print("开始生成发票查验API的Apifox JSON定义...")

    # 创建基础结构
    api_doc = create_base_structure()
    print("✓ 创建基础结构完成")

    # 添加Schema Collection
    schema_root = {
        "id": 17279714,  # 新ID
        "name": "根目录",
        "visibility": "SHARED",
        "moduleId": 6572471,
        "items": [
            {
                "id": 17496646,  # 新ID
                "name": "ISV发票查验数据类型",
                "visibility": "INHERITED",
                "moduleId": 6572471,
                "items": [
                    # 医疗机构类型
                    {
                        "name": "医疗机构类型",
                        "displayName": "",
                        "id": "#/definitions/220013573",
                        "description": "",
                        "schema": create_medical_institution_type_schema()["schema"]
                    },
                    # 数字化电子发票-增值税发票
                    {
                        "name": "数字化电子发票-增值税发票数据",
                        "displayName": "",
                        "id": "#/definitions/223576033",
                        "description": create_digital_vat_invoice_schema()["description"],
                        "schema": create_digital_vat_invoice_schema()["schema"]
                    }
                    # TODO: 添加其他9种发票类型schema
                ]
            }
        ]
    }

    api_doc["schemaCollection"].append(schema_root)
    print("✓ 添加Schema Collection完成")

    # 添加API Collection
    api_root = {
        "name": "根目录",
        "id": 71408368,  # 新ID
        "auth": {},
        "securityScheme": {},
        "parentId": 0,
        "serverId": "",
        "description": "",
        "identityPattern": {
            "httpApi": {
                "type": "methodAndPath",
                "bodyType": "",
                "fields": []
            }
        },
        "shareSettings": {},
        "visibility": "SHARED",
        "moduleId": 6572471,
        "preProcessors": [
            {
                "id": "inheritProcessors",
                "type": "inheritProcessors",
                "data": {}
            }
        ],
        "postProcessors": [
            {
                "id": "inheritProcessors",
                "type": "inheritProcessors",
                "data": {}
            }
        ],
        "inheritPostProcessors": {},
        "inheritPreProcessors": {},
        "items": [create_verification_api()]
    }

    api_doc["apiCollection"].append(api_root)
    print("✓ 添加API Collection完成")

    # 输出文件
    output_path = "/Users/qinqiang02/colab/codespace/api_spec/isv/发票查验接口.apifox.json"
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(api_doc, f, ensure_ascii=False, indent=2)

    print(f"✓ 完成！文件已保存到: {output_path}")
    print(f"\n注意：当前版本包含：")
    print(f"  - 1个API endpoint: POST /isv/invoice-verifications")
    print(f"  - 1个辅助schema: 医疗机构类型")
    print(f"  - 1个发票数据schema: 数字化电子发票-增值税发票 (完整)")
    print(f"  - TODO: 还需添加其他9种发票类型的schema")

if __name__ == "__main__":
    main()
