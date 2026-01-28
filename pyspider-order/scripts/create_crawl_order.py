"""完整的爬虫下单流程脚本"""
import sys
import os
import uuid
from pathlib import Path

# 自动定位插件根目录（向上两级）
PLUGIN_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PLUGIN_ROOT))

from scripts.feishu_client import FeishuClient
from scripts.pyspider_dispatcher import PySpiderDispatcher
from scripts.validate_params import validate_crawl_params, ValidationError
from scripts.check_project_status import check_project_status


class OrderError(Exception):
    """下单失败异常"""
    pass


def create_crawl_order(media_type, keywords, task_user=None, charge_user=None, dry_run=False):
    """
    创建爬虫订单（完整流程）
    
    Args:
        media_type: 媒体类型（如 "Reddit 关键词下的帖子"）
        keywords: 关键词或关键词列表
        task_user: 下单用户ID（默认使用系统用户）
        charge_user: 负责人用户ID（默认使用task_user）
        dry_run: 是否为演练模式（只校验不执行）
        
    Returns:
        dict: {
            'success': bool,
            'record_id': str,
            'task_id': str,
            'project': str,
            'validated_params': dict,
            'error': str
        }
    """
    result = {
        'success': False,
        'record_id': None,
        'task_id': None,
        'project': None,
        'validated_params': None,
        'error': None
    }
    
    try:
        # 步骤1: 参数校验
        validated = validate_crawl_params(media_type, keywords)
        result['validated_params'] = validated
        result['project'] = validated['project']
        
        if dry_run:
            print("✅ 演练模式：参数校验通过")
            print(f"   媒体: {validated['media_type']}")
            print(f"   项目: {validated['project']}")
            print(f"   字段: {validated['field']}")
            print(f"   关键词: {validated['keywords']}")
            result['success'] = True
            return result

        # 步骤2: 检查PySpider项目状态
        print(f"检查项目状态: {validated['project']}")
        status_info = check_project_status(validated['project'])
        
        if not status_info['exists']:
            raise OrderError(
                f"❌ PySpider项目不存在: {validated['project']}\n"
                f"请联系爬虫工程师确认项目配置"
            )
        
        if not status_info['can_run']:
            raise OrderError(
                f"❌ PySpider项目状态异常: {validated['project']}\n"
                f"当前状态: {status_info['status']}\n"
                f"项目必须处于 RUNNING 或 DEBUG 状态才能执行\n"
                f"请联系爬虫工程师处理"
            )
        
        print(f"✓ 项目状态正常: {status_info['status']}")
        
        # 步骤3: 初始化客户端
        feishu = FeishuClient()
        dispatcher = PySpiderDispatcher()
        
        # 用户参数处理（不再设置默认值）
        if not task_user:
            print("⚠️ 未提供task_user，将使用飞书系统默认值")
        task_user = task_user  # 可以是None
        charge_user = charge_user or task_user
        task_id = str(uuid.uuid4())
        result['task_id'] = task_id
        
        # 步骤4: 创建飞书记录
        print(f"创建飞书记录...")
        record_id = feishu.create_record(
            task=validated['media_type'],
            data=validated['keywords'],
            task_user=task_user,
            task_id=task_id,
            charge_user=charge_user
        )

        if not record_id:
            print(f"⚠️ 飞书记录创建失败")
            result['record_id'] = None
            result['success'] = False
            result['error'] = "飞书记录创建失败"
            return result

        result['record_id'] = record_id
        print(f"✓ 飞书记录创建成功: {record_id}")

        # 步骤5: 发送PySpider任务
        print(f"发送PySpider爬虫任务...")
        field_type = validated['field']
        
        try:
            # 每个关键词发送一次
            for keyword in validated['keywords']:
                success = dispatcher.send_task(
                    project=validated['project'],
                    key=field_type,
                    keyword=keyword
                )
                
                if not success:
                    raise OrderError(
                        f"PySpider任务发送失败\n"
                        f"项目: {validated['project']}\n"
                        f"字段: {field_type}\n"
                        f"关键词: {keyword}"
                    )
                
                print(f"✓ 任务已发送: {keyword}")
            
            # 步骤6: 更新飞书状态为"抓取中"
            print(f"更新飞书状态为'抓取中'...")
            feishu.update_status(record_id, "抓取中")
            print(f"✓ 状态已更新")
            
            # 步骤7: 发送飞书通知
            print(f"发送飞书群通知...")
            feishu.send_notification(
                title="💣💣💣开始抓取💣💣💣",
                text=f"准备抓取媒体:【{validated['media_type']}】 关键词:{validated['keywords']}",
                at_user=[task_user] if task_user else []
            )
            print(f"✓ 通知已发送")
            
            result['success'] = True
            return result
            
        except OrderError as task_error:
            # 任务发送失败，更新状态为"等待手动处理"
            print(f"⚠️ {task_error}")
            print(f"更新飞书状态为'等待手动处理'...")
            feishu.update_status(record_id, "等待手动处理")
            print(f"✓ 状态已更新")
            
            # 发送失败通知给爬虫工程师
            print(f"发送失败通知给爬虫工程师...")
            feishu.send_notification(
                title="🆘🆘🆘爬虫任务发送失败🆘🆘🆘",
                text=f"任务发送失败，需要手动处理\n\n"
                     f"项目: {validated['project']}\n"
                     f"媒体类型: {validated['media_type']}\n"
                     f"关键词: {validated['keywords']}\n"
                     f"飞书记录ID: {record_id}\n"
                     f"错误: {str(task_error)}",
                at_user=["ou_a45583a7f2843869b71ff4cc9692cf3d"]  # 爬虫工程师
            )
            print(f"✓ 失败通知已发送")
            
            result['error'] = str(task_error)
            result['success'] = False
            return result

    except ValidationError as e:
        result['error'] = str(e)
        return result
    
    except Exception as e:
        result['error'] = f"未知错误: {str(e)}"
        return result


def format_order_result(result):
    """格式化下单结果"""
    if result['success']:
        lines = [
            "✅ 下单成功！",
            f"",
            f"任务ID: {result['task_id']}",
            f"飞书记录ID: {result['record_id']}",
            f"项目: {result['project']}",
            f"",
            f"爬虫正在运行中，请稍后查询进度"
        ]
        return "\n".join(lines)
    else:
        lines = [
            "❌ 下单失败",
            f"",
            f"错误: {result['error']}",
            f"",
            f"请联系爬虫工程师处理"
        ]
        return "\n".join(lines)


if __name__ == "__main__":
    # 测试
    print("=" * 60)
    print("测试1: 正常下单（演练模式）")
    print("=" * 60)
    result = create_crawl_order(
        media_type="Reddit 关键词下的帖子",
        keywords="AI",
        dry_run=True
    )
    print(format_order_result(result))
    
    print("\n" + "=" * 60)
    print("测试2: 参数校验失败")
    print("=" * 60)
    result = create_crawl_order(
        media_type="不存在的媒体",
        keywords="test"
    )
    print(format_order_result(result))
