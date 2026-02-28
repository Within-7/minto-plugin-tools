# 飞书 MCP 服务器

为飞书（Feishu/Lark）API 提供的 MCP (Model Context Protocol) 服务器实现。

## 功能特性

MCP 服务器提供了以下工具和资源：

### 工具（Tools）

- `get_tenant_access_token` - 获取飞书访问令牌
- `create_bitable` - 创建多维表格应用
- `get_tables` - 获取数据表列表
- `add_table_field` - 添加字段
- `add_record` - 添加记录
- `get_records` - 获取记录
- `add_collaborator` - 添加协作者
- `get_user_by_email` - 通过邮箱获取用户信息

### 资源（Resources）

- `feishu://config` - 当前飞书配置信息

## 安装步骤

### 1. 安装依赖

```bash
cd mcp-server
npm install
```

### 2. 配置环境变量

在 `.mcp.json` 文件中配置你的飞书应用凭证：

```json
{
  "mcpServers": {
    "feishu": {
      "command": "node",
      "args": ["./mcp-server/index.js"],
      "env": {
        "FEISHU_APP_ID": "your_app_id",
        "FEISHU_APP_SECRET": "your_app_secret"
      }
    }
  }
}
```

### 3. 添加到 Minto

```bash
minto mcp add feishu node /Users/mac/Desktop/test/feishu-integration/mcp-server/index.js
```

或使用 JSON 配置：

```bash
minto mcp add-json feishu '{"command": "node", "args": ["/Users/mac/Desktop/test/feishu-integration/mcp-server/index.js"], "env": {"FEISHU_APP_ID": "cli_a9e4652af5f89cca", "FEISHU_APP_SECRET": "4OazKFCmZTT4cjlwK0ecAhr3eAaJ7dhH"}}'
```

### 4. 验证安装

```bash
minto mcp list
```

## 使用示例

### 创建多维表格

```
使用 MCP 工具 create_bitable 创建一个名为"测试表格"的多维表格
```

### 添加记录

```
使用 MCP 工具 add_record 向表格添加一条记录，字段为 {"名字": "张三", "标题": "测试", "阅读量": 100}
```

### 添加协作者

```
使用 get_user_by_email 查找用户邮箱，然后使用 add_collaborator 添加为协作者
```

## 字段类型说明

| 类型值 | 类型名称 | 说明 |
|--------|----------|------|
| 1 | text | 文本 |
| 2 | number | 数字 |
| 3 | select | 单选 |
| 4 | multiSelect | 多选 |
| 5 | dateTime | 日期 |
| 7 | attachment | 附件 |
| 11 | phone | 电话 |
| 12 | email | 邮箱 |
| 13 | url | 网址 |
| 15 | progress | 进度 |

## 权限类型说明

- `view` - 仅查看
- `edit` - 编辑权限
- `full_access` - 完全管理权限

## 依赖项

- `@modelcontextprotocol/sdk` - MCP SDK
- `axios` - HTTP 客户端

## 开发

运行开发模式：

```bash
npm run dev
```

## 故障排除

### 无法连接 MCP 服务器

1. 检查 Node.js 是否已安装
2. 确认依赖已安装：`npm install`
3. 验证环境变量是否正确设置
4. 查看服务器日志：`minto mcp get feishu`

### API 调用失败

1. 验证 FEISHU_APP_ID 和 FEISHU_APP_SECRET 是否正确
2. 确认飞书应用已启用所需权限
3. 检查网络连接
