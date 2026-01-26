# 幻灯片模板快速参考

**插件**: html-presentation-beautifier v2.0
**模板路径**: `templates/`

---

## 🎯 4 种幻灯片模板

| 模板类型 | 文件名 | 用途 | 幻灯片位置 |
|---------|--------|------|------------|
| **封面页** | `cover-slide-template.html` | 演示文稿开场 | 第 1 张 |
| **目录页** | `toc-slide-template.html` | 章节导航 | 第 2 张 |
| **内容页** | `content-slide-template.html` | 主要内容 | 第 3-46 张 |
| **结束页** | `end-slide-template.html` | 感谢结尾 | 最后 1 张 |

---

## 🎨 McKinsey 设计规范

### 颜色（精确匹配）
```css
--primary-accent: #F85d42      /* 主橙色 */
--secondary-accent: #74788d    /* 灰色 */
--deep-blue: #556EE6           /* 深蓝 */
--green: #34c38f                /* 绿色 */
--blue: #50a5f1                 /* 蓝色 */
--yellow: #f1b44c               /* 黄色 */
```

### 字体大小（必须遵守）
```css
标题: 56px (48-64px 范围) ✅
副标题: 32px (28-36px 范围) ✅
正文: 18px (16-20px 范围) ✅
图表标签: 12-14px ✅
```

### 布局（精确数值）
```css
页边距: 40px 垂直, 60px 水平 ✅
元素间距: 20-30px ✅
图表高度: 450px ✅
图表宽度: 最大 900px ✅
```

---

## 📋 内容页模板组件速查

### 文本组件
```html
<h1 class="slide-title">主标题</h1>
<h2 class="slide-subtitle">副标题</h2>
<h3 class="section-heading">分节标题</h3>
<p class="text-content">正文内容</p>
<p class="key-point">关键要点</p>
```

### 列表组件
```html
<ul class="bullet-list">
  <li>无序列表项</li>
</ul>

<ol class="numbered-list">
  <li>有序列表项</li>
</ol>
```

### 布局组件
```html
<div class="two-column">
  <div class="column">左栏</div>
  <div class="column">右栏</div>
</div>
```

### 图表组件
```html
<div class="chart-container">
  <canvas id="chartId"></canvas>
</div>
<script>
new Chart(document.getElementById('chartId'), {
    type: 'bar',
    data: { /* 数据 */ },
    options: { /* 配置 */ }
});
</script>
```

### 强调组件
```html
<div class="emphasis-container">
  <div class="emphasis-box">
    <div class="emphasis-icon">📊</div>
    <div class="emphasis-text">标题</div>
    <div class="emphasis-description">说明</div>
  </div>
</div>

<div class="conclusions-grid">
  <div class="conclusion-card">
    <div class="conclusion-number">01</div>
    <div class="conclusion-title">结论标题</div>
    <div class="conclusion-text">结论内容</div>
  </div>
</div>
```

### 信息/高亮组件
```html
<div class="info-box">
  <div class="info-box-title">信息框</div>
  <div class="info-box-content">内容</div>
</div>

<div class="highlight-box">
  <div class="highlight-title">高亮标题</div>
  <div class="highlight-content">高亮内容</div>
</div>
```

### 流程图组件
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

### 表格组件
```html
<table class="data-table">
  <thead>
    <tr>
      <th>列标题</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>数据</td>
    </tr>
  </tbody>
</table>
```

---

## 🚀 快速使用流程

### 1. 创建新演示文稿

```bash
# Step 1: 复制模板
cp templates/content-slide-template.html my-presentation.html

# Step 2: 编辑内容
# 打开 my-presentation.html，修改：
# - 标题、副标题、正文
# - 图表数据
# - 列表项

# Step 3: 在浏览器中测试
open my-presentation.html

# Step 4: 质量检查
# 运行 html-presentation-reviewer 验证
```

### 2. 组装完整演示文稿

```html
<!DOCTYPE html>
<html>
<head>
    <style>
        /* 复制模板的 CSS */
    </style>
</head>
<body>
    <nav class="navbar">
        <!-- 导航按钮 -->
    </nav>

    <div class="presentation-container">
        <!-- 1. 封面页 -->
        <div class="slide title-slide active" data-slide="1">
            <!-- 复制 cover-slide-template.html 内容 -->
        </div>

        <!-- 2. 目录页 -->
        <div class="slide toc-slide" data-slide="2">
            <!-- 复制 toc-slide-template.html 内容 -->
        </div>

        <!-- 3-46. 内容页 -->
        <div class="slide" data-slide="3">
            <!-- 复制 content-slide-template.html 结构 -->
        </div>

        <!-- ... 更多内容页 ... -->

        <!-- 47. 结束页 -->
        <div class="slide end-slide" data-slide="47">
            <!-- 复制 end-slide-template.html 内容 -->
        </div>
    </div>

    <script>
        // 复制模板的 JavaScript
        // 修改 totalSlides = 47
        // 初始化图表
    </script>
</body>
</html>
```

---

## 📊 图表配置示例

### 柱状图
```javascript
new Chart(ctx, {
    type: 'bar',
    data: {
        labels: ['A', 'B', 'C'],
        datasets: [{
            label: '销售额',
            data: [100, 200, 150],
            backgroundColor: ['#F85d42', '#556EE6', '#34c38f'] // McKinsey 颜色
        }]
    }
});
```

### 折线图
```javascript
new Chart(ctx, {
    type: 'line',
    data: {
        labels: ['2024', '2025', '2026'],
        datasets: [{
            label: '增长趋势',
            data: [100, 150, 200],
            borderColor: '#F85d42',
            backgroundColor: 'rgba(248, 93, 66, 0.1)',
            fill: true
        }]
    }
});
```

### 环形图
```javascript
new Chart(ctx, {
    type: 'doughnut',
    data: {
        labels: ['类型A', '类型B', '类型C'],
        datasets: [{
            data: [30, 50, 20],
            backgroundColor: ['#F85d42', '#556EE6', '#34c38f']
        }]
    }
});
```

---

## ✅ 质量检查清单

生成演示文稿后，使用 `html-presentation-reviewer` 检查：

### 设计风格
- [ ] 颜色精确匹配（8 个标准颜色）
- [ ] 字体大小在规定范围内
- [ ] 页边距 40-60px
- [ ] 元素间距 20-30px

### 内容完整性
- [ ] 无内容精简
- [ ] 数据精度保持
- [ ] 列表项完整
- [ ] 使用原文措辞

### 代码质量
- [ ] HTML 有效
- [ ] CSS 语法正确
- [ ] JavaScript 无错误
- [ ] 图表正常显示

---

## 🎯 使用场景

| 场景 | 推荐模板 | 幻灯片数量 |
|------|----------|-----------|
| 简短汇报 | 封面+内容+结束 | 5-10 张 |
| 标准汇报 | 封面+目录+内容+结束 | 15-30 张 |
| 详细报告 | 封面+目录+内容+结束 | 40-60 张 |

---

## 📁 文件位置

```
html-presentation-beautifier/
├── templates/
│   ├── cover-slide-template.html
│   ├── toc-slide-template.html
│   ├── content-slide-template.html
│   └── end-slide-template.html
├── SLIDE_TEMPLATES_GUIDE.md         # 详细使用指南
└── SLIDE_TEMPLATES_QUICK_REF.md   # 本文档
```

---

**提示**:
- 所有模板都已包含 McKinsey 设计系统 CSS
- 所有模板都有完整的导航和交互功能
- 建议先在模板中测试，再复制到实际项目

---

**版本**: 2.0.0
**更新**: 2025-01-25
