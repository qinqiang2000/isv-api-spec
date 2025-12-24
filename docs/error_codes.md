## 错误处理

本节描述了 API 中错误是如何表示的、使用了哪些 HTTP 状态码，以及如何解释业务级别的错误代码。

该设计遵循 Stripe 和其他计费/发票平台等公共 API 所使用的常见模式（**HTTP 状态码**用于粗略的错误分类，**机器可读的** `code` 用于业务细节，**人类可读的** `message` 用于开发者）。

-----

## 1\. 错误对象模型

所有非 2xx 响应都在响应正文中返回一个标准的错误对象：

```json
{
  "error": {
    "code": "string",
    "message": "string",
    "type": "string",
    "param": "string",
    "details": { },
    "request_id": "string"
  }
}
```

### 字段

* **`error.code`** (string, required) 
  机器可读的错误代码，供客户端用于程序化处理 
  （例如 `tenant_not_found`、`etax_taxno_invalid`）。
* **`error.message`** (string, required) 
  **人类可读的**、对开发者友好的错误描述， 
  适合用于日志或用户界面（翻译后）。
* **`error.type`** (string, required) 
  错误的高级类别，用于快速判断失败原因。 
  可能的取值如下：
  * `invalid_request`  
    
    请求在语法上是有效的 HTTP，但参数缺失或无效。
  * `authentication_error` 
    凭证无效或已过期。
  * `permission_error` 
    调用者没有权限访问资源。
  * `business_error` 
    业务规则或下游服务（例如 ETAX）拒绝了操作。
  * `internal` 
    意外的内部错误。

* **`error.param`** (string, optional)
    当错误是字段特定时，与错误相关的参数名称（例如 `order_no`、`buyer_tax_no`、`X-Tenant-Id`）。

* **`error.details`** (object, optional)
    关于错误的结构化附加信息。
    例如，原始的 ETAX 错误代码，像 `retryable` 这样的标志，或验证细节：

```json   
"details": {     
    "etax_error_code": "ETAX_4001",
    "etax_error_message": "Taxpayer ID not found",
    "retryable": true   
}  
```

  * **`error.request_id`** (string, required)
      请求的唯一标识符，成功响应中也会返回。
      在联系支持人员或搜索日志时使用此字段。

> **重要提示：**
>
>   * 成功的响应**绝不能**包含 `error` 字段（甚至 `error: null` 也不行）。
>   * 错误响应**始终**遵循此结构，无论端点如何。

-----

## 2. HTTP 状态码

API 使用标准的 HTTP 状态码来指示请求是成功还是失败以及原因。

### 2.1 成功代码

  * **200 OK**
      请求成功。

  * **201 Created**
      成功创建了一个新资源（例如 订单、发票、ETAX 账户）。

### 2.2 客户端 / 业务错误代码

  * **400 Bad Request**
      请求由于参数缺失或格式错误而无效。
      示例 `error.type`：`invalid_request`。

  * **401 Unauthorized**
      身份验证失败（访问令牌无效或已过期）。
      示例 `error.type`：`authentication_error`。

  * **403 Forbidden**
      调用者已通过身份验证，但没有执行该操作的权限
      （例如，ISV 无法访问指定的租户或公司）。
      示例 `error.type`：`permission_error`。

  * **404 Not Found**
      请求的资源不存在，或对调用者不可见
      （例如 租户、公司、订单、发票或 ETAX 账户未找到）。
      示例 `error.type`：`invalid_request`。

  * **409 Conflict**
      资源的当前状态与请求的操作冲突
      （例如 重复的订单号，订单处于终结状态）。
      示例 `error.type`：`conflict`。

  * **422 Unprocessable Entity**
      请求在语法上有效，但因不满足业务规则而无法处理。
      这尤其用于**业务错误**，例如：
      * ETAX 验证失败（纳税人号码无效、购买方信息无效）
      * ETAX 开具失败（税务机关拒绝了发票）
      * 订单/发票域规则（例如 金额限制、配置不一致）
               示例 `error.type`：`business_error`。
      

### 2.3 服务器错误代码

  * **500 Internal Server Error**
      服务器端发生了意外错误。

  * **502 / 503 / 504 (optional)**
      在极少数情况下用于表示下游服务中断（例如 ETAX 不可用）。
      在许多情况下，这些可以被归一化为 `422`，其中 `error.type = "business_error"` 且 `details.retryable = true`，以便客户端一致地处理它们。

-----

## 3\. 全局错误代码

本节列出了可能出现在多个端点中的常用 `error.code` 值。

### 3.1 一般错误

| code                | HTTP | type                   | Description                            |
| ------------------- | ---- | ---------------------- | -------------------------------------- |
| `invalid_argument`  | 400  | `invalid_request`      | 参数缺失或格式错误。                   |
| `unauthenticated`   | 401  | `authentication_error` | 访问令牌无效或已过期。                 |
| `permission_denied` | 403  | `permission_error`     | 调用者没有权限。                       |
| `not_found`         | 404  | `invalid_request`      | 资源未找到。                           |
| `conflict`          | 409  | `conflict`             | 资源状态冲突。                         |
| `business_error`    | 422  | `business_error`       | 一般业务错误（详见 message/details）。 |
| `internal_error`    | 500  | `internal`             | 意外的内部服务器错误。                 |

### 3.2 多租户 / ISV 错误

| code                       | HTTP | type               | Description                 |
| -------------------------- | ---- | ------------------ | --------------------------- |
| `tenant_not_found`         | 404  | `invalid_request`  | 租户不存在或对 ISV 不可见。 |
| `tenant_not_belong_to_isv` | 403  | `permission_error` | 租户与当前的 ISV 不关联。   |
| `company_not_found`        | 404  | `invalid_request`  | 公司不存在或对 ISV 不可见。 |

-----

## 4\. 订单错误代码

针对订单相关端点（例如 `/isv/orders`）。

| code                       | HTTP | type              | Description                                   |
| -------------------------- | ---- | ----------------- | --------------------------------------------- |
| `order_not_found`          | 404  | `invalid_request` | 订单不存在。                                  |
| `order_conflict`           | 409  | `conflict`        | 重复的订单号或幂等性冲突。                    |
| `order_status_not_allowed` | 422  | `business_error`  | 当前订单状态不允许此操作（例如 终止或开票）。 |
| `order_already_closed`     | 409  | `conflict`        | 订单已处于终结状态。                          |

示例 – 重复的订单号：

```json
{
  "error": {
    "code": "order_conflict",
    "message": "Duplicate order_no: ISV-ORDER-001",
    "type": "conflict",
    "request_id": "req_1701937730123_44444444"
  }
}
```

-----

## 5\. ETAX / 发票错误代码

这些代码特定于 ETAX 账户和发票开具/验证。

### 5.1 ETAX 账户 / 登录

| code                      | HTTP | type             | Description                  |
| ------------------------- | ---- | ---------------- | ---------------------------- |
| `etax_account_invalid`    | 422  | `business_error` | ETAX 账户配置无效或已过期。  |
| `etax_login_failed`       | 422  | `business_error` | 使用给定账户登录 ETAX 失败。 |
| `etax_password_incorrect` | 422  | `business_error` | ETAX 用户名或密码不正确。    |

### 5.2 ETAX 验证与开具

| code                      | HTTP    | type             | Description                     |
| ------------------------- | ------- | ---------------- | ------------------------------- |
| `etax_taxno_invalid`      | 422     | `business_error` | 纳税人识别号无效。              |
| `etax_buyer_invalid`      | 422     | `business_error` | 购买方信息无效或不完整。        |
| `etax_issue_failed`       | 422     | `business_error` | ETAX 系统拒绝了发票开具请求。   |
| `etax_system_unavailable` | 422/503 | `business_error` | ETAX 服务暂时不可用；可以重试。 |
| `etax_timeout`            | 422     | `business_error` | 调用 ETAX API 时超时。          |

示例 – ETAX 验证失败：

```json
{
  "error": {
    "code": "etax_taxno_invalid",
    "message": "Invalid taxpayer identification number",
    "type": "business_error",
    "details": {
      "etax_error_code": "ETAX_4001",
      "etax_error_message": "Taxpayer ID not found"
    },
    "request_id": "req_1701937730123_55555555"
  }
}
```

-----

## 6\. 异步操作与业务失败

有些操作（例如 发票开具）可能是**异步的**：

  * 创建端点（例如 `POST /isv/invoices`）返回 `201 Created` 时，表示**作业已被接受**，而不是 ETAX 已完成处理。
  * 然后发票资源会公开一个 `status` 字段，例如：

  \* `PENDING` / `PROCESSING`
  \* `SUCCEEDED`
  \* `FAILED`

在此模型中：

  * HTTP `2xx` 表示**请求已被接受且作业已创建**。
  * 业务成功/失败由**资源状态**表示，而不是 HTTP 状态码。
  * 当 `status = "FAILED"` 时，资源包含失败元数据：

<!-- end list -->

```json
{
  "invoice_id": "inv_456",
  "status": "FAILED",
  "fail_code": "etax_issue_failed",
  "fail_message": "ETAX response: buyer taxpayer number is invalid",
  "fail_time": "2025-12-07T12:11:00Z"
}
```

> **经验法则**
>
>   * **同步业务失败** → 使用 HTTP `422` + `error` 对象。
>   * **异步业务失败** → 使用资源上的 `status = FAILED` 和失败字段。

-----

## 7\. 发票查验响应设计

发票查验接口（`/partners/invoice-verifications`）需要区分**技术成功/失败**和**业务查验结果**。

> **设计原则：**
>
> - **查验请求技术成功** → 返回 `200 OK` + 响应体中包含 `result_code` 字段描述业务结果。
> - **查验请求技术失败** → 返回非 `2xx` 状态码 + `error` 对象。

### 7.1 业务查验状态（200 OK）

查验请求技术成功时，返回 `200 OK`，响应体通过 `result_code` 字段表示业务结果：

| result_code | 名称             | 说明                                 |
| ----------- | ---------------- | ------------------------------------ |
| 00          | 成功             | 查验成功，发票信息与税局记录一致     |
| 01          | 失败             | 查验失败（技术或业务原因）           |
| 02          | 查无数据         | 税局无此发票记录                     |
| 03          | 查验不一致       | 发票要素与税局记录不符               |
| 04          | 非本单位开具或取得 | 发票的购买方或销售方与当前企业不匹配 |

**成功响应示例：**

```json
{
  "request_id": "req_1701937730123_12345678",
  "result_code": "00",
  "result_message": "查验成功",
  "invoice_type": "81",
  "verification_data": {
    "invoice_code": "1234567890",
    "invoice_no": "12345678",
    "seller_name": "北京XX科技有限公司",
    "seller_tax_no": "91110000XXXXXXXXXX",
    "buyer_name": "上海YY贸易有限公司",
    "buyer_tax_no": "91310000YYYYYYYYYY",
    "total_amount": "10000.00",
    "total_tax": "1300.00",
    "issue_date": "2024-12-20"
  }
}
```

> **注意：** 无论 `result_code` 为何值（00/01/02/03/04），只要查验请求被成功处理，都返回 `200 OK`。

---

### 7.2 技术错误代码（非 2xx）

以下错误用于**技术失败**或**阻止查验的业务规则**，返回对应的 HTTP 状态码 + `error` 对象。

| code                                  | HTTP | type              | Description                                      |
| ------------------------------------- | ---- | ----------------- | ------------------------------------------------ |
| `invoice_invalid_format`              | 400  | `invalid_request` | 发票信息不规范，请检查必填字段                    |
| `invoice_too_old`                     | 422  | `business_error`  | 该发票超出可查验期限（仅可查验一年内开具的发票）   |
| `verification_daily_limit_exceeded`   | 429  | `business_error`  | 该发票今日已达到税局查验次数上限（5次）           |
| `company_verification_limit_exceeded` | 429  | `business_error`  | 该企业已超过当前发票的当日查验次数限制            |
| `etax_service_unstable`               | 503  | `business_error`  | 当前税局网络不稳定，请稍后重试                    |
| `local_etax_service_unstable`         | 503  | `business_error`  | 地方税局网络暂时不可用，请稍后重试                |
| `invoice_type_not_supported`          | 422  | `business_error`  | 该发票类型暂不支持查验                            |

---

### 7.3 错误响应示例

**超过查验次数（429）：**

```json
{
  "error": {
    "code": "verification_daily_limit_exceeded",
    "message": "该发票今日已查验5次，超过税局当日查验次数限制，请明日再试",
    "type": "business_error",
    "details": {
      "daily_limit": 5,
      "current_count": 5,
      "reset_time": "2025-12-24T00:00:00Z"
    },
    "request_id": "req_1701937730123_77777777"
  }
}
```

-----

## 8\. 客户端集成指南

在与 API 集成时，客户端应：

1.  **首先检查 HTTP 状态码**
   * `2xx` → 视为**技术**成功（然后检查异步流程的业务状态）。
   * 非 `2xx` → 解析 `error` 对象。
   
2.  **使用 `error.code` 进行程序化处理**
   * 实现基于 `error.code` 的 `switch`/映射来驱动业务逻辑。
   * **不要**依赖匹配 `message` 文本。
   
3.  **记录 `request_id` 和 `error`**

   - 始终记录 `request_id`、`error.code` 和 `error.message` 以用于可观察性和支持。

4.  **使用 `details` 进行高级处理**
- 例如，使用 `details.retryable` 或 ETAX 特定的代码来决定是否重试。