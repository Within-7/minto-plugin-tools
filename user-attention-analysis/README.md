# User Attention Analysis Plugin

消费者洞察页面生成器，用于生成第24-29页的用户关注度分析和优选用户展示页面。

## 功能

| 页码 | 类型 | 说明 |
|------|------|------|
| 24 | 散点图 | 用户关注度分析（人群市场分 vs 需求分） |
| 25-29 | 用户画像 | 优选用户展示（左文字 + 右Instagram截图） |

## 安装

### 1. 安装依赖

```bash
pip install -r requirements.txt
python -m playwright install chromium
```

### 2. 安装Plugin

```bash
# 方式1：复制到本地plugins目录
cp -r user-attention-analysis ~/.claude/plugins/

# 方式2：从仓库安装（如果已推送到远程）
/plugin add your-repo/minto-plugin-tools
```

## 使用方法

### 生成第24页（散点图）

```
/user-attention-analysis 生成第24页，主题是户外露营装备
数据：
人群特征,市场得分,需求得分
摄影师,75,88
tennis,10,3.3
licensed cosmetologist,1.33,10
...
```

### 生成第25-29页（用户画像）

```
/user-attention-analysis 继续生成第25页
```

每次调用生成一页，需要再次调用继续下一页。

## 目录结构

```
user-attention-analysis/
├── .claude-plugin/
│   └── plugin.json                # 插件清单
├── skills/
│   └── user-attention-analysis/
│       └── SKILL.md               # 完整SOP
├── templates/
│   ├── scatter_chart.html         # 散点图模板
│   └── user_profile.html          # 用户画像模板
├── assets/
│   └── logo.png                   # 默认Logo
├── scripts/
│   └── instagram_screenshot.py    # Instagram截图脚本
├── examples/
│   └── example_data.json          # 示例数据
├── requirements.txt               # Python依赖
└── README.md                      # 本文件
```

## 输入数据格式

### CSV格式
```
人群特征,市场得分,需求得分
摄影师,75,88
tennis,10,3.3
```

### JSON格式
```json
[
  {"name": "摄影师", "marketScore": 75, "demandScore": 88},
  {"name": "tennis", "marketScore": 10, "demandScore": 3.3}
]
```

## Instagram截图说明

生成第25-29页时，会调用截图脚本：
1. 自动打开Instagram搜索对应hashtag
2. 等待9秒让您点击一个KOL用户
3. 弹出相机图标，点击Edge窗口完成截图

**注意**：截图需要手动配合操作。

## 中文→英文Hashtag映射

| 中文关键词 | 英文Hashtag |
|-----------|-------------|
| 水上活动 | #watersports |
| 自然探索 | #naturelover |
| 极端探险 | #extremesports |
| 长途旅行 | #traveler |
| 家庭旅行 | #familytravel |
| 美甲 | #nailart |
| 婚庆美甲 | #bridalnails |

完整映射见 SKILL.md

## 自定义Logo

默认使用 `assets/logo.png`，可在调用时指定：

```
/user-attention-analysis 生成第24页，logo用 /path/to/my-logo.png
```

## 输出

所有文件输出到 `output/` 目录：
- `24_user_attention.html` - 第24页
- `25_user_profile_1.html` - 第25页
- `26_user_profile_2.html` - 第26页
- ...
- `instagram_*.png` - Instagram截图

## 注意事项

1. 每次只生成一页，需再次调用继续
2. 截图需要手动配合
3. 文字内容会尽量充实撑满左侧区域
4. 25-29页的人群从24页数据中选取

## 版本

- v1.0.0 - 初始版本

## License

MIT
