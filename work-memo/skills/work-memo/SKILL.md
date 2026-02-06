---
name: work-memo
description: Records work information with multi-dimensional tracking. Use when user wants to record work events, tasks, or activities without executing them. Supports webpage content summarization and URL recording.
allowed-tools:
  - Bash
  - Read
  - Write
triggers:
  keywords:
    - record work
    - memo
    - work memo
    - track task
    - log work
    - 记录工作
    - 工作备忘
    - 记录任务
---

# Work Memo Skill

This skill provides intelligent work information recording with multi-dimensional tracking capabilities.

## Purpose

Record work-related information (tasks, meetings, calls, etc.) with automatic categorization, prioritization, and organization. This is a **record-only** system - it does not execute tasks.

## When to Use

Use this skill when:
- User wants to record work information
- User mentions recording tasks, meetings, calls, or work events
- User provides URLs to articles/documentation to save for later
- User wants to track work items with priorities and contexts
- User needs to organize work by tags, contexts, or dates

## Capabilities

### 1. Natural Language Processing
- Parse work descriptions from natural language
- Extract work type, priority, tags, contexts, ands
- Detect urgency and importance levels automatically
- Support both English and Chinese

### 2. Multi-Dimensional Tracking
- **Type**: task, meeting, call, email, bugfix, feature, review, research, coding, design
- **Urgency**: 1-5 scale (detected from keywords like "urgent", "紧急")
- **Importance**: 1-5 scale (detected from keywords like "important", "重要")
- **Tags**: #work, #urgent#meeting, etc.
- **Contexts**: @office, @home, @phone, @computer, etc.
- **Dates**: today, tomorrow, specific dates

### 3. Eisenhower Matrix Classification
Automatic quadrant assignment:
- **Q1**: Urgent + Important (Do First)
- **Q2**: Not Urgent + Important (Schedule)
- **Q3**: Urgent + Not Important (Delegate)
- **Q4**: Not Urgent + Not Important (Eliminate)

### 4. URL Content Processing
- age content from URLs
- Extract and summarize main content
- Store URL as context for easy reference
- Auto-tag with "web" and "reading"
- Default type: "research"

## Implementation

### For Text Input

1. **Parse Input**: Extract work details from natural language
   - Identify title/description
   - Detect work type from keywords
   - Find priority indicators (urgent, important)
   - Extract tags (#tag) and contexts (@context)
   - Parse date references

2. **Execute Recording**: Use `skills/scripts/memo_command.py`
   ```bash
   python3 skills/scripts/memo_command.py "<work description>"
   ```

3. **Return Confirmation**: Include:
   - Recorded title
   - Type
   - Urgency/importance levels
   - Eisenhower quadrant
   - Tags and contexts
   - Date

### For URL Input
date URL**: Check format (http:// or https://)

2. **Fetch Content**: Use web fetching capabilities to retrieve webpage

3. **Summarize**: Extract title and create summary

4. **Record**: Store with:
   - Webpage title as record title
   - URL in contexts
   - Summary in description
   - Type: research
   - Tags: web, reading

5. **Return Confirmation**: Include URL and summary
ples

### Text Input
```
Input: 紧急会议今天 #work @office
Output: {
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

### URL Input
```
Input: https://example.com/article
Output: {
  "status": "success",
  "title": "Article Title",
  "url": "https://example.com/article",
  "summary": "Content summary...",
  "type": "research",
  "tags": ["web", "reading"],
  "eisenhower": "Q2"
}
```

## Natural Language Syntax

### Tags
- Format: `#tagname`
- Examples: #work, #urgent, #project, #meeting, #bug

### Contexts
- Format: `@context`
- Examples: @office, @home, @phone, @computer

### Priority Keywords
- **Urgency**: urgent, emergency, asap, 紧急, 非常紧急
- **Importance**: important, critical, key, 重要, 关键

### Dates
- Natural: today, tomorrow, this week, 今天, 明天, 本周
- Specific: 2026-02-05

## Output Format

Always return a JSON-formatted confirmation with:
- `status`: "recorded" or "success"
- `title`: Work item title
- `type`: Work type
- `urgency`: 1-5 scale
- `importance`: 1-5 scale
- `eisenhower_quadrant` or `eisenhower`: Q1-Q4
- `tags`: Array of tags
- `contexts`: Array of contexts
- `date` or `created_at`: Date timestamp

## Storage System

Records are stored as **Markdown files** with YAML frontmatter:

- **Location**: `~/work-memo/records/`
- **Structure**: `YYYY-MM/DD/[id]_[title].md`
- **Format**: YAML frontmatter + Markdown content
- **Benefits**:
  - Human-readable and editable
  - Version control friendly
  - Easy backup and sync
  - No database required
  - Portable across systems

Example file:
```
~/work-memo/records/2026-02/05/a1b2c3d4_urgent_meeting.md
```

## Notes

- This is a **record-only** system - no execution happens
- All data is stored as Markdown files (not database)
- Natural language parsing provides best results
- More contextetter automatic categorization
- URLs require internet connection
- The `/memo` command uses this skill automatically
- Records can be manually edited in any text editor
- Compatible with git for version control

## Scripts

- Main command: `skills/scripts/memo_command.py`
- Query parser: `skills/scripts/query_parser.py`
- Web scraper: `skills/scripts/web_scra`
- Reporting: `skills/scripts/reporting.py`
- Schema: `skills/scripts/schema.py`
