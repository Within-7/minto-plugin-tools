---
name: feishu-integration
description: 飞书（Feishu/Lark）API集成技能。用于创建多维表格、文档、添加协作者、生成数据可视化等。适用于：需要自动化飞书操作、创建采购订单管理系统、生成数据报表、管理文档权限等场景。
---

# 飞书集成技能

## 快速开始

### 1. 准备凭证

确保有有效的飞书应用凭证：
- `APP_ID`: 飞书应用ID
- `APP_SECRET`: 飞书应用密钥

### 2. 核心脚本

主要脚本位于 `scripts/` 目录：

**创建多维表格应用**
- `create_feishu_app.py` - 创建完整的多维表格应用（推荐）
- `create_feishu_app_mode.py` - 创建应用模式的多维表格
- `create_feishu_bitable.py` - 创建基础多维表格
- `create_purchase_order_bitable.py` - 创建采购订单表格

**协作者管理**
- `add_feishu_collaborator.py` - 添加协作者并设置权限
- `add_admin_to_bitable.py` - 添加管理员到多维表格

**表格字段管理**
- `delete_default_fields.py` - 删除默认字段

**测试工具**
- `test_feishu.py` - 测试飞书API连接
- `test_feishu_permissions.py` - 测试权限设置

### 3. 使用示例

#### 创建采购订单管理系统

```bash
cd scripts
python3 create_feishu_app.py
```

首次运行会创建新的多维表格，后续可通过修改脚本中的 `EXISTING_APP_TOKEN` 复用同一表格。

#### 添加协作者

```bash
cd scripts
python3 add_feishu_collaborator.py
```

按提示输入 `APP_TOKEN`、用户邮箱和权限级别。

## 配置说明

### 使用已有表格

在 `create_feishu_app.py` 中设置：

```python
EXISTING_APP_TOKEN = "your_app_token_here"  # 留空则创建新表格
```

### 权限类型

- `view` - 查看权限
- `edit` - 编辑权限
- `full_access` - 完全管理权限

## 常见问题

### 无法编辑创建的表格

默认情况下，应用创建的表格属于应用而非个人账号。解决方法：

1. 使用 `add_feishu_collaborator.py` 添加自己为协作者
2. 或在飞书界面手动分享给自己

### API返回404

检查应用权限配置：
- 确保在飞书开放平台开通了相关权限
- 重新发布应用并等待权限生效（约10分钟）

### 添加协作者失败

需要应用开通以下权限：
- `permission:permission.member.create`
- 或权限包："分享云文档"

## 脚本依赖

所有脚本需要：
- Python 3.8+
- requests库

安装依赖：
```bash
pip install requests
```

## 参考资源

详细API说明和高级用法，参见：
- 飞书开放平台文档：https://open.feishu.cn/document
- 多维表格API参考：`references/bitable-api.md`
- 权限管理API：`references/permission-api.md`
