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
- 品牌简介页 → 提取Logo、背景信息
- 产品展示页 → 提取产品图、产品信息
- 流量分布页 → 提取柱状图、KPI数据

关键词：品牌背景、产品、KPI、流量分布

### Step 4: 提取图片

| 文件名 | 内容 | 图类型 |
|--------|------|--------|
| `{brand}_logo.png` | 品牌Logo | 小图标 |
| `{brand}_product.png` | 产品展示图 | 大图 |
| `{brand}_traffic_distribution.png` | 独立站流量分布 | **柱状图** |

### Step 5: 生成Markdown数据

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

### Step 6: 输出文件

- 图片：`{output_dir}/assets/brand_details/`
- Markdown：`{output_dir}/data/brand_{brand}_detail.md`

**注意**：品牌详情模式下，图片和数据**分开存放**！

## 布局参考

- `skills/brand-extractor/references/layouts/brand_intro_slide.md`
- `skills/brand-extractor/references/layouts/product_slide.md`
- `skills/brand-extractor/references/layouts/traffic_slide.md`
