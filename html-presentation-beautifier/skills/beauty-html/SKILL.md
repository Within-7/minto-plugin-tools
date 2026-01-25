---
name: html-presentation-beautifier
description: Transform documents and data into professional HTML presentations with McKinsey-style design. Use for: presentation creation, slide beautification, data visualization, McKinsey formatting, professional reports. 将文档、数据、结论转化为通俗连贯的HTML幻灯片，使用McKinsey风格设计系统，通过图表可视化展示结论。不修改原文档内容，仅进行展示性美化输出。
---

# HTML Presentation Beautifier

Transform raw documents and data into professional HTML presentations with McKinsey-style design system, intelligent data visualization, and interactive navigation.

**核心原则**：Preserve all original content, conclusions, and data exactly as provided. Apply McKinsey-style design for visual enhancement only.

## When to Use This Skill

Use this skill when:
- User needs to create professional presentations from documents
- Converting reports, analyses, or research into slide format
- Creating McKinsey-style business presentations
- Visualizing data with professional charts
- Generating HTML slides with interactive navigation

**典型触发场景**：
- "Create a presentation from this report"
- "Transform this document into slides"
- "Generate McKinsey-style presentation"
- "Visualize this data professionally"
- "Make a HTML presentation"

## Process Overview

This skill uses AI-powered subagents to create presentations through 4 phases:

1. **Parse Document** - Extract structure, data, and conclusions
2. **Plan Slides** - Organize content into slide structure
3. **Apply Design** - Apply McKinsey-style design system
4. **Generate HTML** - Create interactive HTML presentation

## Design System (McKinsey/BCG Style)

### Color Palette

| Color Type | Hex Code | Usage |
|------------|----------|-------|
| Primary Background | `#FFFFFF` | Slide background |
| Header Background | `#000000` | Title bars |
| Primary Accent | `#F85d42` | Key highlights, CTAs |
| Secondary Accent | `#74788d` | Supporting text |
| Deep Blue | `#556EE6` | Charts, data points |
| Green | `#34c38f` | Success indicators |
| Blue | `#50a5f1` | Neutral emphasis |
| Yellow | `#f1b44c` | Warnings, notes |

### Typography

- **Title**: 48-64px, Bold, Black (`#000000`)
- **Subtitle**: 28-36px, Bold, Accent Color
- **Body**: 16-20px, Regular, Dark Gray (`#333333`)
- **Chart Labels**: 12-14px, Clear, Readable

### Design Principles

- **Modern Business Style**: Clean, professional, minimal clutter
- **Visual Hierarchy**: Clear distinction between titles, subtitles, and body
- **Consistency**: Uniform design language across all slides
- **Data-Driven**: Use charts and visualizations for quantitative information

## Phase 1: Document Parsing

**Goal**: Extract and analyze source document structure, data points, and conclusions.

**Prerequisites**:
- Source document provided (Markdown, text, or structured format)
- No modifications to original content

**Checklist**:
- [ ] Document format identified and readable
- [ ] Document structure parsed (headings, lists, data tables, conclusions)
- [ ] All data points and metrics extracted
- [ ] All conclusions and insights identified
- [ ] Content hierarchy mapped (H1 → H2 → H3)

**Steps**:
1. Read the source document completely without modification
2. Identify document type (report, analysis, research, etc.)
3. Extract structural elements:
   - Headings and subheadings
   - Bullet points and numbered lists
   - Data tables and numerical data
   - Key conclusions and recommendations
4. Map content hierarchy: main topics → subtopics → supporting details
5. Identify quantitative data suitable for charts/graphs

**Exit Criteria**: Document fully parsed with content structure mapped and data points catalogued.

## Phase 2: Content Structuring (Using Subagent)

**Goal**: Transform parsed content into slide-friendly format while preserving all original meaning and conclusions.

**Approach**: Use the `Task` tool with subagent to intelligently plan slide structure.

**Subagent Specification**:
- **Type**: `general-purpose`
- **Input**: Parsed document with sections, data points, and conclusions
- **Output**: Structured slide plan with slide types, content assignments, and visualizations

**Prompt Template**:
```
You are a presentation planning specialist. Analyze this document and create a detailed slide plan.

DOCUMENT CONTENT: {parsed_document_content}

YOUR TASK:
1. Create a slide plan following this structure:
   - Title slide (always first)
   - Executive summary (if conclusions exist)
   - Data visualization slides (for sections with numerical data)
   - Conceptual slides (for non-numerical frameworks)
   - Content slides (for detailed information)
   - Conclusions slide (if recommendations exist)

2. For each slide, specify:
   - Slide type: [TITLE, EXECUTIVE_SUMMARY, DATA_VISUALIZATION, CONCEPTUAL, CONTENT, CONCLUSIONS]
   - Title: Clear, concise heading
   - Content: Key points to include (preserve exact wording)
   - Visualization type: (for DATA_VISUALIZATION slides)
   - Layout: [title-center, bullet-points, two-column, full-width, conclusions-grid]

3. Smart chart selection for data slides:
   - Rankings/Hierarchy → bar, polarArea
   - Flow/Journey → line, funnel
   - Distribution → bubble, polarArea
   - Time/Cyclical → line, step
   - KPI/Target → bar, bullet
   - Multi-dimensional → radar
   - Proportions → doughnut (≤5 items), pie (≤8 items)
   - Trends → line
   - Comparison → bar

4. For conceptual slides, detect type:
   - Hierarchy → pyramid
   - Process → progression
   - Key Points → emphasis
   - Loop → cycle
   - Before/After → comparison
   - Framework → framework

OUTPUT FORMAT:
Return JSON slide plan with slides array containing slide_number, slide_type, title, content, key_points, chart_type, layout.

CRITICAL RULES:
- Preserve ALL original conclusions and recommendations exactly - 100% of them
- Do NOT fabricate data or insights
- Do NOT compress or summarize - include ALL content
- Do NOT limit bullet points - show every item
- Use exact text from source document - verbatim, no paraphrasing
- Create sufficient slides to accommodate 100% of source content
```

**Exit Criteria**: Structured slide plan received with all slides defined, visualizations assigned, zero content loss.

## Phase 3: Design & Layout

**Goal**: Apply McKinsey-style design system to structured content.

**Checklist**:
- [ ] Slide layouts selected for each content type
- [ ] Color scheme applied consistently
- [ ] Typography hierarchy established
- [ ] White space and spacing optimized
- [ ] Charts designed with professional polish

**Steps**:
1. Select appropriate layout for each slide:
   - **Full-width title** for section headers
   - **Two-column** for comparison slides
   - **Center focus** for key messages
   - **Chart + text** for data slides
2. Apply color scheme:
   - White background for all slides
   - Black header bars with white text
   - Orange accent (`#F85d42`) for key metrics
   - Gray (`#74788d`) for secondary text
3. Set typography hierarchy
4. Optimize spacing and layout (40-60px margins, 20-30px element spacing)
5. Design charts with clean, minimal style

**Exit Criteria**: All slides designed with consistent McKinsey-style branding.

## Phase 4: HTML Generation (Using Subagent)

**Goal**: Generate interactive HTML presentation file.

**Approach**: Use the `Task` tool with subagent to generate complete HTML.

**Subagent Specification**:
- **Type**: `general-purpose`
- **Input**: Structured slide plan from Phase 2
- **Output**: Single-file, self-contained HTML presentation

**Prompt Template**:
```
You are an expert HTML/CSS/JavaScript developer specializing in McKinsey-style presentations.

SLIDE PLAN: {slide_plan_json}

DESIGN SYSTEM:
Colors: Background #FFFFFF, Header #000000, Primary Accent #F85d42, Secondary #74788d, Deep Blue #556EE6, Green #34c38f, Blue #50a5f1, Yellow #f1b44c
Typography: Title 48-64px bold black, Subtitle 28-36px bold accent, Body 16-20px regular dark gray

YOUR TASK:
Generate a complete, single-file HTML presentation with:

1. HTML Structure:
   - DOCTYPE, html, head, body tags
   - Navigation bar (prev/next buttons, slide counter)
   - Slide containers for each slide
   - Fullscreen toggle button

2. Inline CSS (McKinsey-style):
   - Color variables (:root)
   - Global styles (reset, body, fonts)
   - Navigation bar styling
   - Slide layout and transitions
   - Title slide styling
   - Header bar styling
   - Content layouts (two-column, full-width, etc.)
   - Chart containers
   - Responsive breakpoints (1200px, 768px)

3. JavaScript Functionality:
   - Slide navigation (arrow keys, space, click)
   - Keyboard event handlers
   - Fullscreen toggle
   - Slide counter updates
   - Chart.js configurations for data slides
   - Smooth transitions

4. Chart.js Integration:
   - Load from CDN: https://cdn.jsdelivr.net/npm/chart.js
   - Configure each chart based on slide plan
   - Use color palette for chart colors
   - Enable tooltips and legends
   - Responsive sizing

5. CRITICAL Content Requirements:
   - Render EXACT text from slide plan
   - Preserve ALL conclusions word-for-word
   - Use exact data points for charts
   - Apply specified layouts

CHART CONFIGURATION:
- bar: Basic bar chart
- line: Line chart for trends
- pie/doughnut: Part-to-whole (≤5 items doughnut, ≤8 pie)
- radar: Multi-dimensional comparison
- polarArea: Rankings, cyclical data
- bubble: Three dimensions (x, y, size)

OUTPUT FORMAT:
Return ONLY the complete HTML file content. The HTML must be self-contained (inline CSS, inline JS), work immediately in browser, have no external dependencies except Chart.js CDN, include ALL slides, and preserve ALL original content exactly.
```

**Exit Criteria**: Complete HTML presentation file generated, ready to open in browser.

## Interactive Features

### Navigation
- **Buttons**: Previous/Next in navbar
- **Keyboard**: Arrow keys (←/→), Space (next), Escape (exit fullscreen)
- **Slide counter**: Shows current position

### Full-Screen Mode
- Toggle button in bottom-right
- Escape key to exit

## Chart Visualizations

**Smart Chart Selection** based on data characteristics:

**Basic Charts:**
- **Bar Chart** (柱状图) - Category comparisons
- **Horizontal Bar** (条形图) - Long category names
- **Line Chart** (折线图) - Trends over time
- **Pie Chart** (饼图) - Part-to-whole (≤5 items)
- **Doughnut Chart** (环形图) - Part-to-whole with center focus

**Advanced Charts:**
- **Progress Ring** (进度环) - Completion status
- **Gauge** (仪表盘) - KPI metrics
- **Radar Chart** (雷达图) - Multi-dimensional comparison
- **Funnel Chart** (漏斗图) - Process stages
- **Gantt Chart** (甘特图) - Project timelines
- **Heatmap** (热力图) - Density distribution
- **Pyramid Chart** (金字塔图) - Hierarchical levels
- **Sankey Diagram** (桑基图) - Flow between stages
- **Bullet Chart** (子弹图) - Target vs actual
- **Box Plot** (箱型图) - Distribution and outliers
- **Waterfall Chart** (瀑布图) - Sequential additions
- **Bubble Chart** (气泡图) - Three dimensions

**Conceptual Charts** (No numerical data required):
- **Emphasis Box** (强调框) - Highlight key points
- **Progression** (递进图) - Sequential steps
- **Pyramid** (金字塔) - Hierarchical structure
- **Cycle** (圆环) - Cyclical process
- **Venn Diagram** (韦恩图) - Set relationships
- **Timeline** (时间轴) - Sequential events
- **Flowchart** (流程图) - Process with decisions
- **Comparison** (对比图) - Two states comparison

## NEVER Do These

- **NEVER modify original content or conclusions**: Preserve all original meaning, data, and conclusions exactly - 100% of them
- **NEVER delete, skip, or omit any content**: Include every section, bullet, data point
- **NEVER summarize or compress**: Show complete detail level, create more slides if needed
- **NEVER truncate lists**: If source has 15 items, show all 15 items
- **NEVER paraphrase**: Use exact wording from source documents
- **NEVER add fabricated data**: Only use data from the source document
- **NEVER deviate from color scheme**: Strict adherence to McKinsey-style palette
- **NEVER use inconsistent typography**: Maintain hierarchy across all slides
- **NEVER sacrifice content for aesthetics**: Better to have many dense slides than few incomplete ones

## Resources

All essential information is included in this main documentation:

- **Design System**: See "Design System (McKinsey/BCG Style)" section above
- **Phase Details**: See "Phase 1-4" sections with complete checklists
- **Chart Types**: See "Chart Visualizations" section
- **Examples**: See prompt templates in Phase 2 and Phase 4

## Quick Start

This skill uses AI-powered subagents - no manual scripts required.

**Workflow**:

1. **Parse Document** (Phase 1)
   - Read and understand document structure
   - Extract sections, data, conclusions

2. **Plan Slides** (Phase 2)
   - Invoke `Task` tool with `general-purpose` subagent
   - Subagent creates structured slide plan
   - Assigns chart types and visualizations

3. **Apply Design** (Phase 3)
   - McKinsey-style design applied automatically
   - Color palette, typography predefined

4. **Generate HTML** (Phase 4)
   - Invoke `Task` tool with `general-purpose` subagent
   - Subagent generates complete HTML presentation
   - Single-file, self-contained output

**Example Usage**:
```
User: "Create a McKinsey-style presentation from this document"

[Follow Phase 1-4 workflow using subagents]
→ Complete HTML presentation file
```

## Content Integrity Verification (MANDATORY)

**Before Finalizing Presentation**:

Verify that 100% of source content is preserved:

**Step 1**: Count source document elements
- Total sections: _____
- Total bullet points: _____
- Total data points: _____
- Total conclusions: _____

**Step 2**: Count presentation elements
- Total sections shown: _____
- Total bullet points shown: _____
- Total data points visualized: _____
- Total conclusions included: _____

**Step 3**: Verify match
- [ ] Section counts match ✓
- [ ] Bullet counts match ✓
- [ ] Data point counts match ✓
- [ ] Conclusion counts match ✓
- [ ] Exact wording used (no paraphrasing) ✓

**IF ANY COUNT DOES NOT MATCH, REGENERATE.**

**Red Flags**:
- "Key points" instead of complete lists
- Charts showing only top N items
- Bullet counts that don't match source
- Phrasing that doesn't match source exactly
