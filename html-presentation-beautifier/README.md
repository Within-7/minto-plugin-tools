# HTML Presentation Beautifier

Transform documents and data into professional McKinsey-style HTML presentations with intelligent chart selection and interactive navigation.

## Features

- **McKinsey/BCG Style Design** - Professional business presentation appearance
- **50+ Chart Types** - Intelligent chart selection based on content structure
- **Multi-format Support** - Markdown, JSON, Text
- **Single File Output** - All CSS/JavaScript inline, no external dependencies
- **Responsive Design** - Perfect display on any device
- **Keyboard Navigation** - Smooth presentation experience
- **100% Content Preservation** - No summarization or content loss

## Quick Start

### As a Claude Code Plugin

```bash
# Use the /beauty command
/beauty your_document.md
```

The plugin automatically:
1. Parses document structure and data
2. Plans slides with appropriate visualizations
3. Applies McKinsey design system
4. Generates interactive HTML presentation
5. Reviews quality and integrity

### Installation in Other Projects

```bash
# Navigate to your project directory
cd /path/to/your-project

# Run the enable script
/path/to/html-presentation-beautifier/enable-plugin.sh
```

## Usage Examples

```bash
# Single document
/beauty report.md

# Multiple documents with consistent styling
/beauty report.md analysis.md summary.md

# JSON data to visualization
/beauty data.json

# Existing HTML beautification
/beauty presentation.html
```

## Design System

### Color Palette (McKinsey/BCG Style)

| Color Type | Hex Code | Usage |
|------------|----------|-------|
| Primary Background | `#FFFFFF` | Slide background |
| Header Background | `#000000` | Header bar |
| Primary Accent | `#F85d42` | Key highlights |
| Secondary Accent | `#74788d` | Supporting text |
| Deep Blue | `#556EE6` | Chart data |
| Green | `#34c38f` | Success metrics |
| Blue | `#50a5f1` | Neutral emphasis |
| Yellow | `#f1b44c` | Warnings/caution |

### Typography

- **Titles**: 48-64px, bold, black (`#000000`)
- **Subtitles**: 28-36px, bold, accent color
- **Body**: 16-20px, regular, dark gray (`#333333`)
- **Chart Labels**: 12-14px, clear and readable

## Chart Types

### Basic Charts
- Bar Chart, Horizontal Bar, Line Chart, Pie Chart, Doughnut Chart

### Advanced Charts
- Radar Chart, Funnel Chart, Gantt Chart, Heatmap, Waterfall Chart, Sankey Diagram, BCG Matrix, Box Plot, Bubble Chart

### Conceptual Charts
- Pyramid, Timeline, Flowchart, Venn Diagram, Mind Map, SWOT Analysis, Pros-Cons, Problem-Solution, Strategy Roadmap

## Interactive Features

### Navigation
- **Mouse**: Previous/Next buttons
- **Keyboard**: Arrow keys (←/→), Space (next), Escape (exit fullscreen)

### Chart Interaction
- Hover for detailed values
- Click legend to toggle data series
- Smooth animations

### Fullscreen Mode
- Click fullscreen button or press F11
- Perfect presentation experience

## Project Structure

```
html-presentation-beautifier/
├── .claude-plugin/
│   └── plugin.json              # Plugin manifest
├── commands/
│   └── beauty.md                # /beauty command
├── agents/
│   ├── presentation-merger.md   # Multi-file merging
│   ├── content-merger.md        # Content consolidation
│   ├── visualization-optimizer.md  # Chart optimization
│   ├── content-reviewer.md      # Content integrity check
│   └── html-presentation-reviewer.md  # Quality review
├── skills/
│   └── beauty-html/
│       ├── SKILL.md            # Main skill definition
│       ├── assets/             # Chart examples and templates
│       ├── references/         # Design guides and prompts
│       ├── scripts/            # Python utilities
│       └── templates/          # Slide templates
├── docs/
│   ├── guides/                 # Usage guides
│   └── reports/                # Development reports
├── install.sh                  # Installation script
├── enable-plugin.sh            # Quick enable script
└── README.md                   # This file
```

## Documentation

- **[Skill Documentation](skills/beauty-html/SKILL.md)** - Complete workflow and usage
- **[Chart Examples](skills/beauty-html/assets/CHART_EXAMPLES_INDEX.md)** - Available chart types
- **[Design System](skills/beauty-html/references/mckinsey-design-system.md)** - Complete design specifications

## Supported Document Formats

| Format | Extension | Support |
|--------|-----------|---------|
| Markdown | `.md` | ✅ |
| JSON | `.json` | ✅ |
| Text | `.txt` | ✅ |
| HTML | `.html` | ✅ |

## Use Cases

- 📊 Business reports
- 🎓 Academic presentations
- 💼 Project reviews
- 📈 Data analysis presentations
- 📝 Research reports

## License

MIT License

## Version

1.0.0 - Production Ready
