---
name: brand-extractor
description: 从PPT品牌案例文件中提取品牌信息。支持四种模式：(1)品牌目录 - 提取封面图和简短介绍；(2)品牌详情 - 提取品牌背景、产品、流量分布、KPI；(3)品牌分析 - 提取用户定位、流量模型、SEO、外链数据；(4)品牌社媒 - 提取社媒数据、KOL合作、品牌活动。根据用户提到的关键词自动选择模式。
---

# PPT品牌信息提取器

## ⚠️ 存放路径规则（重要）

| 模式 | 图片位置 | 数据位置 | 说明 |
|------|----------|----------|------|
| **品牌目录** | `assets/brands/` | `assets/brands/` | **图片和数据在同一目录** |
| 品牌详情 | `assets/brand_details/` | `data/` | 图片和数据**分开存放** |
| 品牌分析 | `assets/brand_analysis/` | `data/` | 图片和数据**分开存放** |
| 品牌社媒 | `assets/brand_social/` | `data/` | 图片和数据**分开存放** |

**只有品牌目录模式**：JSON和图片都放在 `assets/brands/`
**其他三种模式**：图片在 `assets/xxx/`，数据文件在 `data/`

---

## 四种模式（按顺序）

| 序号 | 模式 | 触发关键词 | 图片 | 数据 |
|------|------|-----------|------|------|
| **1** | 品牌目录 | 品牌目录、品牌列表、brands | 1张 | JSON |
| **2** | 品牌详情 | 品牌背景、产品、KPI | 3张 | Markdown |
| **3** | 品牌分析 | 用户定位、流量模型、SEO、外链 | 6张 | JSON |
| **4** | 品牌社媒 | 社媒、KOL、品牌活动、社媒数据 | 7张 | JSON |

---

## 输入参数

| 参数 | 说明 | 是否必需 |
|------|------|----------|
| ppt_file | PPT文件路径 | 必需 |
| output_dir | 输出目录 | 可选（默认询问） |
| brand_name | 品牌名称 | 可选（默认从PPT提取） |

---

## 模式一：品牌目录 (catalog)

### 触发条件
用户提到：品牌目录、品牌列表、brands、封面图

### 固定输出（1张图片）

| 文件名 | 内容 | 来源 |
|--------|------|------|
| `{brand}.png` | 品牌主图/封面图 | Slide 1 image1.png |

### JSON数据
```json
{
  "name": "CHEWY",
  "nameCN": "Chewy 宠物用品在线平台",
  "description": "美国宠物电商龙头"
}
```

### 输出目录
```
{output_dir}/
└── assets/
    └── brands/
        ├── {brand}.png
        └── brand_{brand}_catalog.json
```

**注意**：JSON和图片都放在 `assets/brands/` 目录下

### 布局参考
- [封面页布局](references/layouts/cover_slide.md)

---

## 模式二：品牌详情 (detail)

### 触发条件
用户提到：品牌背景、品牌简介、产品信息、KPI、流量分布、品牌详情

### 固定输出（3张图片）

| 文件名 | 内容 | 图类型 |
|--------|------|--------|
| `{brand}_logo.png` | 品牌Logo | 小图标 |
| `{brand}_product.png` | 产品展示图 | 大图 |
| `{brand}_traffic_distribution.png` | 独立站流量分布 | **柱状图** |

### Markdown数据
- 品牌背景与定位
- 爆款产品（名称、价格、7个特点）
- 核心KPI指标

### 输出目录
```
{output_dir}/
├── assets/brand_details/
│   ├── {brand}_logo.png
│   ├── {brand}_product.png
│   └── {brand}_traffic_distribution.png
└── data/
    └── brand_{brand}_detail.md
```

### 布局参考
- [品牌简介页](references/layouts/brand_intro_slide.md)
- [产品展示页](references/layouts/product_slide.md)
- [流量分布页](references/layouts/traffic_slide.md)

---

## 模式三：品牌分析 (analysis)

### 触发条件
用户提到：用户定位、用户画像、流量模型、SEO、外链、品牌分析

### 固定输出（6张图片）

| 文件名 | 内容 | 图类型 |
|--------|------|--------|
| `{brand}_user_position.png` | 用户定位分布 | 饼图 |
| `{brand}_persona_1.png` | 用户画像1 | 截图 |
| `{brand}_persona_2.png` | 用户画像2 | 截图 |
| `{brand}_flow_model.png` | 流量模型流程图 | 流程图 |
| `{brand}_backlink_pie.png` | 外链来源分布 | **饼图** |
| `{brand}_backlink_bar.png` | 外链热门关键词 | **横向柱状图** |

### JSON数据
- 用户需求（核心诉求、使用场景、决策因素、购买渠道）
- SEO流量（说明文字、关键词表格数据）
- 外链类型说明
- 外链热门关键词

### 输出目录
```
{output_dir}/
├── assets/brand_analysis/
│   ├── {brand}_user_position.png
│   ├── {brand}_persona_1.png
│   ├── {brand}_persona_2.png
│   ├── {brand}_flow_model.png
│   ├── {brand}_backlink_pie.png
│   └── {brand}_backlink_bar.png
└── data/
    └── brand_{brand}_analysis.json
```

### 布局参考
- [用户定位页](references/layouts/user_position_slide.md)
- [用户画像页](references/layouts/persona_slide.md)
- [流量模型页](references/layouts/traffic_model_slide.md)
- [SEO页面](references/layouts/seo_slide.md)
- [外链分布页](references/layouts/backlink_slide.md)
- [外链关键词页](references/layouts/backlink_keywords_slide.md)

---

## 模式四：品牌社媒 (social)

### 触发条件
用户提到：社媒、社交媒体、KOL、品牌活动、社媒数据、社媒风格

### 固定输出（7张图片）

| 文件名 | 内容 | 图类型 |
|--------|------|--------|
| `{brand}_kol_chart.png` | KOL合作统计 | 柱状图/图表 |
| `{brand}_style_1.png` | 社媒风格1 | 截图 |
| `{brand}_style_2.png` | 社媒风格2 | 截图 |
| `{brand}_style_3.png` | 社媒风格3 | 截图 |
| `{brand}_activity_1.png` | 品牌活动1 | 截图 |
| `{brand}_activity_2.png` | 品牌活动2 | 截图 |
| `{brand}_activity_3.png` | 品牌活动3 | 截图 |

### JSON数据
```json
{
  "kolStats": {
    "summary": "KOL合作数据摘要",
    "imagePath": "../assets/brand_social/{brand}_kol_chart.png"
  },
  "socialMediaData": {
    "platforms": [
      {"icon": "ig", "name": "Instagram", "followers": "xxx", "posts": "xxx", "frequency": "x帖/x天", "likes": "xxx"},
      {"icon": "tt", "name": "TikTok", "followers": "xxx", "posts": "xxx", "frequency": "x帖/x天", "views": "xxx"},
      {"icon": "yt", "name": "YouTube", "followers": "xxx", "posts": "xxx", "frequency": "x帖/x天", "views": "xxx"}
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

### 输出目录
```
{output_dir}/
├── assets/brand_social/
│   ├── {brand}_kol_chart.png
│   ├── {brand}_style_1.png
│   ├── {brand}_style_2.png
│   ├── {brand}_style_3.png
│   ├── {brand}_activity_1.png
│   ├── {brand}_activity_2.png
│   └── {brand}_activity_3.png
└── data/
    └── brand_{brand}_social.json
```

**注意**：图片和数据**分开存放**，图片在 `assets/brand_social/`，JSON在 `data/`

### 布局参考
- [KOL合作页](references/layouts/kol_slide.md)
- [社媒平台数据页](references/layouts/social_platform_slide.md)
- [社媒风格页](references/layouts/social_style_slide.md)
- [品牌活动页](references/layouts/social_activity_slide.md)

---

## ⚠️ 关键区别

### 流量图区别
| 项目 | 品牌详情 | 品牌分析 |
|------|----------|----------|
| 流量图类型 | **柱状图**（独立站流量） | **饼图**（外链来源） |
| 流量图文件 | `_traffic_distribution.png` | `_backlink_pie.png` |

**不要搞混！**

### 存放路径区别
| 模式 | 图片位置 | 数据位置 |
|------|----------|----------|
| 品牌目录 | `assets/brands/` | `assets/brands/` ← **同一目录** |
| 品牌详情 | `assets/brand_details/` | `data/` |
| 品牌分析 | `assets/brand_analysis/` | `data/` |
| 品牌社媒 | `assets/brand_social/` | `data/` |

**只有品牌目录的数据文件放在assets，其他都放在data目录！**

---

## 依赖说明

本技能依赖以下工具/技能：

| 依赖 | 用途 | 说明 |
|------|------|------|
| **skills-pptx** | PPT解包 | 用于解包 .pptx 文件，提取XML和图片资源 |
| Python 3 | 辅助脚本 | 运行 `scripts/extract_brand.py` 可选辅助工具 |

---

## 快速开始

### 示例：提取品牌详情

```bash
# 1. 用户请求示例
"请从 /path/to/brand.pptx 提取品牌详情，输出到 /path/to/output"

# 2. AI执行步骤
# 2.1 解包PPT
unzip brand.pptx -d workspace/unpacked

# 2.2 扫描定位相关slide
# 2.3 提取图片到 assets/brand_details/
# 2.4 提取数据写入 data/brand_xxx_detail.md

# 3. 最终输出结构
output/
├── assets/brand_details/
│   ├── chewy_logo.png
│   ├── chewy_product.png
│   └── chewy_traffic_distribution.png
└── data/
    └── brand_chewy_detail.md
```

---

## 执行流程（详细）

### 第1步：解包PPT文件

```bash
# 方法1：使用unzip（推荐）
unzip /path/to/brand.pptx -d ./workspace/unpacked

# 方法2：使用skills-pptx的unpack脚本
python ooxml/scripts/unpack.py /path/to/brand.pptx ./workspace/unpacked
```

解包后目录结构：
```
unpacked/
├── ppt/
│   ├── slides/
│   │   ├── slide1.xml
│   │   ├── slide2.xml
│   │   └── ...
│   ├── media/
│   │   ├── image1.png
│   │   ├── image2.png
│   │   └── ...
│   └── slides/_rels/
│       ├── slide1.xml.rels
│       └── ...
└── ...
```

### 第2步：扫描文本，选择模式

1. 读取所有 `slideN.xml` 文件
2. 提取文本内容
3. 根据关键词匹配选择模式：
   - "品牌目录"、"封面" → 模式一
   - "品牌背景"、"产品"、"KPI" → 模式二
   - "用户定位"、"SEO"、"外链" → 模式三
   - "社媒"、"KOL"、"品牌活动" → 模式四

### 第3步：定位候选slide

1. 根据关键词找到候选slide
2. 对照布局参考文件确认
3. 记录slide编号

### 第3.5步：⚠️ 必须绘制布局结构再识别图片

**这是关键步骤，不能跳过！**

在提取图片之前，必须先执行以下流程：

#### 3.5.1 解析Slide XML获取元素位置

```python
import xml.etree.ElementTree as ET

def parse_slide_layout(slide_path, rels_path):
    """解析slide布局，返回所有元素的位置信息"""
    # 1. 解析slide XML获取所有元素位置
    tree = ET.parse(slide_path)
    # 提取每个元素的 x, y, cx, cy (位置和尺寸)

    # 2. 解析rels文件获取rId到图片的映射
    # rId1 -> image3.jpeg, rId2 -> image2.png ...

    return elements_info
```

#### 3.5.2 输出Markdown布局图

**必须输出类似以下格式的布局图：**

```markdown
## Slide X 布局结构

| 元素 | 位置 (x, y) | 尺寸 (w×h) | rId | 图片文件 | 用途 |
|------|-------------|------------|-----|----------|------|
| 图片1 | (6, 4) | 34×34 | rId2 | image2.png | 左上角小logo ⚠️忽略 |
| 图片2 | (172, 60) | 327×79 | rId8 | image9.png | **品牌Logo** ✓ |
| 图片3 | (680, 12) | 608×760 | rId1 | image3.jpeg | 全屏背景图 |

### 布局示意图
┌─────────────────────────────────────────────────┐
│ [34×34]                                        │
│ image2   品牌概览                                │
│                                                 │
│    ┌─────────────────────────┐                  │
│    │ [品牌Logo image9.png]   │                  │
│    │ (327×79)                │                  │
│    └─────────────────────────┘                  │
│                                                 │
│    [icon] 创立于 2017 年                         │
│    [icon] 美国密歇根州                           │
│                                                 │
│                           [背景图 image3.jpeg]  │
└─────────────────────────────────────────────────┘
```

#### 3.5.3 图片用途判断规则

| 图片类型 | 识别特征 | 位置特征 |
|----------|----------|----------|
| **品牌Logo** | 在品牌概览页，品牌名区域 | 尺寸 200-400×50-150，位置居中偏上 |
| **产品图** | 在"爆款产品"页面 | 通常是最大尺寸的图片 |
| **流量分布图** | 在"独立站流量来源分布"页面 | 柱状图特征，中等尺寸 |
| **装饰图标** | 行首小图 | 尺寸 <50×50，**忽略** |
| **背景图** | 全屏或右侧大图 | 尺寸 >500×500 |

#### 3.5.4 与用户确认

**在复制图片之前，必须和用户确认图片对应关系！**

```
我识别到以下图片：
- 品牌Logo: image9.png (327×79) - 位于品牌名区域
- 产品图: image16.png (1965×1298) - 爆款产品展示
- 流量分布图: image12.png (580×340) - 独立站流量来源分布

请确认是否正确？
```

### 第4步：提取图片和数据

1. 从 `ppt/media/` 复制图片到目标目录
2. 重命名为规范文件名
3. 从XML提取文本数据

### 第5步：按规范输出文件

1. 创建必要的目录结构
2. 写入图片文件
3. 写入数据文件（JSON或Markdown）

---

## 相关文件

- [提取规则总结](references/extraction_rules.md)
- [提示词模板](PROMPT_TEMPLATE.md)
- [布局参考目录](references/layouts/)
- [辅助提取脚本](../../scripts/extract_brand.py)

---

## 常见问题

### Q1：如何确定图片对应哪个slide？
查看 `ppt/slides/_rels/slideN.xml.rels` 文件，里面记录了该slide引用的所有图片资源。

### Q2：图片文件名如何确定？
通过slide的关系文件（.rels）找到 `Target="media/imageX.png"`，然后从 `ppt/media/` 目录获取实际图片。

### Q3：提取的数据格式不对怎么办？
参考 `references/layouts/` 目录下的布局参考文件，里面有详细的字段说明和示例。
