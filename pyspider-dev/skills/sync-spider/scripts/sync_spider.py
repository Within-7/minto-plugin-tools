#!/usr/bin/env python3
"""
同步 PySpider 脚本到代码仓库

用法:
    python sync_spider.py --project_name "ScrapingAmazonList" --script_content "..."
    python sync_spider.py --project_name "ScrapingAmazonList" --script_content "..." --commit_message "fix: 修复bug"
"""

import argparse
import os
import subprocess
import sys
from datetime import datetime


# 配置
SPIDERS_X_PATH = "/Users/mac/Desktop/spiders-x"


def run_command(cmd, cwd=None):
    """执行命令并返回结果"""
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=cwd or SPIDERS_X_PATH,
            capture_output=True,
            text=True
        )
        return result.returncode == 0, result.stdout, result.stderr
    except Exception as e:
        return False, "", str(e)


def sync_spider(project_name, script_content, commit_message=None):
    """
    同步脚本到代码仓库
    
    Args:
        project_name: 项目名
        script_content: 脚本内容
        commit_message: 自定义 commit 信息
    
    Returns:
        (success, message)
    """
    # 1. 检查目录是否是 git 仓库
    success, _, _ = run_command("git rev-parse --git-dir")
    if not success:
        return False, f"错误: {SPIDERS_X_PATH} 不是 git 仓库"
    
    # 2. 写入文件
    file_path = os.path.join(SPIDERS_X_PATH, f"{project_name}.py")
    is_new = not os.path.exists(file_path)
    
    try:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(script_content)
    except Exception as e:
        return False, f"写入文件失败: {e}"
    
    # 3. git add
    success, stdout, stderr = run_command(f'git add "{project_name}.py"')
    if not success:
        return False, f"git add 失败: {stderr}"
    
    # 4. 生成 commit 信息
    if not commit_message:
        action = "新增" if is_new else "更新"
        commit_message = f"feat: {action}爬虫脚本 {project_name}"
    
    # 5. git commit
    success, stdout, stderr = run_command(f'git commit -m "{commit_message}"')
    if not success:
        # 可能是没有变更
        if "nothing to commit" in stdout or "nothing to commit" in stderr:
            return True, f"文件无变更: {project_name}"
        return False, f"git commit 失败: {stderr}"
    
    # 6. git push
    success, stdout, stderr = run_command("git push")
    if not success:
        return False, f"git push 失败: {stderr}"
    
    action = "新增" if is_new else "更新"
    return True, f"成功{action}: {project_name}"


def main():
    parser = argparse.ArgumentParser(description='同步 PySpider 脚本到代码仓库')
    parser.add_argument('--project_name', required=True, help='项目名')
    parser.add_argument('--script_content', required=True, help='脚本内容')
    parser.add_argument('--commit_message', help='自定义 commit 信息')
    
    args = parser.parse_args()
    
    success, message = sync_spider(
        args.project_name,
        args.script_content,
        args.commit_message
    )
    
    if success:
        print(f"✅ {message}")
        sys.exit(0)
    else:
        print(f"❌ {message}")
        sys.exit(1)


if __name__ == "__main__":
    main()
