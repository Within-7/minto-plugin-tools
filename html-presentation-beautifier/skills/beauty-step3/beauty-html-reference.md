# HTML/CSS参考库

本文档提供幻灯片HTML/CSS的完整参考，包括设计系统、布局结构和组件模板。

**重要参考**：
- 本文档是beauty-html skill的简化版参考
- 完整布局索引请参考 `beauty-html/LAYOUTS_INDEX.md`
- 完整组件索引请参考 `beauty-html/COMPONENTS_INDEX.md`
- 详细示例请参考 `beauty-html/assets/layouts/*.html` 和 `beauty-html/assets/components/*.html`
- 如果项目存在 `.ppt_assets/INDEX.md`，必须优先使用其中的布局和组件示例

---

## 1 设计系统

### 1.1 配色方案 [强制]

**必须使用以下颜色规范，禁止使用其他颜色方案。**

```css
:root {
    /* 基础色 */
    --color-bg: #FFFFFF;
    --color-primary: #000000;
    --color-accent-primary: #F85d42;
    
    /* 辅助色系 */
    --color-gray: #74788d;
    --color-blue: #556EE6;
    --color-green: #34c38f;
    --color-light-blue: #50a5f1;
    --color-yellow: #f1b44c;
    
    /* 文本色 */
    --color-text-primary: #1A202C;
    --color-text-secondary: #4A5568;
}
```

### 1.2 字体规范

```css
:root {
    /* 字体族 */
    --font-family-primary: -apple-system, BlinkMacSystemFont, "Segoe UI", "PingFang SC", "Hiragino Sans GB", "Microsoft YaHei", sans-serif;
    --font-family-mono: "SF Mono", "Monaco", "Inconsolata", "Fira Mono", "Droid Sans Mono", monospace;
    
    /* 字号 */
    --font-size-display: 64px;
    --font-size-h1: 48px;
    --font-size-h2: 36px;
    --font-size-h3: 28px;
    --font-size-h4: 24px;
    --font-size-body-large: 20px;
    --font-size-body: 18px;
    --font-size-body-secondary: 16px;
    --font-size-caption: 14px;
    
    /* 字重 */
    --font-weight-bold: 700;
    --font-weight-semibold: 600;
    --font-weight-medium: 500;
    --font-weight-regular: 400;
    
    /* 行高 */
    --line-height-tight: 1.25;
    --line-height-normal: 1.6;
    --line-height-relaxed: 1.75;
}
```

### 1.3 间距规范

```css
:root {
    /* 基础间距 */
    --spacing-xs: 4px;
    --spacing-sm: 8px;
    --spacing-md: 16px;
    --spacing-lg: 24px;
    --spacing-xl: 32px;
    --spacing-2xl: 48px;
    --spacing-3xl: 64px;
    --spacing-4xl: 96px;
    
    /* 页面边距 */
    --page-padding: 80px 60px 60px 60px;
    
    /* 内容区宽度 */
    --content-max-width: 1200px;
}
```

---

## 2 布局结构

### 2.1 幻灯片容器

```css
.presentation-container {
    width: 100%;
    height: 100vh;
    position: relative;
    overflow: hidden;
    background: var(--color-bg);
}

.slide {
    position: absolute;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: var(--color-bg);
    padding: var(--page-padding);
    box-sizing: border-box;
    opacity: 0;
    visibility: hidden;
    transition: opacity 0.4s ease, visibility 0.4s ease;
    overflow-y: auto;
}

.slide.active {
    opacity: 1;
    visibility: visible;
    z-index: 1;
}
```

### 2.2 导航栏

```css
.slide-header {
    position: fixed;
    top: 0;
    left: 0;
    right: 0;
    height: 60px;
    background: var(--color-primary);
    color: white;
    display: flex;
    align-items: center;
    padding: 0 60px;
    z-index: 100;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.15);
}

.slide-title {
    font-size: var(--font-size-body);
    font-weight: var(--font-weight-medium);
    color: white;
    margin: 0;
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
}

/* 封面页不显示导航栏 */
.cover-slide .slide-header {
    display: none;
}
```

### 2.3 布局类型

#### 单列布局

```css
.single-column {
    display: grid;
    grid-template-columns: 1fr;
    gap: var(--spacing-xl);
    max-width: var(--content-max-width);
    margin: 0 auto;
}
```

#### 两列布局

```css
.two-column {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: var(--spacing-2xl);
    max-width: var(--content-max-width);
    margin: 0 auto;
}

@media (max-width: 768px) {
    .two-column {
        grid-template-columns: 1fr;
    }
}
```

#### 三列布局

```css
.three-column {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: var(--spacing-lg);
    max-width: var(--content-max-width);
    margin: 0 auto;
}

@media (max-width: 992px) {
    .three-column {
        grid-template-columns: repeat(2, 1fr);
    }
}

@media (max-width: 576px) {
    .three-column {
        grid-template-columns: 1fr;
    }
}
```

---

## 3 列表样式

### 3.1 标准要点列表

```css
.bullet-list {
    list-style: none;
    padding-left: 0;
}

.bullet-list li {
    position: relative;
    padding-left: 28px;
    margin-bottom: 18px;
    font-size: var(--font-size-body);
    line-height: var(--line-height-normal);
}

.bullet-list li::before {
    content: "•";
    position: absolute;
    left: 8px;
    color: var(--color-accent-primary);
    font-weight: bold;
}
```

### 3.2 编号列表

```css
.numbered-list {
    list-style: none;
    padding-left: 0;
    counter-reset: item;
}

.numbered-list li {
    position: relative;
    padding-left: 50px;
    margin-bottom: 18px;
    font-size: var(--font-size-body);
    line-height: var(--line-height-normal);
}

.numbered-list li::before {
    counter-increment: item;
    content: counter(item);
    position: absolute;
    left: 0;
    width: 36px;
    height: 36px;
    background: var(--color-accent-primary);
    color: white;
    text-align: center;
    line-height: 36px;
    font-weight: bold;
    border-radius: 0;
}
```

### 3.3 卡片列表

```css
.card-list {
    list-style: none;
    padding-left: 0;
}

.card-list li {
    background: var(--color-bg-secondary);
    border-left: 4px solid var(--color-primary);
    padding: var(--spacing-lg);
    margin-bottom: var(--spacing-md);
}

.card-list li:nth-child(2) {
    border-left-color: var(--color-accent-primary);
}

.card-list li:nth-child(3) {
    border-left-color: var(--color-success);
}

.card-list li:nth-child(4) {
    border-left-color: var(--color-info);
}
```

---

## 4 组件模板

### 4.1 封面页

```html
<div class="slide cover-slide active" id="slide-1" data-page-type="cover">
    <div class="cover-slide-background" style="background-color: [背景颜色];">
        <div class="cover-slide-content" style="color: [文字颜色];">
            <div class="cover-subtitle">副标题（如有）</div>
            <h1 class="cover-title">文档主标题</h1>
            <div class="cover-meta">
                <span class="cover-date">2024年12月</span>
                <span class="cover-author">作者名称</span>
            </div>
        </div>
    </div>
</div>

<style>
.cover-slide-background {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    display: flex;
    align-items: center;
    justify-content: center;
}

.cover-slide-content {
    text-align: center;
    max-width: 800px;
}

.cover-subtitle {
    font-size: var(--font-size-h4);
    opacity: 0.8;
    margin-bottom: var(--spacing-md);
}

.cover-title {
    font-size: var(--font-size-display);
    font-weight: var(--font-weight-bold);
    line-height: var(--line-height-tight);
    margin-bottom: var(--spacing-2xl);
}

.cover-meta {
    display: flex;
    justify-content: center;
    gap: var(--spacing-xl);
    font-size: var(--font-size-body-secondary);
    opacity: 0.8;
}
</style>
```

### 4.2 章节首页

```html
<div class="slide chapter-slide" id="slide-5" data-chapter="1">
    <div class="chapter-cover-background" style="background-color: [背景颜色];">
        <div class="chapter-cover-content" style="color: [文字颜色];">
            <div class="chapter-number">01</div>
            <h1 class="chapter-title">第一章 章节标题</h1>
            <p class="chapter-description">章节描述文字，概括本章核心内容。</p>
            
            <div class="chapter-overview">
                <h3 class="overview-title">本章内容</h3>
                <ul class="overview-list">
                    <li class="overview-item">
                        <span class="overview-page-num">06</span>
                        <span class="overview-title-text">子章节1.1 标题</span>
                    </li>
                    <li class="overview-item">
                        <span class="overview-page-num">08</span>
                        <span class="overview-title-text">子章节1.2 标题</span>
                    </li>
                    <li class="overview-item">
                        <span class="overview-page-num">10</span>
                        <span class="overview-title-text">子章节1.3 标题</span>
                    </li>
                </ul>
            </div>
        </div>
    </div>
</div>
```

### 4.3 内容页（带导航栏）

```html
<div class="slide" id="slide-6" data-page-type="content">
    <header class="slide-header">
        <h1 class="slide-title">子章节1.1 标题</h1>
    </header>
    
    <div class="content-area">
        <div class="two-column">
            <div class="column chart-column">
                <div class="chart-container">
                    <!-- 图表内容 -->
                </div>
            </div>
            <div class="column insight-column">
                <h3 class="insight-title">关键洞察</h3>
                <ul class="bullet-list">
                    <li>洞察点1：详细说明</li>
                    <li>洞察点2：详细说明</li>
                    <li>洞察点3：详细说明</li>
                </ul>
            </div>
        </div>
    </div>
</div>
```

### 4.4 结束页

```html
<div class="slide ending-slide" id="slide-last" data-page-type="ending">
    <div class="ending-slide-background" style="background-color: [背景颜色];">
        <div class="ending-slide-content" style="color: [文字颜色];">
            <h1 class="ending-title">谢谢</h1>
            <div class="ending-contact">
                <p>contact@example.com</p>
            </div>
            <div class="ending-qa">
                <p>Q&A</p>
            </div>
        </div>
    </div>
</div>
```

---

## 5 导航功能

### 5.1 导航按钮

```css
.nav-button {
    position: fixed;
    top: 50%;
    transform: translateY(-50%);
    width: 50px;
    height: 50px;
    background: rgba(255, 255, 255, 0.95);
    border: 1px solid var(--color-border);
    cursor: pointer;
    z-index: 200;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 24px;
    color: var(--color-text-secondary);
    transition: all 0.2s ease;
}

.nav-button:hover {
    background: var(--color-accent-primary);
    color: white;
    border-color: var(--color-accent-primary);
}

.nav-prev {
    left: 20px;
}

.nav-next {
    right: 20px;
}
```

### 5.2 页面计数器

```css
.slide-counter {
    position: fixed;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    background: rgba(255, 255, 255, 0.95);
    padding: 10px 20px;
    font-size: var(--font-size-body-secondary);
    color: var(--color-text-secondary);
    z-index: 200;
    box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
    border-radius: 20px;
}
```

### 5.3 全屏按钮

```css
.fullscreen-button {
    position: fixed;
    top: 20px;
    right: 20px;
    width: 40px;
    height: 40px;
    background: rgba(255, 255, 255, 0.95);
    border: 1px solid var(--color-border);
    cursor: pointer;
    z-index: 200;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 18px;
    color: var(--color-text-secondary);
    transition: all 0.2s ease;
}

.fullscreen-button:hover {
    background: var(--color-accent-primary);
    color: white;
    border-color: var(--color-accent-primary);
}
```

### 5.4 JavaScript导航逻辑

```javascript
// 导航功能
let currentSlide = 1;
const totalSlides = document.querySelectorAll('.slide').length;

function updateSlide(slideNumber) {
    // 隐藏所有幻灯片
    document.querySelectorAll('.slide').forEach(slide => {
        slide.classList.remove('active');
    });
    
    // 显示目标幻灯片
    const targetSlide = document.getElementById(`slide-${slideNumber}`);
    if (targetSlide) {
        targetSlide.classList.add('active');
    }
    
    // 更新导航栏标题
    const slideTitle = targetSlide.querySelector('.slide-title, .content-page-title');
    if (slideTitle) {
        document.querySelector('.slide-header .slide-title').textContent = slideTitle.textContent;
    }
    
    // 更新计数器
    document.querySelector('.slide-counter').textContent = `${slideNumber} / ${totalSlides}`;
    
    // 更新按钮状态
    document.querySelector('.nav-prev').disabled = slideNumber === 1;
    document.querySelector('.nav-next').disabled = slideNumber === totalSlides;
    
    // 更新当前幻灯片索引
    currentSlide = slideNumber;
}

// 上一页
document.querySelector('.nav-prev').addEventListener('click', () => {
    if (currentSlide > 1) {
        updateSlide(currentSlide - 1);
    }
});

// 下一页
document.querySelector('.nav-next').addEventListener('click', () => {
    if (currentSlide < totalSlides) {
        updateSlide(currentSlide + 1);
    }
});

// 键盘导航
document.addEventListener('keydown', (e) => {
    if (e.key === 'ArrowLeft' && currentSlide > 1) {
        updateSlide(currentSlide - 1);
    } else if (e.key === 'ArrowRight' && currentSlide < totalSlides) {
        updateSlide(currentSlide + 1);
    }
});

// 全屏功能
document.querySelector('.fullscreen-button').addEventListener('click', () => {
    if (document.fullscreenElement) {
        document.exitFullscreen();
    } else {
        document.documentElement.requestFullscreen();
    }
});

// 初始化
updateSlide(1);
```

---

## 6 禁止使用的样式

### 6.1 AI生成色板

```css
/* ⛔ 禁止使用 */
.prohibited-gradient-1 {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.prohibited-gradient-2 {
    background: linear-gradient(135deg, #5c258d 0%, #4389a2 100%);
}

.prohibited-gradient-3 {
    background: linear-gradient(135deg, #11998e 0%, #38ef7d 100%);
}

.prohibited-gradient-4 {
    background: linear-gradient(135deg, #f85d42 0%, #ff9966 100%);
}
```

### 6.2 过度装饰样式

```css
/* ⛔ 禁止使用过度装饰的样式 */
.over-decorated {
    box-shadow: 0 10px 40px rgba(102, 126, 234, 0.4);
    border-radius: 20px;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
}

.excessive-glow {
    box-shadow: 0 0 30px rgba(102, 126, 234, 0.6);
    text-shadow: 0 0 10px rgba(102, 126, 234, 0.8);
}
```

---

## 7 使用说明

### 7.1 创建新页面

1. 在`.presentation-container`内添加新的`<div class="slide">`元素
2. 设置唯一的`id`（如`slide-6`）
3. 设置`data-page-type`属性（cover/toc/chapter/content/ending）
4. 添加页面内容

### 7.2 修改背景颜色

1. 在beauty-html-reference.md定义的配色方案中选择颜色
2. 计算与文字颜色的对比度（≥4.5:1）
3. 应用到页面的背景色属性

### 7.3 添加图表

1. 确定图表类型（柱状图/折线图/饼图等）
2. 选择两列或三列布局
3. 在左侧列添加图表容器
4. 在右侧列添加洞察要点

---

## 8 图表解释说明组件规范 [NEW]

本章节定义图表页的解释说明组件规范，确保每个图表都有完整的文字解读和洞察分析。

### 8.1 图表+洞察布局规范

**图表页必须使用两列布局**，左侧为图表，右侧为洞察面板：

```css
.chart-insight-layout {
    display: grid;
    grid-template-columns: 55% 45%;
    gap: var(--spacing-xl, 32px);
    margin-top: var(--spacing-xl, 32px);
}

.chart-container {
    background: var(--color-bg-secondary, #F5F7FA);
    padding: var(--spacing-lg, 24px);
    border-radius: var(--radius-lg, 8px);
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 400px;
}

.insight-panel {
    padding: var(--spacing-xl, 32px);
    background: var(--color-bg-secondary, #F5F7FA);
    border-radius: var(--radius-lg, 8px);
    height: 100%;
    overflow-y: auto;
}

@media (max-width: 992px) {
    .chart-insight-layout {
        grid-template-columns: 1fr;
    }
    
    .chart-container {
        min-height: 300px;
    }
}
```

### 8.2 洞察面板组件结构

**每个图表页必须包含以下四个部分**：

```html
<div class="insight-panel">
    <!-- 图表概述 -->
    <div class="insight-section chart-overview">
        <h4>图表概述</h4>
        <p>[图表主题、数据范围、时间跨度等基本信息]</p>
    </div>
    
    <!-- 数据解读 -->
    <div class="insight-section data-interpretation">
        <h4>数据解读</h4>
        <p>[每个数据点的具体数值和含义说明]</p>
    </div>
    
    <!-- 洞察分析 -->
    <div class="insight-section insight-analysis">
        <h4>洞察分析</h4>
        <p>[从数据中提炼的关键洞察]</p>
    </div>
    
    <!-- 行动建议 -->
    <div class="insight-section action-recommendations">
        <h4>行动建议</h4>
        <p>[基于洞察提出的具体建议]</p>
    </div>
</div>
```

### 8.3 洞察面板CSS样式

```css
.insight-section {
    margin-bottom: var(--spacing-xl, 32px);
}

.insight-section:last-child {
    margin-bottom: 0;
}

.insight-section h4 {
    font-size: var(--font-size-h5, 16px);
    font-weight: var(--font-weight-semibold, 600);
    color: var(--color-accent-primary, #F85d42);
    margin-bottom: var(--spacing-md, 16px);
    padding-bottom: var(--spacing-sm, 8px);
    border-bottom: 2px solid rgba(248, 93, 66, 0.2);
}

.insight-section p {
    font-size: var(--font-size-body, 14px);
    line-height: var(--line-height-normal, 1.6);
    color: var(--color-text-primary, #1A202C);
}

.insight-section ul {
    margin-top: var(--spacing-sm, 8px);
    padding-left: var(--spacing-lg, 24px);
}

.insight-section li {
    font-size: var(--font-size-body, 14px);
    line-height: var(--line-height-normal, 1.6);
    color: var(--color-text-primary, #1A202C);
    margin-bottom: var(--spacing-xs, 4px);
}

/* 行动建议特殊样式 */
.insight-section .action-recommendations {
    background: rgba(52, 195, 143, 0.1);
    padding: var(--spacing-md, 16px);
    border-radius: var(--radius-md, 4px);
    border-left: 3px solid var(--color-green, #34c38f);
}

.insight-section .action-recommendations h4 {
    color: var(--color-green, #34c38f);
    border-bottom-color: rgba(52, 195, 143, 0.3);
}
```

### 8.4 内容页描述组件规范

**每个内容页必须包含页面导语和要点详细展开**：

```css
/* 页面导语样式 */
.page-intro {
    background: var(--color-bg-secondary, #F5F7FA);
    padding: var(--spacing-lg, 24px);
    border-left: 4px solid var(--color-accent-primary, #F85d42);
    margin-bottom: var(--spacing-xl, 32px);
    border-radius: 0 var(--radius-md, 4px) var(--radius-md, 4px) 0;
}

.page-intro p {
    font-size: var(--font-size-body, 14px);
    line-height: var(--line-height-relaxed, 1.6);
    color: var(--color-text-primary, #1A202C);
    margin: 0;
}

/* 要点详细展开样式 */
.content-point {
    margin-bottom: var(--spacing-xl, 32px);
    padding-bottom: var(--spacing-lg, 24px);
    border-bottom: 1px solid var(--color-border, #E2E8F0);
}

.content-point:last-child {
    border-bottom: none;
    margin-bottom: 0;
}

.point-title {
    font-size: var(--font-size-h4, 24px);
    font-weight: var(--font-weight-semibold, 600);
    color: var(--color-blue, #556EE6);
    margin-bottom: var(--spacing-md, 16px);
}

.point-content {
    background: var(--color-bg, #FFFFFF);
    padding: var(--spacing-lg, 24px);
    border-radius: var(--radius-md, 4px);
    border: 1px solid var(--color-border, #E2E8F0);
}

.point-content strong {
    color: var(--color-accent-primary, #F85d42);
    font-weight: var(--font-weight-semibold, 600);
}

/* 数据支撑特殊样式 */
.point-content .data-support {
    background: rgba(85, 110, 230, 0.08);
    padding: var(--spacing-sm, 8px) var(--spacing-md, 16px);
    border-radius: var(--radius-sm, 4px);
    border-left: 3px solid var(--color-blue, #556EE6);
    margin-top: var(--spacing-md, 16px);
}

/* 结论特殊样式 */
.point-content .conclusion {
    background: rgba(248, 93, 66, 0.08);
    padding: var(--spacing-sm, 8px) var(--spacing-md, 16px);
    border-radius: var(--radius-sm, 4px);
    border-left: 3px solid var(--color-accent-primary, #F85d42);
    margin-top: var(--spacing-md, 16px);
}
```

### 8.5 关联说明组件规范

```css
.content-connections {
    background: var(--color-bg-secondary, #F5F7FA);
    padding: var(--spacing-lg, 24px);
    border-radius: var(--radius-md, 4px);
    margin-top: var(--spacing-xl, 32px);
    border: 1px dashed var(--color-gray, #74788d);
}

.content-connections h4 {
    font-size: var(--font-size-h5, 16px);
    font-weight: var(--font-weight-semibold, 600);
    color: var(--color-gray, #74788d);
    margin-bottom: var(--spacing-md, 16px);
}

.content-connections p {
    font-size: var(--font-size-body, 14px);
    line-height: var(--line-height-relaxed, 1.6);
    color: var(--color-text-primary, #1A202C);
}
```

### 8.6 内容页HTML结构模板

```html
<!-- 内容页 -->
<div class="slide" id="slide-N" data-title="[页面标题]">
    <div class="slide-header">
        <span class="slide-title">[页面标题]</span>
    </div>
    
    <div class="slide-content">
        <h2 class="page-title">[页面标题]</h2>
        
        <!-- 页面导语 -->
        <div class="page-intro">
            <p>[用1-2段话概括本页面核心观点，说明这些内容的重要性和意义]</p>
        </div>
        
        <!-- 详细内容 -->
        <div class="content-body">
            <!-- 要点1 -->
            <div class="content-point">
                <h3 class="point-title">[要点标题]</h3>
                <div class="point-content">
                    <p><strong>背景描述：</strong>[相关背景信息]</p>
                    <p><strong>具体内容：</strong>[该要点的完整描述]</p>
                    <p class="data-support"><strong>数据支撑：</strong>[相关数据]</p>
                    <p><strong>影响分析：</strong>[该要点对整体的影响]</p>
                    <p class="conclusion"><strong>结论说明：</strong>[基于该要点的结论]</p>
                </div>
            </div>
            
            <!-- 要点2... -->
        </div>
        
        <!-- 关联说明 -->
        <div class="content-connections">
            <h4>要点关联说明</h4>
            <p>[多个要点之间的逻辑关系说明]</p>
        </div>
    </div>
</div>
```

### 8.7 图表页HTML结构模板

```html
<!-- 图表页 -->
<div class="slide" id="slide-N" data-title="[页面标题]">
    <div class="slide-header">
        <span class="slide-title">[页面标题]</span>
    </div>
    
    <div class="slide-content">
        <h2 class="page-title">[页面标题]</h2>
        
        <!-- 图表+洞察布局 -->
        <div class="chart-insight-layout">
            <!-- 图表容器 -->
            <div class="chart-container">
                <!-- 图表HTML（柱状图/折线图/饼图等） -->
                <canvas id="chart-[N]"></canvas>
            </div>
            
            <!-- 洞察面板 -->
            <div class="insight-panel">
                <div class="insight-section chart-overview">
                    <h4>图表概述</h4>
                    <p>[说明图表展示的主题和数据范围，概括图表的核心发现]</p>
                </div>
                
                <div class="insight-section data-interpretation">
                    <h4>数据解读</h4>
                    <p><strong>[数据系列1名称]：</strong>[数据值] - [解读]</p>
                    <p><strong>[数据系列2名称]：</strong>[数据值] - [解读]</p>
                </div>
                
                <div class="insight-section insight-analysis">
                    <h4>洞察分析</h4>
                    <p><strong>洞察1：</strong>[基于数据的分析结论]</p>
                    <p><strong>洞察2：</strong>[另一个关键发现]</p>
                </div>
                
                <div class="insight-section action-recommendations">
                    <h4>行动建议</h4>
                    <ul>
                        <li>[基于洞察提出的具体建议]</li>
                        <li>[另一项行动建议]</li>
                    </ul>
                </div>
            </div>
        </div>
    </div>
</div>
```

### 8.8 禁止行为清单

**❌ 绝对禁止**：

- ❌ 图表页没有洞察面板或解释说明
- ❌ 洞察面板只有简单的一两句话
- ❌ 省略图表中的关键数据解读
- ❌ 只保留图表，没有文字说明
- ❌ 内容页只有要点列表，没有详细展开
- ❌ 只列出要点标题，没有完整描述
- ❌ 删除数据单位（如"$"、"亿"、"%"）
- ❌ 简化专业术语的解释

**✅ 正确做法**：

- ✅ 每个图表必须配合完整的洞察面板
- ✅ 洞察面板必须包含：图表概述、数据解读、洞察分析
- ✅ 每个内容页必须有页面导语
- ✅ 每个要点必须包含：背景描述、具体内容、数据支撑、影响分析、结论
- ✅ 所有数据点（数字、百分比、金额）必须完整保留
- ✅ 专业术语必须有必要的解释说明
