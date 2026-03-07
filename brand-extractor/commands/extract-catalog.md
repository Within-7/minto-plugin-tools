---
description: 从PPT提取品牌目录信息（封面图+简短介绍）
args: PPT文件路径 [输出目录]
allowed-tools: [Bash, Read, Write, Glob, Grep]
---

# 品牌目录提取命令 v2.0

你是一个品牌信息提取专家。用户请求: **{args}**

## ⚠️ 强制要求

**你必须严格按照以下步骤执行，不允许跳过任何步骤，不允许使用其他方法。**

## 任务

从品牌案例PPT中提取品牌目录信息：
1. 品牌封面图（1张）
2. 品牌基本信息（JSON格式）

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

### Step 3: 定位封面页

**必须执行：**

1. 读取 `ppt/slides/slide1.xml` 确认这是封面页
2. 读取 `ppt/slides/_rels/slide1.xml.rels` 获取该页面的图片引用列表

### Step 4: 识别品牌封面图

**必须执行以下判断逻辑：**

1. 从 slide1.xml.rels 获取所有图片 rId 和文件名映射
2. 分析每张图片的位置和尺寸（从 slide1.xml 中的 `<a:xfrm>` 元素）
3. 选择规则：
   - 优先选择**尺寸最大**的图片
   - 或选择**位置居中**的主图
   - 忽略小图标（尺寸 < 100x100）
4. 记录选中的图片文件名（如 `image1.png`）

### Step 5: 复制图片

**必须执行：**

```bash
cp "./workspace/unpacked/ppt/media/{选中的图片文件}" "{output_dir}/assets/brands/{brand_name}.png"
```

品牌名称从 PPT 文件名或 slide1 文本中提取，转换为小写字母+下划线格式。

### Step 6: 提取品牌文本信息

**必须执行：**

从 slide1.xml 中提取以下文本：
- 品牌英文名称（通常是最显眼的标题）
- 品牌中文名称（如果有）
- 品牌简短描述（副标题或描述文字）

### Step 7: 回写JSON数据

**必须执行：**

在 `{output_dir}/assets/brands/` 目录创建 JSON 文件：

```json
{
  "name": "BRAND_NAME_EN",
  "nameCN": "品牌中文名",
  "description": "品牌简短描述"
}
```

### Step 8: 确认输出

**必须执行：**

检查以下文件是否存在：
- `{output_dir}/assets/brands/{brand_name}.png`
- `{output_dir}/assets/brands/brand_{brand_name}_catalog.json`

输出完成确认信息。

---

## 输出目录结构

```
{output_dir}/
└── assets/
    └── brands/
        ├── {brand}.png                    # 品牌封面图
        └── brand_{brand}_catalog.json     # 品牌基本信息
```

## JSON数据格式

```json
{
  "name": "BUFFY",
  "nameCN": "Buffy 四季被",
  "description": "美国环保床上用品品牌"
}
```

## 错误处理

如果遇到以下情况，必须停止并报告错误：
- PPT 文件不存在
- 无法解包 PPT
- Slide 1 没有图片
- 无法识别品牌名称

## 规则配置

详见 `rules/catalog.json`
