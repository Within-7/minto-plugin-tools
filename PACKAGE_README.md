# Minto Plugin Tools - Skill Package

**版本**: v1.3.0
**发布日期**: 2026-01-27
**包大小**: 1.4 MB

---

## 📦 包内容

这是一个完整的 Claude Code 技能工具包，包含以下核心工具：

### 1. **HTML Presentation Beautifier** (主要工具)
将 Markdown 文档转换为专业的 McKinsey 风格 HTML 演示文稿

**核心功能：**
- 🎨 McKinsey 设计风格
- 📊 自动图表生成（Chart.js）
- 🎯 智能布局选择（7种布局类型）
- 📱 响应式设计
- 🔧 图表显示修复（解决 width=0 问题）

**命令：** `/beauty <文档路径>`

### 2. **Skill Creator**
创建新的 Claude Code 技能

**命令：** `/skill-create`

### 3. **Skill Optimizer**
优化现有技能质量

**命令：** `/skill-optimize`

### 4. **Plugin Creator**
创建 Claude Code 插件

**命令：** `/plugin-create`

---

## 🚀 快速开始

### 安装步骤

```bash
# 1. 解压包
tar -xzf minto-plugin-tools-skill.tar.gz

# 2. 进入目录
cd minto-plugin-tools

# 3. 开始使用！
```

### 使用示例

```bash
# 转换文档为 HTML 演示文稿
/beauty ~/Desktop/报告.md

# 输出文件会自动生成在同级目录
# 例如：报告.md → 报告_final.html
```

---

## ✨ 主要特性（v1.3.0）

### 布局优先原则
- ✅ **先确定布局，再选择图表**（核心优化）
- ✅ 7种智能布局类型：
  - L1: 单列布局（1个观点）
  - L2: 双列布局（2-3个观点）
  - L3: 三列布局（3个并列观点）
  - L4: 卡片网格布局（4-6个观点）⭐ 新增
  - L5: 图表+文本布局（数据可视化）
  - L6: 纯图表布局（数据密集型）
  - L7: 混合布局（复杂结构）

### 图表显示修复
- ✅ 修复宽度为0的问题
- ✅ 强制 width: 100%
- ✅ Chart.js responsive: true
- ✅ maintainAspectRatio: false

### 空间利用优化
- ✅ 优先横向布局（避免纵向滚动）
- ✅ 充分利用横向空间
- ✅ 卡片网格自动适配
- ✅ 随机选择机制（增加多样性）

---

## 📋 版本历史

### v1.3.0 (2026-01-27) - 布局优化版
- ✨ 新增布局优先原则
- ✨ 新增7种布局类型
- 🐛 修复图表宽度为0问题
- 🐛 修复纵向长列表问题
- 📊 优化空间利用率

### v1.2.0 (2026-01-26)
- ✨ 新增图表显示修复
- ✨ 新增智能布局选择

### v1.1.0
- ✨ 初始版本
- ✨ 基础 HTML 转换功能

---

## 📁 目录结构

```
minto-plugin-tools/
├── html-presentation-beautifier/    # HTML 演示美化工具 ⭐
│   ├── commands/
│   │   └── beauty.md                # 主命令定义
│   ├── skills/
│   │   ├── beauty.md                # 美化技能
│   │   ├── presentation-merger.md   # 合并技能
│   │   └── ...
│   └── utils/                       # 工具函数
├── plugin-creator/                  # 插件创建工具
├── skill-creator/                   # 技能创建工具
├── skill-optimizer/                 # 技能优化工具
├── README.md                        # 项目说明
└── .gitignore
```

---

## 🔧 系统要求

- **Claude Code CLI**: 最新版本
- **操作系统**: macOS, Linux, Windows (WSL)
- **依赖**:
  - Chart.js (自动引入，无需安装)
  - 无需额外依赖

---

## 📖 使用指南

### Beauty 命令完整流程

1. **读取文档** (自动)
   - 读取 Markdown 文件
   - 分析内容结构

2. **确定布局** (步骤2.0 - 新增)
   - 分析观点数量
   - 选择最佳布局类型
   - 应用随机选择机制

3. **选择图表类型** (步骤2.1)
   - 基于确定的布局
   - 选择合适的可视化方式

4. **转换为 HTML** (步骤3)
   - 生成 McKinsey 风格 HTML
   - 应用响应式 CSS
   - 配置 Chart.js

5. **质量检验** (步骤5)
   - 图表显示验证
   - 布局合理性验证
   - 内容完整性验证

### 支持的文档类型

- ✅ Markdown (.md)
- ✅ 纯文本 (.txt)
- ✅ 支持中文和英文

---

## 🐛 已知问题修复

### 问题1：图表宽度为0 ✅ 已修复
**症状**: `<canvas width="0">`

**修复**:
- CSS: `width: 100% !important`
- Chart.js: `responsive: true, maintainAspectRatio: false`

### 问题2：纵向长列表 ✅ 已修复
**症状**: 6+个观点纵向排列，需要滚动

**修复**:
- 使用卡片网格布局
- 优先横向布局
- 充分利用横向空间

---

## 📞 技术支持

- 查看详细文档: `README.md`
- 问题反馈: 提交 Issue
- 更新日志: 本文件的"版本历史"部分

---

## 📄 许可证

MIT License

---

## 🎯 下一步计划

- [ ] 添加更多布局模板（四列、瀑布流）
- [ ] 支持导出为 PDF
- [ ] 添加图表交互增强
- [ ] 性能优化（大文件处理）

---

**Made with ❤️ by Minto Plugin Tools Team**
