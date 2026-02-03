#!/usr/bin/env python3
"""PySpider爬虫下单 - 极简版本

功能：
1. 校验参数（Facebook URL格式）
2. 检查PySpider项目状态
3. 创建飞书记录
4. 发送PySpider任务
5. 更新飞书状态并发送通知
"""
import sys
import os
import uuid
from pathlib import Path

# 添加插件根目录到路径
PLUGIN_ROOT = Path(__file__).parent.parent
sys.path.insert(0, str(PLUGIN_ROOT))

from scripts.feishu_client import FeishuClient
from scripts.pyspider_dispatcher import PySpiderDispatcher
from scripts.check_project_status import check_project_status
from scripts.crawlers import get_crawler_info, list_crawlers, format_crawlers_for_display


def validate_facebook_url(url: str) -> bool:
    """Facebook URL必须以 https://www.facebook.com/ 开头"""
    return url.startswith('https://www.facebook.com/')


def create_order(media_type: str, keywords: list, task_user: str = None) -> dict:
    """
    创建爬虫订单
    
    Args:
        media_type: 媒体类型（如 "Reddit 关键词下的帖子"）
        keywords: 关键词列表
        task_user: 飞书用户ID
        
    Returns:
        dict: {'success': bool, 'message': str}
    """
    try:
        # 0. 环境变量检查（开发环境有默认值，可跳过）
        # 生产环境建议配置环境变量覆盖默认值
        # 生产环境必须配置的环境变量：MONGODB_URL, FEISHU_API_URL, PYSPIDER_BASE_URL
        debug_mode = os.getenv('MINTO_DEBUG', 'false').lower() == 'true'
        
        if debug_mode:
            print("[DEBUG] Running in debug mode (environment variable check skipped)")
        
        # 1. 获取爬虫配置
        crawler_info = get_crawler_info(media_type)
        if not crawler_info:
            # 爬虫不存在，显示可用列表
            available = format_crawlers_for_display()
            return {
                'success': False,
                'message': f'❌ 不支持的爬虫类型: {media_type}\\n\\n{available}'
            }
        
        project_name = crawler_info["project"]
        field_type = crawler_info["field"]
        
        # 2. 参数校验（仅Facebook Ads需要特殊校验）
        if "validation" in crawler_info and crawler_info["validation"]:
            for kw in keywords:
                if not validate_facebook_url(kw):
                    return {
                        'success': False,
                        'message': f'❌ Facebook URL格式错误: {kw}\\n必须以 https://www.facebook.com/ 开头'
                    }
        
        # 3. 检查项目状态
        status_info = check_project_status(project_name)
        
        if not status_info['exists']:
            return {
                'success': False,
                'message': f'❌ PySpider项目不存在: {project_name}'
            }
        
        if not status_info['can_run']:
            return {
                'success': False,
                'message': f'❌ PySpider项目状态异常: {status_info["status"]}\\n项目必须处于 RUNNING 或 DEBUG 状态'
            }
        
        # 4. 初始化客户端（环境变量已在客户端构造函数中验证）
        feishu = FeishuClient()
        dispatcher = PySpiderDispatcher()
        task_id = str(uuid.uuid4())
        
        # 5. 创建飞书记录
        print(f"[DEBUG] Creating Feishu record for {media_type}...")
        record_id = feishu.create_record(
            task=media_type,
            data=keywords,
            task_user=task_user or 'system',
            task_id=task_id
        )
        
        if not record_id:
            print(f"[DEBUG] Feishu record creation failed")
            return {
                'success': False,
                'message': '❌ 飞书记录创建失败，请联系爬虫工程师\n可能原因：飞书API异常、表格权限问题、字段配置错误'
            }
        
        # 6. 发送PySpider任务
        print(f"[DEBUG] Sending PySpider tasks for {len(keywords)} keywords...")
        success_count = 0
        
        for keyword in keywords:
            print(f"[DEBUG] Sending task for keyword: {keyword}...")
            try:
                if dispatcher.send_task(project_name, field_type, keyword):
                    success_count += 1
                    print(f"[DEBUG] ✓ Task sent successfully for: {keyword}")
                else:
                    print(f"[DEBUG] ✗ Task send failed for: {keyword}")
            except Exception as e:
                print(f"[DEBUG] Exception during task send: {e}")
        
        if success_count == 0:
            print(f"[DEBUG] All {len(keywords)} tasks failed, marking as manual processing")
            feishu.update_status(record_id, "等待手动处理")
            return {
                'success': False,
                'message': f'❌ PySpider任务发送失败（{success_count}/{len(keywords)} 成功）\n请联系爬虫工程师检查PySpider服务和网络连接'
            }
        
        # 7. 更新飞书状态为"抓取中"
        print(f"[DEBUG] Updating status to '抓取中'...")
        feishu.update_status(record_id, "抓取中")
        print(f"[DEBUG] Status updated successfully")
        
        # 8. 发送飞书通知
        print(f"[DEBUG] Sending Feishu notification...")
        feishu.send_notification(
            title="[Minto] 💣💣💣开始抓取💣💣💣",
            text=f"媒体:【{media_type}】\\n关键词: {keywords}\\n\\n通过 Minto 自动化插件下单",
            at_user=[task_user] if task_user else ['all']
        )
        
        return {
            'success': True,
            'message': f'✅ 下单成功！\\n任务ID: {task_id}\\n飞书记录ID: {record_id}\\n项目: {project_name}\\n成功发送 {success_count}/{len(keywords)} 个关键词'
        }
        
    except Exception as e:
        return {
            'success': False,
            'message': f'❌ 下单失败: {str(e)}'
        }


if __name__ == "__main__":
    # 测试
    result = create_order(
        media_type="Reddit 关键词下的帖子",
        keywords=["AI", "machine learning"],
        task_user="ou_test"
    )
    print(result['message'])
