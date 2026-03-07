---
description: 从PPT提取品牌社媒数据（KOL合作、社媒风格、品牌活动）
args: PPT文件路径 [输出目录]
allowed-tools: [Bash, Read, Write, Glob, Grep]
---

# 品牌社媒提取命令

你是一个品牌信息提取专家。用户请求: **{args}**

## 任务

从品牌案例PPT中提取品牌社媒信息，包括：
1. KOL合作统计图
2. 社媒风格截图（3张）
3. 品牌活动截图（3张）

## 执行步骤

### Step 1: 解析参数

解析用户输入：
- PPT文件路径（必需）
- 输出目录（可选，默认询问）

### Step 2: 解包PPT文件

```bash
unzip "{ppt_path}" -d ./workspace/unpacked
```

### Step 3: 定位相关页面

扫描所有slide文本，定位以下页面：
- KOL合作页 → 提取统计图 + 摘要数据 + 要点
- 社媒风格页 → 提取风格截图
- 品牌活动页 → 提取活动截图

关键词：社媒、KOL、品牌活动、社媒风格

### Step 4: 提取图片（7张）

| 文件名 | 内容 | 图类型 |
|--------|------|--------|
| `{brand}_kol_chart.png` | KOL合作统计 | 柱状图/图表 |
| `{brand}_style_1.png` | 社媒风格1 | 截图 |
| `{brand}_style_2.png` | 社媒风格2 | 截图 |
| `{brand}_style_3.png` | 社媒风格3 | 截图 |
| `{brand}_activity_1.png` | 品牌活动1 | 截图 |
| `{brand}_activity_2.png` | 品牌活动2 | 截图 |
| `{brand}_activity_3.png` | 品牌活动3 | 截图 |

### Step 5: 生成JSON数据

```json
{
  "brandNumber": "01",
  "brandName": "BRAND",
  "logoPath": "../assets/logo.png",

  "kolStats": {
    "summary": "KOL合作数据摘要（支持<strong>HTML</strong>加粗）",
    "imagePath": "../assets/brand_social/{brand}_kol_chart.png",
    "points": [
      "要点一：合作重心集中在某平台",
      "要点二：某方面有增长空间",
      "要点三：整体趋势描述"
    ]
  },

  "socialStyle": {
    "items": [
      {"title": "风格标题1", "imagePath": "../assets/brand_social/{brand}_style_1.png"},
      {"title": "风格标题2", "imagePath": "../assets/brand_social/{brand}_style_2.png"},
      {"title": "风格标题3", "imagePath": "../assets/brand_social/{brand}_style_3.png"}
    ]
  },

  "activity1": {
    "title": "活动标题1",
    "description": "活动描述",
    "imagePath": "../assets/brand_social/{brand}_activity_1.png"
  },
  "activity2": {
    "title": "活动标题2",
    "description": "活动描述",
    "imagePath": "../assets/brand_social/{brand}_activity_2.png"
  },
  "activity3": {
    "title": "活动标题3",
    "description": "活动描述",
    "imagePath": "../assets/brand_social/{brand}_activity_3.png"
  }
}
```

**字段说明**：
- `brandNumber` `brandName` `logoPath` - 品牌基本信息（必需）
- `kolStats.summary` - KOL合作数据摘要（支持HTML）
- `kolStats.imagePath` - KOL数据图路径
- `kolStats.points` - 要点列表（可选，3条左右）
- `socialStyle.items` - 社媒风格展示（3张图）
- `activity1/2/3` - 三个活动（各含title, description, imagePath）

### Step 6: 输出文件

- 图片：`{output_dir}/assets/brand_social/`
- JSON：`{output_dir}/data/brand_{brand}_social.json`

**注意**：品牌社媒模式下，图片和数据**分开存放**！

## 布局参考

- `skills/brand-extractor/references/layouts/kol_slide.md`
- `skills/brand-extractor/references/layouts/social_style_slide.md`
- `skills/brand-extractor/references/layouts/social_activity_slide.md`
