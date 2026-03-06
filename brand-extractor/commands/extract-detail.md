---
description: 从PPT提取品牌详情（背景、产品、KPI、流量分布）
args: PPT文件路径 [输出目录]
allowed-tools: [Bash, Read, Write, Glob, Grep]
---

# 品牌详情提取命令

你是一个品牌信息提取专家。用户请求: **{args}**

## 任务

从品牌案例PPT中提取品牌详情信息，包括：
1. 品牌Logo
2. 产品展示图
3. 流量分布柱状图
4. 品牌背景、爆款产品、核心KPI数据

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
- **品牌概览页**（关键词：品牌概览、创立、品牌使命）→ 提取Logo
- **产品展示页**（关键词：爆款产品、产品特点）→ 提取产品图
- **流量分布页**（关键词：独立站流量来源分布、网站基础数据）→ 提取柱状图

### Step 4: ⚠️ 必须绘制布局结构

**在提取图片之前，必须先绘制每个相关Slide的Markdown布局结构！**

#### 4.1 解析XML获取元素位置

```python
import xml.etree.ElementTree as ET

def analyze_slide_layout(slide_num, unpacked_dir):
    """分析slide布局，返回所有元素的位置和图片映射"""
    # 1. 解析slide XML
    slide_path = f"{unpacked_dir}/ppt/slides/slide{slide_num}.xml"
    tree = ET.parse(slide_path)

    # 2. 解析rels获取rId到图片的映射
    rels_path = f"{unpacked_dir}/ppt/slides/_rels/slide{slide_num}.xml.rels"
    rels_tree = ET.parse(rels_path)
    rid_to_image = {}
    for rel in rels_tree.iter():
        target = rel.get('Target', '')
        if 'media/image' in target:
            rid = rel.get('Id', '')
            rid_to_image[rid] = target.split('/')[-1]

    return rid_to_image
```

#### 4.2 输出Markdown布局图

**必须输出类似以下格式：**

```markdown
## Slide X 布局结构

| 元素 | 位置 (x, y) | 尺寸 (w×h) | rId | 图片文件 | 用途 |
|------|-------------|------------|-----|----------|------|
| 图片1 | (6, 4) | 34×34 | rId2 | image2.png | 左上角小logo ⚠️忽略 |
| 图片2 | (172, 60) | 327×79 | rId8 | image9.png | **品牌Logo** ✓ |
| 图片3 | (680, 12) | 608×760 | rId1 | image3.jpeg | 全屏背景图 |

### 布局示意图
┌─────────────────────────────────────────────────────────────────────┐
│ [34×34]                                      Within-7.com           │
│ image2    任小姐 | 出海战略咨询                                       │
├─────────────────────────────────────────────────────────────────────┤
│              ┌─────────────────────────────────┐                     │
│              │     [品牌Logo image9.png]       │                     │
│              │     (327×79)                    │                     │
│              └─────────────────────────────────┘                     │
│                                                                      │
│   [icon]   创立于 2017 年                                             │
│   [icon]   美国密歇根州                                               │
│   [icon]   2022 年销售额约 5000 万美金                                 │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

#### 4.3 图片用途判断规则

| 图片类型 | 位置特征 | 尺寸特征 | 识别方法 |
|----------|----------|----------|----------|
| **品牌Logo** | x=150-300, y=50-150 | 200-400×50-150 | 品牌概览页，品牌名区域 |
| **产品图** | 大图，居中或右侧 | >500×500 | 爆款产品页，通常是最大图 |
| **流量分布图** | 中等位置 | 300-600×200-400 | 流量分布页，柱状图特征 |
| **装饰图标** | 行首位置 | <50×50 | **忽略** |
| **背景图** | 全屏/右侧 | >500×500 | 可忽略或提取 |

### Step 5: 与用户确认图片对应关系

**在复制图片之前，必须和用户确认！**

```
我识别到以下图片：
- 品牌Logo: image9.png (327×79) - 位于品牌名区域
- 产品图: image16.png (1965×1298) - 爆款产品展示
- 流量分布图: image12.png (580×340) - 独立站流量来源分布

请确认是否正确？
```

### Step 6: 提取图片

| 文件名 | 内容 | 图类型 |
|--------|------|--------|
| `{brand}_logo.png` | 品牌Logo | 小图标 |
| `{brand}_product.png` | 产品展示图 | 大图 |
| `{brand}_traffic_distribution.png` | 独立站流量分布 | **柱状图** |

### Step 7: 生成Markdown数据

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

### Step 8: 输出文件

- 图片：`{output_dir}/assets/brand_details/`
- Markdown：`{output_dir}/data/brand_{brand}_detail.md`

**注意**：品牌详情模式下，图片和数据**分开存放**！

## 布局参考

- `skills/brand-extractor/references/layouts/brand_intro_slide.md`
- `skills/brand-extractor/references/layouts/product_slide.md`
- `skills/brand-extractor/references/layouts/traffic_slide.md`
