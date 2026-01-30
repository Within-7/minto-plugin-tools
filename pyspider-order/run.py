#!/usr/bin/env python3
"""
统一的命令行入口 - 处理路径问题，提供便捷的命令行接口

Usage:
    python run.py list                    # 列出所有爬虫
    python run.py validate <媒体类型> <关键词>    # 校验参数
    python run.py order <媒体类型> <关键词> [用户ID]  # 创建订单
"""
import sys
from pathlib import Path

# 自动定位插件根目录
PLUGIN_ROOT = Path(__file__).parent
sys.path.insert(0, str(PLUGIN_ROOT))


def cmd_list():
    """列出所有可用的爬虫"""
    from scripts.list_all_crawlers import list_all_crawlers, format_crawlers_for_display

    categories = list_all_crawlers()
    print(format_crawlers_for_display(categories))


def cmd_validate(media_type, keywords):
    """校验爬虫参数"""
    from scripts.validate_params import validate_crawl_params, ValidationError

    try:
        result = validate_crawl_params(media_type, keywords)
        print("✅ 参数校验通过")
        print(f"   媒体类型: {result['media_type']}")
        print(f"   PySpider项目: {result['project']}")
        print(f"   字段类型: {result['field']}")
        print(f"   关键词: {result['keywords']}")
        return True
    except ValidationError as e:
        print(f"❌ 参数校验失败: {e}")
        return False


def cmd_order(media_type, keywords, task_user=None):
    """创建爬虫订单"""
    from scripts.create_crawl_order import create_crawl_order, format_order_result

    result = create_crawl_order(media_type, keywords, task_user)
    print(format_order_result(result))
    return result['success']


def main():
    """主函数"""
    if len(sys.argv) < 2:
        print("PySpider爬虫下单工具")
        print("\nUsage:")
        print("  python run.py list                              列出所有爬虫")
        print("  python run.py validate <媒体类型> <关键词>       校验参数")
        print("  python run.py order <媒体类型> <关键词> [用户ID]  创建订单")
        print("\nExamples:")
        print("  python run.py list")
        print("  python run.py validate 'Reddit 关键词下的帖子' 'AI'")
        print("  python run.py order 'Reddit 关键词下的帖子' 'AI' 'ou_xxx'")
        return 0

    command = sys.argv[1]

    if command == "list":
        cmd_list()
    elif command == "validate":
        if len(sys.argv) < 4:
            print("❌ 用法: python run.py validate <媒体类型> <关键词>")
            return 1
        cmd_validate(sys.argv[2], sys.argv[3])
    elif command == "order":
        if len(sys.argv) < 4:
            print("❌ 用法: python run.py order <媒体类型> <关键词> [用户ID]")
            return 1
        task_user = sys.argv[4] if len(sys.argv) > 4 else None
        success = cmd_order(sys.argv[2], sys.argv[3], task_user)
        return 0 if success else 1
    else:
        print(f"❌ 未知命令: {command}")
        print("可用命令: list, validate, order")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
