#!/usr/bin/env python3
"""
Memo Command - 优化的工作备忘录命令

专注于记录信息，不执行具体任务。
使用自然语言快速记录工作事项。

Usage:
    python memo_command.py "紧急会议明天 #work @office"
    python memo_command.py "完成项目报告 --urgency 5 --importance 4"
"""

import sys
import argparse
import re
from pathlib import Path
from typing import Optional, List
from datetime import datetime, timedelta

# 添加 scripts 目录到路径
SCRIPT_DIR = Path(__file__).parent
sys.path.insert(0, str(SCRIPT_DIR))

from markdown_storage import MarkdownStorage
from ai_analyzer import AIAnalyzer
from schema import WorkRecord, WorkType, Status, Person
from query_parser import QueryParser


def record_memo(description: str, urgency: Optional[int] = None, importance: Optional[int] = None, type_str: Optional[str] = None, tags: Optional[list] = None) -> dict:
    """
    记录工作备忘录（不执行任务）

    Args:
        description: 工作描述
        urgency: 紧急程度 (1-5)
        importance: 重要程度 (1-5)
        type_str: 工作类型
        tags: 标签列表

    Returns:
        dict: 创建的记录信息
    """
    storage = MarkdownStorage()
    analyzer = AIAnalyzer()
    parser = QueryParser()

    # AI 分析
    ai_analysis = analyzer.analyze(description)

    # 解析自然语言描述
    parsed = parser.parse(description)

    # 从 AI 分析中提取信息
    extracted = ai_analysis.get("extracted_info", {})

    # 清理标题
    title = parsed.get('title', description)
    title = re.sub(r'#\w+', '', title)
    title = re.sub(r'@\w+', '', title)
    title = re.sub(r'project:\S+', '', title)
    title = title.strip()

    # 映射工作类型
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

    # 映射紧急度和重要度
    urgency_map = {"很低": 1, "低": 2, "中等": 3, "高": 4, "非常高": 5}
    importance_map = {"很低": 1, "低": 2, "中等": 3, "高": 4, "非常高": 5}

    # 创建记录
    record = WorkRecord(
        title=title,
        status=Status.TODO,  # 默认为待办状态，不执行
    )

    # 设置工作类型
    if type_str:
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
            'note': WorkType.OTHER,  # 备注类型
        }
        record.type = type_map.get(type_str.lower(), WorkType.OTHER)
    else:
        record.type = type_map.get(work_type_str, WorkType.TASK)

    # 设置优先级
    if urgency is not None:
        record.urgency = max(1, min(5, urgency))
    else:
        record.urgency = urgency_map.get(extracted.get('紧急程度', '中等'), 3)

    if importance is not None:
        record.importance = max(1, min(5, importance))
    else:
        record.importance = importance_map.get(extracted.get('重要程度', '中等'), 3)

    record.difficulty = 5  # 默认中等难度

    # 设置截止日期
    if 'due_date_end' in parsed:
        record.due_date = parsed['due_date_end']

    # 设置标签
    final_tags = []
    if tags:
        final_tags.extend(tags)
    if 'tags' in parsed:
        final_tags.extend(parsed['tags'])
    if final_tags:
        record.tags = list(set(final_tags))  # 去重

    # 设置上下文
    if 'contexts' in parsed:
        record.contexts = parsed['contexts']

    # 保存到数据库（仅记录，不执行），包含 AI 分析
    record_id = storage.create(record, original_input=description, ai_analysis=ai_analysis)

    # 返回记录信息
    result = {
        'id': record.id,
        'title': record.title,
        'type': record.type.value,
        'status': record.status.value,
        'urgency': record.urgency,
        'importance': record.importance,
        'difficulty': record.difficulty,
        'due_date': record.due_date,
        'tags': record.tags,
        'contexts': record.contexts,
        'eisenhower': record.get_eisenhower_quadrant(),
        'created_at': record.created_at,
    }

    storage.close()
    return result


def search_memos(query: str, limit: int = 10) -> list:
    """
    搜索工作备忘录

    Args:
        query: 搜索查询
        limit: 返回结果数量限制

    Returns:
        list: 匹配的记录列表
    """
    storage = MarkdownStorage()
    parser = QueryParser()

    filters = parser.parse(query)
    results = storage.search(filters)[:limit]

    # 格式化结果
    formatted_results = []
    for record in results:
        formatted_results.append({
            'id': record.id,
            'title': record.title,
            'type': record.type.value,
            'status': record.status.value,
            'urgency': record.urgency,
            'importance': record.importance,
            'due_date': record.due_date,
            'tags': record.tags,
            'contexts': record.contexts,
            'eisenhower': record.get_eisenhower_quadrant(),
            'created_at': record.created_at,
        })

    return formatted_results


def list_memos(quadrant: Optional[str] = None, status: Optional[str] = None, limit: int = 20) -> list:
    """
    列出工作备忘录

    Args:
        quadrant: Eisenhower 象限过滤 (Q1/Q2/Q3/Q4)
        status: 状态过滤
        limit: 返回结果数量限制

    Returns:
        list: 记录列表
    """
    storage = MarkdownStorage()

    if quadrant:
        records = storage.get_by_quadrant(quadrant.upper())
    else:
        records = storage.get_all()

    # 状态过滤
    if status:
        records = [r for r in records if r.status.value == status]

    # 限制数量
    records = records[:limit]

    # 格式化结果
    formatted_results = []
    for record in records:
        formatted_results.append({
            'id': record.id,
            'title': record.title,
            'type': record.type.value,
            'status': record.status.value,
            'urgency': record.urgency,
            'importance': record.importance,
            'due_date': record.due_date,
            'tags': record.tags,
            'contexts': record.contexts,
            'eisenhower': record.get_eisenhower_quadrant(),
            'created_at': record.created_at,
        })

    return formatted_results


def print_record(record: dict):
    """格式化打印记录"""
    print(f"📝 已记录: {record['id']}")
    print(f"   标题: {record['title']}")
    print(f"   类型: {record['type']}")
    print(f"   状态: {record['status']}")
    print(f"   优先级: 紧急度 {record['urgency']}/5, 重要度 {record['importance']}/5")
    if record['due_date']:
        print(f"   截止: {record['due_date']}")
    if record['tags']:
        print(f"   标签: {', '.join(record['tags'])}")
    if record['contexts']:
        print(f"   上下文: {', '.join(record['contexts'])}")
    if record.get('projects'):
        print(f"   项目: {', '.join(record['projects'])}")
    print(f"   Eisenhower: {record['eisenhower']}")
    print(f"   创建时间: {record['created_at']}")


def print_results(results: list):
    """格式化打印搜索结果"""
    if not results:
        print("没有找到记录")
        return

    print(f"找到 {len(results)} 条记录:\n")
    for i, record in enumerate(results, 1):
        urgency_str = f"[U{record['urgency']}]" if record['urgency'] >= 4 else ""
        importance_str = f"[I{record['importance']}]" if record['importance'] >= 4 else ""
        print(f"{i}. {record['title']} {urgency_str}{importance_str} [{record['eisenhower']}]")
        print(f"   类型: {record['type']}, 状态: {record['status']}")
        if record['due_date']:
            print(f"   截止: {record['due_date']}")
        if record['tags']:
            print(f"   标签: {', '.join(record['tags'])}")
        print()


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="工作备忘录命令 - 记录信息，不执行任务",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 记录工作（自然语言）
  python memo_command.py "紧急会议明天 #work @office"
  python memo_command.py "完成项目报告"

  # 记录工作（带参数）
  python memo_command.py "修复登录bug" --urgency 5 --importance 4 --type bugfix
  python memo_command.py "团队例会" --type meeting --tags work

  # 搜索记录
  python memo_command.py --search "紧急"
  python memo_command.py --search "#work"

  # 列出记录
  python memo_command.py --list
  python memo_command.py --list --quadrant Q1
  python memo_command.py --list --status todo
        """
    )

    # 记录命令
    parser.add_argument(
        'description',
        nargs='?',
        help='工作描述（自然语言）'
    )
    parser.add_argument(
        '--urgency',
        type=int,
        choices=range(1, 6),
        help='紧急程度 (1-5, 5=最紧急)'
    )
    parser.add_argument(
        '--importance',
        type=int,
        choices=range(1, 6),
        help='重要程度 (1-5, 5=最重要)'
    )
    parser.add_argument(
        '--type',
        type=str,
        help='工作类型 (task/meeting/call/email/review/coding/design/writing/research/planning/documentation/bugfix/feature/note)'
    )
    parser.add_argument(
        '--tags',
        nargs='+',
        help='标签列表'
    )

    # 搜索命令
    parser.add_argument(
        '--search',
        type=str,
        help='搜索记录'
    )

    # 列出命令
    parser.add_argument(
        '--list',
        action='store_true',
        help='列出所有记录'
    )
    parser.add_argument(
        '--quadrant',
        type=str,
        choices=['Q1', 'Q2', 'Q3', 'Q4'],
        help='按 Eisenhower 象限过滤'
    )
    parser.add_argument(
        '--status',
        type=str,
        help='按状态过滤'
    )

    args = parser.parse_args()

    # 执行相应命令
    if args.search:
        # 搜索记录
        results = search_memos(args.search)
        print_results(results)
    elif args.list:
        # 列出记录
        results = list_memos(quadrant=args.quadrant, status=args.status)
        print_results(results)
    elif args.description:
        # 记录工作
        result = record_memo(
            description=args.description,
            urgency=args.urgency,
            importance=args.importance,
            type_str=args.type,
            tags=args.tags,
        )
        print_record(result)
        print("\n✅ 已记录（不执行任务）")
    else:
        # 显示帮助
        parser.print_help()


if __name__ == '__main__':
    main()
