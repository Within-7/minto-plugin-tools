# Minto Slides

演示文稿页面生成器，支持生成消费者洞察(第24-29页)和行业结论(第49-50页)页面。

## 功能

| 模块 | 页码 | 类型 | 说明 |
|------|------|------|------|
| 消费者洞察 | 24 | 散点图 | 用户关注度分析（市场分 vs 需求分） |
| 消费者洞察 | 25-29 | 用户画像 | 优选用户展示（文字 + 截图） |
| 行业结论 | 49-50 | 卡片布局 | 12个行业结论卡片，每页6个 |

## 安装

### 1. 安装依赖

```bash
pip install -r requirements.txt
```

**注意**：如果不需要自动截图功能，可以跳过 playwright 安装。

### 2. 安装Plugin

```bash
# 方式1：复制到本地plugins目录
cp -r minto-slides ~/.claude/plugins/

# 方式2：从仓库安装
/plugin add your-repo/minto-plugin-tools
```

## 项目目录结构

在当前项目目录下创建以下结构：

```
当前项目目录/
├── assets/
│   ├── logo.png                     # Logo文件（必需）
│   └── profiles/                    # 25-29页用户画像截图
│       ├── 水上活动.png
│       ├── 自然探索.png
│       └── ...
├── slides/                          # 生成的HTML文件
│   ├── 24_user_attention.html
│   ├── 25_user_profile_1.html
│   └── ...
└── .minto-state.json                # 状态文件（自动生成）
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

**Step 1：准备截图**

将截图放入 `assets/profiles/` 目录：
- 尺寸：480px × 850-900px
- 格式：PNG 或 JPG
- 命名：`{人群名称}.png`

**Step 2：调用生成**

```
/minto-slides 生成25-29页
```

如果图片缺失，会提示你上传。上传完成后回复"继续"即可批量生成5页。

### 生成第49-50页（行业结论）

```
/minto-slides 生成行业结论页面，主题是户外露营装备
内容：
[自由文本，AI会自动解析并扩展到12个卡片]
```

一次调用生成49-50页全部2页。

## 截图格式要求

| 项目 | 要求 |
|------|------|
| 宽度 | 480px |
| 高度 | 850-900px（推荐） |
| 格式 | PNG 或 JPG |
| 命名 | `{人群名称}.png` |
| 位置 | `assets/profiles/` |

**示例**：
```
assets/profiles/水上活动.png
assets/profiles/自然探索.png
assets/profiles/极端探险.png
assets/profiles/长途旅行.png
assets/profiles/家庭旅行.png
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
  {"name": "摄影师", "marketScore": 75, "demandScore": 88}
]
```

### 行业结论文本（第49-50页）

自由文本格式，AI会自动解析和扩展：

```
户外露营装备行业是一个专注于露营相关装备的行业。
核心产品包括帐篷、睡袋、照明设备等。
2024年全球市场规模约为968亿美元...
```

## 插件目录结构

```
minto-slides/
├── .claude-plugin/
│   └── plugin.json
├── skills/
│   └── minto-slides/
│       └── SKILL.md
├── templates/
│   ├── scatter_chart.html
│   ├── user_profile.html
│   └── industry_conclusion.html
├── assets/
│   └── logo.png
├── scripts/
│   └── instagram_screenshot.py  # 可选工具
├── examples/
│   ├── example_scatter.json
│   └── example_conclusion.txt
├── requirements.txt
└── README.md
```

## 注意事项

1. **Logo**：首次使用会自动复制默认logo到项目目录
2. **截图前置检查**：25-29页生成前会检查图片是否存在
3. **批量生成**：一次调用生成多页
4. **文字充实**：用户画像页面文字会自动扩展

## 版本

- v2.1.0 - 优化目录结构，支持批量生成，添加前置检查
- v2.0.0 - 重命名为 minto-slides，新增第49-50页
- v1.0.0 - 初始版本

## License

MIT
