# HTML 演示文稿幻灯片模板使用指南

**插件**: html-presentation-beautifier
**版本**: 2.0.0
**更新日期**: 2025-01-25

---

## 概述

本插件提供 **4 种专业的 McKinsey 风格幻灯片模板**，用于生成高质量的 HTML 演示文稿。

### 模板类型

1. **封面页模板** (`cover-slide-template.html`)
2. **目录页模板** (`toc-slide-template.html`)
3. **内容页模板** (`content-slide-template.html`)
4. **结束页模板** (`end-slide-template.html`)

---

## 模板详解

### 1. 封面页模板 (Cover Slide)

**文件**: `templates/cover-slide-template.html`

**用途**: 演示文稿的第一张幻灯片，用于展示标题和基本信息

**设计特点**:
- 渐变背景（深蓝到橙色）
- 主标题：64px，粗体，白色
- 副标题：36px，白色
- 元信息区域：汇报人、日期、部门

**HTML 结构**:
```html
<div class="slide title-slide active" data-slide="1">
    <h1 class="main-title">演示文稿主标题</h1>
    <div class="decorative-line"></div>
    <p class="subtitle">演示文稿副标题或补充说明</p>

    <div class="meta-info">
        <div class="meta-item">
            <div class="meta-label">汇报人</div>
            <div class="meta-value">姓名</div>
        </div>
        <!-- 更多元信息项 -->
    </div>
</div>
```

**使用场景**:
- 商业汇报开场
- 项目介绍
- 战略规划展示

**自定义要点**:
- 修改 `.main-title`: 主标题
- 修改 `.subtitle`: 副标题
- 修改 `.meta-item`: 添加/删除元信息项

---

### 2. 目录页模板 (Table of Contents)

**文件**: `templates/toc-slide-template.html`

**用途**: 展示演示文稿的整体结构和章节导航

**设计特点**:
- 两栏网格布局
- 5 个主要部分快速导航
- 可点击跳转到对应章节
- 显示总幻灯片数和预计时间

**HTML 结构**:
```html
<div class="slide toc-slide active" data-slide="1">
    <div class="toc-header">
        <h1 class="toc-title">目录</h1>
        <p class="toc-subtitle">Table of Contents</p>
    </div>

    <div class="toc-container">
        <a href="#section1" class="toc-section" onclick="jumpToSlide(2); return false;">
            <div class="toc-number">1</div>
            <div class="toc-section-title">第一部分：商业模式介绍</div>
            <div class="toc-section-subtitle">亚马逊品牌流量价值转化模式</div>
        </a>
        <!-- 更多部分 -->
    </div>

    <div class="toc-footer">
        <p class="toc-footer-text">
            <strong>共 47 张幻灯片</strong> | 预计演示时间：<strong>45-60 分钟</strong>
        </p>
    </div>
</div>
```

**使用场景**:
- 长篇演示文稿（20+ 张幻灯片）
- 需要章节导航的演示
- 会议、培训、演讲

**自定义要点**:
- 修改 `.toc-section`: 添加/删除章节
- 修改 `onclick="jumpToSlide(X)"`: 设置跳转目标
- 修改幻灯片总数和预计时间

---

### 3. 内容页模板 (Content Slide)

**文件**: `templates/content-slide-template.html`

**用途**: 所有内容幻灯片的通用模板，支持多种内容布局

**设计特点**:
- McKinsey 风格精确匹配
- 多种布局组件（两栏、列表、图表等）
- 8 个 Chart.js 图表集成
- 响应式设计

**支持的布局组件**:

#### 3.1 标题组件
```html
<!-- 主标题 -->
<h1 class="slide-title">章节标题</h1>

<!-- 副标题 -->
<h2 class="slide-subtitle">副标题或关键信息</h2>

<!-- 分节标题 -->
<h3 class="section-heading">分节标题</h3>
```

#### 3.2 文本内容
```html
<p class="text-content">
    正文内容，支持多段落，18px，行高 1.8
</p>

<p class="key-point">
    关键要点，使用强调色，20px 粗体
</p>
```

#### 3.3 列表组件

**无序列表**:
```html
<ul class="bullet-list">
    <li>列表项 1</li>
    <li>列表项 2</li>
    <li>列表项 3</li>
</ul>
```

**有序列表**:
```html
<ol class="numbered-list">
    <li>步骤 1</li>
    <li>步骤 2</li>
    <li>步骤 3</li>
</ol>
```

#### 3.4 布局组件

**两栏布局**:
```html
<div class="two-column">
    <div class="column">
        <!-- 左栏内容 -->
    </div>
    <div class="column">
        <!-- 右栏内容 -->
    </div>
</div>
```

#### 3.5 Chart.js 图表

**柱状图**:
```html
<div class="chart-container">
    <canvas id="chart1"></canvas>
</div>
<script>
new Chart(document.getElementById('chart1'), {
    type: 'bar',
    data: { /* 数据 */ },
    options: { /* 配置 */ }
});
</script>
```

**折线图**:
```html
<div class="chart-container">
    <canvas id="lineChart"></canvas>
</div>
```

**环形图**:
```html
<div class="chart-container">
    <canvas id="doughnutChart"></canvas>
</div>
```

**饼图**:
```html
<div class="chart-container">
    <canvas id="pieChart"></canvas>
</div>
```

#### 3.6 强调框组件

**强调框容器**:
```html
<div class="emphasis-container">
    <div class="emphasis-box">
        <div class="emphasis-icon">📊</div>
        <div class="emphasis-text">标题文本</div>
        <div class="emphasis-description">详细说明</div>
    </div>
</div>
```

**结论网格**:
```html
<div class="conclusions-grid">
    <div class="conclusion-card">
        <div class="conclusion-number">01</div>
        <div class="conclusion-title">结论标题</div>
        <div class="conclusion-text">结论内容</div>
    </div>
</div>
```

**信息框**:
```html
<div class="info-box">
    <div class="info-box-title">信息框标题</div>
    <div class="info-box-content">信息框内容</div>
</div>
```

**高亮框**:
```html
<div class="highlight-box">
    <div class="highlight-title">高亮标题</div>
    <div class="highlight-content">高亮内容</div>
</div>
```

#### 3.7 流程图组件

```html
<div class="flow-container">
    <div class="flow-step">
        <div class="flow-number">1</div>
        <div class="flow-content">
            <div class="flow-title">步骤标题</div>
            <div class="flow-description">步骤描述</div>
        </div>
    </div>
</div>
```

#### 3.8 数据表格

```html
<table class="data-table">
    <thead>
        <tr>
            <th>列标题 1</th>
            <th>列标题 2</th>
            <th>列标题 3</th>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>数据 1</td>
            <td>数据 2</td>
            <td>数据 3</td>
        </tr>
    </tbody>
</table>
```

---

### 4. 结束页模板 (End Slide)

**文件**: `templates/end-slide-template.html`

**用途**: 演示文稿的最后一张幻灯片，感谢和联系方式

**设计特点**:
- 渐变背景（橙色到深蓝）
- 大号"感谢聆听"标题（72px）
- 联系信息卡片
- 公司信息展示
- 淡入动画效果

**HTML 结构**:
```html
<div class="slide end-slide active" data-slide="47">
    <div class="decorative-icon">🎉</div>
    <h1 class="thank-you">感谢聆听！</h1>
    <p class="main-message">
        感谢您的时间和关注<br>
        期待与您的进一步交流与合作
    </p>

    <div class="contact-info">
        <div class="contact-title">联系方式</div>
        <div class="contact-details">
            📧 Email: your.email@example.com<br>
            📱 电话: +86 138-xxxx-xxxx<br>
            🌐 网站: www.yourcompany.com
        </div>
    </div>

    <div class="company-info">
        <div class="company-logo">LOGO</div>
        <div class="company-name">公司名称</div>
    </div>
</div>
```

**使用场景**:
- 商业汇报结束
- 产品演示结尾
- 学术演讲结束
- 客户提案结尾

**自定义要点**:
- 修改 `.thank-you`: 感谢语（可改为"谢谢"、"Q&A"等）
- 修改 `.contact-details`: 联系方式
- 修改 `.company-name`: 公司名称
- 修改 `.company-logo`: Logo 或公司标识

---

## McKinsey 设计规范

### 颜色系统

| 用途 | 颜色 | Hex 值 |
|------|------|--------|
| 主背景 | 白色 | `#FFFFFF` |
| 标题栏 | 黑色 | `#000000` |
| 主强调色 | 橙色 | `#F85d42` |
| 辅助色 | 灰色 | `#74788d` |
| 深蓝色 | | `#556EE6` |
| 绿色 | | `#34c38f` |
| 蓝色 | | `#50a5f1` |
| 黄色 | | `#f1b44c` |

### 字体规范

| 元素类型 | 大小 | 字重 | 颜色 |
|---------|------|------|------|
| 标题 | 48-64px | bold | `#000000` |
| 副标题 | 28-36px | bold | `#F85d42` |
| 正文 | 16-20px | normal | `#333333` |
| 图表标签 | 12-14px | normal | `#333333` |

### 布局规范

| 参数 | 数值 | 说明 |
|------|------|------|
| 幻灯片内边距 | 40-60px | 垂直 40px，水平 60px |
| 元素间距 | 20-30px | 内容块之间 |
| 图表容器高度 | 450px | 标准高度 |
| 图表容器宽度 | 最大 900px | 最大宽度 |

---

## 使用流程

### 步骤 1: 选择合适的模板

根据幻灯片类型选择对应模板：
- 第 1 张幻灯片 → `cover-slide-template.html`
- 第 2 张幻灯片 → `toc-slide-template.html`
- 中间内容幻灯片 → `content-slide-template.html`
- 最后一张幻灯片 → `end-slide-template.html`

### 步骤 2: 复制模板代码

从模板文件中复制整个 HTML 代码，粘贴到你的生成工具或 subagent 中。

### 步骤 3: 自定义内容

根据模板中的注释，修改以下内容：
- 文本内容（标题、正文、列表项）
- 数据（Chart.js 图表数据）
- 样式微调（如需）

### 步骤 4: 组装完整演示文稿

将所有幻灯片组合到一个 HTML 文件中：
```html
<!DOCTYPE html>
<html>
<head>
    <style>
        /* 所有 CSS 样式 */
    </style>
</head>
<body>
    <!-- 导航栏 -->
    <nav class="navbar">...</nav>

    <!-- 幻灯片容器 -->
    <div class="presentation-container">
        <!-- 封面页 -->
        <div class="slide title-slide active" data-slide="1">...</div>

        <!-- 目录页 -->
        <div class="slide toc-slide" data-slide="2">...</div>

        <!-- 内容页 1 -->
        <div class="slide" data-slide="3">...</div>

        <!-- 更多内容页 -->

        <!-- 结束页 -->
        <div class="slide end-slide" data-slide="47">...</div>
    </div>

    <!-- 全屏按钮 -->
    <button class="fullscreen-btn">全屏 ⛶</button>

    <!-- JavaScript -->
    <script>
        // 导航和交互功能
    </script>
</body>
</html>
```

---

## 图表集成指南

### 支持的图表类型

| 图表类型 | 适用场景 | Chart.js 类型 |
|---------|---------|--------------|
| 柱状图 | 数据对比、排名 | `bar` |
| 折线图 | 趋势分析 | `line` |
| 饼图 | 部分构成（≤5项） | `pie` |
| 环形图 | 部分构成（≤8项） | `doughnut` |
| 散点图 | 三维数据 | `bubble` |
| 雷达图 | 多维对比 | `radar` |
| 极坐标图 | 周期性数据 | `polarArea` |

### 图表配置示例

```javascript
// 柱状图示例
new Chart(document.getElementById('myChart'), {
    type: 'bar',
    data: {
        labels: ['类别1', '类别2', '类别3'],
        datasets: [{
            label: '数据系列',
            data: [100, 200, 150],
            backgroundColor: ['#F85d42', '#556EE6', '#34c38f'] // McKinsey 颜色
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: {
                display: true,
                position: 'top',
                labels: {
                    font: {
                        size: 14
                    }
                }
            },
            title: {
                display: true,
                text: '图表标题',
                font: {
                    size: 18,
                    weight: 'bold'
                }
            }
        },
        scales: {
            y: {
                beginAtZero: true,
                grid: {
                    color: '#e9ecef'
                }
            }
        }
    }
});
```

---

## 响应式设计

所有模板都支持响应式设计，自动适配不同屏幕尺寸：

| 断点 | 屏幕宽度 | 适配 |
|------|----------|------|
| 桌面端 | 1200px+ | 最佳体验 |
| 平板 | 768px-1200px | 中等布局 |
| 移动端 | <768px | 简化布局 |

### 移动端优化

- 导航栏按钮变小
- 字体大小自动调整
- 图表高度自动缩放
- 布局自动切换为单栏

---

## 交互功能

### 键盘快捷键

| 按键 | 功能 |
|------|------|
| `→` 或 `空格` | 下一张 |
| `←` | 上一张 |
| `F` | 全屏模式 |
| `ESC` | 退出全屏 |
| `Home` | 第一张 |
| `End` | 最后一张 |

### 鼠标操作

- 点击导航按钮：上一张/下一张
- 点击全屏按钮：全屏模式
- 悬停图表：查看详细数据
- 点击目录项：跳转到对应章节

---

## 最佳实践

### 1. 内容组织

- **封面页**: 清晰的标题和副标题
- **目录页**: 5-7 个主要部分
- **内容页**: 每张幻灯片 1 个核心主题
- **结束页**: 感谢和联系方式

### 2. 设计一致性

- **所有幻灯片使用相同的颜色系统**
- **字体大小保持在规定范围内**
- **页边距和间距保持一致**
- **导航栏在所有幻灯片中位置一致**

### 3. 数据可视化

- **优先使用 McKinsey 配色方案**
- **图表标题清晰明确**
- **数据标签精度一致**
- **图例位置合理**

### 4. 内容完整性

- **100% 保留源文档内容**
- **不精简、不总结**
- **保持数据精度**
- **使用原文措辞**

---

## 常见问题

### Q1: 如何修改图表数据？

**A**: 在 JavaScript 部分，修改 `data` 数组：
```javascript
data: [365.875, 1723.498, 123.55]  // 保持精度
```

### Q2: 如何添加新的幻灯片？

**A**:
1. 复制整个 `<div class="slide">...</div>` 块
2. 修改 `data-slide` 属性（递增数字）
3. 填充内容
4. 更新 `totalSlides` 变量

### Q3: 如何修改颜色？

**A**: 在 `:root` 中修改 CSS 变量：
```css
:root {
    --primary-accent: #F85d42;  /* 修改这个值 */
}
```

### Q4: 如何调整幻灯片数量？

**A**:
1. 修改导航栏中的 `totalSlides` 显示
2. 修改 JavaScript 中的 `totalSlides = 47` 变量
3. 确保 `data-slide` 属性连续（1, 2, 3...）

### Q5: 如何添加自定义图表？

**A**:
1. 添加 `<div class="chart-container"><canvas id="myChart"></canvas></div>`
2. 在 `<script>` 中初始化图表：
   ```javascript
   const ctx = document.getElementById('myChart');
   new Chart(ctx, { /* 配置 */ });
   ```

---

## 文件结构

```
html-presentation-beautifier/
├── templates/
│   ├── cover-slide-template.html      # 封面页模板
│   ├── toc-slide-template.html        # 目录页模板
│   ├── content-slide-template.html     # 内容页模板
│   └── end-slide-template.html        # 结束页模板
├── agents/
│   └── html-presentation-reviewer.md
├── skills/
│   └── beauty-html/
│       └── SKILL.md
└── commands/
    └── beauty.md
```

---

## 更新日志

**v2.0.0** (2025-01-25):
- ✅ 新增 4 种幻灯片模板
- ✅ 封面页模板：渐变背景，元信息展示
- ✅ 目录页模板：两栏网格，快速导航
- ✅ 内容页模板：完整组件库，8种图表集成
- ✅ 结束页模板：感谢页面，联系方式
- ✅ McKinsey 设计系统精确匹配
- ✅ 响应式设计支持
- ✅ 完整交互功能

---

**使用建议**:

1. **快速开始**: 直接复制对应模板代码到你的生成工具
2. **自定义**: 根据需要修改内容、数据、样式
3. **组合使用**: 将不同模板组合到同一个 HTML 文件
4. **质量检查**: 生成后使用 html-presentation-reviewer 验证质量
5. **持续优化**: 根据反馈不断调整和改进

**获取帮助**:
- 查看模板文件中的注释
- 参考本文档的使用说明
- 使用 reviewer agent 检查质量
- 阅读 McKinsey 设计规范指南

---

**版本**: 2.0.0
**维护者**: Claude Code
**最后更新**: 2025-01-25
