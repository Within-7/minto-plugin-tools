# Minto Slides

演示文稿页面生成器，支持生成消费者洞察(第24-29页)和行业结论(第49-50页)页面。

## 功能

| 模块 | 页码 | 类型 | 说明 |
|------|------|------|------|
| 消费者洞察 | 24 | 散点图 | 用户关注度分析（市场分 vs 需求分） |
| 消费者洞察 | 25-29 | 用户画像 | 优选用户展示（文字 + Instagram截图） |
| 行业结论 | 49-50 | 卡片布局 | 12个行业结论卡片，每页6个 |

## 安装

### 1. 安装依赖

```bash
pip install -r requirements.txt
python -m playwright install chromium
```

### 2. 安装Plugin

```bash
# 方式1：复制到本地plugins目录
cp -r minto-slides ~/.claude/plugins/

# 方式2：从仓库安装
/plugin add your-repo/minto-plugin-tools
```

## 使用方法

### 生成第24页（散点图）

```
/minto-slides 生成第24页，主题是户外露营装备
数据：
人群特征,市场得分,需求得分
摄影师,75,88
tennis,10,3.3
...
```

### 生成第25-29页（用户画像）

```
/minto-slides 继续生成第25页
```

每次调用生成一页，需要再次调用继续下一页。

### 生成第49-50页（行业结论）

```
/minto-slides 生成行业结论页面，主题是户外露营装备
内容：
[自由文本，AI会自动解析并扩展到12个卡片]
```

AI会自动：
1. 分析文本，提取/生成12个主题
2. 扩展每个卡片的内容
3. 分配颜色主题
4. 生成两页HTML（49页卡片1-6，50页卡片7-12）

## 目录结构

```
minto-slides/
├── .claude-plugin/
│   └── plugin.json                # 插件清单
├── skills/
│   └── minto-slides/
│       └── SKILL.md               # 完整SOP
├── templates/
│   ├── scatter_chart.html         # 散点图模板（第24页）
│   ├── user_profile.html          # 用户画像模板（第25-29页）
│   └── industry_conclusion.html   # 行业结论模板（第49-50页）
├── assets/
│   └── logo.png                   # 默认Logo
├── scripts/
│   └── instagram_screenshot.py    # Instagram截图脚本
├── examples/
│   ├── example_scatter.json       # 散点图示例数据
│   └── example_conclusion.txt     # 行业结论文本示例
├── requirements.txt               # Python依赖
└── README.md                      # 本文件
```

## 输入数据格式

### 散点图数据（第24页）

**CSV格式**
```
人群特征,市场得分,需求得分
摄影师,75,88
tennis,10,3.3
```

**JSON格式**
```json
[
  {"name": "摄影师", "marketScore": 75, "demandScore": 88},
  {"name": "tennis", "marketScore": 10, "demandScore": 3.3}
]
```

### 行业结论文本（第49-50页）

**自由文本格式** - AI会自动解析和扩展

```
户外露营装备行业是一个专注于露营相关装备的研发、制造和销售的行业。
核心产品包括帐篷、睡袋、照明设备、炊具等。
行业发展从军用转民用开始...
```

## 输出

所有文件输出到 `output/` 目录：

### 消费者洞察
- `24_user_attention.html` - 第24页（散点图）
- `25_user_profile_1.html` - 第25页（用户画像1）
- `26_user_profile_2.html` - 第26页（用户画像2）
- ...
- `instagram_*.png` - Instagram截图

### 行业结论
- `49_industry_conclusion_1.html` - 第49页（卡片1-6）
- `50_industry_conclusion_2.html` - 第50页（卡片7-12）

## Instagram截图说明

生成第25-29页时，会调用截图脚本：
1. 自动打开Instagram搜索对应hashtag
2. 等待9秒让您点击一个KOL用户
3. 弹出截图工具，点击窗口完成截图

**注意**：截图需要手动配合操作。

## 自定义Logo

默认使用 `assets/logo.png`，可在调用时指定：

```
/minto-slides 生成第24页，logo用 /path/to/my-logo.png
```

## 注意事项

1. 每次只生成一页，需再次调用继续
2. 截图需要手动配合
3. 文字内容会尽量充实
4. 25-29页的人群从24页数据中选取
5. 49-50页支持AI自动扩展内容

## 版本

- v2.0.0 - 重命名为 minto-slides，新增第49-50页行业结论生成
- v1.0.0 - 初始版本

## License

MIT
