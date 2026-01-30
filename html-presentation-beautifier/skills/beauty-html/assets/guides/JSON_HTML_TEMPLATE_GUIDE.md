# JSON+HTML 演示文稿模板使用指南 / JSON+HTML Presentation Template Guide

本指南说明如何使用 JSON 数据驱动的方式生成 McKinsey 风格 HTML 演示文稿。

This guide explains how to generate McKinsey-style HTML presentations using JSON-driven approach.

---

## 📋 目录 / Table of Contents

1. [模板结构 / Template Structure](#模板结构--template-structure)
2. [JSON 数据格式 / JSON Data Format](#json-数据格式--json-data-format)
3. [渲染引擎 / Rendering Engine](#渲染引擎--rendering-engine)
4. [幻灯片类型 / Slide Types](#幻灯片类型--slide-types)
5. [使用示例 / Usage Examples](#使用示例--usage-examples)

---

## 模板结构 / Template Structure

JSON+HTML 模板由三个核心部分组成：

The JSON+HTML template consists of three core parts:

### 1. HTML 框架 / HTML Framework
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <!-- Meta 信息 / Meta Information -->
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>演示文稿标题</title>
    
    <!-- Chart.js 库 / Chart.js Library -->
    <script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.0/dist/chart.umd.min.js"></script>
    
    <!-- McKinsey 设计系统样式 / McKinsey Design System Styles -->
    <style>
        /* 完整的 CSS 样式 */
    </style>
</head>
<body>
    <!-- 导航栏 / Navigation Bar -->
    <div class="navbar">...</div>
    
    <!-- 演示容器 / Presentation Container -->
    <div class="presentation-container" id="slidesContainer">
        <!-- 动态生成的幻灯片 / Dynamically Generated Slides -->
    </div>
    
    <!-- JavaScript 渲染引擎 / JavaScript Rendering Engine -->
    <script>
        // JSON 数据 + 渲染逻辑
    </script>
</body>
</html>
```

### 2. JSON 数据结构 / JSON Data Structure
```javascript
const presentationData = {
    "metadata": {
        "title": "演示文稿标题",
        "subtitle": "副标题",
        "author": "作者",
        "date": "日期",
        "totalSlides": 数量
    },
    "slides": [
        // 幻灯片数组
    ]
};
```

### 3. JavaScript 渲染引擎 / JavaScript Rendering Engine
```javascript
// 初始化函数
function initPresentation() { ... }

// 渲染函数
function renderSlide(slide) { ... }

// 导航函数
function showSlide(index) { ... }
function nextSlide() { ... }
function previousSlide() { ... }
```

---

## JSON 数据格式 / JSON Data Format

### Metadata 对象 / Metadata Object

```json
{
    "metadata": {
        "title": "演示文稿主标题 / Main Title",
        "subtitle": "副标题（可选）/ Subtitle (Optional)",
        "author": "作者姓名 / Author Name",
        "date": "创建日期 / Creation Date",
        "totalSlides": 5
    }
}
```

### Slide 对象 / Slide Object

每个幻灯片包含以下字段：

Each slide contains the following fields:

```json
{
    "id": 1,                    // 唯一标识符 / Unique Identifier
    "type": "cover",            // 幻灯片类型 / Slide Type
    "title": "标题",            // 幻灯片标题 / Slide Title
    "content": { ... }          // 内容对象（根据类型不同）/ Content Object (varies by type)
}
```

---

## 幻灯片类型 / Slide Types

### 1. 封面页 / Cover Slide

**类型标识 / Type Identifier**: `"type": "cover"`

**JSON 结构 / JSON Structure**:
```json
{
    "id": 1,
    "type": "cover",
    "title": "演示文稿标题",
    "subtitle": "副标题",
    "metadata": "作者 | 日期"
}
```

**渲染结果 / Rendered Output**:
```html
<div class="slide slide-cover">
    <h1>演示文稿标题</h1>
    <div class="subtitle">副标题</div>
    <div class="metadata">作者 | 日期</div>
</div>
```

---

### 2. 目录页 / Table of Contents Slide

**类型标识 / Type Identifier**: `"type": "toc"`

**JSON 结构 / JSON Structure**:
```json
{
    "id": 2,
    "type": "toc",
    "title": "目录",
    "content": {
        "items": [
            { "number": "01", "title": "章节标题1" },
            { "number": "02", "title": "章节标题2" },
            { "number": "03", "title": "章节标题3" }
        ]
    }
}
```

**布局规则 / Layout Rules**:
- ✅ **≤3 项**：单列布局 / Single column layout
- ✅ **>3 项**：双列布局 / Two column layout
- ✅ 移动端自动切换为单列 / Auto switch to single column on mobile

**渲染逻辑 / Rendering Logic**:
```javascript
case 'toc':
    // 根据项目数量动态决定布局
    const tocClass = slide.content.items.length <= 3 ? 'single-column' : 'two-columns';
    slideDiv.innerHTML = `
        <h2>${slide.title}</h2>
        <ul class="toc-list ${tocClass}">
            ${slide.content.items.map(item => `
                <li class="toc-item">
                    <span class="toc-number">${item.number}</span>
                    <span class="toc-title">${item.title}</span>
                </li>
            `).join('')}
        </ul>
    `;
    break;
```

**视觉效果 / Visual Effects**:
- ✅ 左边框橙色强调
- ✅ 鼠标悬停背景变深
- ✅ 悬停时向右移动 10px
- ✅ 大号编号（36px）+ 标题（24px）

**渲染结果 / Rendered Output**:
```html
<div class="slide slide-toc">
    <h2>目录</h2>
    <ul class="toc-list single-column">  <!-- 或 two-columns -->
        <li class="toc-item">
            <span class="toc-number">01</span>
            <span class="toc-title">章节标题1</span>
        </li>
        <li class="toc-item">
            <span class="toc-number">02</span>
            <span class="toc-title">章节标题2</span>
        </li>
        <li class="toc-item">
            <span class="toc-number">03</span>
            <span class="toc-title">章节标题3</span>
        </li>
    </ul>
</div>
```

---

### 3. 章节目录页 / Chapter Overview Slide

**类型标识 / Type Identifier**: `"type": "chapter-overview"`

**JSON 结构 / JSON Structure**:
```json
{
    "id": 3,
    "type": "chapter-overview",
    "title": "第一章：战略基础",
    "content": {
        "intro": "本章节深入分析跨境垂直平台的战略定位、核心优势和发展路径，为后续决策提供理论基础。",
        "points": [
            {
                "number": "1.1",
                "title": "核心战略方向",
                "description": "明确跨境垂直平台的战略定位，聚焦数据驱动和可持续发展模式"
            },
            {
                "number": "1.2",
                "title": "竞争优势分析",
                "description": "对比平台模式与个人IP模式的差异，评估长期竞争力"
            },
            {
                "number": "1.3",
                "title": "资源投入规划",
                "description": "分析时间、人力、资金等资源的投入策略和预期回报"
            }
        ]
    }
}
```

**特点 / Features**:
- ✅ **章节介绍** / Chapter Introduction：`intro` 字段提供章节概览
- ✅ **卡片布局** / Card Layout：每个要点以卡片形式呈现
- ✅ **三层信息** / Three-level Information：编号 + 标题 + 描述
- ✅ **响应式网格** / Responsive Grid：自动适配屏幕宽度
- ✅ **交互效果** / Interactive Effects：鼠标悬停时卡片上浮

**布局规则 / Layout Rules**:
```css
.chapter-points-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(400px, 1fr));
    gap: 30px;
}
```
- 最小卡片宽度：400px
- 自动适配列数（1列、2列或更多）
- 卡片间距：30px

**视觉效果 / Visual Effects**:
- ✅ 编号：42px，橙色，粗体
- ✅ 标题：22px，黑色，粗体
- ✅ 描述：16px，灰色，行高1.7
- ✅ 悬停：卡片上移5px，添加阴影

**与全局目录的区别 / Differences from Global TOC**:

| 特性 | 全局目录 (toc) | 章节目录 (chapter-overview) |
|------|----------------|---------------------------|
| **用途** | 演示文稿整体导航 | 单个章节详细介绍 |
| **信息层次** | 编号 + 标题 | 编号 + 标题 + 描述 |
| **布局** | 列表式（1列或2列）| 卡片网格（自适应） |
| **描述** | ❌ 无 | ✅ 有详细描述 |
| **章节介绍** | ❌ 无 | ✅ 有 intro 字段 |
| **交互效果** | 水平移动 | 垂直上浮 + 阴影 |

**渲染结果 / Rendered Output**:
```html
<div class="slide slide-chapter-overview">
    <h2>第一章：战略基础</h2>
    <div class="chapter-intro">本章节深入分析跨境垂直平台的战略定位、核心优势和发展路径...</div>
    <div class="chapter-points-grid">
        <div class="chapter-point-card">
            <div class="chapter-point-number">1.1</div>
            <div class="chapter-point-title">核心战略方向</div>
            <div class="chapter-point-description">明确跨境垂直平台的战略定位...</div>
        </div>
        <div class="chapter-point-card">
            <div class="chapter-point-number">1.2</div>
            <div class="chapter-point-title">竞争优势分析</div>
            <div class="chapter-point-description">对比平台模式与个人IP模式的差异...</div>
        </div>
        <div class="chapter-point-card">
            <div class="chapter-point-number">1.3</div>
            <div class="chapter-point-title">资源投入规划</div>
            <div class="chapter-point-description">分析时间、人力、资金等资源的投入策略...</div>
        </div>
    </div>
</div>
```

**使用建议 / Usage Recommendations**:
- ✅ 在重要章节开始时使用
- ✅ 提供足够的上下文信息
- ✅ 描述应简洁明了（建议40-80字）
- ✅ 编号建议使用章节号格式（如 1.1, 1.2, 2.1）

---

### 4. 内容页 / Content Slide

**类型标识 / Type Identifier**: `"type": "content"`

**JSON 结构 / JSON Structure**:
```json
{
    "id": 3,
    "type": "content",
    "title": "幻灯片标题",
    "content": {
        "points": [
            "要点1",
            "要点2",
            "要点3"
        ]
    }
}
```

**渲染结果 / Rendered Output**:
```html
<div class="slide slide-content">
    <h2>幻灯片标题</h2>
    <div class="content-body">
        <ul class="content-list">
            <li>要点1</li>
            <li>要点2</li>
            <li>要点3</li>
        </ul>
    </div>
</div>
```

---

### 5. 两列布局 / Two-Column Slide

**类型标识 / Type Identifier**: `"type": "two-column"`

**JSON 结构 / JSON Structure**:
```json
{
    "id": 4,
    "type": "two-column",
    "title": "对比分析",
    "content": {
        "columns": [
            {
                "title": "左列标题",
                "points": ["要点1", "要点2", "要点3"]
            },
            {
                "title": "右列标题",
                "points": ["要点1", "要点2", "要点3"]
            }
        ]
    }
}
```

**渲染结果 / Rendered Output**:
```html
<div class="slide slide-two-column">
    <h2>对比分析</h2>
    <div class="two-column">
        <div class="column">
            <h3>左列标题</h3>
            <ul class="content-list">
                <li>要点1</li>
                <li>要点2</li>
                <li>要点3</li>
            </ul>
        </div>
        <div class="column">
            <h3>右列标题</h3>
            <ul class="content-list">
                <li>要点1</li>
                <li>要点2</li>
                <li>要点3</li>
            </ul>
        </div>
    </div>
</div>
```

---

### 6. 图表页 / Chart Slide

**类型标识 / Type Identifier**: `"type": "chart"`

**JSON 结构 / JSON Structure**:
```json
{
    "id": 5,
    "type": "chart",
    "title": "数据分析",
    "content": {
        "chartType": "line",
        "chartConfig": {
            "labels": ["Q1", "Q2", "Q3", "Q4"],
            "datasets": [
                {
                    "label": "数据系列1",
                    "data": [65, 59, 80, 81],
                    "borderColor": "#F85d42",
                    "backgroundColor": "rgba(248, 93, 66, 0.1)",
                    "borderWidth": 3,
                    "tension": 0.4,
                    "fill": true
                }
            ]
        }
    }
}
```

**支持的图表类型 / Supported Chart Types**:
- `line` - 折线图 / Line Chart
- `bar` - 柱状图 / Bar Chart
- `pie` - 饼图 / Pie Chart
- `doughnut` - 环形图 / Doughnut Chart
- `radar` - 雷达图 / Radar Chart

---

### 7. 结束页 / End Slide

**类型标识 / Type Identifier**: `"type": "end"`

**JSON 结构 / JSON Structure**:
```json
{
    "id": 6,
    "type": "end",
    "title": "谢谢",
    "subtitle": "Thank You",
    "message": "期待与您的进一步交流",
    "contact": {
        "email": "contact@example.com",
        "website": "www.example.com"
    }
}
```

**渲染结果 / Rendered Output**:
```html
<div class="slide slide-end">
    <h1>谢谢</h1>
    <div class="subtitle">Thank You</div>
    <div class="end-message">期待与您的进一步交流</div>
    <div class="contact-info">
        <div>邮箱：contact@example.com</div>
        <div>网站：www.example.com</div>
    </div>
</div>
```

---

## 渲染引擎 / Rendering Engine

### 核心函数 / Core Functions

#### 1. initPresentation()
**功能 / Function**: 初始化演示文稿

**执行流程 / Execution Flow**:
```javascript
function initPresentation() {
    // 1. 设置标题
    document.getElementById('presentationTitle').textContent = presentationData.metadata.title;
    
    // 2. 设置幻灯片总数
    document.getElementById('totalSlides').textContent = presentationData.metadata.totalSlides;
    
    // 3. 渲染所有幻灯片
    const container = document.getElementById('slidesContainer');
    presentationData.slides.forEach(slide => {
        const slideElement = renderSlide(slide);
        container.appendChild(slideElement);
    });
    
    // 4. 显示第一张幻灯片
    showSlide(0);
}
```

#### 2. renderSlide(slide)
**功能 / Function**: 根据 JSON 数据渲染单个幻灯片

**参数 / Parameters**:
- `slide` - 幻灯片 JSON 对象

**返回值 / Returns**:
- HTML DOM 元素

**示例 / Example**:
```javascript
function renderSlide(slide) {
    const slideDiv = document.createElement('div');
    slideDiv.className = `slide slide-${slide.type}`;
    slideDiv.dataset.slideId = slide.id;
    
    switch(slide.type) {
        case 'cover':
            // 渲染封面页
            break;
        case 'content':
            // 渲染内容页
            break;
        case 'two-column':
            // 渲染两列布局
            break;
        case 'chart':
            // 渲染图表页
            break;
    }
    
    return slideDiv;
}
```

#### 3. showSlide(index)
**功能 / Function**: 显示指定索引的幻灯片

**参数 / Parameters**:
- `index` - 幻灯片索引（从0开始）

**执行流程 / Execution Flow**:
```javascript
function showSlide(index) {
    // 1. 获取所有幻灯片
    const slides = document.querySelectorAll('.slide');
    
    // 2. 索引边界处理
    if (index < 0) index = slides.length - 1;
    if (index >= slides.length) index = 0;
    
    // 3. 移除所有 active 类
    slides.forEach(slide => slide.classList.remove('active'));
    
    // 4. 添加 active 类到当前幻灯片
    slides[index].classList.add('active');
    
    // 5. 更新当前索引
    currentSlideIndex = index;
    document.getElementById('currentSlide').textContent = index + 1;
    
    // 6. 如果是图表页，渲染图表
    const activeSlide = slides[index];
    if (activeSlide.classList.contains('slide-chart')) {
        renderChart(activeSlide);
    }
}
```

---

## 使用示例 / Usage Examples

### 示例 1：基础演示文稿 / Example 1: Basic Presentation

```javascript
const presentationData = {
    "metadata": {
        "title": "季度业绩报告",
        "subtitle": "2024年Q1",
        "author": "财务部",
        "date": "2024年4月",
        "totalSlides": 3
    },
    "slides": [
        {
            "id": 1,
            "type": "cover",
            "title": "季度业绩报告",
            "subtitle": "2024年Q1",
            "metadata": "财务部 | 2024年4月"
        },
        {
            "id": 2,
            "type": "content",
            "title": "核心业绩指标",
            "content": {
                "points": [
                    "营收同比增长25%",
                    "利润率提升3个百分点",
                    "客户满意度达到92%",
                    "市场份额增加2%"
                ]
            }
        },
        {
            "id": 3,
            "type": "content",
            "title": "下一步计划",
            "content": {
                "points": [
                    "扩大市场覆盖",
                    "优化产品线",
                    "提升服务质量"
                ]
            }
        }
    ]
};
```

### 示例 2：带图表的演示文稿 / Example 2: Presentation with Charts

```javascript
const presentationData = {
    "metadata": {
        "title": "销售数据分析",
        "totalSlides": 2
    },
    "slides": [
        {
            "id": 1,
            "type": "cover",
            "title": "销售数据分析",
            "subtitle": "月度趋势报告"
        },
        {
            "id": 2,
            "type": "chart",
            "title": "销售趋势",
            "content": {
                "chartType": "line",
                "chartConfig": {
                    "labels": ["1月", "2月", "3月", "4月", "5月", "6月"],
                    "datasets": [
                        {
                            "label": "销售额（万元）",
                            "data": [150, 180, 220, 210, 280, 320],
                            "borderColor": "#F85d42",
                            "backgroundColor": "rgba(248, 93, 66, 0.1)",
                            "borderWidth": 3,
                            "tension": 0.4,
                            "fill": true
                        }
                    ]
                }
            }
        }
    ]
};
```

---

## 🎨 McKinsey 设计规范 / McKinsey Design Standards

### 颜色使用 / Color Usage

```css
:root {
    --color-bg: #FFFFFF;              /* 背景色 / Background */
    --color-text-primary: #000000;    /* 主文本 / Primary Text */
    --color-text-secondary: #333333;  /* 次文本 / Secondary Text */
    --color-accent-primary: #F85d42;  /* 主强调色 / Primary Accent */
    --color-accent-secondary: #74788d;/* 次强调色 / Secondary Accent */
    --color-blue: #556EE6;            /* 蓝色 / Blue */
    --color-green: #34c38f;           /* 绿色 / Green */
    --color-light-blue: #50a5f1;      /* 浅蓝 / Light Blue */
    --color-yellow: #f1b44c;          /* 黄色 / Yellow */
}
```

### 字体规范 / Font Standards

| 元素 / Element | 大小 / Size | 粗细 / Weight | 颜色 / Color |
|----------------|-------------|---------------|--------------|
| 封面标题 / Cover Title | 64px | 700 | #000000 |
| 内容标题 / Content Title | 48px | 700 | #000000 |
| 副标题 / Subtitle | 32px | 400 | #74788d |
| 正文 / Body Text | 20px | 400 | #333333 |
| 列表项 / List Item | 20px | 400 | #333333 |

### 间距规范 / Spacing Standards

| 区域 / Area | 间距 / Spacing |
|-------------|----------------|
| 幻灯片内边距 / Slide Padding | 60px 80px |
| 标题下边距 / Title Bottom Margin | 40px |
| 列表项间距 / List Item Spacing | 15px 0 |
| 两列间距 / Two-Column Gap | 40px |

---

## 🔧 自定义扩展 / Custom Extensions

### 添加新的幻灯片类型 / Adding New Slide Types

1. **定义 JSON 结构 / Define JSON Structure**:
```json
{
    "id": 5,
    "type": "custom-type",
    "title": "自定义标题",
    "content": { ... }
}
```

2. **在 renderSlide() 中添加处理逻辑 / Add Logic in renderSlide()**:
```javascript
function renderSlide(slide) {
    // ...existing code...
    
    switch(slide.type) {
        // ...existing cases...
        
        case 'custom-type':
            slideDiv.innerHTML = `
                <!-- 自定义HTML结构 -->
            `;
            break;
    }
    
    return slideDiv;
}
```

3. **添加对应的 CSS 样式 / Add Corresponding CSS**:
```css
.slide-custom-type {
    /* 自定义样式 */
}
```

---

## ✅ 最佳实践 / Best Practices

### 1. JSON 数据组织 / JSON Data Organization
- ✅ 保持数据结构清晰简洁
- ✅ 使用语义化的字段名
- ✅ 避免深层嵌套
- ✅ 统一命名规范

### 2. 性能优化 / Performance Optimization
- ✅ 图表仅在显示时渲染（懒加载）
- ✅ 使用 CSS 动画替代 JavaScript
- ✅ 避免在渲染函数中进行复杂计算
- ✅ 复用 DOM 元素

### 3. 可维护性 / Maintainability
- ✅ 分离数据和逻辑
- ✅ 使用函数封装重复逻辑
- ✅ 添加必要的注释
- ✅ 保持代码格式一致

### 4. 内容质量 / Content Quality
- ✅ 每页要点不超过8个
- ✅ 使用简洁明了的语言
- ✅ 数据可视化优先
- ✅ 保持视觉层次清晰

---

## 📚 参考资源 / Reference Resources

### 示例文件 / Example Files
- `json-html-example.html` - 完整示例 / Complete Example
- `presentation-template.html` - 基础模板 / Basic Template

### 相关指南 / Related Guides
- `mckinsey-design-system.md` - McKinsey 设计系统
- `best-practices.md` - HTML 最佳实践
- `TEMPLATE_USAGE_GUIDE.md` - 模板使用指南

---

## 🤝 技术支持 / Technical Support

如有问题，请参考：
- 项目文档 / Project Documentation
- 示例文件 / Example Files
- 设计规范 / Design Standards

For questions, please refer to:
- Project Documentation
- Example Files
- Design Standards
