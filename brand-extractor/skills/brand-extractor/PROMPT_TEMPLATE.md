# 品牌信息提取提示词模板

本文档提供四种模式的提取提示模板，供AI助手参考使用。

---

## 通用前置步骤

在提取任何模式之前，必须：

1. **解包PPT文件**
   ```
   使用 skills-pptx 的 unpack 功能解包 .pptx 文件
   ```

2. **确认品牌名称**
   - 从封面页提取品牌英文名（如 CHEWY）
   - 转换为小写作为文件名（如 chewy）

3. **确认输出目录**
   - 如果用户未指定，询问输出目录

---

## 模式一：品牌目录 (catalog)

### 使用场景
用户提到：品牌目录、品牌列表、brands、封面图

### 提取指令模板

```
请从以下PPT中提取品牌目录信息：

PPT文件：{ppt_path}
品牌名称：{brand}
输出目录：{output_dir}

需要提取：
1. 品牌主图/封面图 → assets/brands/{brand}.png
2. 品牌基本信息 → assets/brands/brand_{brand}_catalog.json

JSON格式：
{
  "name": "{BRAND}",
  "nameCN": "{品牌中文名}",
  "description": "{5-10字简短介绍}"
}
```

### 输出位置
- 图片：`assets/brands/{brand}.png`
- JSON：`assets/brands/brand_{brand}_catalog.json`

---

## 模式二：品牌详情 (detail)

### 使用场景
用户提到：品牌背景、品牌简介、产品信息、KPI、流量分布、品牌详情

### 提取指令模板

```
请从以下PPT中提取品牌详情信息：

PPT文件：{ppt_path}
品牌名称：{brand}
输出目录：{output_dir}

需要提取：
1. 品牌Logo → assets/brand_details/{brand}_logo.png
2. 产品展示图 → assets/brand_details/{brand}_product.png
3. 流量分布柱状图 → assets/brand_details/{brand}_traffic_distribution.png
4. Markdown数据 → data/brand_{brand}_detail.md

Markdown格式：
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
- 产品特点（7条）：
  1. ...
  ...

## 流量来源分布
![流量分布图](../assets/brand_details/{brand}_traffic_distribution.png)

## 核心运营指标
| 指标 | 数值 |
|-----|-----|
| 日均活跃用户 | ... |
| 平均停留时长 | ... |
| 人均访问页面 | ... |
| 用户跳出率 | ... |
```

### 输出位置
- 图片：`assets/brand_details/`
- Markdown：`data/brand_{brand}_detail.md`

---

## 模式三：品牌分析 (analysis)

### 使用场景
用户提到：用户定位、用户画像、流量模型、SEO、外链、品牌分析

### 提取指令模板

```
请从以下PPT中提取品牌分析信息：

PPT文件：{ppt_path}
品牌名称：{brand}
输出目录：{output_dir}

需要提取6张图片：
1. 用户定位饼图 → assets/brand_analysis/{brand}_user_position.png
2. 用户画像1 → assets/brand_analysis/{brand}_persona_1.png
3. 用户画像2 → assets/brand_analysis/{brand}_persona_2.png
4. 流量模型流程图 → assets/brand_analysis/{brand}_flow_model.png
5. 外链分布饼图 → assets/brand_analysis/{brand}_backlink_pie.png
6. 外链关键词柱状图 → assets/brand_analysis/{brand}_backlink_bar.png

JSON数据 → data/brand_{brand}_analysis.json
```

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

### 输出位置
- 图片：`assets/brand_analysis/`
- JSON：`data/brand_{brand}_analysis.json`

---

## 模式四：品牌社媒 (social)

### 使用场景
用户提到：社媒、社交媒体、KOL、品牌活动、社媒数据、社媒风格

### 提取指令模板

```
请从以下PPT中提取品牌社媒信息：

PPT文件：{ppt_path}
品牌名称：{brand}
输出目录：{output_dir}

需要提取7张图片：
1. KOL合作统计图 → assets/brand_social/{brand}_kol_chart.png
2. 社媒风格1 → assets/brand_social/{brand}_style_1.png
3. 社媒风格2 → assets/brand_social/{brand}_style_2.png
4. 社媒风格3 → assets/brand_social/{brand}_style_3.png
5. 品牌活动1 → assets/brand_social/{brand}_activity_1.png
6. 品牌活动2 → assets/brand_social/{brand}_activity_2.png
7. 品牌活动3 → assets/brand_social/{brand}_activity_3.png

JSON数据 → data/brand_{brand}_social.json
```

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

### 输出位置
- 图片：`assets/brand_social/`
- JSON：`data/brand_{brand}_social.json`

---

## 特殊情况处理

### 情况1：品牌名称包含中文
- 使用英文品牌名或拼音作为文件名
- 示例：瑞幸咖啡 → `luckin`

### 情况2：找不到指定图片
- 列出所有候选图片供用户选择
- 不要编造或跳过

### 情况3：数据不完整
- 在输出中标注 `[未找到]`
- 告知用户缺少哪些信息

### 情况4：多个候选图片
```
找到以下候选图片：

【产品图候选】
1. image15.png (4.0MB) - Slide 10 产品展示
   描述：产品实物图，清晰度高

2. image16.png (2.5MB) - Slide 11 订阅服务
   描述：服务页面截图

请选择使用哪张图片（输入序号）？
```
