# 品牌信息提取规则总结

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

## 模式一：品牌目录 (catalog)

### 触发条件
用户提到：品牌目录、品牌列表、brands、封面图

### 固定输出（1张图片 + JSON）

| 内容 | 文件名 | 说明 |
|------|--------|------|
| 品牌主图 | `{brand}.png` | 封面图/品牌代表图 |
| 品牌数据 | `brand_{brand}_catalog.json` | 简短信息 |

### 图片来源
- Slide 1 封面页
- `image1.png` - 全屏背景图（品牌主图）

### JSON结构
```json
{
  "name": "CHEWY",
  "nameCN": "Chewy 宠物用品在线平台",
  "description": "美国宠物电商龙头"
}
```

### 简短介绍规则（5-10字）
- 突出行业地位（龙头/领先）
- 突出业务特点（电商/零售/订阅）
- 突出地区（美国/欧洲/全球）

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
- `reference/layouts/cover_slide.md`

---

## 模式二：品牌详情 (detail)

### 触发条件
用户提到：品牌背景、品牌简介、产品信息、KPI、流量分布、品牌详情

### 固定输出（3张图片 + Markdown）

| 序号 | 文件名 | 内容 | 图类型 |
|------|--------|------|--------|
| 1 | `{brand}_logo.png` | 品牌Logo | 小图标 |
| 2 | `{brand}_product.png` | 产品展示图 | 大图 |
| 3 | `{brand}_traffic.png` | 独立站流量分布 | **柱状图** |

### Markdown结构
```markdown
# 品牌详情：{品牌名}
品牌序号：{序号}

## 品牌背景与定位
- 基本信息：...
- 用户画像：...
- 品牌使命：...
- 竞争优势：...

## 爆款产品
- 产品名称：...
- 产品价格：...
- 产品特点（7条）：...

## 流量来源分布
![流量分布图](../assets/brand_details/{brand}_traffic.png)

## 核心运营指标
| 指标 | 数值 |
|-----|-----|
| 日均活跃用户 | ... |
| 平均停留时长 | ... |
| 人均访问页面 | ... |
| 用户跳出率 | ... |
```

### 输出目录
```
{output_dir}/
├── assets/
│   └── brand_details/
│       ├── {brand}_logo.png
│       ├── {brand}_product.png
│       └── {brand}_traffic.png
└── data/
    └── brand_{brand}_detail.md
```

### 布局参考
- `reference/layouts/brand_intro_slide.md`
- `reference/layouts/product_slide.md`
- `reference/layouts/traffic_slide.md`

---

## 模式三：品牌分析 (analysis)

### 触发条件
用户提到：用户定位、用户画像、流量模型、SEO、外链、品牌分析

### 固定输出（6张图片 + JSON）

| 序号 | 文件名 | 内容 | 图类型 |
|------|--------|------|--------|
| 1 | `{brand}_user_position.png` | 用户定位分布 | 饼图 |
| 2 | `{brand}_persona_1.png` | 用户画像1 | 截图 |
| 3 | `{brand}_persona_2.png` | 用户画像2 | 截图 |
| 4 | `{brand}_traffic_model.png` | 流量模型流程图 | 流程图 |
| 5 | `{brand}_backlink_pie.png` | 外链来源分布 | **饼图** |
| 6 | `{brand}_backlink_bar.png` | 外链热门关键词 | **横向柱状图** |

### JSON结构
```json
{
  "brandNumber": "01",
  "brandName": "BRAND",
  "userNeeds": {
    "coreNeeds": "核心诉求",
    "scenarios": "使用场景",
    "decisionFactors": "决策因素",
    "channels": "购买渠道"
  },
  "seoTraffic": {
    "text": "SEO说明文字",
    "keywords": [{"rank": 1, "keyword": "xxx", "traffic": 1000}]
  },
  "backlinkTypes": "外链合作网站类型说明",
  "backlinkKeywords": "外链热门关键词说明"
}
```

### 输出目录
```
{output_dir}/
├── assets/
│   └── brand_analysis/
│       ├── {brand}_user_position.png
│       ├── {brand}_persona_1.png
│       ├── {brand}_persona_2.png
│       ├── {brand}_flow_model.png
│       ├── {brand}_backlink_pie.png
│       └── {brand}_backlink_bar.png
└── data/
    └── brand_{brand}_analysis.json
```

### 布局参考
- `reference/layouts/user_position_slide.md`
- `reference/layouts/persona_slide.md`
- `reference/layouts/traffic_model_slide.md`
- `reference/layouts/seo_slide.md`
- `reference/layouts/backlink_slide.md`
- `reference/layouts/backlink_keywords_slide.md`

---

## 模式四：品牌社媒 (social)

### 触发条件
用户提到：社媒、社交媒体、KOL、品牌活动、社媒数据、社媒风格

### 固定输出（7张图片 + JSON）

| 序号 | 文件名 | 内容 | 图类型 |
|------|--------|------|--------|
| 1 | `{brand}_kol_chart.png` | KOL合作统计 | 柱状图/图表 |
| 2 | `{brand}_style_1.png` | 社媒风格1 | 截图 |
| 3 | `{brand}_style_2.png` | 社媒风格2 | 截图 |
| 4 | `{brand}_style_3.png` | 社媒风格3 | 截图 |
| 5 | `{brand}_activity_1.png` | 品牌活动1 | 截图 |
| 6 | `{brand}_activity_2.png` | 品牌活动2 | 截图 |
| 7 | `{brand}_activity_3.png` | 品牌活动3 | 截图 |

### JSON结构
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
├── assets/
│   └── brand_social/
│       ├── {brand}_kol_chart.png
│       ├── {brand}_style_1.png
│       ├── {brand}_style_2.png
│       ├── {brand}_style_3.png
│       ├── {brand}_activity_1.png
│       ├── {brand}_activity_2.png
│       └── {brand}_activity_3.png
└── data/
    └── brand_{brand}_social.json
```

**注意**：图片和数据**分开存放**，图片在 `assets/brand_social/`，JSON在 `data/`

### 布局参考
- `reference/layouts/kol_slide.md`
- `reference/layouts/social_platform_slide.md`
- `reference/layouts/social_style_slide.md`
- `reference/layouts/social_activity_slide.md`

---

## ⚠️ 关键区别（易混淆）

### 流量图区别
| 项目 | 品牌详情 | 品牌分析 |
|------|----------|----------|
| 流量图类型 | **柱状图**（独立站流量） | **饼图**（外链来源） |
| 流量图文件 | `_traffic.png` | `_backlink_pie.png` |
| 来源页面 | "独立站流量来源分布" | "外链（冷流量）" |

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

## 常见错误

### ❌ 错误1：混淆两种流量图
- 品牌详情用**柱状图**（独立站流量）
- 品牌分析用**饼图**（外链分布）

### ❌ 错误2：提取了宠物定位饼图
- 用户定位 ≠ 宠物定位

### ❌ 错误3：外链柱状图选错
- 要选**横向柱状图**，不是网站截图

### ❌ 错误4：把PPT原生表格当成图片
- PPT原生表格不是图片，需要找截图版本

### ❌ 错误5：数据文件放错位置
- 品牌目录JSON放在 `assets/brands/`
- 其他模式JSON/MD放在 `data/`
