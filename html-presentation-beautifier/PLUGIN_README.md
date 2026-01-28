# HTML Presentation Beautifier

**将 Markdown 文档转换为专业的 McKinsey 风格 HTML 演示文稿**

[![Version](https://img.shields.io/badge/version-v1.3.0-blue.svg)](https://github.com)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Claude Code](https://img.shields.io/badge/Claude_Code-compatible-purple.svg)](https://claude.com/claude-code)

---

## ✨ 特性

### 🎯 智能布局
- **7种布局类型**: 单列、双列、三列、卡片网格等
- **自动选择**: 根据内容智能选择最佳布局
- **布局优先**: 先确定布局，再生成内容（v1.3.0 新增）

### 📊 数据可视化
- **自动图表生成**: 支持柱状图、折线图、饼图等
- **Chart.js 集成**: 专业、美观、交互性强
- **图表修复**: 解决显示问题，确保100%宽度

### 🎨 McKinsey 设计
- **专业配色**: 企业级配色方案
- **排版规范**: 遵循 McKinsey 设计指南
- **视觉层次**: 清晰的信息架构

### 📱 响应式
- **移动端适配**: 自适应各种屏幕尺寸
- **现代浏览器**: 兼容所有主流浏览器
- **零依赖**: 无需安装额外依赖

---

## 🚀 快速开始

### 安装

```bash
# 解压
tar -xzf html-presentation-beautifier-v1.3.0.tar.gz

# 安装到 Claude Code
cd html-presentation-beautifier
cp -r . ~/.claude-code/plugins/

# 重启 Claude Code
```

### 使用

```bash
# 在 Claude Code 中
/beauty ~/Desktop/报告.md

# 输出
# 报告_final.html
```

---

## 📖 使用示例

### 输入文档 (Markdown)

```markdown
# 销售分析报告

## 市场份额

- 产品A: 35%
- 产品B: 28%
- 产品C: 22%
- 其他: 15%

## 增长趋势

2020年: $100M
2021年: $120M
2022年: $145M
2023年: $175M

## 关键洞察

1. 产品A保持领先地位
2. 整体市场增长稳健
3. 新兴市场潜力巨大
```

### 输出演示文稿 (HTML)

- ✅ 自动生成饼图展示市场份额
- ✅ 自动生成折线图展示增长趋势
- ✅ 使用卡片网格布局展示3个洞察
- ✅ McKinsey 风格配色和排版
- ✅ 完全响应式设计

---

## 🎯 布局类型

| 布局类型 | 适用场景 | 观点数量 |
|---------|---------|---------|
| L1: 单列布局 | 封面页、核心观点 | 1个 |
| L2: 双列布局 | 并列观点、A/B对比 | 2-3个 |
| L3: 三列布局 | 3个并列观点 | 3个 |
| L4: 卡片网格 | 多个并列观点 | 4-6个 |
| L5: 图表+文本 | 数据可视化+洞察 | 混合 |
| L6: 纯图表 | 数据密集型 | 大量数据 |
| L7: 混合布局 | 复杂结构 | 灵活 |

---

## 📊 图表类型

| 图表类型 | 适用场景 | 示例 |
|---------|---------|------|
| 柱状图 | 数据对比、排名 | 销售额对比 |
| 折线图 | 趋势分析、时间序列 | 收入增长 |
| 饼图 | 占比分析、结构 | 市场份额 |
| 堆叠柱状图 | 多维度对比 | 收入构成 |
| 金字塔图 | 层级结构、优先级 | 需求层次 |

---

## 📁 项目结构

```
html-presentation-beautifier/
├── commands/
│   └── beauty.md              # 主命令
├── agents/                    # 5个专业代理
│   ├── content-merger.md
│   ├── content-reviewer.md
│   ├── html-presentation-reviewer.md
│   ├── presentation-merger.md
│   └── visualization-optimizer.md
├── skills/
│   └── beauty-html/
│       ├── SKILL.md           # 主技能
│       ├── assets/            # 资源
│       ├── references/        # 参考
│       └── scripts/           # 脚本
├── docs/                      # 文档
├── plugin.json                # 配置
├── README.md                  # 说明
└── INSTALL.md                 # 安装指南
```

---

## 🔧 系统要求

- Claude Code CLI (最新版本)
- 现代浏览器
- 无需其他依赖

---

## 📝 版本历史

### v1.3.0 (2026-01-27) - 布局优化版
- ✨ 布局优先原则
- ✨ 7种智能布局
- 🐛 修复图表显示问题
- 🐛 修复空间利用问题
- 📊 优化布局多样性

### v1.2.0 (2026-01-26)
- ✨ 图表显示修复
- ✨ 智能布局选择

### v1.1.0
- ✨ 初始版本

---

## 🤝 贡献

欢迎贡献！请查看 [CONTRIBUTING.md](CONTRIBUTING.md)

---

## 📄 许可证

MIT License - 详见 [LICENSE](LICENSE)

---

## 📞 支持

- 📧 邮件: support@example.com
- 🐛 Issues: [GitHub Issues](https://github.com)
- 💬 Discussions: [GitHub Discussions](https://github.com)

---

## 🙏 致谢

- McKinsey & Company - 设计系统灵感
- Chart.js - 数据可视化库
- Claude Code - AI 辅助开发平台

---

**Made with ❤️**

**Version**: v1.3.0 | **Date**: 2026-01-27
