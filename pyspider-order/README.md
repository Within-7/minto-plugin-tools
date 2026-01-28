# PySpider Order Plugin

让分析师通过自然语言下单 PySpider 爬虫任务的 Minto 插件。

## 功能

- ✅ 支持 20+ 种爬虫任务（Reddit、Instagram、TikTok、Twitter、Amazon、SEMrush 等）
- ✅ 自然语言理解，自动提取媒体类型和关键词
- ✅ 飞书 API 集成，自动创建工单、更新状态、发送通知
- ✅ PySpider 项目状态检查，确保任务可执行
- ✅ 严格的参数校验，防止错误订单

## 安装后使用

### 在 Minto 中使用（推荐）

安装插件后，直接对话即可：

```
> 帮我抓取 Reddit 上关于 AI 的帖子
> 抓 Amazon 上 "wireless headphone" 的评论
> 查一下任务进度
```

### 手动测试

```bash
# 1. 安装依赖（首次）
pip install -r requirements.txt

# 2. 列出所有可用爬虫
python run.py list

# 3. 校验参数
python run.py validate "Reddit 关键词下的帖子" "AI"

# 4. 创建订单
python run.py order "Reddit 关键词下的帖子" "AI" "ou_xxx"

# 5. 查询进度
python run.py progress
```

## 配置（可选）

插件支持通过环境变量自定义配置：

| 环境变量 | 说明 | 默认值 |
|---------|------|--------|
| `FEISHU_API_URL` | 飞书 API 地址 | `http://3.144.97.122` |
| `FEISHU_TABLE_TOKEN` | 飞书表格 Token | `bascn92h2DxjIZom4hsB1U9irLc` |
| `FEISHU_WEBHOOK` | 飞书 Webhook URL | 内置默认值 |
| `PYSPIDER_BASE_URL` | PySpider 服务地址 | `https://pyspider-dev.within-7.com` |
| `MONGODB_URL` | MongoDB 连接字符串 | 内置默认值 |

### 设置环境变量

```bash
# 临时设置（当前终端）
export FEISHU_API_URL="http://your-api-url"
export PYSPIDER_BASE_URL="https://your-pyspider-url"

# 永久设置（添加到 ~/.bashrc 或 ~/.zshrc）
echo 'export FEISHU_API_URL="http://your-api-url"' >> ~/.bashrc
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

### 其他
- Google Index 任务
- Pinterest 个人资料

完整列表请运行 `python run.py list` 查看。

## 目录结构

```
pyspider-order/
├── run.py                 # 统一命令行入口 ⭐
├── requirements.txt       # Python 依赖
├── plugin.json           # 插件元数据
├── SKILL.md              # AI 系统提示词
├── README.md             # 本文档
├── config/               # 配置文件
│   └── feishudb.ScrapingMongoQuery.csv
├── scripts/              # 核心脚本（不要直接调用，用 run.py）
│   ├── feishu_client.py          # 飞书 API 客户端
│   ├── pyspider_dispatcher.py   # PySpider 调度器
│   ├── validate_params.py        # 参数校验
│   ├── create_crawl_order.py     # 创建订单
│   ├── check_project_status.py   # 检查项目状态
│   ├── list_all_crawlers.py      # 列出所有爬虫
│   └── query_task_progress.py    # 查询任务进度
└── references/            # 参考文档
    └── media_mapping.md
```

## 工作流程

1. **理解请求** - AI 解析自然语言，提取媒体类型和关键词
2. **引导用户** - 如果请求不明确，显示可用爬虫列表
3. **参数校验** - 严格校验 URL 格式、关键词长度、危险字符等
4. **确认执行** - 显示订单详情，等待用户确认
5. **创建工单** - 在飞书多维表格创建记录
6. **发送任务** - 调用 PySpider API 启动爬虫
7. **更新状态** - 更新工单状态为"抓取中"
8. **发送通知** - 通过飞书机器人发送通知

## 故障排查

### `ModuleNotFoundError: No module named 'requests'`
```bash
pip install -r requirements.txt
```

### `❌ 无法连接飞书服务器`
- 检查网络连接
- 确认 `FEISHU_API_URL` 配置正确
- 联系爬虫工程师确认服务状态

### `❌ PySpider项目状态异常`
- 联系爬虫工程师检查项目状态
- 项目必须处于 RUNNING 或 DEBUG 状态

### `❌ 配置文件未找到`
- 确保 `config/feishudb.ScrapingMongoQuery.csv` 存在
- 或将配置文件放在项目根目录

## 技术栈

- Python 3.8+
- requests（HTTP 客户端）
- pymongo（MongoDB 客户端）
- 飞书 Open API
- PySpider API

## 版本历史

- **1.0.0** (2025-01) - 初始版本
  - 支持 20+ 种爬虫平台
  - 飞书 API 集成
  - 自然语言交互

## 许可证

内部使用 - within-7

## 联系方式

如有问题，请联系爬虫工程师团队。
