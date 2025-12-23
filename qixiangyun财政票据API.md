# 企享云财政票据

## API Spec

https://openapi.qixiangyun.com/api-89495807

## 生产Sample

### 1

#### Requst body

```json
[
  {
    "cyList": [
      {
        "fpdm": "43060125",
        "xzpj": true,
        "kprq": "20251121",
        "je": "873.6",
        "fphm": "0118120003",
        "jym": "7b1c11"
      }
    ]
  }
]
```

#### Response

```json
[
  {
    "code": "2000",
    "success": true,
    "message": null,
    "data": [
      {
        "customReqId": "100021121e3a22f8df06412aa07da7cebb682df5",
        "czpjMxcx": false,
        "data": {
          "bz": null,
          "ch": "01",
          "chrq": null,
          "chsj": null,
          "chyy": null,
          "czbmyz": null,
          "czbmyzbh": null,
          "detailUrl": "https://fsgzfw.czt.hunan.gov.cn:8081/bill/billCheckShow.html?eInvoiceCode=43060125&eInvoiceNumber=0118120003&randomNumber=7b1c11&TotalAmount=873.6&IssueDate=2025-11-21&InvoicingPartyName=%E6%B9%96%E5%8D%97%E4%B8%AD%E5%8C%BB%E8%8D%AF%E5%A4%A7%E5%AD%A6%E7%AC%AC%E4%B8%80%E9%99%84%E5%B1%9E%E5%8C%BB%E9%99%A2&PayerPartyName=%E9%99%88%E5%BB%BA%E5%9B%BD&ticket_id=430601250118120003&is_switch=&is_rush=0&is_new=1",
          "dy": "01",
          "fhr": "苏蔚",
          "fpdm": "43060125",
          "fphm": "0118120003",
          "jehj": "873.60",
          "jehjcn": "捌佰柒拾叁圆陆角",
          "jkr": "陈建国",
          "jkrnsrsbh": "510102********8534",
          "jym": "7b1c11",
          "kprq": "2025-11-21",
          "pjmc": "湖南省医疗门诊收费票据（电子）",
          "qtxx": [
            {
              "cn": "业务流水号",
              "en": "ywlsh",
              "value": "20240202536380"
            },
            {
              "cn": "门诊号",
              "en": "mzh",
              "value": "25041404269"
            },
            {
              "cn": "就诊日期",
              "en": "jzrq",
              "value": "20250414"
            },
            {
              "cn": "医疗机构类型",
              "en": "yljglx",
              "value": "综合医院"
            },
            {
              "cn": "医保类型",
              "en": "yblx",
              "value": "国家医保"
            },
            {
              "cn": "医保编号",
              "en": "ybbh",
              "value": "43000019900000178421"
            },
            {
              "cn": "性别",
              "en": "xb",
              "value": "男"
            },
            {
              "cn": "医保统筹基金支付",
              "en": "ybtcjjzf",
              "value": "0.00"
            },
            {
              "cn": "其他支付",
              "en": "qtzf",
              "value": "0.00"
            },
            {
              "cn": "个人账户支付",
              "en": "grzhzf",
              "value": "0.00"
            },
            {
              "cn": "个人现金支付",
              "en": "grxjzf",
              "value": "873.60"
            },
            {
              "cn": "个人自付",
              "en": "grzfu",
              "value": "0.00"
            },
            {
              "cn": "个人自费",
              "en": "grzfe",
              "value": "0.00"
            }
          ],
          "rz": "",
          "skdw": "湖南中医药大学第一附属医院",
          "skr": "苏蔚",
          "xmmx": [],
          "xmqd": [
            {
              "bz": "",
              "dw": null,
              "ggbz": null,
              "je": "368.60",
              "sl": "",
              "xmbh": null,
              "xmmc": "西药费",
              "xmqdmc": null,
              "xmxh": null,
              "zfblv": null,
              "zfje": null,
              "zflx": null
            },
            {
              "bz": "",
              "dw": null,
              "ggbz": null,
              "je": "505.00",
              "sl": "",
              "xmbh": null,
              "xmmc": "中成药费",
              "xmqdmc": null,
              "xmxh": null,
              "zfblv": null,
              "zfje": null,
              "zflx": null
            }
          ]
        },
        "dq": "43",
        "fpdm": "43060125",
        "fphm": "0118120003",
        "fplx": "101",
        "je": 873.6,
        "jshj": null,
        "jym": "7b1c11",
        "kprq": "2025-11-21 00:00:00",
        "mxcxMessage": null,
        "success": true,
        "time": null,
        "times": 1
      }
    ],
    "timestamp": "2025-12-22 10:55:28",
    "reqId": "a78818435de6d4d147559937794eaa32"
  }
]
```

