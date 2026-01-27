"""Command-line interface for Work Memo skill."""

import argparse
import sys
from typing import Dict, Any, Optional

sys.path.insert(0, __file__)

from markdown_storage import MarkdownStorage
from ai_analyzer import AIAnalyzer
from schema import WorkRecord, WorkType, Status, Person, Location
from query_parser import QueryParser
from reporting import Reporting


def cmd_add(args) -> None:
    """Add new work record"""
    storage = MarkdownStorage()
    analyzer = AIAnalyzer()

    parser = QueryParser()

    title = args.title or input("Title: ")

    work_type = WorkType.TASK
    if args.type:
        type_map = {
            'task': WorkType.TASK,
            'meeting': WorkType.MEETING,
            'call': WorkType.CALL,
            'email': WorkType.EMAIL,
            'review': WorkType.REVIEW,
            'coding': WorkType.CODING,
            'design': WorkType.DESIGN,
            'writing': WorkType.WRITING,
            'research': WorkType.RESEARCH,
            'planning': WorkType.PLANNING,
            'documentation': WorkType.DOCUMENTATION,
            'bugfix': WorkType.BUGFIX,
            'feature': WorkType.FEATURE,
        }
        work_type = type_map.get(args.type.lower(), WorkType.TASK)

    urgency = args.urgency or int(input("Urgency (1-5) [default: 3]: ") or 3)
    urgency = max(1, min(5, urgency))

    importance_val = args.importance or int(input("Importance (1-5) [default: 3]: ") or 3)
    importance = max(1, min(5, importance_val))

    difficulty_val = args.difficulty or int(input("Difficulty (1-10) [default: 5]: ") or 5)
    difficulty = max(1, min(10, difficulty_val))

    record = WorkRecord(
        title=title,
        type=work_type,
        status=Status.TODO,
        urgency=urgency,
        importance=importance_val,
        difficulty=difficulty_val,
    )

    if args.description:
        record.description = input("Description: ")

    if args.assignee:
        record.assignee = Person(name=args.assignee)

    if args.due_date:
        record.due_date = args.due_date

    if args.tags:
        record.tags = args.tags

    storage.create(record)
    print(f"✓ Created record: {record.id}")
    print(f"  Title: {record.title}")
    print(f"  Type: {record.type.value}")
    print(f"  Urgency: {record.urgency}, Importance: {record.importance}")
    print(f"  Difficulty: {record.difficulty}")
    if record.due_date:
        print(f"  Due: {record.due_date}")


def cmd_memo(args) -> None:
    """Quick add using natural language description with AI analysis"""
    storage = MarkdownStorage()
    analyzer = AIAnalyzer()
    parser = QueryParser()

    description = args.description

    # AI Analysis
    print(f"\n🤖 Analyzing: '{description}'")
    ai_analysis = analyzer.analyze(description)

    # Parse with query parser for structured data
    parsed = parser.parse(description)

    # Extract information from AI analysis
    extracted = ai_analysis.get("extracted_info", {})

    # Determine title
    title = parsed.get('title', description)
    # Clean up title by removing tags and contexts
    import re
    title = re.sub(r'#\w+', '', title)
    title = re.sub(r'@\w+', '', title)
    title = re.sub(r'project:\S+', '', title)
    title = title.strip()

    print(f"  Title: {title}")
    if '工作类型' in extracted:
        print(f"  Type: {extracted['工作类型']}")
    if '紧急程度' in extracted:
        print(f"  Urgency: {extracted['紧急程度']}")
    if '重要程度' in extracted:
        print(f"  Importance: {extracted['重要程度']}")
    if '建议优先级' in extracted:
        print(f"  Priority: {extracted['建议优先级']}")

    # Map work type
    type_map = {
        '任务': WorkType.TASK,
        '会议': WorkType.MEETING,
        '电话': WorkType.CALL,
        '邮件': WorkType.EMAIL,
        '审查/评审': WorkType.REVIEW,
        '编码': WorkType.CODING,
        '设计': WorkType.DESIGN,
        '写作': WorkType.WRITING,
        '研究': WorkType.RESEARCH,
        '规划': WorkType.PLANNING,
        'Bug修复': WorkType.BUGFIX,
        '新功能': WorkType.FEATURE,
    }
    work_type_str = extracted.get('工作类型', '任务')
    work_type = type_map.get(work_type_str, WorkType.TASK)

    # Map urgency text to number
    urgency_map = {
        "很低": 1, "低": 2, "中等": 3, "高": 4, "非常高": 5
    }
    urgency = urgency_map.get(extracted.get('紧急程度', '中等'), 3)

    # Map importance text to number
    importance_map = {
        "很低": 1, "低": 2, "中等": 3, "高": 4, "非常高": 5
    }
    importance = importance_map.get(extracted.get('重要程度', '中等'), 3)

    # Create record
    record = WorkRecord(
        title=title,
        type=work_type,
        status=Status.TODO,
        urgency=urgency,
        importance=importance,
        difficulty=5,
    )

    # Set tags, contexts, and projects from parsed
    if 'tags' in parsed:
        record.tags = parsed['tags']
    if 'contexts' in parsed:
        record.contexts = parsed['contexts']
    if 'projects' in parsed:
        record.projects = parsed['projects']

    # Set due date from AI analysis or parsed
    if 'due_date_end' in parsed:
        record.due_date = parsed['due_date_end']

    # Interactive mode for missing fields
    if args.interactive:
        try:
            user_urgency = input(f"Urgency (1-5) [current: {record.urgency}]: ") or ""
            if user_urgency:
                record.urgency = max(1, min(5, int(user_urgency)))
        except (EOFError, KeyboardInterrupt):
            pass

        try:
            user_importance = input(f"Importance (1-5) [current: {record.importance}]: ") or ""
            if user_importance:
                record.importance = max(1, min(5, int(user_importance)))
        except (EOFError, KeyboardInterrupt):
            pass

        try:
            user_desc = input(f"Description [optional]: ") or ""
            if user_desc.strip():
                record.description = user_desc
        except (EOFError, KeyboardInterrupt):
            pass

        try:
            assignee_name = input(f"Assignee [optional]: ") or ""
            if assignee_name.strip():
                record.assignee = Person(name=assignee_name)
        except (EOFError, KeyboardInterrupt):
            pass

    # Create record with AI analysis
    record_id = storage.create(record, original_input=description, ai_analysis=ai_analysis)

    print(f"\n✅ Created memo: {record_id}")
    print(f"   Title: {record.title}")
    print(f"   Type: {record.type.value}")
    print(f"   Status: {record.status.value}")
    print(f"   Urgency: {record.urgency}/5, Importance: {record.importance}/5")
    print(f"   Eisenhower: {record.get_eisenhower_quadrant()}")
    print(f"   Priority Score: {record.get_priority_score():.2f}")
    if record.due_date:
        print(f"   Due: {record.due_date}")
    if record.tags:
        print(f"   Tags: {', '.join(record.tags)}")
    if record.contexts:
        print(f"   Contexts: {', '.join(record.contexts)}")
    if record.projects:
        print(f"   Projects: {', '.join(record.projects)}")

    # Show AI suggestions
    if ai_analysis.get("suggestions"):
        print(f"\n💡 AI Suggestions:")
        for suggestion in ai_analysis["suggestions"][:2]:
            print(f"   • {suggestion['title']}: {suggestion['content']}")


def cmd_search(args) -> None:
    """Search work records"""
    storage = MarkdownStorage()
    parser = QueryParser()

    query = args.query if args.query else input("Search query: ")
    filters = parser.parse(query)

    results = storage.search(filters)

    if not results:
        print("No matching records found")
        return

    print(f"Found {len(results)} matching record(s):\n")

    for i, record in enumerate(results, 1):
        urgency_str = f"[U{record.urgency}]" if record.urgency >= 4 else ""
        importance_str = f"[I{record.importance}]" if record.importance >= 4 else ""

        print(f"{i}. {record.title} {urgency_str}{importance_str}")
        print(f"   Type: {record.type.value}, Status: {record.status.value}")
        if record.due_date:
            print(f"   Due: {record.due_date}")
        if record.tags:
            print(f"   Tags: {', '.join(record.tags)}")
        print()


def cmd_list(args) -> None:
    """List all work records"""
    storage = MarkdownStorage()

    records = storage.get_all()

    if not records:
        print("No records found")
        return

    if args.quadrant:
        quadrant = args.quadrant.upper()
        records = storage.get_by_quadrant(quadrant)
        print(f"=== Eisenhower Quadrant {quadrant} ({len(records)} records) ===")
    else:
        print(f"=== All Records ({len(records)}) ===")

    for i, record in enumerate(records, 1):
        urgency_str = f"[U{record.urgency}]" if record.urgency >= 4 else ""
        importance_str = f"[I{record.importance}]" if record.importance >= 4 else ""
        quadrant_str = f" [{record.get_eisenhower_quadrant()}]"

        print(f"{i}. {record.title} {urgency_str}{importance_str}{quadrant_str}")
        print(f"   Type: {record.type.value}, Status: {record.status.value}")
        if record.due_date:
            print(f"   Due: {record.due_date}")
        if record.tags:
            print(f"   Tags: {', '.join(record.tags)}")
        print()


def cmd_report(args) -> None:
    """Generate reports"""
    storage = MarkdownStorage()
    reporting = Reporting(storage)

    if args.daily:
        report = reporting.get_daily_report(args.daily)
        print(reporting.format_daily_report(report))
    elif args.weekly:
        report = reporting.get_weekly_report()
        print(reporting.format_weekly_report(report))
    elif args.monthly:
        report = reporting.get_monthly_report()
        print(reporting.format_monthly_report(report))
    else:
        print("Please specify --daily, --weekly, or --monthly")


def cmd_suggest(args) -> None:
    """Get work recommendations"""
    storage = MarkdownStorage()

    records = storage.get_all()

    pending = [r for r in records if r.status.value != 'done']

    if not pending:
        print("No pending tasks to suggest")
        return

    for record in pending:
        score = record.get_priority_score()

    sorted_records = sorted(pending, key=lambda r: r.get_priority_score(), reverse=True)

    print(f"=== Work Recommendations (Top {args.limit or 10}) ===\n")

    for i, record in enumerate(sorted_records[:args.limit or 10], 1):
        score = record.get_priority_score()
        quadrant = record.get_eisenhower_quadrant()

        urgency_str = f"[U{record.urgency}]" if record.urgency >= 4 else ""
        importance_str = f"[I{record.importance}]" if record.importance >= 4 else ""

        print(f"{i}. {record.title} {urgency_str}{importance_str} [{quadrant}]")
        print(f"   Priority Score: {score:.2f}, Difficulty: {record.difficulty}")
        if record.due_date:
            print(f"   Due: {record.due_date}")
        if record.tags:
            print(f"   Tags: {', '.join(record.tags)}")
        print()


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description="Work Memo: Personal work record management system",
        formatter_class=argparse.RawDescriptionHelpFormatter
    )

    subparsers = parser.add_subparsers(dest='command', help='Available commands')

    parser_add = subparsers.add_parser('add', help='Add new work record')
    parser_add.add_argument('title', help='Work title')
    parser_add.add_argument('--type', help='Work type (task, meeting, call, etc.)')
    parser_add.add_argument('--urgency', type=int, help='Urgency level (1-5)')
    parser_add.add_argument('--importance', type=int, help='Importance level (1-5)')
    parser_add.add_argument('--difficulty', type=int, help='Difficulty level (1-10)')
    parser_add.add_argument('--description', help='Detailed description')
    parser_add.add_argument('--assignee', help='Person assigned to')
    parser_add.add_argument('--due-date', help='Due date (ISO 8601 format)')
    parser_add.add_argument('--tags', nargs='+', help='Tags')

    parser_memo = subparsers.add_parser('memo', help='Quick add using natural language description')
    parser_memo.add_argument('description', help='Natural language work description')
    parser_memo.add_argument('--interactive', action='store_true', help='Interactive mode for missing fields')

    parser_search = subparsers.add_parser('search', help='Search work records')
    parser_search.add_argument('query', help='Natural language search query')

    parser_list = subparsers.add_parser('list', help='List all records')
    parser_list.add_argument('--quadrant', help='Filter by Eisenhower quadrant (Q1-Q4)')

    parser_report = subparsers.add_parser('report', help='Generate reports')
    parser_report.add_argument('--daily', help='Daily report')
    parser_report.add_argument('--weekly', action='store_true', help='Weekly report')
    parser_report.add_argument('--monthly', action='store_true', help='Monthly report')

    parser_suggest = subparsers.add_parser('suggest', help='Get work recommendations')
    parser_suggest.add_argument('--limit', type=int, default=10, help='Number of suggestions')

    args = parser.parse_args()

    if args.command == 'add':
        cmd_add(args)
    elif args.command == 'memo':
        cmd_memo(args)
    elif args.command == 'search':
        cmd_search(args)
    elif args.command == 'list':
        cmd_list(args)
    elif args.command == 'report':
        cmd_report(args)
    elif args.command == 'suggest':
        cmd_suggest(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
