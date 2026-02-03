---
name: feishu-integration
description: 飞书（Feishu/Lark）API集成指南。当用户要求"创建飞书应用"、"管理多维表格"、"添加协作者"、"生成飞书报表"、"设置飞书权限"或"自动化飞书操作"时使用。涵盖多维表格创建、权限管理、数据可视化、文档操作和常见飞书自动化模式。
---

# 飞书集成技能

飞书（Feishu/Lark）API集成和自动化综合指南。

## 插件结构

本插件遵循 Claude Code 插件格式：

- **plugin.json**: 插件清单
- **.claude-plugin/**: 内部插件配置
- **SKILL.md**: 本技能文档
- **commands/**: 用户调用的斜杠命令
- **scripts/**: 飞书 API 自动化脚本
- **assets/**: 模板和资源

## Quick Start

### 1. 设置凭证

确保你有有效的飞书应用凭证：
- `APP_ID`: 飞书应用ID
- `APP_SECRET`: 飞书应用密钥

### 2. 核心脚本

主要脚本位于 `scripts/` 目录：

**创建多维表格应用**
- `create_feishu_app.py` - 创建完整的多维表格应用（推荐）
- `create_feishu_app_mode.py` - 创建应用模式的多维表格
- `create_feishu_bitable.py` - 创建基础多维表格
- `create_purchase_order_bitable.py` - 创建采购订单表格

**权限管理**
- `add_admin_to_bitable.py` - 向多维表格添加管理员用户
- `add_feishu_collaborator.py` - 添加具有指定权限的协作者
- `test_feishu_permissions.py` - 测试权限设置

**字段管理**
- `delete_default_fields.py` - 删除默认字段

**测试工具**
- `test_feishu.py` - 测试飞书 API 连接

**数据可视化**
- `generate_local_charts.py` - 从多维表格数据生成图表

### 3. 使用示例

#### 创建采购订单管理系统

```bash
cd scripts
python3 create_feishu_app.py
```

首次运行会创建新的多维表格。后续运行可以通过在脚本中设置 `EXISTING_APP_TOKEN` 来重用同一表格。

#### 添加协作者

```bash
cd scripts
python3 add_feishu_collaborator.py
```

按照提示输入表格 APP_TOKEN、成员 Open ID 和权限级别。
支持单个或批量添加成员。

## 配置说明

### 使用已有表格

在 `create_feishu_app.py` 中设置：

```python
EXISTING_APP_TOKEN = "your_app_token_here"  # 留空则创建新表格
```

### 权限类型

- `view` - 仅查看
- `edit` - 编辑权限
- `full_access` - 完全管理权限

## 常见问题

### 无法编辑创建的表格

默认情况下，应用创建的表格属于应用而非个人账号。解决方案：

1. 使用 `add_feishu_collaborator.py` 将自己添加为具有编辑权限的协作者
2. 或在飞书界面手动分享给自己

### API 返回 404

检查应用权限配置：
- 确保在飞书开放平台启用了相关权限
- 重新发布应用并等待权限生效（约10分钟）

### 添加协作者失败

应用需要以下权限：
- `permission:permission.member.create`
- 或权限包："分享云文档"

## 脚本依赖

所有脚本需要：
- Python 3.8+
- requests 库
- lark-oapi（权限管理脚本）

安装依赖：
```bash
pip install requests lark-oapi
```

## 插件安装

本插件可以安装到 Claude Code：

```bash
# 复制到 Claude 插件目录
cp -r feishu-integration ~/.claude/plugins/
```

## 参考文档

详细的 API 文档和高级用法，参见：
- 飞书开放平台：https://open.feishu.cn/document
- 多维表格 API 参考：`references/bitable-api.md`
- 权限管理 API：`references/permission-api.md`

## 插件组件

### 命令
- `commands/feishu-integration.md` - 飞书操作的主命令

### 脚本
所有自动化脚本都在 `scripts/` 目录：

**核心脚本：**
- `create_feishu_app.py` - 创建完整的多维表格应用
- `create_feishu_bitable.py` - 创建基础多维表格
- `create_purchase_order_bitable.py` - 创建采购订单系统

**权限管理：**
- `add_admin_to_bitable.py` - 添加管理员用户
- `add_feishu_collaborator.py` - 添加具有权限的协作者

**实用工具：**
- `delete_default_fields.py` - 删除默认字段
- `generate_local_charts.py` - 生成数据可视化
- `test_feishu.py` - 测试 API 连接
- `test_feishu_permissions.py` - 测试权限

## 最佳实践

- 始终先用 `test_feishu.py` 测试 API 连接
- 通过设置 `EXISTING_APP_TOKEN` 使用已有表格，避免重复创建
- 创建表格后将自己添加为协作者以确保编辑权限
- 运行脚本前检查权限要求
- 批量 API 调用时处理速率限制

## 验证清单

- [ ] 配置了有效的 APP_ID 和 APP_SECRET
- [ ] 在飞书开放平台启用了所需权限
- [ ] 已安装 Python 3.8+
- [ ] 已安装依赖（requests、lark-oapi）
- [ ] API 连接测试成功
- [ ] 将自己添加为创建表格的协作者

## 资源

- 官方文档：https://open.feishu.cn/document
- 社区：GitHub 搜索 "feishu-integration"
- 插件结构：基于 Claude Code 插件格式
