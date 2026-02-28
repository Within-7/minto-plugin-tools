---
description: 飞书集成命令 - 创建多维表格、管理权限、添加数据
args:
  - name: action
    description: 操作类型（create_table/add_data/add_permission/test）
    required: true
  - name: table_name
    description: 表格名称（创建表格时需要）
    required: false
  - name: table_type
    description: 表格类型（crm/project/inventory/expense/purchase）
    required: false
---

# 飞书集成命令

飞书（Feishu/Lark）多维表格管理助手。

## 可用操作

### 1. 创建多维表格
```
/feishu-integration create_table <table_name> --type=<table_type>
```

**支持的表格类型：**
- `crm` - 客户关系管理系统
- `project` - 项目任务管理系统
- `inventory` - 库存管理系统
- `expense` - 费用报销系统
- `purchase` - 采购订单管理系统

**示例：**
```
/feishu-integration create_table 客户管理系统 --type=crm
/feishu-integration create_table 项目任务表 --type=project
/feishu-integration create_table 采购订单表 --type=purchase
```

### 2. 添加数据到表格
```
/feishu-integration add_data <app_token> <table_id>
```

**示例：**
```
/feishu-integration add_data app_xxxxx table_xxxxx
```

### 3. 添加协作者权限
```
/feishu-integration add_permission <app_token> <user_email> --perm=<permission>
```

**权限类型：**
- `view` - 仅查看
- `edit` - 编辑
- `full_access` - 完全管理

**示例：**
```
/feishu-integration add_permission app_xxxxx user@example.com --perm=edit
```

### 4. 测试连接
```
/feishu-integration test
```

验证飞书API连接状态。

## 工作流程

### 创建完整的多维表格系统

1. **验证连接**
   - 使用 `get_tenant_access_token` 确认API可用

2. **创建多维表格**
   - 调用 `create_bitable` 创建应用
   - 获取返回的 `app_token`

3. **设计表格结构**
   - 调用 `get_tables` 获取 `table_id`
   - 调用 `add_table_field` 添加所需字段
   - 配置字段类型和选项

4. **添加初始数据**
   - 调用 `add_record` 插入示例数据

5. **设置权限**
   - 调用 `get_user_by_email` 获取用户ID
   - 调用 `add_collaborator` 添加协作者

## MCP工具说明

本命令优先使用以下MCP工具：

### 认证工具
- `mcp__feishu__get_tenant_access_token` - 获取访问令牌

### 表格管理
- `mcp__feishu__create_bitable` - 创建多维表格
- `mcp__feishu__get_tables` - 获取数据表列表
- `mcp__feishu__add_table_field` - 添加字段

### 数据操作
- `mcp__feishu__add_record` - 添加记录
- `mcp__feishu__get_records` - 获取记录

### 权限管理
- `mcp__feishu__add_collaborator` - 添加协作者
- `mcp__feishu__get_user_by_email` - 通过邮箱查找用户

## 字段类型参考

| 类型值 | 类型名称 | 用途 |
|--------|----------|------|
| 1 | text | 文本（姓名、描述等） |
| 2 | number | 数字（金额、数量等） |
| 3 | select | 单选（状态、类型等） |
| 4 | multiSelect | 多选（标签、技能等） |
| 5 | dateTime | 日期时间 |
| 7 | attachment | 附件 |
| 11 | phone | 电话号码 |
| 12 | email | 邮箱 |
| 13 | url | 网址链接 |
| 15 | progress | 进度条（0-100%） |

## 配置要求

确保以下环境变量已配置：
- `FEISHU_APP_ID` - 飞书应用ID
- `FEISHU_APP_SECRET` - 飞书应用密钥

获取方式：访问 https://open.feishu.cn 创建应用并获取凭证。

## 示例场景

### 创建客户管理系统
```
用户: /feishu-integration create_table CRM系统 --type=crm

执行步骤:
1. 创建多维表格 "CRM系统"
2. 添加字段：客户名称、联系人、电话、客户阶段、成交金额
3. 配置单选选项：潜在客户/意向客户/谈判中/已成交
4. 添加示例数据
5. 添加当前用户为管理员
6. 返回表格链接
```

### 创建项目任务表
```
用户: /feishu-integration create_table 项目管理 --type=project

执行步骤:
1. 创建多维表格 "项目管理系统"
2. 创建"项目列表"表：项目名称、状态、进度、负责人
3. 创建"任务列表"关联表：任务名称、所属项目、负责人、截止时间
4. 设置两个表的关联关系
5. 添加示例项目和任务
6. 返回双表结构说明
```

## 注意事项

1. **权限配置**：首次使用需在飞书开放平台启用相关权限
2. **Token保存**：创建的 `app_token` 需保存以便后续操作
3. **批量操作**：大量数据操作建议使用Python脚本
4. **错误处理**：API返回错误时检查权限配置和Token有效期

## 参考资源

- [飞书开放平台文档](https://open.feishu.cn/document)
- [多维表格API](https://open.feishu.cn/document/server-docs/docs/bitable-v1/app-list)
- [权限管理API](https://open.feishu.cn/document/server-docs/docs/permission-v2/permission/add_member)
