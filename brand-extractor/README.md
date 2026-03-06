# Brand Extractor - PPT品牌信息提取器

Claude Code 插件，从品牌案例PPT中自动提取结构化的品牌信息。

## 功能特性

- 📋 **四种模式**：品牌目录、品牌详情、品牌分析、品牌社媒
- 🖼️ **图片提取**：自动识别并提取PPT中的关键图片
- 📊 **数据结构化**：输出JSON或Markdown格式数据
- 📁 **规范输出**：按固定目录结构组织输出文件

## 安装

```bash
# 复制到项目 .claude 目录
cp -r brand-extractor /path/to/your-project/.claude/plugins/

# 或复制组件
cp commands/*.md /path/to/your-project/.claude/commands/
cp -r skills/brand-extractor /path/to/your-project/.claude/skills/
```

## 依赖

本插件依赖 **skills-pptx** 插件来解包PPT文件：
- 确保已安装 skills-pptx 插件
- 或使用 `unzip` 命令解包PPT

## 使用方法

### 品牌目录提取
```
/extract-catalog <PPT文件路径> [输出目录]
```

### 品牌详情提取
```
/extract-detail <PPT文件路径> [输出目录]
```

### 品牌分析提取
```
/extract-analysis <PPT文件路径> [输出目录]
```

### 品牌社媒提取
```
/extract-social <PPT文件路径> [输出目录]
```

## 四种模式对比

| 模式 | 触发关键词 | 输出图片 | 数据格式 |
|------|-----------|----------|----------|
| 品牌目录 | 目录、列表、封面 | 1张 | JSON |
| 品牌详情 | 背景、产品、KPI | 3张 | Markdown |
| 品牌分析 | 用户定位、SEO、外链 | 6张 | JSON |
| 品牌社媒 | KOL、社媒、活动 | 7张 | JSON |

## 输出目录结构

```
{output_dir}/
├── assets/
│   ├── brands/              # 品牌目录图片
│   ├── brand_details/       # 品牌详情图片
│   ├── brand_analysis/      # 品牌分析图片
│   └── brand_social/        # 品牌社媒图片
└── data/
    ├── brand_xxx_catalog.json
    ├── brand_xxx_detail.md
    ├── brand_xxx_analysis.json
    └── brand_xxx_social.json
```

## 存放路径规则

| 模式 | 图片位置 | 数据位置 |
|------|----------|----------|
| 品牌目录 | `assets/brands/` | `assets/brands/` |
| 品牌详情 | `assets/brand_details/` | `data/` |
| 品牌分析 | `assets/brand_analysis/` | `data/` |
| 品牌社媒 | `assets/brand_social/` | `data/` |

**注意**：只有品牌目录的数据文件放在assets，其他都放在data目录！

## 示例

```bash
# 提取Chewy品牌目录
/extract-catalog /path/to/chewy.pptx /output

# 提取品牌详情
/extract-detail /path/to/brand.pptx ./workspace

# 提取品牌分析数据
/extract-analysis /path/to/brand.pptx ./output
```

## 版本历史

- v1.1.0 - 新增图片识别SOP：必须先绘制布局结构再定位图片；添加品牌Logo专用识别规则
- v1.0.0 - 初始版本，支持四种提取模式

## 许可证

MIT
