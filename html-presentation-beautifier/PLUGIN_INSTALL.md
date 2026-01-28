# HTML Presentation Beautifier - 安装指南

**版本**: v1.3.0
**类型**: Claude Code 插件
**发布日期**: 2026-01-27

---

## 📦 插件简介

HTML Presentation Beautifier 是一个强大的 Claude Code 插件，能够将 Markdown 文档自动转换为专业的 McKinsey 风格 HTML 演示文稿。

### 核心功能

- ✨ **智能布局选择**: 根据内容自动选择最佳布局（7种布局类型）
- 📊 **自动图表生成**: 使用 Chart.js 生成专业数据可视化
- 🎨 **McKinsey 设计风格**: 专业配色方案和排版
- 📱 **响应式设计**: 支持桌面和移动设备
- 🔧 **图表显示修复**: 解决图表宽度为0的问题
- 📐 **空间优化**: 充分利用横向空间，避免纵向滚动

---

## 🚀 快速安装

### 方法1：安装到 Claude Code 插件目录（推荐）

```bash
# 1. 解压文件
tar -xzf html-presentation-beautifier-v1.3.0.tar.gz

# 2. 进入插件目录
cd html-presentation-beautifier

# 3. 复制到 Claude Code 插件目录
cp -r . ~/.claude-code/plugins/html-presentation-beautifier/

# 4. 重启 Claude Code
```

### 方法2：符号链接安装（开发推荐）

```bash
# 1. 解压文件
tar -xzf html-presentation-beautifier-v1.3.0.tar.gz

# 2. 创建符号链接
ln -s $(pwd)/html-presentation-beautifier ~/.claude-code/plugins/html-presentation-beautifier

# 3. 重启 Claude Code
```

### 方法3：手动安装

```bash
# 1. 解压到任意位置
tar -xzf html-presentation-beautifier-v1.3.0.tar.gz

# 2. 在 Claude Code 设置中添加插件路径
# Claude Code > Settings > Plugins > Add Plugin Path
# 选择: /path/to/html-presentation-beautifier
```

---

## 📖 使用方法

### 基本用法

安装完成后，在 Claude Code 中使用：

```
/beauty /path/to/your/document.md
```

### 示例

```bash
# 转换单个文档
/beauty ~/Desktop/报告.md

# 输出文件会自动生成在同级目录
# 例如：报告.md → 报告_final.html

# 在浏览器中打开
open ~/Desktop/报告_final.html
```

---

## 🎯 支持的布局类型

### L1: 单列布局
- **适用**: 1个观点，封面页
- **特点**: 纵深展示，强调重点

### L2: 双列布局
- **适用**: 2-3个并列观点，A/B对比
- **特点**: 左右对比，清晰明了

### L3: 三列布局 ⭐ 新增
- **适用**: 3个并列观点
- **特点**: 横向展开，充分利用空间

### L4: 卡片网格布局 ⭐ 新增
- **适用**: 4-6个并列观点
- **特点**: 网格排列，视觉丰富
- **变体**: 2x2网格、2x3网格、3x2网格

### L5: 图表+文本布局
- **适用**: 包含数据可视化+关键洞察
- **特点**: 图文并茂，数据驱动

### L6: 纯图表布局
- **适用**: 数据密集型内容
- **特点**: 大图表展示，数据突出

### L7: 混合布局
- **适用**: 复杂结构内容
- **特点**: 灵活组合，适应性强

---

## 📊 支持的图表类型

### 1. 柱状图 (Bar Chart)
- **适用**: 数据对比，排名展示
- **示例**: 销售额对比，各维度得分

### 2. 折线图 (Line Chart)
- **适用**: 趋势分析，时间序列
- **示例**: 收入增长趋势，用户增长

### 3. 饼图/环形图 (Pie/Doughnut Chart)
- **适用**: 占比分析，结构展示
- **示例**: 市场份额，成本构成

### 4. 堆叠柱状图 (Stacked Bar Chart)
- **适用**: 多维度对比
- **示例**: 各产品线收入构成

### 5. 金字塔图 (Pyramid Chart)
- **适用**: 层级结构，优先级
- **示例**: Maslow需求层次，策略金字塔

---

## ✨ v1.3.0 核心优化

### 1. 布局优先原则 ⭐ 新增
```
步骤2.0: 页面布局规划（优先级最高）
  └─ 分析观点数量、数据密度
  └─ 选择最佳布局类型
  └─ 应用随机选择机制

步骤2.1: 图表/图文选择（基于确定的布局）
  └─ 根据布局选择合适的可视化方式
```

### 2. 图表显示修复 🐛 修复
**问题**: 图表 canvas 宽度为0，不可见
```html
<!-- 修复前 -->
<canvas id="chart" width="0" style="width: 0px;">

<!-- 修复后 -->
<style>
.chart-container {
  width: 100% !important;
  min-width: 300px !important;
  height: 500px;
}
.chart-container canvas {
  width: 100% !important;
  height: 100% !important;
}
</style>
```

### 3. 空间利用优化 📊 增强
**问题**: 多个观点纵向排列，左右空白，需要滚动
```
修复前: 6个观点纵向排列（单列布局）
修复后: 6个卡片横向排列（2x3网格布局）
```

---

## 📁 插件结构

```
html-presentation-beautifier/
├── commands/
│   └── beauty.md                    # 主命令定义
├── agents/
│   ├── content-merger.md            # 内容合并代理
│   ├── content-reviewer.md          # 内容审核代理
│   ├── html-presentation-reviewer.md # HTML审核代理
│   ├── presentation-merger.md       # 演示文稿合并代理
│   └── visualization-optimizer.md   # 可视化优化代理
├── skills/
│   └── beauty-html/
│       ├── SKILL.md                 # 主技能定义
│       ├── assets/                  # 资源文件
│       ├── references/              # 参考文档
│       │   ├── best-practices.md
│       │   ├── chart-selection-guide.md
│       │   ├── mckinsey-design-system.md
│       │   └── template-guide.md
│       └── scripts/                 # 脚本文件
├── docs/
│   ├── guides/                      # 指南文档
│   └── reports/                     # 报告文档
├── plugin.json                      # 插件配置
├── README.md                        # 插件说明
├── CHANGELOG.md                     # 更新日志
└── INSTALL.md                       # 安装指南
```

---

## 🔧 系统要求

- **Claude Code CLI**: 最新版本
- **操作系统**: macOS, Linux, Windows (WSL)
- **浏览器**: 现代浏览器（Chrome, Firefox, Safari, Edge）
- **依赖**: 无需额外依赖（Chart.js 通过 CDN 引入）

---

## 🐛 常见问题

### Q1: 安装后命令不生效
**A**:
1. 确认已重启 Claude Code
2. 检查插件路径是否正确：`~/.claude-code/plugins/html-presentation-beautifier/`
3. 查看 Claude Code 日志

### Q2: 图表不显示
**A**:
1. 检查浏览器控制台错误
2. 确认网络连接正常（需要加载 Chart.js CDN）
3. 验证 HTML 文件中的 CSS 样式

### Q3: 中文显示乱码
**A**:
1. 确认 HTML 文件编码为 UTF-8
2. 在浏览器中正确设置编码

### Q4: 如何自定义样式
**A**:
编辑生成的 HTML 文件中的 `<style>` 部分，或修改 `commands/beauty.md` 中的 CSS 模板

---

## 📝 更新日志

### v1.3.0 (2026-01-27)
- ✨ 新增布局优先原则
- ✨ 新增7种智能布局类型
- 🐛 修复图表宽度为0的问题
- 🐛 修复纵向长列表问题
- 📊 优化空间利用率
- 📚 完善文档

### v1.2.0 (2026-01-26)
- ✨ 新增图表显示修复
- ✨ 新增智能布局选择

### v1.1.0
- ✨ 初始版本发布
- ✨ 基础 HTML 转换功能

---

## 🤝 贡献

欢迎提交 Issue 和 Pull Request！

**GitHub**: [Repository URL]

---

## 📄 许可证

MIT License

---

## 📞 技术支持

- 查看文档: `README.md`, `CHANGELOG.md`
- 问题反馈: 提交 Issue
- 使用指南: 查看 `docs/guides/` 目录

---

## 🎯 下一步

安装完成后：

1. ✅ 尝试转换一个示例文档
2. ✅ 查看生成的 HTML 文件
3. ✅ 阅读文档了解高级功能
4. ✅ 根据需要自定义样式

---

**Made with ❤️ by HTML Presentation Beautifier Team**
**Version**: v1.3.0
**Date**: 2026-01-27
