# 发票云ISV领域字典表（精简版）

> **版本**: v1.0
> **更新日期**: 2024-12-24
> **适用范围**: 新API设计、数据库表设计、系统开发

---

## 一、领域字典术语表

### 1.1 发票核心标识字段

| 中文名 | 英文字段名 | 数据类型 | 长度 | 业务定义 |
|--------|-----------|---------|------|---------|
| 发票类型 | invoice_type | string | 2-3 | 发票的票种分类代码（01-88, F1等） |
| 发票代码 | invoice_code | string | 10-12 | 税务机关分配的发票代码，纸质发票必有 |
| 发票号码 | invoice_number | string | 8-20 | 发票的唯一编号，所有发票必有 |
| 开票日期 | issue_date | string | 8-10 | 发票开具的日期（YYYYMMDD或YYYY-MM-DD） |
| 校验码 | verification_code | string | 20 | 发票查验的后6位或20位校验码 |
| 税控码 | tax_control_code | string | 84 | 税控设备生成的防伪码（可选） |
| 发票状态 | invoice_status | integer | 1 | 发票当前状态（0-8）|
| 是否蓝字发票 | is_blue_invoice | string | 1 | 是否为蓝字发票：Y-是，N-否（红字） |

### 1.2 交易主体字段

| 中文名 | 英文字段名 | 数据类型 | 长度 | 业务定义 |
|--------|-----------|---------|------|---------|
| 销方名称 | seller_name | string | 1-100 | 销售方（开票方）企业名称 |
| 销方税号 | seller_tax_no | string | 15-20 | 销售方纳税人识别号（统一社会信用代码） |
| 销方地址电话 | seller_address_phone | string | - | 销售方地址和电话（可选） |
| 销方银行账号 | seller_bank_account | string | - | 销售方开户银行及账号（可选） |
| 销方纳税人类型 | seller_taxpayer_type_code | string | 1 | 1-一般纳税人，2-小规模纳税人，3-5其他 |
| 购方名称 | buyer_name | string | 1-100 | 购买方（受票方）企业名称 |
| 购方税号 | buyer_tax_no | string | 15-20 | 购买方纳税人识别号 |
| 购方地址电话 | buyer_address_phone | string | - | 购买方地址和电话（可选） |
| 购方银行账号 | buyer_bank_account | string | - | 购买方开户银行及账号（可选） |
| 代开销方税号 | proxy_seller_tax_no | string | 15-20 | 代开发票时真实销售方的税号 |
| 代开销方名称 | proxy_seller_name | string | 1-100 | 代开发票时真实销售方的名称 |

### 1.3 金额税费字段

| 中文名 | 英文字段名 | 数据类型 | 长度 | 业务定义 |
|--------|-----------|---------|------|---------|
| 价税合计 | total_amount | number | - | 含税总金额（amount + tax_amount） |
| 不含税金额 | amount | number | - | 不含税的商品或服务金额 |
| 税额 | tax_amount | number | - | 增值税税额 |
| 税率 | tax_rate | number/string | - | 增值税税率（如0.13, 0.09, 0.06等） |
| 含税税率标识 | tax_rate_flag | integer | 1 | 0-不含税税率，1-含税税率，2-差额征税 |
| 零税率标识 | zero_tax_rate_flag | string | 1 | 空/0-出口退税/1-免税/2-不征税/3-普通零税率 |

### 1.4 发票明细字段

| 中文名 | 英文字段名 | 数据类型 | 长度 | 业务定义 |
|--------|-----------|---------|------|---------|
| 明细序号 | sequence_no | integer | - | 发票明细行的序号（从1开始） |
| 商品编码 | product_code | string | - | 税收分类编码或商品编码 |
| 商品名称 | product_name | string | 1-100 | 商品或服务名称 |
| 规格型号 | specification | string | - | 商品的规格型号（可选） |
| 单位 | unit | string | - | 商品的计量单位 |
| 数量 | quantity | number | - | 商品数量 |
| 单价 | unit_price | number | - | 商品不含税单价 |
| 明细金额 | item_amount | number | - | 明细行不含税金额 |
| 明细税率 | item_tax_rate | number/string | - | 明细行税率 |
| 明细税额 | item_tax_amount | number | - | 明细行税额 |

### 1.5 机动车/二手车特有字段

| 中文名 | 英文字段名 | 数据类型 | 长度 | 业务定义 |
|--------|-----------|---------|------|---------|
| 车架号 | vehicle_identification_no | string | 17 | 车辆识别代号VIN码 |
| 发动机号 | engine_no | string | - | 发动机编号 |
| 厂牌型号 | product_model | string | - | 车辆品牌和型号 |
| 车辆类型 | vehicle_type_code | string | - | 车辆类型代码 |
| 车价 | vehicle_price | number | - | 车辆价格含价外费用 |
| 合格证号 | compliance_no | string | - | 车辆合格证书号 |
| 进口证明书号 | import_no | string | - | 进口车辆的证明书号 |
| 抵扣标志 | deduction_flag | string | 1 | 是否可抵扣标志 |

### 1.6 业务流程字段

| 中文名 | 英文字段名 | 数据类型 | 长度 | 业务定义 |
|--------|-----------|---------|------|---------|
| 订单号 | order_no | string | - | 业务订单编号 |
| 内部订单号 | inner_order_no | string | - | 系统内部订单号 |
| 租户ID | tenant_id | string | - | 多租户系统的租户标识 |
| 企业ID | enterprise_id | string | - | 企业主体标识 |
| 电子税局账号ID | etax_account_id | string | - | 电子税局账号标识 |
| 查验请求ID | request_id | string | - | 发票查验请求的唯一标识 |
| 查验结果代码 | result_code | string | 2 | 00-成功/01-失败/02-查无数据/03-不一致/04-非本单位 |
| 查验结果消息 | result_message | string | - | 查验结果的文字描述 |

### 1.7 日期时间字段

| 中文名 | 英文字段名 | 数据类型 | 长度 | 业务定义 |
|--------|-----------|---------|------|---------|
| 创建时间 | created_at | string/timestamp | - | 记录创建的时间戳 |
| 更新时间 | updated_at | string/timestamp | - | 记录最后更新的时间戳 |
| 激活时间 | activated_at | string/timestamp | - | 订单或账号激活时间 |
| 关闭时间 | closed_at | string/timestamp | - | 订单或任务关闭时间 |
| 账单开始日期 | billing_start_date | string | 10 | 账单周期开始日期（YYYY-MM-DD） |
| 账单周期天数 | billing_duration_days | integer | - | 账单周期的天数 |

---

## 二、枚举值字典

### 2.1 发票类型（invoice_type）

| 枚举值 | 中文名称 | 适用说明 |
|--------|---------|---------|
| 01 | 增值税专用发票 | 纸质专票，一般纳税人开具 |
| 02 | 货物运输业增值税专用发票 | 运输行业专用（已较少使用） |
| 03 | 机动车销售统一发票 | 新车销售发票 |
| 04 | 增值税普通发票 | 纸质普票 |
| 08 | 增值税电子专用发票 | 电子版专票 |
| 10 | 增值税电子普通发票 | 电子版普票 |
| 11 | 增值税普通发票（卷式） | 卷式纸质发票 |
| 14 | 增值税电子普通发票（通行费） | 高速公路通行费电子发票 |
| 15 | 二手车销售统一发票 | 二手车交易发票 |
| 51 | 电子发票（铁路电子客票） | 铁路客运电子票 |
| 61 | 电子发票（航空运输电子客票行程单） | 航空客运电子票 |
| 81 | 电子发票（增值税专用发票） | 数电专票 |
| 82 | 电子发票（普通发票） | 数电普票 |
| 83 | 电子发票（机动车销售统一发票） | 数电机动车发票 |
| 84 | 电子发票（二手车销售统一发票） | 数电二手车发票 |
| 85 | 纸质发票（增值税专用发票） | 数电纸质专票 |
| 86 | 纸质发票（普通发票） | 数电纸质普票 |
| 87 | 纸质发票（机动车销售统一发票） | 数电纸质机动车发票 |
| 88 | 纸质发票（二手车销售统一发票） | 数电纸质二手车发票 |
| F1 | 财政票据 | 政府非税收入票据 |

### 2.2 发票状态（invoice_status）

| 枚举值 | 中文名称 | 说明 |
|--------|---------|------|
| 0 | 正常 | 发票正常有效 |
| 1 | 失控 | 发票失控（仅纸票，已较少使用） |
| 2 | 作废 | 发票已作废（仅纸票） |
| 3 | 红冲 | 发票已红冲（仅纸票） |
| 4 | 异常 | 发票异常（已较少使用） |
| 5 | 非正常 | 发票非正常（已较少使用） |
| 6 | 红字发票待确认 | 红字申请待确认 |
| 7 | 部分红冲 | 发票部分金额被红冲 |
| 8 | 全额红冲 | 数电发票全额红冲 |

### 2.3 发票状态标识（invoice_status_flag）- 传统增值税发票

| 枚举值 | 中文名称 | 说明 |
|--------|---------|------|
| 0 | 正数票 | 正常的正数发票 |
| 1 | 负数票 | 红字负数发票 |
| 2 | 空白作废发票 | 未开具前作废 |
| 3 | 正数作废发票 | 正数票开具后作废 |
| 4 | 负数作废发票 | 负数票开具后作废 |

### 2.4 特殊票种（special_invoice_type）

| 枚举值 | 中文名称 |
|--------|---------|
| 02 | 农产品收购发票 |
| 03 | 稀土矿产品发票 |
| 04 | 稀土产成品发票 |
| 05 | 石脑油发票 |
| 08 | 成品油发票 |
| 20 | 会员单位投资性黄金发票 |
| 21 | 会员单位非投资性黄金发票 |
| 22 | 客户标准黄金发票 |

### 2.5 纳税人类型（seller_taxpayer_type_code）

| 枚举值 | 中文名称 | 说明 |
|--------|---------|------|
| 1 | 一般纳税人 | 可开具增值税专用发票 |
| 2 | 小规模纳税人 | 通常开具普通发票 |
| 3 | 其他类型纳税人 | 特殊类型 |
| 4 | 扣缴义务人 | 代扣代缴 |
| 5 | 个体工商户 | 个体经营者 |

### 2.6 查验结果代码（result_code）

| 枚举值 | 中文名称 | 说明 |
|--------|---------|------|
| 00 | 查验成功 | 发票信息一致 |
| 01 | 查验失败 | 查验过程失败 |
| 02 | 查无此票 | 税务系统无此发票记录 |
| 03 | 查验不一致 | 提交信息与税务记录不一致 |
| 04 | 非本单位发票 | 发票不属于查验企业 |

### 2.7 含税税率标识（tax_rate_flag）

| 枚举值 | 中文名称 |
|--------|---------|
| 0 | 不含税税率 |
| 1 | 含税税率 |
| 2 | 差额征税 |

### 2.8 零税率标识（zero_tax_rate_flag）

| 枚举值 | 中文名称 |
|--------|---------|
| (空) | 非零税率 |
| 0 | 出口退税 |
| 1 | 出口免税和其他免税 |
| 2 | 不征税 |
| 3 | 普通零税率 |

### 2.9 财政票据冲红标志（red_reversal_flag）

| 枚举值 | 中文名称 |
|--------|---------|
| 01 | 正常票据 |
| 02 | 冲红票据 |

### 2.10 财政票据打印状态（print_status）

| 枚举值 | 中文名称 |
|--------|---------|
| 01 | 未打印 |
| 02 | 已打印 |

### 2.11 财政票据入账状态（accounting_status）

| 枚举值 | 中文名称 |
|--------|---------|
| 01 | 未入账 |
| 02 | 已入账 |

---

## 三、新旧API对照表

### 3.1 发票类型编码对照（开具API vs 查验API）

| 开具API编码 | 查验API编码 | 发票名称 |
|------------|------------|---------|
| 26 | 82 | 电子发票（普通发票） |
| 27 | 81 | 电子发票（增值税专用发票） |
| 3 | 03 | 机动车销售统一发票 |
| 4 | 04 | 增值税普通发票 |
| 12 | 08 | 增值税电子专用发票 |
| 13 | 10 | 增值税电子普通发票 |
| 83 | 83 | 电子发票（机动车销售统一发票） |
| 84 | 84 | 电子发票（二手车销售统一发票） |

**建议**: 新系统统一使用查验API的标准编码（01-88, F1体系）

### 3.2 发票状态字段对照

| 旧字段名 | 新字段名 | 建议 |
|---------|---------|------|
| invoice_status_flag | invoice_status | 新系统使用invoice_status（0-8）|
| red_reversal_flag | invoice_status | 财政票据也统一使用invoice_status |

### 3.3 发票号码字段对照

| 旧字段名 | 新字段名 | 建议 |
|---------|---------|------|
| paper_invoice_no | invoice_number | 统一使用invoice_number |
| bill_no | invoice_number | 统一使用invoice_number |
| used_vehicle_invoice_no | invoice_number | 统一使用invoice_number |

### 3.4 金额字段对照

| 旧字段名 | 新字段名 | 含义 |
|---------|---------|------|
| invoice_amount | amount | 不含税金额 |
| vehicle_price | total_amount | 价税合计（机动车特殊情况） |

---

## 四、使用说明

### 4.1 字段命名规范

1. **统一使用snake_case命名**: 所有字段名使用小写字母+下划线
2. **主体字段前缀**: seller_（销方）、buyer_（购方）、proxy_（代开）
3. **金额字段后缀**: _amount（金额）、_price（价格）
4. **时间字段后缀**: _at（时间点）、_date（日期）

### 4.2 数据库表设计建议

```sql
-- 发票主表示例
CREATE TABLE invoices (
  id BIGINT PRIMARY KEY,
  invoice_type VARCHAR(3) NOT NULL,
  invoice_code VARCHAR(12),
  invoice_number VARCHAR(20) NOT NULL,
  issue_date VARCHAR(10) NOT NULL,
  invoice_status TINYINT DEFAULT 0,
  seller_tax_no VARCHAR(20) NOT NULL,
  buyer_tax_no VARCHAR(20),
  total_amount DECIMAL(15,2) NOT NULL,
  amount DECIMAL(15,2),
  tax_amount DECIMAL(15,2),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  INDEX idx_invoice_number (invoice_number),
  INDEX idx_seller_tax_no (seller_tax_no),
  INDEX idx_issue_date (issue_date)
);

-- 发票明细表示例
CREATE TABLE invoice_items (
  id BIGINT PRIMARY KEY,
  invoice_id BIGINT NOT NULL,
  sequence_no INT NOT NULL,
  product_code VARCHAR(50),
  product_name VARCHAR(100) NOT NULL,
  quantity DECIMAL(15,4),
  unit_price DECIMAL(15,6),
  item_amount DECIMAL(15,2),
  item_tax_rate VARCHAR(10),
  item_tax_amount DECIMAL(15,2),
  FOREIGN KEY (invoice_id) REFERENCES invoices(id)
);
```

### 4.3 API响应示例

```json
{
  "invoice_type": "82",
  "invoice_number": "23372000000012345678",
  "issue_date": "20231224",
  "invoice_status": 0,
  "seller_name": "北京XX科技有限公司",
  "seller_tax_no": "91110108XXXXXXXXXX",
  "buyer_name": "上海YY贸易有限公司",
  "buyer_tax_no": "91310115XXXXXXXXXX",
  "total_amount": 11300.00,
  "amount": 10000.00,
  "tax_amount": 1300.00,
  "items": [
    {
      "sequence_no": 1,
      "product_name": "技术服务费",
      "quantity": 1,
      "unit_price": 10000.00,
      "item_amount": 10000.00,
      "item_tax_rate": "0.13",
      "item_tax_amount": 1300.00
    }
  ]
}
```

---

## 附录：核心字段统计

- **总字段数**: 57个
- **核心标识字段**: 8个
- **交易主体字段**: 11个
- **金额税费字段**: 6个
- **发票明细字段**: 10个
- **特有字段**: 8个（机动车/二手车）
- **业务流程字段**: 8个
- **日期时间字段**: 6个

- **枚举类型**: 11类
- **发票类型**: 20种
- **发票状态**: 9种（标准）+ 5种（传统）
