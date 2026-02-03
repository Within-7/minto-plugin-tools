# PySpider Order Plugin

让分析师通过自然语言下单 PySpider 爬虫任务的 Minto 插件。

## 功能

- ✅ 支持 20+ 种爬虫任务（Reddit、Instagram、TikTok、Twitter、Facebook、Amazon、SEMrush 等）
- ✅ 自然语言理解，自动提取媒体类型和关键词
- ✅ 飞书 API 集成，自动创建工单、更新状态、发送通知
- ✅ PySpider 项目状态检查，确保任务可执行
- ✅ 严格的参数校验，防止错误订单

## 环境变量配置

**必需环境变量**：

```bash
# MongoDB
export MONGODB_URL="mongodb://user:password@host:port"

# 飞书 API
export FEISHU_API_URL="http://your-api.com"
export FEISHU_TABLE_TOKEN="your_token"
export FEISHU_TABLE_ID="your_table_id"
export FEISHU_WEBHOOK="https://open.feishu.cn/..."

# PySpider
export PYSPIDER_BASE_URL="https://pyspider.your-domain.com"
export PYSPIDER_SESSION_COOKIE="your_session_cookie"

# 可选
export CRAWLER_ENGINEER_USER_ID="ou_xxx"  # 爬虫工程师用户ID
```

## 使用示例

在 Minto 中直接对话：

```
> 帮我抓取 Reddit 上关于 AI 的帖子
> 抓 Amazon 上 "wireless headphone" 的评论
> 查一下任务进度
```

## 支持的爬虫平台

### 社交媒体
- Reddit（关键词）
- Instagram（标签）
- TikTok（标签）
- Twitter（关键词）
- Facebook（Ads、Group）
- YouTube（关键词）
- Pinterest（关键词）

### 电商
- Amazon（关键词、产品列表）
- 卖家精灵（品牌、卖家、关键词、分类）

### SEO 工具
- SEMrush（外链数据）

## 项目结构

```
pyspider-order/
├── plugin.json          # 插件元数据
├── README.md            # 本文档
├── skills/              # AI 技能
│   └── SKILL.md
├── scripts/             # Python 脚本
│   ├── order.py                 # 主流程
│   ├── feishu_client.py         # 飞书 API
│   ├── pyspider_dispatcher.py   # PySpider 调度
│   └── check_project_status.py  # 项目状态检查
└── config/              # 爬虫配置
    └── feishudb.ScrapingMongoQuery.csv
```

## 技术栈

- Python 3.8+
- requests（HTTP 客户端）
- pymongo（MongoDB 客户端）
- 飞书 Open API
- PySpider API

## 版本历史

- **1.0.1** (2025-01-30) - 安全与极简优化
  - 移除硬编码敏感信息
  - 精简代码（1649行 → 635行）
  - 优化目录结构

- **1.0.0** (2025-01) - 初始版本

## 许可证

内部使用 - within-7
