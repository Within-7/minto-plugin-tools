# Skill Optimizer

Comprehensive skill optimization and validation plugin for Claude Code. Analyzes, validates, and optimizes skills according to best practices.

## Features

### 🔍 Analysis
- **Comprehensive Analysis**: Analyze skill structure, content, and best practices compliance
- **Quality Scoring**: Dynamic 0-100 scoring based on issues found
- **Detailed Reports**: Identify problems with severity levels (critical, major, minor)

### ✅ Validation
- **Automated Checks**: Validate YAML syntax, required fields, naming conventions
- **Content Quality**: Check descriptions, trigger phrases, and formatting
- **Best Practices**: Verify compliance with latest skill standards

### 🚀 Optimization
- **Interactive Workflow**: Step-by-step optimization with user control
- **Smart Suggestions**: Context-aware improvement recommendations
- **Safe Application**: Review suggestions before applying any changes

### 🤖 Autonomous Agent
- **Proactive Analysis**: Automatically triggers when editing SKILL.md files
- **Real-time Feedback**: Provides suggestions during skill creation
- **Quality Guardian**: Monitors and maintains skill quality standards

## Installation

### Local Installation
```bash
cp -r skill-optimizer /path/to/your/project/.claude-plugin/
```

### Global Installation
```bash
cp -r skill-optimizer ~/.claude/plugins/
```

## Usage

### Commands

#### Analyze Skills
```bash
/skill-opt:analyze plugins/your-plugin/skills
```
Analyzes all skills in the specified directory and generates a comprehensive report.

#### Optimize Skills
```bash
/skill-opt:optimize plugins/your-plugin/skills
```
Interactive workflow to review and fix issues one by one.

#### Validate Skills
```bash
/skill-opt:validate plugins/your-plugin/skills
```
Quick validation with quality score and issue list.

### Autonomous Agent

The `skill-optimizer` agent automatically activates when:
- You create or edit SKILL.md files
- You ask about skill quality or best practices
- You create new skill directories

It provides proactive suggestions and quality feedback.

## Skill Components

### skill-best-practices
Comprehensive guide covering:
- Skill structure and formatting
- Trigger phrase optimization
- Content quality standards
- Progressive disclosure patterns
- Common mistakes and fixes

Reference files:
- `structure-guide.md` - Structure and format standards
- `trigger-patterns.md` - Trigger phrase patterns and examples
- `content-quality.md` - Content quality checklist
- `common-mistakes.md` - Common errors and how to fix them

## Scripts

### validate-skill.sh
Comprehensive validation script checking:
- YAML frontmatter syntax
- Required fields
- File naming conventions
- Markdown formatting
- Content quality

### score-skill.py
Dynamic scoring system based on:
- Issues found
- Severity levels
- Impact on quality

### fix-skill.sh
Generates fix recommendations without modifying files.

## Scoring System

Quality scores are calculated dynamically:
- **90-100**: Excellent - Follows all best practices
- **70-89**: Good - Minor improvements needed
- **50-69**: Fair - Several issues to address
- **Below 50**: Needs significant work

## Issue Severity

- **Critical**: Must fix (broken syntax, missing required fields)
- **Major**: Should fix (affects functionality)
- **Minor**: Nice to fix (style, clarity improvements)

## Best Practices Covered

### Structure
- ✅ Proper YAML frontmatter
- ✅ Required fields (name, description)
- ✅ Kebab-case naming
- ✅ Correct file organization

### Content
- ✅ Third-person descriptions
- ✅ Imperative instructions
- ✅ Strong trigger phrases
- ✅ Progressive disclosure

### Quality
- ✅ Clear and concise writing
- ✅ Working examples
- ✅ Proper documentation
- ✅ Accessibility considerations

## Examples

### Analyze a Plugin
```bash
# Analyze all skills in a plugin
/skill-opt:analyze ./my-plugin/skills

# Output includes:
# - Quality score (0-100)
# - Issue list with severity
# - Detailed recommendations
# - Best practices compliance
```

### Optimize Interactively
```bash
/skill-opt:optimize ./my-plugin/skills

# Process:
# 1. Scan all skills
# 2. Show issues one by one
# 3. For each issue:
#    - Describe the problem
#    - Show current code
#    - Provide fix suggestion
#    - Ask to apply or skip
# 4. Generate summary report
```

### Quick Validation
```bash
/skill-opt:validate ./my-plugin/skills

# Output:
# Score: 85/100
# Issues: 3
# - [MAJOR] Missing version field
# - [MINOR] Description could be more specific
# - [MINOR] Consider adding examples
```

## Development

### Requirements
- Bash shell
- Python 3.x
- Claude Code with plugin support

### Testing
Test the plugin locally:
```bash
cc --plugin-dir /path/to/skill-optimizer
```

## Contributing

Contributions welcome! Please ensure:
- All components follow best practices
- Scripts are well-documented
- Changes maintain backward compatibility

## License

MIT

## Version

0.1.0 - Initial release
