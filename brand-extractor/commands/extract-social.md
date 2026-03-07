---
description: 从PPT提取品牌社媒数据（KOL合作、社媒风格、品牌活动）
args: PPT文件路径 [输出目录]
allowed-tools: [Bash, Read, Write, Glob, Grep]
---

# 品牌社媒提取命令 v2.0

你是一个品牌信息提取专家。用户请求: **{args}**

## ⚠️ 强制要求

**你必须严格按照以下步骤执行，不允许跳过任何步骤，不允许使用其他方法。**

## 任务

从品牌案例PPT中提取品牌社媒信息：
1. KOL合作数据图（1张）
2. 社媒风格截图（3张）
3. 品牌活动截图（3张）
4. KOL数据、社媒数据、活动描述（JSON格式）

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
2. 解析目录文本，找到 "营销活动" 章节：
   - KOL合作数据
   - 官方社媒风格
   - 品牌活动（活动1/2/3）
3. 估算每个子章节对应的 slide 范围

### Step 4: 定位目标Slides

**必须执行：**

根据 TOC 解析结果，确定：
- KOL合作数据 → slide X
- 官方社媒风格 → slide Y
- 品牌活动 → slide Z, Z+1, Z+2

### Step 5: 绘制布局结构

**必须执行：为每个目标slide绘制布局结构**

```markdown
## Slide X 布局结构

| 元素 | 位置 (x, y) | 尺寸 (w×h) | rId | 图片文件 | 用途 |
|------|-------------|------------|-----|----------|------|
| 图片1 | (...) | ...×... | rId1 | image1.png | KOL数据图表 ✓ |
```

### Step 6: 识别图片

**必须执行以下判断逻辑：**

1. **KOL合作数据图**：
   - 在"KOL合作"slide范围内
   - 图表类型：柱状图/表格截图
   - 命名：`{brand}_kol_chart.png`

2. **社媒风格截图（3张）**：
   - 在"官方社媒风格"slide范围内
   - 通常是3张并排的截图
   - 按从左到右顺序命名：`{brand}_style_1.png`, `{brand}_style_2.png`, `{brand}_style_3.png`

3. **品牌活动截图（3张）**：
   - 在"品牌活动"slide范围内
   - 每个活动一张截图
   - 命名：`{brand}_activity_1.png`, `{brand}_activity_2.png`, `{brand}_activity_3.png`

### Step 7: 复制图片

**必须执行：**

```bash
cp "./workspace/unpacked/ppt/media/{kol图片}" "{output_dir}/assets/brand_social/{brand}_kol_chart.png"
cp "./workspace/unpacked/ppt/media/{style_1图片}" "{output_dir}/assets/brand_social/{brand}_style_1.png"
cp "./workspace/unpacked/ppt/media/{style_2图片}" "{output_dir}/assets/brand_social/{brand}_style_2.png"
cp "./workspace/unpacked/ppt/media/{style_3图片}" "{output_dir}/assets/brand_social/{brand}_style_3.png"
cp "./workspace/unpacked/ppt/media/{activity_1图片}" "{output_dir}/assets/brand_social/{brand}_activity_1.png"
cp "./workspace/unpacked/ppt/media/{activity_2图片}" "{output_dir}/assets/brand_social/{brand}_activity_2.png"
cp "./workspace/unpacked/ppt/media/{activity_3图片}" "{output_dir}/assets/brand_social/{brand}_activity_3.png"
```

### Step 8: 提取文本数据

**必须执行：**

从对应的 slide XML 中提取：
- KOL合作数据摘要（支持HTML格式）
- KOL合作要点（3条左右）
- 社媒风格标题（3个）
- 品牌活动标题和描述（3个活动）

### Step 9: 回写JSON数据

**必须执行：**

在 `{output_dir}/data/` 目录创建 JSON 文件：

```json
{
  "brandNumber": "01",
  "brandName": "BRAND",
  "logoPath": "../assets/logo.png",

  "kolStats": {
    "summary": "KOL合作数据摘要（支持<strong>HTML</strong>）",
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
    "description": "活动描述1",
    "imagePath": "../assets/brand_social/{brand}_activity_1.png"
  },
  "activity2": {
    "title": "活动标题2",
    "description": "活动描述2",
    "imagePath": "../assets/brand_social/{brand}_activity_2.png"
  },
  "activity3": {
    "title": "活动标题3",
    "description": "活动描述3",
    "imagePath": "../assets/brand_social/{brand}_activity_3.png"
  }
}
```

### Step 10: 确认输出

**必须执行：**

检查以下文件是否存在：
- `{output_dir}/assets/brand_social/{brand}_kol_chart.png`
- `{output_dir}/assets/brand_social/{brand}_style_1.png`
- `{output_dir}/assets/brand_social/{brand}_style_2.png`
- `{output_dir}/assets/brand_social/{brand}_style_3.png`
- `{output_dir}/assets/brand_social/{brand}_activity_1.png`
- `{output_dir}/assets/brand_social/{brand}_activity_2.png`
- `{output_dir}/assets/brand_social/{brand}_activity_3.png`
- `{output_dir}/data/brand_{brand}_social.json`

输出完成确认信息。

---

## 输出目录结构

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

## 错误处理

如果遇到以下情况，必须停止并报告错误：
- PPT 文件不存在
- 无法解包 PPT
- 无法找到 TOC 页
- 无法定位"营销活动"章节
- 目标 slide 中没有图片
- 无法识别品牌名称

## 规则配置

详见 `rules/social.json`
