---
name: memo
description: Records work information with multi-dimensional tracking. Use when user wants to record work events, tasks, or activities without executing them.
---

# Memo Command

This command records work information using the work-memo skill's capabilities. It's designed for information recording only - no task execution.

## Usage

Run this command with your work information:
```
/memo 填写的信息
```

## Process

1. **Parse the input** to extract work details from natural language
2. **Identify dimensions** (type, urgency, importance, tags, contexts, dates)
3. **Record the information** using the work-memo storage system
4. **Return confirmation** with recorded details

## Implementation

When this command is triggered:

1. Parse the user's input to extract:
   - Title/description of the work
   - Type (task, meeting, call, email, review, coding, design, etc.)
   - Priority indicators (urgent, important)
   - Tags (#work, #urgent, #project)
   - Contexts (@office, @home, @phone)
   - Dates (today, tomorrow, this week, etc.)

2. Use the work-memo skill's `memo_command.py` script to record the information

3. Return a confirmation with:
   - Recorded title
   - Identified type
   - Priority levels
   - Eisenhower quadrant
   - Tags and contexts

## Examples

- `/memo 紧急会议今天 #work @office` → Records an urgent meeting for today
- `/memo 完成项目报告` → Records a task to complete a project report
- `/memo 修复登录bug #urgent` → Records an urgent bug fix task
- `/memo 团队例会 #meeting` → Records a team meeting
- `/memo 重要电话明天 @phone` → Records an important phone call for tomorrow

## Supported Features

### Natural Language Elements

- **Tags**: Use # followed by tag name (e.g., #work, #urgent, #project)
- **Contexts**: Use @ followed by context (e.g., @office, @home, @phone)
- **Priority**: Words like "urgent", "important", "紧急", "重要"
- **Dates**: "today", "tomorrow", "this week", "今天", "明天", "本周"

### Automatic Detection

The command automatically detects:
- **Work Type**: Based on keywords (meeting, call, bug, report, etc.)
- **Urgency Level**: 1-5 scale based on urgency indicators
- **Importance Level**: 1-5 scale based on importance indicators
- **Eisenhower Quadrant**: Q1-Q4 based on urgency/importance combination

## Output Format

The command returns a structured confirmation:

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
  "date": "2026-01-20"
}
```

## Notes

- This is a **record-only** command - no tasks are executed
- All information is stored in the work-memo database
- Use natural language for best results
- The more context you provide, the better the categorization