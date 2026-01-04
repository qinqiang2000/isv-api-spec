# 金蝶发票云API 设计规范（Internal Standard）v1.2

## 0. 总体概述

### 0.1 适用范围

本规范适用于金蝶发票云所有对外及对内 HTTP API，包括但不限于：

- ISV / 伙伴接口
- 客户直连 API
- 内部 BFF(Backend For Frontend) / Gateway API
- 对税局及第三方系统的对外暴露接口

------

### 0.2 设计取向与遵循实践

本规范统一遵循以下业界成熟实践，并做了收敛与约束：

- Resource-Oriented REST API
- Stripe / OpenAI 风格 API 设计
- Google / Microsoft API Guidelines（裁剪版）
- OpenAPI 3.x 可生成 SDK 友好设计
- AI-First API Design（面向 GPT 等模型稳定生成客户端代码）

**核心目标：**API 结构高度确定、低歧义，使 AI 无需理解业务即可稳定生成正确调用代码。

------

## 1. URL Path（Endpoint）设计规范

### 1.1 资源导向原则

- Path 必须表达“资源”，而非行为
- 使用名词，不使用动词
- 通过层级关系表达资源归属

**示例：**

```
/orders
/orders/{order_id}
/orders/{order_id}/items
/etax-accounts/{account_id}
```

------

### 1.2 Path 命名风格（强制）

- 全小写
- 使用 **kebab-case（短横线 `-`）**
- 禁止使用 `_`
- 禁止 camelCase
- 禁止 get / query / do 等前缀

**正例：**

```
/invoice-items
/etax-accounts
/orders/{order_id}/activate
```

**反例：**

```
/invoice_items
/invoiceItems
/getOrder
```

------

### 1.3 动作型 Endpoint（Action Endpoint）

当业务语义无法用 CRUD 表达时，允许使用动作型接口：

**统一规则：**

```
POST /{resource}/{id}/{action}
```

**示例：**

```
POST /orders/{order_id}/activate
POST /orders/{order_id}/close
POST /orders/{order_id}/cancel
POST /etax-accounts/{account_id}/verify
POST /invoices/{invoice_id}/submit
```

约束：

- action 必须为动词
- 仅用于状态变化或业务行为
- 不得出现动词 + 名词混合资源

------

### 1.4 批量操作规范

#### 批量创建

```
POST /orders
```

#### 批量删除（强制使用 POST）

```
POST /invoice-items/delete
```

原因：避免 DELETE Body 在部分网关 / SDK 中的不兼容问题。

------

## 2. HTTP Method 使用规范

| **操作** | **Method** | **说明**          |
| -------- | ---------- | ----------------- |
| 创建     | POST       | 返回创建后的资源  |
| 查询单个 | GET        | 返回资源          |
| 查询列表 | GET / POST | 复杂条件允许 POST |
| 全量更新 | PUT        | 覆盖式更新        |
| 局部更新 | PATCH      | 推荐方式          |
| 单个删除 | DELETE     | 仅限单个          |
| 批量删除 | POST       | `/xxx/delete`     |

------

## 3. Header 规范（多租户 SaaS）

### 3.1 多租户身份

多租户 / 企业身份 **必须通过 Header 传递**：

```
X-Tenant-Id
X-Customer-Id
```

规则：

- Header 中出现 → Body 中禁止重复
- Body 只承载业务字段

------

### 3.2 鉴权与身份解耦

```
Authorization: Bearer <token>
```

- token 标识调用方（ISV / 应用）
- tenant / customer 标识业务归属
- 二者必须解耦

------

## 4. 字段（JSON Key）命名规范

### 4.1 命名风格（强制）

- JSON 字段统一使用 **snake_case**
- 禁止 camelCase

**示例：**

JSON

```
{
  "order_id": "ord_1",
  "created_at": "2025-01-01T10:00:00Z"
}
```

------

### 4.2 ID 字段规范

- 主键统一为 `{resource}_id`

```
order_id
invoice_id
item_id
tenant_id
```

禁止使用：

```
id
orderId
orderID
```

------

### 4.3 时间字段规范

- 时间格式统一为 ISO 8601（UTC）

```
2025-01-01T10:00:00Z
```

------

## 5. 请求 / 响应结构规范

### 5.1 成功响应（禁止 error）

#### 单资源返回（平铺）

JSON

```
{
  "request_id": "req_xxx",
  "order_id": "ord_1",
  "status": "CREATED"
}
```

------

#### 列表返回

JSON

```
{
  "request_id": "req_xxx",
  "items": [
    { "order_id": "ord_1" }
  ],
  "pagination": {
    "page": 1,
    "page_size": 20,
    "total": 42,
    "has_more": true
  }
}
```

------

### 5.2 request_id

- 所有响应必须包含
- 用于日志、链路追踪、问题排查

------

## 6. 错误模型（Error Model）

### 6.1 统一错误结构

JSON

```
{
  "error": {
    "code": "invalid_argument",
    "message": "page_size must be <= 100",
    "type": "invalid_request",
    "request_id": "req_xxx"
  }
}
```

------

### 6.2 HTTP Status Code 规范

| **场景**               | **HTTP** |
| ---------------------- | -------- |
| 参数错误               | 400      |
| 未认证                 | 401      |
| 权限不足               | 403      |
| 资源不存在             | 404      |
| 状态冲突               | 409      |
| 业务校验失败（含税局） | 422      |
| 内部系统错误           | 500      |
| 系统不可用             | 503      |

说明：

- 税局失败优先使用 422
- 异步失败通过 `status = FAILED` 表达，不使用 HTTP error

------

### 6.3 错误码稳定性

- `error.code` 属于 API 契约
- 不得随意修改或复用
- 全局错误码 + 业务模块子集扩展

------

### 6.4 资源不存在处理规范（业界最佳实践）

为了确保 AI 客户端生成的调用代码具备最高稳定性，并符合全球主流 API（如 Stripe, GitHub）的设计直觉，必须严格区分“特定资源查询”与“集合搜索”：

1. **查询单个特定资源 (GET /resource/{id})**
   - **状态码**：**404 Not Found**
   - **场景**：URL 路径中指定了明确的 `id`，但数据库查无此类资源。
   - **逻辑**：此 URL 指向的实体不存在。返回 404 可让 AI 和 SDK 自动触发“异常处理”逻辑（如 `NotFoundException`），避免处理无效数据。
2. **按条件搜索或列出资源 (GET /resource?filter=xxx)**
   - **状态码**：**200 OK**
   - **响应结构**：`"items": []`
   - **场景**：查询条件（如状态、时间范围）有效，但目前没有符合条件的资源。
   - **逻辑**：请求的“集合资源”是存在的，只是结果为空集。返回 200 可确保客户端直接使用 `.map()` 或 `.length` 等数组方法，而不会因为 404 导致程序逻辑中断。

**总结**：URL 里带 ID 没找到给 404；URL 里没带 ID（列表/搜索）没找到给 200 + 空数组。

------

## 7. 明确禁止项（硬性规则）

- 成功响应中禁止出现：

  ```
  code / msg / success / error / error: null
  ```

- Body 中禁止出现：

  ```
  tenant_id / customer_id
  ```

- Path 中禁止：

  ```
  getXxx / doXxx / queryXxx
  ```

------

## 8. 一句话规范总结

> 成功只返回资源，失败只返回 error；
>
> Path 用 kebab-case，JSON 用 snake_case；
>
> 业务枚举大写，错误码小写；
>
> 多租户在 Header，request_id 必带。

## 附录：API 设计评审 Checklist（精简版）

- [ ] 命名统一

  Path 使用小写 + kebab-case，资源名使用复数；

  JSON 字段使用 snake_case，主键命名为 {resource}_id。

- [ ] HTTP Method 正确

  Create=POST / Query=GET / Update=PATCH（或 PUT）/ Delete=DELETE；

  批量删除统一使用 POST /xxx/delete。

- [ ] 动作型接口规范

  状态或业务行为类操作统一使用

  POST /{resource}/{id}/{action}。

- [ ] 多租户与鉴权

  租户/企业身份仅通过 Header 传递（不进入 Body）；

  Authorization 与租户身份解耦。

- [ ] 响应结构干净

  成功响应仅返回资源数据及 request_id；

  列表返回统一使用 items + pagination。

- [ ] 枚举与错误区分

  业务枚举值使用全大写；

  error.code 使用小写 snake_case，作为稳定错误标识符。

- [ ] 错误模型与状态码

  统一 error 响应结构；

  业务及税局校验失败统一使用 HTTP 422。

------

### 一票否决项（命中即不通过）

- [ ] 成功响应中出现 `error` / `code` / `msg`
- [ ] Request Body 中包含租户或企业标识
- [ ] Path 中出现 `get / do / query` 等动词前缀
