# HTML Presentation Beautifier - Plugin Guide

Complete guide for using the HTML Presentation Beautifier plugin with Claude Code.

## Overview

This plugin transforms documents, reports, and data into professional McKinsey-style HTML presentations with intelligent chart selection and interactive navigation.

**Core Principle**: Preserve 100% of original content while applying professional McKinsey-style design.

## Installation

### Current Project

The plugin is already configured in the current directory. Simply use:

```
/beauty your_document.md
```

### Other Projects

```bash
# Navigate to your project
cd /path/to/your-project

# Enable the plugin
/path/to/html-presentation-beautifier/enable-plugin.sh
```

## Usage

### Basic Command

```bash
/beauty document.md
```

This generates `document_beautified.html` with:
- Professional McKinsey-style design
- Intelligent chart selection
- Interactive navigation
- Responsive layout
- Full content preservation

### Multiple Documents

```bash
/beauty report.md analysis.md summary.md
```

Each document generates its own presentation with consistent styling.

### Supported Formats

- **Markdown** (.md) - Structured documents with headings, lists, data
- **JSON** (.json) - Structured data
- **Text** (.txt) - Plain text documents
- **HTML** (.html) - Existing presentations needing redesign

## Workflow

The plugin uses a 6-phase AI-powered workflow:

1. **Document Parsing** (~1 min)
   - Extract structure, data, and conclusions
   - Identify quantitative data for visualization

2. **Slide Planning** (~2 min)
   - Transform content into slide-friendly structure
   - Assign appropriate visualizations to each slide

3. **Design Application** (~1 min)
   - Apply McKinsey color palette
   - Set typography hierarchy
   - Optimize spacing and layout

4. **Content Visualization** (~2 min)
   - Enhance with charts and graphics
   - Avoid plain text bullet lists for insights

5. **HTML Generation** (~3 min)
   - Create single-file, self-contained HTML
   - Inline CSS/JavaScript
   - Interactive features

6. **Quality Review** (~2 min)
   - Verify content integrity (100% preservation)
   - Check McKinsey style compliance
   - Validate code quality
   - Generate quality report

**Total**: ~10-12 minutes for typical presentation

## Output Features

### Interactive Navigation
- Previous/Next buttons
- Keyboard shortcuts (←/→, Space, Escape)
- Slide counter
- Fullscreen mode

### Chart Visualizations
- **50+ chart types** intelligently selected based on content structure
- Interactive hover tooltips
- Legend toggling
- Smooth animations

### Responsive Design
- Desktop, tablet, and mobile layouts
- Optimized breakpoints (1200px, 768px)
- Scalable typography

### Single File Output
- All CSS inline in `<style>` tag
- All JavaScript inline in `<script>` tag
- Chart.js loaded from CDN
- No external dependencies

## Design System

### Colors

The plugin uses McKinsey-standard colors:

```css
--primary-background: #FFFFFF    /* Slide background */
--header-background: #000000     /* Header bar */
--primary-accent: #F85d42        /* Key highlights */
--secondary-accent: #74788d      /* Supporting text */
--deep-blue: #556EE6             /* Chart data */
--green: #34c38f                 /* Success metrics */
--blue: #50a5f1                  /* Neutral emphasis */
--yellow: #f1b44c                /* Warnings */
```

### Typography

- **Titles**: 48-64px, bold, black
- **Subtitles**: 28-36px, bold, accent color
- **Body**: 16-20px, regular, dark gray
- **Chart labels**: 12-14px, clear

## Content Integrity

The plugin guarantees **100% content preservation**:

- ✅ No summarization or compression
- ✅ No paraphrasing - exact wording preserved
- ✅ No deleted or omitted content
- ✅ All data points visualized
- ✅ All conclusions displayed
- ✅ Exact counts match source

## Quality Assurance

Each generated presentation undergoes automatic review:

1. **Content Integrity** - Verifies 100% preservation
2. **Code Quality** - HTML/CSS/JS validity
3. **McKinsey Style** - Design standards compliance
4. **Chart Validity** - Visualization correctness
5. **Interactivity** - Feature testing

**Score Interpretation**:
- ≥85: Approved, optional improvements
- 75-84: Acceptable, address major issues
- <75: Needs regeneration

## Agents

The plugin includes specialized agents:

- **presentation-merger** - Merge multiple presentations
- **content-merger** - Consolidate content from multiple sources
- **visualization-optimizer** - Optimize chart selection
- **content-reviewer** - Verify content integrity
- **html-presentation-reviewer** - Comprehensive quality review

## Troubleshooting

### Command Not Recognized

1. Verify symlink created correctly
2. Check `.claude-plugin/plugin.json` exists
3. Restart Claude Code

### Python Script Errors

```bash
# Check Python version
python3 --version  # Requires 3.7+

# Add execution permissions
chmod +x skills/scripts/*.py
```

### Chart Not Rendering

1. Check internet connection (Chart.js loads from CDN)
2. Verify browser console for errors
3. Ensure data format is correct

## Examples

See the `skills/beauty-html/assets/` directory for example charts and visualizations:

- `pyramid-chart-example.html` - Hierarchical structures
- `timeline-example.html` - Project milestones
- `swot-analysis-example.html` - Strategic analysis
- `funnel-chart-example.html` - Conversion flows
- And 30+ more examples

## Documentation

- **[Skill Documentation](skills/beauty-html/SKILL.md)** - Complete workflow
- **[Chart Examples](skills/beauty-html/assets/CHART_EXAMPLES_INDEX.md)** - Available chart types
- **[Design System](skills/beauty-html/references/mckinsey-design-system.md)** - Design specifications

## License

MIT License - See LICENSE file for details.
