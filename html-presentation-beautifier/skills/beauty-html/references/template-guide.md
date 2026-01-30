# Template Usage Guide

**Purpose**: Comprehensive guide for using the 4 pre-built McKinsey-style slide templates with strict quality enforcement.

**⚠️ CRITICAL: HTML Generation Quality Standards**

This guide enforces the **4-Stage Generation Process** from beauty.md Step 3 with mandatory quality checks:

---

## ⚠️ MANDATORY RULES - MUST FOLLOW

### Stage-Based Generation (分阶段生成 - 强制执行)

**✅ Stage 1: HTML Framework + Complete CSS**
- Generate DOCTYPE, head, meta, Chart.js CDN
- Generate **COMPLETE CSS** (600-800 lines) in one pass
- Generate body tag, navigation structure
- **MUST include**:
  - `.slide-header` and `.slide-header-title` styles for content page headers
  - McKinsey color palette CSS variables
  - Two-column and three-column layout styles
  - Chart container styles (min-height: 400px)
  - Responsive design breakpoints
- ❌ **NEVER split CSS across stages**

**✅ Stage 2: Generate Slides by Chapter**
- Generate cover slide (P1)
- Generate table of contents slides (P2)
- Generate chapter cover slides (P3) for each H2 section
- Generate content slides (P4) for each subsection
  - **MUST use fixed header navigation bar for content page titles**
  - **MUST NOT exceed 8 bullet points per page**
  - **MUST use numbered titles (一、二、三...) for multi-page content**
  - **MUST use two-column layout for charts (chart + insights)**
  - **MUST use three-column layout for multiple chart comparisons**
- Generate closing slide (P5)
- **Prompt user "继续" after each chapter completion**

**✅ Stage 3: Generate JavaScript + Closing Tags**
- Generate all Chart.js configuration code
- Generate closing </body> and </html> tags
- **NEVER simplify or omit chart configurations**

**⚠️ Token Limit Handling**:
```
IF current stage output > token limit:
    ├─ Complete current stage as much as possible
    ├─ Prompt: "当前阶段内容较长，已生成部分内容，请输入'继续'以获取剩余部分"
    ├─ Wait for user: "继续"
    └─ Continue with remaining content of current stage
    
CRITICAL RULES:
    ❌ NEVER skip stages or combine stages to save tokens
    ❌ NEVER simplify content to fit within token limit
    ❌ NEVER omit CSS, HTML, or JavaScript code
    ✅ ALWAYS use "continue" mechanism to preserve 100% quality
```

---

## Template Overview

| Template | File | Slide Position | When to Use |
|----------|------|----------------|-------------|
| Cover | `cover-slide-template.html` | #1 (always) | First slide of any presentation |
| TOC | `toc-slide-template.html` | #2 (optional) | Presentations with 10+ slides |
| Content | `content-slide-template.html` | #3 to #N-1 | All middle slides |
| End | `end-slide-template.html` | #N (always) | Final slide |

**⚠️ Content Page Template Requirements**:
- **Title Display**: Fixed header navigation bar at top left (NOT in content area)
- **Content Limit**: Maximum 8 bullet points per page
- **Chart Layout**: Two-column (chart + insights) or three-column (multiple charts)
- **Multi-Page**: Use numbered titles (一、二、三...) when splitting content

---

## 1. Cover Slide Template

**Location**: `templates/cover-slide-template.html`

**Purpose**: First slide with title and metadata

**Structure**:
```html
<div class="slide title-slide active" data-slide="1">
    <h1 class="main-title">{presentation_title}</h1>
    <div class="decorative-line"></div>
    <p class="subtitle">{subtitle}</p>
    <div class="meta-info">
        <div class="meta-item">
            <div class="meta-label">汇报人</div>
            <div class="meta-value">{presenter_name}</div>
        </div>
        <div class="meta-item">
            <div class="meta-label">日期</div>
            <div class="meta-value">{date}</div>
        </div>
    </div>
</div>
```

**Customization Points**:
- `.main-title`: Main presentation title (64px, white, bold)
- `.subtitle`: Subtitle or tagline (36px, white)
- `.meta-item`: Add/remove metadata fields as needed

**Design Features**:
- Gradient background (deep blue to orange)
- Fade-in animations
- Centered layout

## 2. Table of Contents Template

**Location**: `templates/toc-slide-template.html`

**Purpose**: Navigation slide showing presentation structure

**When to Use**: Only for presentations with 10+ slides

**Structure**:
```html
<div class="slide toc-slide" data-slide="2">
    <div class="toc-header">
        <h1 class="toc-title">目录</h1>
        <p class="toc-subtitle">Table of Contents</p>
    </div>
    <div class="toc-container">
        <a href="#section1" class="toc-section" onclick="jumpToSlide(3); return false;">
            <div class="toc-number">1</div>
            <div class="toc-section-title">{section_title}</div>
            <div class="toc-section-subtitle">{section_description}</div>
        </a>
        <!-- Repeat for each section -->
    </div>
    <div class="toc-footer">
        <div class="toc-meta">
            <span>📊 共 {total_slides} 页</span>
            <span>⏱️ 预计 {estimated_time} 分钟</span>
        </div>
    </div>
</div>
```

**Customization Points**:
- `.toc-section`: One block per major section
- `onclick="jumpToSlide(X)"`: Set jump target slide number
- `.toc-meta`: Update total slides and time estimaDesign Features**:
- Two-column grid layout
- Clickable sections with hover effects
- Quick navigation

## 3. Content Slide Template

**Location**: `templates/content-slide-template.html`

**Purpose**: Universal template for all content slides

**⚠️ CRITICAL LAYOUT RULES**:
- **Title Location**: MUST use fixed header navigation bar (`.slide-header`) for content page titles
- **Content Limit**: Maximum 8 bullet points per page - strictly enforced
- **Chart Layout**: MUST use two-column (chart + insights) or three-column (multiple charts)
- **Multi-Page Splitting**: Use numbered titles (一、二、三...) when content > 8 points

**Available Components**:

### Header Components (MANDATORY for Content Pages)
- `.slide-header`: Fixed navigation bar at top (80px height)
  - `.slide-header-title`: Page title display in header (32px)
- **NOTE**: Content pages do NOT use `.slide-title` in content area

### Text Components
- `.section-heading`: Section heading (24px)
- `.text-content`: Body text (16-20px)
- `.key-point`: Emphasized point (20px bold)

### List Components
- `.bullet-list`: Unordered list with McKinsey bullets (MAX 8 items)
- `.numbered-list`: Ordered list with numbering (MAX 8 items)

### Layout Components (MANDATORY for Charts)
- `.two-column`: Two-column grid layout
  - `.column`: Column child (50% width each)
  - **USE FOR**: Chart + Insights layout
- `.three-column`: Three-column grid layout
  - `.column`: Column child (33% width each)
  - **USE FOR**: Multiple chart comparisons
- `.full-width`: Full-width container (for non-chart content only)

### Chart Components (MANDATORY Two/Three-Column Layout)
- `.chart-container`: Container for Chart.js charts (min-height: 400px)
  - `<canvas id="chartX">`: Canvas element for chart
  - **MUST be placed in `.column` within `.two-column` or `.three-column`**
- `.chart-caption`: Chart source/description

### Emphasis Components
- `.emphasis-container`: Grid of emphasis boxes
- `.emphasis-box`: Individual emphasis box
- `.conclusions-grid`: Grid for conclusions
- `.conclusion-card`: Individual conclusion card
- `.info-box`: Information box with icon
- `.highlight-box`: Highlighted content box

### Flow Components
- `.flow-container`: Container for flow diagrams
- `.flow-step`: Individual flow step
- `.flow-number`: Step number circle
- `.flow-title`: Step title
- `.flow-description`: Step description

### Table Components
- `.data-table`: Professional data table
  - `<thead>`: Table header
  - `<tbody>`: Table body

---

## Example Layouts (Updated for New Requirements)

### ✅ CORRECT: Content Page with Fixed Header + Two-Column Chart Layout

```html
<div class="slide content-slide" data-slide="3">
    <!-- Fixed Header Navigation Bar (Title Display) -->
    <div class="slide-header">
        <h2 class="slide-header-title">一、Market Growth Analysis</h2>
    </div>
    
    <!-- Main Content Area -->
    <div class="slide-content">
        <div class="two-column">
            <!-- Left Column: Chart (50-60%) -->
            <div class="column">
                <div class="chart-container">
                    <canvas id="chart3"></canvas>
                </div>
                <p class="chart-caption">Data Source: Market Research 2024</p>
            </div>
            
            <!-- Right Column: Insights (40-50%) -->
            <div class="column">
                <h3 class="section-heading">Key Insights</h3>
                <ul class="bullet-list">
                    <li><strong>30% Growth</strong>: Market expanding rapidly</li>
                    <li><strong>Q2 Peak</strong>: Highest demand in Q2</li>
                    <li><strong>Trend</strong>: Consistent upward trajectory</li>
                    <li><strong>Forecast</strong>: Expected to reach $500M by 2025</li>
                </ul>
            </div>
        </div>
    </div>
</div>
```

### ✅ CORRECT: Content Page with Three-Column Chart Comparison

```html
<div class="slide content-slide" data-slide="4">
    <div class="slide-header">
        <h2 class="slide-header-title">二、Regional Performance Comparison</h2>
    </div>
    
    <div class="slide-content">
        <div class="three-column">
            <!-- Column 1: Asia -->
            <div class="column">
                <div class="chart-container">
                    <canvas id="asiaChart"></canvas>
                </div>
                <p class="chart-caption">Asia Pacific: +35%</p>
            </div>
            
            <!-- Column 2: Europe -->
            <div class="column">
                <div class="chart-container">
                    <canvas id="europeChart"></canvas>
                </div>
                <p class="chart-caption">Europe: +22%</p>
            </div>
            
            <!-- Column 3: Americas -->
            <div class="column">
                <div class="chart-container">
                    <canvas id="americasChart"></canvas>
                </div>
                <p class="chart-caption">Americas: +18%</p>
            </div>
        </div>
    </div>
</div>
```

### ✅ CORRECT: Content Page with Text Only (Single Column, ≤8 Points)

```html
<div class="slide content-slide" data-slide="5">
    <div class="slide-header">
        <h2 class="slide-header-title">Strategic Priorities</h2>
    </div>
    
    <div class="slide-content">
        <ul class="bullet-list">
            <li><strong>Priority 1</strong>: Expand market share in Asia Pacific</li>
            <li><strong>Priority 2</strong>: Develop new product lines</li>
            <li><strong>Priority 3</strong>: Strengthen digital capabilities</li>
            <li><strong>Priority 4</strong>: Optimize supply chain efficiency</li>
            <li><strong>Priority 5</strong>: Invest in talent development</li>
            <li><strong>Priority 6</strong>: Enhance customer experience</li>
        </ul>
    </div>
</div>
```

### ❌ WRONG: Title in Content Area (Old Pattern - DO NOT USE)

```html
<!-- ❌ INCORRECT - Title should NOT be in content area for content pages -->
<div class="slide" data-slide="3">
    <h1 class="slide-title">Market Growth Analysis</h1>
    <div class="two-column">
        <div class="column">
            <p class="text-content">{text}</p>
        </div>
        <div class="column">
            <div class="chart-container">
                <canvas id="chart3"></canvas>
            </div>
        </div>
    </div>
</div>
```

### ❌ WRONG: Single-Column Chart Layout (Old Pattern - DO NOT USE)

```html
<!-- ❌ INCORRECT - Charts must use two-column or three-column layout -->
<div class="slide content-slide" data-slide="4">
    <div class="slide-header">
        <h2 class="slide-header-title">Market Data</h2>
    </div>
    <div class="slide-content">
        <div class="chart-container">
            <canvas id="chart4"></canvas>
        </div>
    </div>
</div>
```

### ❌ WRONG: More Than 8 Bullet Points (DO NOT USE)

```html
<!-- ❌ INCORRECT - Exceeds 8 bullet points limit -->
<div class="slide content-slide" data-slide="5">
    <div class="slide-header">
        <h2 class="slide-header-title">Market Trends</h2>
    </div>
    <div class="slide-content">
        <ul class="bullet-list">
            <li>Point 1</li>
            <li>Point 2</li>
            <li>Point 3</li>
            <li>Point 4</li>
            <li>Point 5</li>
            <li>Point 6</li>
            <li>Point 7</li>
            <li>Point 8</li>
            <li>Point 9</li> <!-- ❌ Exceeds limit -->
            <li>Point 10</li> <!-- ❌ Exceeds limit -->
        </ul>
    </div>
</div>

<!-- ✅ CORRECT - Split into two pages with numbered titles -->
<div class="slide content-slide" data-slide="5">
    <div class="slide-header">
        <h2 class="slide-header-title">一、Market Trends</h2>
    </div>
    <div class="slide-content">
        <ul class="bullet-list">
            <li>Point 1</li>
            <li>Point 2</li>
            <li>Point 3</li>
            <li>Point 4</li>
            <li>Point 5</li>
            <li>Point 6</li>
            <li>Point 7</li>
            <li>Point 8</li>
        </ul>
    </div>
</div>

<div class="slide content-slide" data-slide="6">
    <div class="slide-header">
        <h2 class="slide-header-title">二、Market Trends</h2>
    </div>
    <div class="slide-content">
        <ul class="bullet-list">
            <li>Point 9</li>
            <li>Point 10</li>
        </ul>
    </div>
</div>
```

---

**Flow diagram**:
```html
<div class="slide content-slide" data-slide="7">
    <div class="slide-header">
        <h2 class="slide-header-title">Implementation Process</h2>
    </div>
    <div class="slide-content">
        <div class="flow-container">
            <div class="flow-step">
                <div class="flow-number">1</div>
                <div class="flow-content">
                    <div class="flow-title">{step_title}</div>
                    <div class="flow-description">{step_description}</div>
                </div>
            </div>
            <!-- Repeat for each step -->
        </div>
    </div>
</div>
```
</div>
```

**Emphasis boxes**:
```html
<div class="slide" data-slide="5">
    <h1 class="slide-title">{title}</h1>
    <div class="emphasis-container">
        <div class="emphasis-box">
            <div class="emphasis-number">1</div>
            <div class="emphasis-title">{point_title}</div>
            <div class="emphasis-content">{point_content}</div>
        </div>
        <!-- Repeat for each point -->
    </div>
</div>
```

## 4. End Slide Template

**Location**: `templates/end-slide-template.html`

**Purpose**: Final thank you/closing slide

**Structure**:
```html
<div class="slide end-slide" data-slide="{total_slides}">
    <div class="decorative-icon">🎉</div>
    <h1 class="thank-you">感谢聆听！</h1>
    <p class="main-message">感谢您的时间和关注</p>

    <div class="contact-info">
        <div class="contact-title">联系方式</div>
        <div class="contact-details">
            📧 Email: {email}<br>
            📱 电话: {phone}
        </div>
    </div>

    <div class="company-info">
        <div class="company-logo">LOGO</div>
        <div class="company-name">{company_name}</div>
    </div>
</div>
```

**Customization Points**:
- `.thank-you`: Thank you message (可改为"谢谢"、"Q&A"等)
- `.contact-details`: Contact information
- `.company-name`: Company name
- `.company-logo`: Logo or company identifier

**Design Features**:
- Gradient background (orange to deep blue)
- Large thank you text (72px)
- Glass-effect contact card
- Fade-in animations

## Template Assembly Workflow

**Step 1**: Copy cover slide structure → Slide #1
**Step 2**: Copy TOC slide structure → Slide #2 (if 10+ slides)
**Step 3**: Copy content slide structure → Slides #3 to #N-1
**Step 4**: Copy end slide structure → Final slide

**Step 5**: Combine into single HTML file:
```html
<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <title>{presentation_title}</title>
    <style>
        /* Copy CSS from any template (all have same McKinsey CSS) */
    </style>
</head>
<body>
    <nav class="navbar">...</nav>
    <div class="presentation-container">
        <!-- All slides here -->
    </div>
    <button class="fullscreen-btn">全屏 ⛶</button>
    <script>
        // Copy JavaScript from any template
        // Initialize charts
    </script>
    <script src="https://cdn.jsdelivr.net/npm/chart.js"></script>
</body>
</html>
```

## Chart.js Integration

**For each chart in content slides**:

```javascript
new Chart(document.getElementById('chart{slide_number}'), {
    type: '{chart_type}',  // bar, line, pie, doughnut, radar, polarArea, bubble, scatter
    data: {
        labels: {data_labels},
        datasets: [{
            label: '{series_label}',
            data: {data_values},
            backgroundColor: ['#F85d42', '#556EE6', '#34c38f', '#50a5f1', '#f1b44c']
        }]
    },
    options: {
        responsive: true,
        maintainAspectRatio: false,
        plugins: {
            legend: { position: 'top' },
            title: {
                display: true,
                text: '{chart_title}',
                font: { size: 18, weight: 'bold' }
            }
        }
    }
});
```

## Template Quality Guarantees

All templates ensure:
- ✅ Exact McKinsey color codes
- ✅ Precise font sizes
- ✅ Standardized layouts
- ✅ Responsive design (1200px, 768px breakpoints)
- ✅ Interactive features (navigation, keyboard shortcuts, fullscreen)
- ✅ Chart.js integration with McKinsey colors
- ✅ Professional animations
