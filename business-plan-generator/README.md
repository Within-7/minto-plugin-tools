# Business Plan Generator Plugin

通用商业计划书生成插件,支持任何行业。通过大纲确认+数据输入,快速生成专业商业计划书。

## 📋 概述

本插件为商业分析提供一键生成专业商业计划书的能力:

- 🎯 **多行业支持**: 宠物、电商、SaaS、餐饮、教育等
- 📝 **灵活大纲**: 根据行业提供对应框架
- 📊 **数据驱动**: 整合市场数据、竞品数据、财务数据
- 🚀 **快速生成**: 3步完成商业计划书

## 🔄 工作流程

### 第1步: 创建大纲 (必须)

首先根据行业类型创建商业计划书大纲框架:

```bash
/create-outline --industry ecommerce --type startup
```

**此步骤会**:
- 提供行业对应的大纲框架
- 显示大纲结构供你确认
- 询问是否需要调整大纲内容
- 询问是否有市场数据要补充

### 第2步: 添加数据 (可选)

如果你有市场数据、竞品数据或财务数据,可以添加:

```bash
# 市场数据
/add-data --market-size 1000 --competitor-count 5 --growth-rate 15

# 财务数据
/add-data --initial-investment 200 --pricing 150 --margin 25

# 自定义数据
/add-data --custom "目标客户:25-35岁女性,客单价$50"
```

**如果没有数据**: 可以跳过此步骤,直接进入第3步

### 第3步: 生成计划书

根据大纲和(可选的)数据生成完整商业计划书:

```bash
/generate-plan
```

**生成逻辑**:
- **如果有数据**: 根据大纲结构,填充数据内容,生成数据驱动的商业计划书
- **如果没有数据**: 基于大纲框架,生成通用商业计划书模板,使用占位符和示例数据

输出格式:
- Markdown格式(默认)
- 结构清晰的8大章节
- 数据驱动的专业内容(如果有数据)

## 📊 商业计划书结构

### 通用框架(所有行业)

1. **执行摘要** - 项目概述、核心亮点、融资需求
2. **公司描述** - 业务模式、愿景使命、法律结构
3. **市场分析** - 市场规模、目标客户、市场趋势
4. **产品/服务** - 产品介绍、独特卖点、竞争优势
5. **市场推广策略** - 定价策略、渠道策略、营销计划
6. **运营计划** - 团队结构、运营流程、里程碑
7. **财务计划** - 收入预测、成本分析、盈利模型
8. **风险管理** - 市场风险、运营风险、应对策略

## 🚀 快速开始

### 方式1: 有数据 (推荐)

如果你有市场数据或财务数据:

```bash
# 第1步: 创建大纲
/create-outline --industry ecommerce --type startup

# 第2步: 添加数据
/add-data --market-size 1000 --competitor-count 5
/add-data --initial-investment 200 --pricing 150

# 第3步: 生成计划书
/generate-plan
```

### 方式2: 无数据

如果你没有具体数据,只需要一个框架:

```bash
# 第1步: 创建大纲
/create-outline --industry ecommerce --type startup

# 第2步: 跳过数据添加,直接生成
/generate-plan
```

**结果**: 生成包含占位符和示例数据的商业计划书模板

## 💡 使用示例

### 示例1: 有数据 (电动滑板车电商)

```bash
# 1. 创建电商行业大纲
/create-outline --industry ecommerce --type startup

# 系统询问: 是否需要调整大纲? 是否有数据要补充?
# 用户回答: 大纲OK,有数据

# 2. 添加数据
/add-data --market-size 5000万 --competitor-count 5
/add-data --growth-rate 15
/add-data --initial-investment 200万

# 3. 生成商业计划书
/generate-plan
```

**输出示例**:
```
# 电动滑板车电商商业计划书

## 1. 执行摘要
本项目是一家专注于电动滑板车的电商平台...

## 2. 公司描述
业务模式: D2C电商平台...

## 3. 市场分析
市场规模: 5000万
竞品数量: 5个
年增长率: 15%...

[使用真实数据填充各章节]
```

### 示例2: 无数据 (新业务构思)

```bash
# 1. 创建电商行业大纲
/create-outline --industry ecommerce --type startup

# 系统询问: 是否需要调整大纲? 是否有数据要补充?
# 用户回答: 大纲OK,没有数据

# 2. 跳过数据添加,直接生成
/generate-plan
```

**输出示例**:
```
# 电商行业商业计划书

## 1. 执行摘要
[项目概述 - 待填充]

## 2. 公司描述
业务模式: [待填充]

## 3. 市场分析
市场规模: [待填写具体数据]
目标客户: [待填写具体数据]
市场趋势: [待填写具体数据]...

[包含占位符和示例数据,供用户后续填充]
```

### 示例3: SaaS行业

```bash
# 1. 创建大纲
/create-outline --industry saas --type startup

# 2. 有数据,添加财务信息
/add-data --initial-investment 500万

# 3. 生成
/generate-plan
```

## 🎨 优势

### 灵活工作流
- **有数据**: 生成数据驱动的专业商业计划书
- **无数据**: 生成包含占位符的模板框架

### 多行业支持
不绑定特定行业,任何行业都可以使用

### 数据驱动
如果有数据,基于真实数据生成计划,而非空泛描述

### 灵活定制
大纲可以调整,数据可以分步添加

### 专业输出
符合商业计划书标准格式的结构化文档

## 📁 安装

```bash
# 安装插件
minto plugin install ./business-plan-generator

# 验证安装
minto
/help
```

## 🔧 配置

插件无需额外配置,开箱即用。

## 📚 更多信息

- [插件开发指南](https://code.claude.com/docs/en/plugins)
- [命令参考](https://code.claude.com/docs/en/plugins-reference)
- [技能参考](https://code.claude.com/docs/en/skills)

---

**版本**: 1.0.0
**作者**: within-7
**许可**: Apache-2.0
