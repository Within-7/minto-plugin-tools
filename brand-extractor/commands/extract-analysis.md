---
description: 从PPT提取品牌分析数据（用户定位、流量模型、SEO、外链）
args: PPT文件路径 [输出目录]
allowed-tools: [Bash, Read, Write, Glob, Grep]
---

# 品牌分析提取命令 v2.0

你是一个品牌信息提取专家。用户请求: **{args}**

## ⚠️ 强制要求

**你必须严格按照以下步骤执行，不允许跳过任何步骤，不允许使用其他方法。**

## 任务

从品牌案例PPT中提取品牌分析信息：
1. 用户定位饼图（1张）
2. 用户画像截图（2张）
3. 流量模型流程图（1张）
4. 外链分布饼图（1张）
5. 外链关键词柱状图（1张）
6. SEO数据、外链数据（JSON格式）

## 执行步骤（必须按顺序执行）

### Step 1: 解析参数

解析用户输入：
- PPT文件路径（必需）
- 输出目录（可选，默认询问用户）

**如果输出目录未提供，必须先询问用户。**

### Step 2: 解包PPT文件

**必须执行：**

```bash
unzip "{ppt_path}" -d ./workspace/unpacked
```

### Step 3: 解析TOC目录结构

**必须执行：**

1. 读取 `ppt/slides/slide4.xml`（TOC通常在Slide 4）
2. 解析目录文本，找到以下章节：
   - "用户定位" → 用户定位饼图
   - "用户画像" → 用户画像截图
   - "流量模型" → 流量模型流程图
   - "基石流量" → "外链分析" → 外链饼图 + 柱状图
3. 估算每个章节对应的 slide 范围

### Step 4: 定位外链分析Slides（关键！）

**必须执行：**

外链图片在 "基石流量" 章节下的 "外链分析" 子章节：
- 根据 TOC 结构定位 "基石流量" 章节
- 在该章节内找到 "外链分析" 子章节
- 记录对应的 slide 编号范围

### Step 5: 绘制布局结构

**必须执行：为每个目标slide绘制布局结构**

```markdown
## Slide X 布局结构

| 元素 | 位置 (x, y) | 尺寸 (w×h) | rId | 图片文件 | 用途 |
|------|-------------|------------|-----|----------|------|
| 图片1 | (...) | ...×... | rId1 | image1.png | 用户定位饼图 ✓ |
```

### Step 6: 识别图片

**必须执行以下判断逻辑：**

1. **用户定位饼图**：
   - 在"用户定位"slide范围内
   - 图表类型：饼图/环形图
   - 命名：`{brand}_user_position.png`

2. **用户画像截图（2张）**：
   - 在"用户画像"slide范围内
   - 通常是两张并排的截图
   - 命名：`{brand}_persona_1.png`, `{brand}_persona_2.png`

3. **流量模型流程图**：
   - 在"流量模型"slide范围内
   - 图表类型：流程图
   - 命名：`{brand}_flow_model.png`

4. **外链分布饼图**：
   - 在"外链分析"slide范围内（**关键：必须通过TOC定位！**）
   - 图表类型：饼图/环形图
   - 命名：`{brand}_backlink_pie.png`

5. **外链关键词柱状图**：
   - 在"外链分析"slide范围内
   - 图表类型：横向柱状图
   - 命名：`{brand}_backlink_bar.png`

### Step 7: 复制图片

**必须执行：**

```bash
cp "./workspace/unpacked/ppt/media/{user_position图片}" "{output_dir}/assets/brand_analysis/{brand}_user_position.png"
cp "./workspace/unpacked/ppt/media/{persona_1图片}" "{output_dir}/assets/brand_analysis/{brand}_persona_1.png"
cp "./workspace/unpacked/ppt/media/{persona_2图片}" "{output_dir}/assets/brand_analysis/{brand}_persona_2.png"
cp "./workspace/unpacked/ppt/media/{flow_model图片}" "{output_dir}/assets/brand_analysis/{brand}_flow_model.png"
cp "./workspace/unpacked/ppt/media/{backlink_pie图片}" "{output_dir}/assets/brand_analysis/{brand}_backlink_pie.png"
cp "./workspace/unpacked/ppt/media/{backlink_bar图片}" "{output_dir}/assets/brand_analysis/{brand}_backlink_bar.png"
```

### Step 8: 提取文本数据

**必须执行：**

从对应的 slide XML 中提取：
- 用户需求（核心诉求、使用场景、决策因素、购买渠道）
- SEO流量说明和关键词列表
- 外链类型说明
- 外链关键词说明

### Step 9: 回写JSON数据

**必须执行：**

在 `{output_dir}/data/` 目录创建 JSON 文件：

```json
{
  "brandNumber": "01",
  "brandName": "BRAND",
  "logoPath": "../assets/logo.png",

  "userPositionImagePath": "../assets/brand_analysis/{brand}_user_position.png",

  "userNeeds": {
    "coreNeeds": "核心诉求文本",
    "scenarios": "使用场景文本",
    "decisionFactors": "决策因素文本",
    "channels": "购买渠道文本"
  },

  "personaImage1Path": "../assets/brand_analysis/{brand}_persona_1.png",
  "personaImage2Path": "../assets/brand_analysis/{brand}_persona_2.png",

  "flowModelImagePath": "../assets/brand_analysis/{brand}_flow_model.png",

  "seoTraffic": {
    "text": "SEO说明文字（支持<strong>HTML</strong>）",
    "keywords": [
      {"rank": 1, "keyword": "关键词1", "type": "类型", "traffic": "流量值"},
      {"rank": 2, "keyword": "关键词2", "type": "类型", "traffic": "流量值"}
    ]
  },

  "backlinkTypes": "外链合作网站类型说明",
  "backlinkKeywords": "外链热门关键词说明",
  "backlinkPieImagePath": "../assets/brand_analysis/{brand}_backlink_pie.png",
  "backlinkBarImagePath": "../assets/brand_analysis/{brand}_backlink_bar.png"
}
```

### Step 10: 确认输出

**必须执行：**

检查以下文件是否存在：
- `{output_dir}/assets/brand_analysis/{brand}_user_position.png`
- `{output_dir}/assets/brand_analysis/{brand}_persona_1.png`
- `{output_dir}/assets/brand_analysis/{brand}_persona_2.png`
- `{output_dir}/assets/brand_analysis/{brand}_flow_model.png`
- `{output_dir}/assets/brand_analysis/{brand}_backlink_pie.png`
- `{output_dir}/assets/brand_analysis/{brand}_backlink_bar.png`
- `{output_dir}/data/brand_{brand}_analysis.json`

输出完成确认信息。

---

## 输出目录结构

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

## ⚠️ 关键改进：外链图片定位

**旧方法（错误）**：用关键词"外链"搜索所有68张图片 → 可能选错
**新方法（正确）**：通过TOC定位"基石流量→外链分析"章节 → 精准定位slide范围

## 错误处理

如果遇到以下情况，必须停止并报告错误：
- PPT 文件不存在
- 无法解包 PPT
- 无法找到 TOC 页
- 无法定位目标章节（特别是外链分析）
- 目标 slide 中没有图片
- 无法识别品牌名称

## 规则配置

详见 `rules/analysis.json`
