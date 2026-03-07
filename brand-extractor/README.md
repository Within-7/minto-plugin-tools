# Brand Extractor - PPT品牌信息提取器 v2.0

Claude Code 插件，从品牌案例PPT中自动提取结构化的品牌信息。

## v2.0 核心变化

### 新的提取方法：目录结构驱动

```
旧方法（v1.x）：
关键词搜索所有68张图片 → 靠猜测识别图片用途 → 容易出错

新方法（v2.0）：
解析TOC目录结构 → 定位目标章节 → 精准识别图片 → 准确率高
```

### 核心改进

| 改进点 | 旧版 | 新版 |
|--------|------|------|
| 定位方法 | 关键词搜索 | TOC目录结构驱动 |
| 图片识别 | 靠文件名猜测 | 规则配置 + 位置/尺寸判断 |
| 外链识别 | 经常选错 | 精准定位到"基石流量→外链分析"章节 |
| 代码结构 | 单文件 | 模块化（extractor/toc_parser/image_identifier/writer） |

## 功能特性

- 📋 **四种模式**：品牌目录、品牌详情、品牌分析、品牌社媒
- 🗂️ **目录驱动**：通过解析PPT目录结构精准定位内容
- 🖼️ **智能识别**：基于规则配置识别图片用途
- 📊 **数据结构化**：输出JSON或Markdown格式数据
- 📁 **规范输出**：按固定目录结构组织输出文件

## 项目结构

```
brand-extractor/
├── commands/                    # 命令入口
│   ├── extract-catalog.md
│   ├── extract-detail.md
│   ├── extract-analysis.md
│   └── extract-social.md
│
├── scripts/                     # 核心脚本
│   ├── extractor.py             # 主提取器
│   ├── toc_parser.py            # TOC解析器
│   ├── image_identifier.py      # 图片识别器
│   └── writer.py                # 数据回写模块
│
├── rules/                       # 规则配置
│   ├── catalog.json             # catalog模式规则
│   ├── detail.json              # detail模式规则
│   ├── analysis.json            # analysis模式规则
│   └── social.json              # social模式规则
│
└── skills/
    └── brand-extractor/
        ├── SKILL.md             # 技能说明
        └── references/          # 参考文档
```

## 安装

```bash
# 复制到项目 .claude 目录
cp -r brand-extractor /path/to/your-project/.claude/plugins/
```

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

## 提取流程（v2.0）

```
Step 1: 解包PPT
         ↓
Step 2: 解析TOC（目录结构）
         ↓
Step 3: 根据mode定位目标章节的slide范围
         ↓
Step 4: 在目标slides中识别图片
         ↓
Step 5: 复制图片到目标目录，重命名
         ↓
Step 6: 回写数据文件（JSON/MD）
```

## 核心模块说明

### extractor.py - 主提取器
- 协调各模块完成提取流程
- 支持四种模式的参数解析
- 提供命令行入口

### toc_parser.py - TOC解析器
- 定位TOC页（通常是Slide 4）
- 解析目录结构，提取章节名称和层级
- 估算每个章节的slide范围

### image_identifier.py - 图片识别器
- 根据规则配置识别图片用途
- 支持多种图片类型：cover/logo/product/pie/bar/flow/screenshot
- 基于位置、尺寸、图表类型判断

### writer.py - 数据回写模块
- 支持JSON和Markdown格式输出
- 保持与v1.x兼容的输出格式
- 自动创建目录结构

## 版本历史

- **v2.0.0** - 重构：目录结构驱动提取方法；模块化代码结构；规则配置文件
- v1.3.0 - 新增完整示例文档、图片识别精确规则、自检清单
- v1.2.0 - 统一图片命名规范；添加错误处理指南
- v1.1.0 - 新增图片识别SOP
- v1.0.0 - 初始版本

## 许可证

MIT
