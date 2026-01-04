# 字段对应关系表

## 核心字段统一命名方案

### 主要金额字段

| 中文字段名 | 文档标识符 | **新字段名 (New Field Name)** | 旧字段名 (Old Field Name) | 说明 |
|----------|-----------|----------------------------|------------------------|------|
| 合计金额（不含税） | hjje | `amount_excluding_tax` | `total_untaxed_amount` | 合计不含税金额，DECIMAL 18,2 |
| 合计税额 | hjse | `tax_amount` | `total_tax_amount` | 合计税额，DECIMAL 18,2 |
| 价税合计 | jshj | `amount_including_tax` | `total_amount` | 价税合计（含税金额），DECIMAL 18,2 |
| 价税合计(大写) | jshjdx | `amount_in_words` | `amount_with_tax_in_words` | 价税合计大写，STRING |

### 机动车发票特殊字段

| 中文字段名 | 文档标识符 | **新字段名** | 旧字段名 | 说明 |
|----------|-----------|------------|---------|------|
| 税额（增值税税额） | se | `vat_tax_amount` | `tax_amount` | 机动车发票的增值税税额，与合计税额区分 |
| 不含税价 | bhsj | `price_without_tax` | `price_without_tax` | 不变 |

### 二手车发票特殊字段

| 中文字段名 | 文档标识符 | **新字段名** | 旧字段名 | 说明 |
|----------|-----------|------------|---------|------|
| 车价合计（不含税） | cjhj | `vehicle_price_total` | `vehicle_price_total` | 不变 |
| 车价合计大写 | - | `vehicle_price_total_in_words` | `vehicle_price_total_in_words` | 不变 |

## 已修改的发票类型

### 1. 数字化电子发票-增值税发票数据 (81/82/85/86)

**Schema位置**: invoice_verification.apifox.json 行 3092-4569

| 旧字段名 | 新字段名 | 中文名称 |
|---------|---------|---------|
| `total_untaxed_amount` | `amount_excluding_tax` | 合计金额（不含税） |
| `total_tax_amount` | `tax_amount` | 合计税额 |
| `total_amount` | `amount_including_tax` | 价税合计 |
| `amount_with_tax_in_words` | `amount_in_words` | 价税合计(大写) |

### 2. 数字化电子发票-机动车销售统一发票数据 (83/87)

**Schema位置**: invoice_verification.apifox.json 行 7194-7509

| 旧字段名 | 新字段名 | 中文名称 |
|---------|---------|---------|
| `total_untaxed_amount` | `amount_excluding_tax` | 合计金额（不含税） |
| `total_tax_amount` | `tax_amount` | 合计税额 |
| `total_amount` | `amount_including_tax` | 价税合计 |
| `amount_with_tax_in_words` | `amount_in_words` | 价税合计(大写) |
| `tax_amount` (车辆税额) | `vat_tax_amount` | 税额（增值税税额） |

**注意**: 机动车发票有两个税额字段，`tax_amount` 是合计税额，`vat_tax_amount` 是增值税税额。

### 3. 数字化电子发票-二手车销售统一发票数据 (84/88)

**Schema位置**: invoice_verification.apifox.json 行 7501-7900

| 旧字段名 | 新字段名 | 中文名称 |
|---------|---------|---------|
| `total_untaxed_amount` | `amount_excluding_tax` | 合计金额（不含税） |
| `total_tax_amount` | `tax_amount` | 合计税额 |
| `total_amount` | `amount_including_tax` | 价税合计 |
| `amount_with_tax_in_words` | `amount_in_words` | 价税合计(大写) |

### 4. 航空运输客票电子行程单数据 (61)

**Schema位置**: invoice_verification.apifox.json 行 6189-6708

| 旧字段名 | 新字段名 | 中文名称 |
|---------|---------|---------|
| `total_amount` | `amount_excluding_tax` | 合计金额（合计不含税金额） |
| `total_tax_amount` | `tax_amount` | 合计税额 |
| **新增** | `amount_including_tax` | 价税合计 |
| `amount_with_tax_in_words` | `amount_in_words` | 价税合计（大写） |

**注意**: 航空客票原本用 `total_amount` 表示不含税金额，这与其他发票相反！

## 映射文档需要修改的内容

### 所有数字化电子发票映射文档 (81/82/83/84/85/86/87/88)

需要将以下字段名统一更新：

1. `total_amount` → `amount_including_tax`（大部分发票）
2. `total_untaxed_amount` → `amount_excluding_tax`（如果有）
3. `total_tax_amount` → `tax_amount`
4. `amount_with_tax_in_words` → `amount_in_words`

### 航空运输客票映射文档 (51/61)

特别注意：
- 原 `total_amount` → `amount_excluding_tax`（与其他发票相反！）
- 需要添加 `amount_including_tax`

### 机动车发票映射文档 (03/83/87)

特别注意：
- 文档中的 `se` (税额) → `vat_tax_amount`
- 文档中的 `hjse` (合计税额) → `tax_amount`

## 命名规范说明

### 为什么选择这个命名方案？

1. **语义自解释**: `excluding_tax` vs `including_tax` 一目了然
2. **符合英语习惯**: Stripe, QuickBooks, Xero 等国际发票系统都用类似命名
3. **避免歧义**: `total_amount` 不明确是含税还是不含税
4. **AI友好**: GPT/Claude 等模型训练数据中大量包含这种命名模式

### 字段顺序建议

推荐按照以下顺序排列金额相关字段：

```json
{
  "amount_excluding_tax": 10000.00,  // 不含税金额
  "tax_amount": 1300.00,             // 税额
  "amount_including_tax": 11300.00,  // 含税金额 (= amount_excluding_tax + tax_amount)
  "amount_in_words": "壹万壹仟叁佰圆整" // 大写
}
```



以下发票类型也进行相关修改，你需逐个确认：

- 51 - 铁路电子客票
- 01 - 增值税专用发票
- 03 - 机动车销售统一发票
- 04 - 增值税普通发票
- 08 - 增值税电子专用发票
- 10 - 增值税电子普通发票
- 11 - 增值税普通发票（卷式）
- 14 - 增值税普通发票（通行费）
- 15 - 二手车销售统一发票
