# Work Memo Plugin

Personal work record management with multi-dimensional tracking, natural language search, and smart prioritization. A record-only system for work events with comprehensive filtering and reporting capabilities.

## Features

- **Natural Language Input**: Record work information using simple, natural language
- **Multi-dimensional Tracking**: Track work by type, urgency, importance, tags, contexts, and dates
- **Eisenhower Matrix**: Automatic quadrant classification (Q1-Q4) based on urgency and importance
- **URL Support**: Fetch and summarize webpage content automatically
- **Flexible Search**: Natural language search with advanced filtering
- **Smart Prioritization**: Priority scoring based on multiple dimensions

## Installation

```bash
claude plugins install work-memo
```

## Usage

### Recording Work Items

Use the `/memo` command to record work information:

```bash
# Simple task
/memo Complete project report

# With priority and tags
/memo 紧急会议明天 #work @office

# Bug fix with urgency
/memo 修复登录bug #urgent

# Meeting
/memo 团队例会 #meeting

# Important call
/memo 重要电话明天 @phone
```

### Recording from URLs

Record and summarize webpage content:

```bash
# Article or documentation
/memo https://example.com/article

# GitHub README
/memo https://github.com/project/readme #project

# Technical documentation
/memo https://docs.python.org/tutorial
```

## Natural Language Syntax

### Tags
Use `#` followed by tag name:
- `#work` - Work related
- `#urgent` - Urgent items
- `#project` - Project specific
- `#meeting` - Meetings
- `#bug` - Bug fixes

### Contexts
Use `@` followed by context:
- `@office` - Office work
- `@home` - Home work
- `@phone` - Phone calls
- `@computer` - Computer work

### Priority Keywords
The system automatically detects:
- **Urgency**: urgent, emergency, asap, 紧急, 非常紧急
- **Importance**: important, critical, key, 重要, 关键

### Time References
Natural language dates:
- `today`, `tomorrow`, `今天`, `明天`
- `this week`, `next week`, `本周`, `下周`
- Specific dates: `2026-02-05`

## Work Types

Automatically detected types:
- `task` - General tasks
- `meeting` - Meetings and calls
- `bugfix` - Bug fixes
- `feature` - New features
- `review` - Code reviews
- `research` - Research and reading
- `email` - Email communications
- `call` - Phone calls
- `coding` - Coding work
- `design` - Design work

## Eisenhower Matrix

Items are automatically categorized into quadrants:

- **Q1**: Urgent + Important (Do First)
- **Q2**: Not Urgent + Important (Schedule)
- **Q3**: Urgent + Not Important (Delegate)
- **Q4**: Not Urgent + Not Important (Eliminate)

## Storage System

All work records are stored as **Markdown files** with YAML frontmatter in `~/work-memo/records/`:

- **File Structure**: `YYYY-MM/DD/[id]_[title].md`
- **Format**: YAML frontmatter + Markdown content
- **Benefits**:
  - Human-readable and editable
  - Version control friendly (git)
  - Easy to backup and sync
  - Portable across systems
  - No database required

Example file loc`
~/work-memo/records/2026-02/05/a1b2c3d4_urgent_meeting.md
```

Each file contains:
- Complete metadata in YAML frontmatter
- Original input and AI analysis
- Full work description
- Automatic Eisenhower quadrant calculation

## Output Format

After recording, you'll receive confirmation with:
- Title
- Type
- Urgency level (1-5)
- Importance level (1-5)
- Eisenhower quadrant (Q1-Q4)
- Tags
- Contexts
- Date

### Example Output

```json
{
  "status": "recorded",
  "title": "紧急会议",
  "type": "meeting",
  "urgency": 4,
  "importance": 3,
  "eisenhower_quadrant": "Q1",
  "tags": ["work"],
  "contexts": ["office"],
  "date": "2026-02-05"
}
```

### URL Recording Output

```json
{
  "status": "success",
  "id": "123",
  "title": "Article Title",
  "url": "https://example.com/article",
  "summary": "Content summary...",
  "type": "research",
  "urgency": 3,
  "importance": 3,
  "tags": ["web", "reading"],
  "contexts": ["https://example.com/article"],
  "eisenhower": "Q2",
  "created_"2026-02-05T10:00:00"
}
```

## Advanced Usage

### Explicit Parameters

```bash
# With explicit urgency and importance
/memo "任务描述" --urgency 5 --importance 4

# With explicit type and tags
/memo "任务描述" --type bugfix --tags urgent
```

## Important Notes

- This is a **record-only** system - no tasks are executed
- All information is stored as **Markdown files** in `~/work-memo/records/`
- Files are organized by date (YYYY-MM/DD) for easy browsing
- Use natural language for best automatic categorization
- More context = better categorization
- URLs are fetched and summarized but not executed
- Requires internet connection for URL processing
- Records can be edited directly in any text editor
- Compatible with version control systems (git)

## Help

Get help anytime:

```bash
/memo help
```

## Author

Created by within7 (wxj@within-7.com)

## Version

1.0.0

## License

See LICENSE file tails.
