# Best Practices

This guide provides best practices for creating professional McKinsey-style HTML presentations.

## Content Principles

### 1. Content Preservation

**DO**:
- Preserve all original text exactly as written
- Maintain all numerical data points
- Keep all conclusions and recommendations word-for-word
- Respect original document structure and hierarchy

**DON'T**:
- Summarize or paraphrase content
- Add fabricated data or insights
- Modify conclusions or recommendations
- Interpret or add meaning to original text

### 2. Information Hierarchy

**DO**:
- Start with executive summary (top 3-5 points)
- Group related content together
- Use consistent ordering (importance, chronology, or logical flow)
- Maintain visual hierarchy (title → subtitle → body)

**DON'T**:
- Bury key insights in detail slides
- Mix unrelated topics on same slide
- Use random or inconsistent ordering
- Flattened hierarchy (everything same size)

### 3. Data Visualization

**DO**:
- Choose chart type based on data nature:
  - Bar chart: Category comparisons
  - Line chart: Trends over time
  - Pie chart: Percentage breakdowns
  - Table: Detailed multi-metric data
- Use consistent color palette
- Keep charts simple and readable
- Add clear labels and captions

**DON'T**:
- Use wrong chart type for data
- Clutter charts with too many data points
- Use colors outside the defined palette
- Remove labels or make them hard to read
- Create unnecessary or decorative charts

## Design Principles

### 1. Color Usage

**DO**:
- Strict adherence to McKinsey palette:
  - Primary background: #FFFFFF
  - Header: #000000
  - Accent: #F85d42
  - Secondary: #74788d
  - Charts: #556EE6, #34c38f, #50a5f1, #f1b44c
- Use accent color sparingly for emphasis
- Maintain color consistency across all slides
- Ensure high contrast for readability

**DON'T**:
- Add custom colors or variations
- Use purple gradients or AI-generated palettes
- Apply colors randomly
- Use low contrast combinations
- Overuse accent color (loses impact)

### 2. Typography

**DO**:
- Use defined font sizes:
  - Title: 64px (bold, black)
  - Subtitle: 36px (bold, accent color)
  - Section header: 28px (bold, black)
  - Body text: 18px (regular, dark gray)
  - Chart labels: 14px (clear, readable)
- Maintain consistent font family (system fonts)
- Use bold for emphasis, not styling
- Ensure line height 1.6-1.8 for readability

**DON'T**:
- Use inconsistent font sizes
- Mix multiple font families
- Use italic or decorative fonts
- Use underlining for emphasis
- Set line height too tight (<1.4) or loose (>2.0)

### 3. Layout & Spacing

**DO**:
- Use generous white space (40-60px margins)
- Maintain consistent spacing:
  - Between elements: 20-30px
  - Between sections: 40-60px
  - Within cards: 20-30px
- Align all elements to grid
- Balance visual weight across slide

**DON'T**:
- Crowd elements together
- Use inconsistent spacing
- Create unaligned layouts
- Leave large empty areas without purpose
- Create visually unbalanced slides

### 4. Visual Elements

**DO**:
- Use subtle shadows for depth (0-2px, 0-4px)
- Add minimal borders for separation
- Use colored borders for emphasis (4px accent color)
- Keep chart design clean and minimal
- Ensure all elements serve purpose

**DON'T**:
- Use heavy or multiple shadows
- Add unnecessary borders
- Use decorative elements without purpose
- Create complex or cluttered charts
- Add clipart, icons, or decorative graphics

## Slide Design Patterns

### Title Slide

**Purpose**: Introduce presentation with maximum impact

**Pattern**:
```html
<div class="title-slide">
  <h1 class="title">Main Title</h1>
  <h2 class="subtitle">Context or Subtitle</h2>
  <p class="date">Date</p>
</div>
```

**Best Practices**:
- Keep text minimal and bold
- Use large, impactful title (64px)
- Add context through subtitle
- Center align for focus
- No charts or data

### Executive Summary

**Purpose**: Present top 3-5 conclusions or key takeaways

**Pattern**:
```html
<div class="header-bar">
  <h1 class="slide-title">Executive Summary</h1>
</div>
<div class="slide-content">
  <ul class="key-points">
    <li class="key-point">✓ Conclusion 1</li>
    <li class="key-point">✓ Conclusion 2</li>
    <li class="key-point">✓ Conclusion 3</li>
  </ul>
</div>
```

**Best Practices**:
- Limit to 3-5 key points
- Most important first
- Use checkmarks for visual cue
- Bold key metrics or numbers
- Clear, concise statements

### Data Slide (Chart + Insights)

**Purpose**: Present quantitative data with analysis

**⚠️ CRITICAL RULE**: Charts MUST use two-column or three-column layout, NEVER single column

**⚠️ Content Page Layout Rules**:
- **Slide Header**: Title must be displayed in the fixed header navigation bar at the top left
- **Slide Content**: Main content area starts below the header (with padding-top to avoid overlap)
- **Content Limit**: Maximum 8 bullet points per page; if more, split into multiple pages with numbered titles (一、二、三...)

**Pattern 1: Two-Column Layout (Chart + Insights)**:
```html
<!-- Content Page with Header Navigation -->
<div class="slide content-slide">
  <!-- Fixed Header Navigation Bar (Title Display) -->
  <div class="slide-header">
    <h2 class="slide-header-title">一、Market Analysis</h2>
  </div>

  <!-- Main Content Area (NO Title Here) -->
  <div class="slide-content">
    <div class="two-column">
      <div class="column">
        <div class="chart-container">
          <canvas id="chart1"></canvas>
        </div>
        <p class="chart-caption">Chart Description</p>
      </div>
      <div class="column">
        <h3 class="section-heading">Key Insights</h3>
        <ul class="bullet-list">
          <li>Insight 1</li>
          <li>Insight 2</li>
          <li>Insight 3</li>
          <li>Insight 4</li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

**Pattern 2: Two-Column Layout (Chart + Data Summary)**:
```html
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">二、Data Overview</h2>
  </div>

  <div class="slide-content">
    <div class="two-column">
      <div class="column">
        <div class="chart-container">
          <canvas id="chart1"></canvas>
        </div>
        <p class="chart-caption">Data Source: XXX</p>
      </div>
      <div class="column">
        <div class="emphasis-container">
          <div class="emphasis-box">
            <div class="emphasis-title">Key Metric 1</div>
            <div class="emphasis-text">Value and description</div>
          </div>
          <div class="emphasis-box">
            <div class="emphasis-title">Key Metric 2</div>
            <div class="emphasis-text">Value and description</div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
```
        <div class="emphasis-text">Value and description</div>
      </div>
      <div class="emphasis-box">
        <div class="emphasis-title">Key Metric 2</div>
        <div class="emphasis-text">Value and description</div>
      </div>
    </div>
  </div>
</div>
```

**Pattern 3: Three-Column Layout (Multiple Charts Comparison)**:
```html
<div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 30px; margin: 20px 0;">
  <div class="column">
    <div class="chart-container" style="height: 350px;">
      <canvas id="chart1"></canvas>
    </div>
    <p class="chart-caption">Chart 1 Title</p>
  </div>
  <div class="column">
    <div class="chart-container" style="height: 350px;">
      <canvas id="chart2"></canvas>
    </div>
    <p class="chart-caption">Chart 2 Title</p>
  </div>
  <div class="column">
    <div class="chart-container" style="height: 350px;">
      <canvas id="chart3"></canvas>
    </div>
    <p class="chart-caption">Chart 3 Title</p>
  </div>
</div>
```

**Best Practices**:
- ✅ ALWAYS use two-column or three-column layout for charts
- ✅ Chart on left (50-60%), insights on right (40-50%)
- ✅ 3-5 insights maximum per chart
- ✅ Relate insights directly to chart data
- ✅ Clear chart caption with data source
- ✅ Simple, readable chart design
- ✅ **Content page title in fixed header navigation bar**
- ✅ **Maximum 8 bullet points per page**
- ✅ **Use numbered titles (一、二、三...) for multi-page content**
- ❌ NEVER use single-column layout for charts alone
- ❌ NEVER center-align chart without context
- ❌ NEVER put more than 8 bullet points on one page
- ❌ NEVER display title in content area for content pages

### Content Page (Text-Only)

**Purpose**: Present information with bullet points or numbered lists

**⚠️ CRITICAL RULES**:
- **Maximum 8 bullet points per page** - strictly enforced
- **Multi-page splitting**: If content exceeds 8 points, split into multiple pages with numbered titles
- **Title location**: Display in fixed header navigation bar, NOT in content area
- **Layout first**: Choose layout before distributing content

**Pattern 1: Single Column (≤8 Points)**:
```html
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">Strategic Overview</h2>
  </div>

  <div class="slide-content">
    <ul class="bullet-list">
      <li><strong>Point 1:</strong> Description</li>
      <li><strong>Point 2:</strong> Description</li>
      <li><strong>Point 3:</strong> Description</li>
      <li><strong>Point 4:</strong> Description</li>
      <li><strong>Point 5:</strong> Description</li>
      <li><strong>Point 6:</strong> Description</li>
    </ul>
  </div>
</div>
```

**Pattern 2: Multi-Page Split (>8 Points)**:
```html
<!-- Page 1 of 2 -->
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">一、Strategic Overview</h2>
  </div>

  <div class="slide-content">
    <ul class="bullet-list">
      <li><strong>Point 1:</strong> Description</li>
      <li><strong>Point 2:</strong> Description</li>
      <li><strong>Point 3:</strong> Description</li>
      <li><strong>Point 4:</strong> Description</li>
      <li><strong>Point 5:</strong> Description</li>
      <li><strong>Point 6:</strong> Description</li>
      <li><strong>Point 7:</strong> Description</li>
      <li><strong>Point 8:</strong> Description</li>
    </ul>
  </div>
</div>

<!-- Page 2 of 2 -->
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">二、Strategic Overview</h2>
  </div>

  <div class="slide-content">
    <ul class="bullet-list">
      <li><strong>Point 9:</strong> Description</li>
      <li><strong>Point 10:</strong> Description</li>
      <li><strong>Point 11:</strong> Description</li>
      <li><strong>Point 12:</strong> Description</li>
    </ul>
  </div>
</div>
```

**Pattern 3: Two-Column Layout (≤8 Points Total)**:
```html
<div class="slide content-slide">
  <div class="slide-header">
    <h2 class="slide-header-title">Comparative Analysis</h2>
  </div>

  <div class="slide-content">
    <div class="two-column">
      <div class="column">
        <h3 class="section-heading">Category A</h3>
        <ul class="bullet-list">
          <li>Point 1</li>
          <li>Point 2</li>
          <li>Point 3</li>
          <li>Point 4</li>
        </ul>
      </div>
      <div class="column">
        <h3 class="section-heading">Category B</h3>
        <ul class="bullet-list">
          <li>Point 1</li>
          <li>Point 2</li>
          <li>Point 3</li>
          <li>Point 4</li>
        </ul>
      </div>
    </div>
  </div>
</div>
```

**Best Practices**:
- ✅ **Strictly limit to 8 points per page**
- ✅ **Choose layout first, then distribute content**
- ✅ **Use numbered titles (一、二、三...) for multi-page content**
- ✅ **Display title in fixed header, not content area**
- ✅ Bold key terms at start of each point
- ✅ Keep points concise and parallel
- ✅ Use hierarchy (primary/secondary points)
- ✅ Group related points together
- ❌ NEVER exceed 8 points per page
- ❌ NEVER compress content to fit on one page
- ❌ NEVER display title in content area for content pages
- ❌ NEVER split content arbitrarily without considering logical grouping

### Detailed Findings

**Purpose**: Present supporting analysis and evidence

**Pattern**:
```html
<div class="slide-content">
  <h3 class="section-header">Finding Category 1</h3>
  <p class="body-text">Detailed explanation...</p>

  <div class="data-table-container">
    <table class="data-table">
      <!-- table content -->
    </table>
  </div>
</div>
```

**Best Practices**:
- 3-5 paragraphs maximum
- Clear section headers
- Use tables for detailed data
- Moderate text length (100-150 words)
- Avoid walls of text

### Conclusion Slide

**Purpose**: Present final conclusions and recommendations

**Pattern**:
```html
<div class="conclusions-grid">
  <div class="conclusion-card">
    <h3 class="card-title">Conclusion 1</h3>
    <p class="card-text">Text...</p>
  </div>
</div>
<div class="recommendations-box">
  <h3 class="section-header accent-text">Key Recommendations</h3>
  <ol class="numbered-list">
    <li>Recommendation 1</li>
  </ol>
</div>
```

**Best Practices**:
- 3-6 conclusion cards in grid
- Card accent color for visual emphasis
- Recommendations in separate box
- Numbered recommendations for action
- Clear, actionable items

## Anti-Patterns to Avoid

### Content Anti-Patterns

**AI-Generated Style**:
- Purple gradients on white backgrounds
- All corners rounded to 8px
- Cookie-cutter card layouts
- Generic "professional" templates without personality
- Overused fonts (Inter, Roboto, Arial)

**Content Destruction**:
- Summarizing instead of preserving
- Removing "minor" details
- Rephrasing to "improve" readability
- Combining separate points
- Adding clarifying text

### Design Anti-Patterns

**Visual Clutter**:
- Too many elements on one slide
- Excessive colors or accents
- Multiple charts on single slide
- Decorative icons or graphics
- Unnecessary animations

**Poor Hierarchy**:
- All elements same size
- No clear focal point
- Random ordering
- Mixed font weights
- Inconsistent styling

**Accessibility Issues**:
- Low contrast text (<4.5:1)
- Small font sizes (<14px)
- Unclear color differentiation
- Missing chart labels
- Poor keyboard navigation

## Quality Checklist

Before finalizing presentation, verify:

**Content**:
- [ ] All original content preserved
- [ ] No fabricated data or insights
- [ ] All conclusions present
- [ ] Clear information hierarchy
- [ ] Logical flow and organization

**Design**:
- [ ] Strict color palette adherence
- [ ] Consistent typography
- [ ] Generous white space
- [ ] Aligned, balanced layouts
- [ ] Professional, McKinsey-style quality

**Functionality**:
- [ ] Navigation works (buttons, keyboard)
- [ ] All charts render correctly
- [ ] Responsive design tested
- [ ] Fullscreen mode works
- [ ] No console errors

**Accessibility**:
- [ ] High contrast text
- [ ] Readable font sizes
- [ ] Clear chart labels
- [ ] Keyboard navigation
- [ ] Screen reader compatible

## Common Mistakes

| Mistake | Impact | Fix |
|---------|--------|-----|
| Summarizing content | Loss of detail and meaning | Preserve exact text |
| Too many slides | Loss of focus | Combine related content |
| Wrong chart type | Confusion | Match chart to data nature |
| Inconsistent colors | Unprofessional look | Strict palette adherence |
| Poor spacing | Cluttered look | Generous white space |
| Missing conclusions | Incomplete presentation | Ensure all conclusions included |
| Low contrast | Unreadable text | Ensure 4.5:1 contrast ratio |
| Cluttered slides | Confusing message | Simplify and focus |
