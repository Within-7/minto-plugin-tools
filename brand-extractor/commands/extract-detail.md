---
description: 从PPT提取品牌详情（背景、产品、KPI、流量分布）
args: PPT文件路径 [输出目录]
allowed-tools: [Bash, Read, Write, Glob, Grep]
---

# 品牌详情提取命令 v2.0

你是一个品牌信息提取专家。用户请求: **{args}**

## ⚠️ 强制要求

**你必须严格按照以下步骤执行，不允许跳过任何步骤，不允许使用其他方法。**

## 任务

从品牌案例PPT中提取品牌详情信息：
1. 品牌Logo（1张）
2. 产品展示图（1张）
3. 流量分布图（1张）
4. 品牌背景、产品信息、KPI数据（Markdown格式）

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
   - "品牌介绍" 或 "品牌概览" → 品牌Logo
   - "产品定位" 或 "爆款产品" → 产品展示图
   - "流量分布" 或 "独立站流量" → 流量分布柱状图
3. 估算每个章节对应的 slide 范围

### Step 4: 定位目标Slides

**必须执行：**

根据 TOC 解析结果，确定每个章节的 slide 编号：
- 品牌介绍章节 → slide X-Y
- 产品定位章节 → slide Y-Z
- 流量分布章节 → slide Z-W

### Step 5: 绘制布局结构

**必须执行：为每个目标slide绘制布局结构**

```markdown
## Slide X 布局结构

| 元素 | 位置 (x, y) | 尺寸 (w×h) | rId | 图片文件 | 用途 |
|------|-------------|------------|-----|----------|------|
| 图片1 | (6, 4) | 34×34 | rId2 | image2.png | 装饰小图标 ⚠️忽略 |
| 图片2 | (172, 60) | 327×79 | rId8 | image9.png | **品牌Logo** ✓ |
| 图片3 | (680, 12) | 608×760 | rId1 | image3.jpeg | 产品展示图 ✓ |
```

### Step 6: 识别图片

**必须执行以下判断逻辑：**

1. **品牌Logo识别**：
   - 在"品牌介绍"slide范围内
   - 尺寸：200-500px 宽，50-200px 高
   - 位置：通常在品牌名称旁边
   - 忽略小图标（< 50x50）

2. **产品展示图识别**：
   - 在"产品定位"slide范围内
   - 通常是该slide最大的图片
   - 或是产品主图区域

3. **流量分布图识别**：
   - 在"流量分布"slide范围内
   - 图表类型：柱状图
   - 尺寸：中等大小（300-600px）

### Step 7: 复制图片

**必须执行：**

```bash
cp "./workspace/unpacked/ppt/media/{logo图片}" "{output_dir}/assets/brand_details/{brand}_logo.png"
cp "./workspace/unpacked/ppt/media/{product图片}" "{output_dir}/assets/brand_details/{brand}_product.png"
cp "./workspace/unpacked/ppt/media/{traffic图片}" "{output_dir}/assets/brand_details/{brand}_traffic.png"
```

### Step 8: 提取文本数据

**必须执行：**

从对应的 slide XML 中提取：
- 品牌背景与定位（基本信息、用户画像、品牌使命、竞争优势）
- 爆款产品（名称、价格、7个产品特点）
- 流量来源分布（5个来源及占比）
- 核心运营指标（4个KPI）

### Step 9: 回写Markdown数据

**必须执行：**

在 `{output_dir}/data/` 目录创建 Markdown 文件：

```markdown
# 品牌详情：{BRAND_NAME}
品牌序号：{number}

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
  2. ...

## 流量来源分布
| 来源 | 占比 |
|-----|-----|
| Direct | ... |
| Search | ... |
| Social | ... |
| Referrals | ... |
| Mail | ... |

## 核心运营指标
| 指标 | 数值 |
|-----|-----|
| 日均活跃用户 | ... |
| 平均停留时长 | ... |
| 人均访问页面 | ... |
| 用户跳出率 | ... |
```

### Step 10: 确认输出

**必须执行：**

检查以下文件是否存在：
- `{output_dir}/assets/brand_details/{brand}_logo.png`
- `{output_dir}/assets/brand_details/{brand}_product.png`
- `{output_dir}/assets/brand_details/{brand}_traffic.png`
- `{output_dir}/data/brand_{brand}_detail.md`

输出完成确认信息。

---

## 输出目录结构

```
{output_dir}/
├── assets/
│   └── brand_details/
│       ├── {brand}_logo.png       # 品牌Logo
│       ├── {brand}_product.png    # 产品展示图
│       └── {brand}_traffic.png    # 流量分布图
└── data/
    └── brand_{brand}_detail.md    # 品牌详情Markdown
```

## 错误处理

如果遇到以下情况，必须停止并报告错误：
- PPT 文件不存在
- 无法解包 PPT
- 无法找到 TOC 页
- 无法定位目标章节
- 目标 slide 中没有图片
- 无法识别品牌名称

## 规则配置

详见 `rules/detail.json`
