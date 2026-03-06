---
description: 从PPT提取品牌目录信息（封面图+简短介绍）
args: PPT文件路径 [输出目录]
allowed-tools: [Bash, Read, Write, Glob, Grep]
---

# 品牌目录提取命令

你是一个品牌信息提取专家。用户请求: **{args}**

## 任务

从品牌案例PPT中提取品牌目录信息，包括：
1. 品牌主图/封面图
2. 品牌基本信息（英文名、中文名、简短介绍）

## 执行步骤

### Step 1: 解析参数

解析用户输入：
- PPT文件路径（必需）
- 输出目录（可选，默认询问）

### Step 2: 解包PPT文件

```bash
unzip "{ppt_path}" -d ./workspace/unpacked
```

### Step 3: 定位封面页

- 找到Slide 1（封面页）
- 识别品牌名称（从封面标题）
- 提取image1.png作为品牌主图

### Step 4: 提取数据

生成JSON数据：
```json
{
  "name": "{BRAND}",
  "nameCN": "{品牌中文名}",
  "description": "{5-10字简短介绍}"
}
```

### Step 5: 输出文件

输出到以下位置：
- 图片：`{output_dir}/assets/brands/{brand}.png`
- JSON：`{output_dir}/assets/brands/brand_{brand}_catalog.json`

**注意**：品牌目录模式下，JSON和图片都放在 `assets/brands/` 目录！

## 布局参考

参考 `skills/brand-extractor/references/layouts/cover_slide.md` 了解封面页布局。

## 输出确认

完成后确认：
- [ ] 图片已保存到正确位置
- [ ] JSON文件已保存
- [ ] 数据格式正确
