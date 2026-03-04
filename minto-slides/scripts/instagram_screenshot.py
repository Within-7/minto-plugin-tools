#!/usr/bin/env python3
"""
Instagram KOL 截图工具
流程：打开#tag页面 → 用户点击用户 → 截图用户主页
"""

import sys
import os
import time
import subprocess
import re
from pathlib import Path

OUTPUT_DIR = Path("/Users/mac/Desktop/HTML/output")
TEMPLATE_HTML = OUTPUT_DIR / "slide25_user_profile.html"

KEYWORD_MAPPING = {
    "水上活动": "watersports",
    "自然探索": "naturelover",
    "极端探险": "extremesports",
    "长途旅行": "traveler",
    "家庭旅行": "familytravel",
}

def get_tag(keyword):
    for k, v in KEYWORD_MAPPING.items():
        if k in keyword: return v
    return keyword.lower()

def run_as(script):
    r = subprocess.run(['osascript', '-e', script], capture_output=True, text=True)
    return r.stdout.strip(), r.returncode

def main(keyword):
    print(f"\n{'='*40}")
    print(f"Instagram截图: {keyword}")
    print(f"{'='*40}\n")

    tag = get_tag(keyword)
    OUTPUT_DIR.mkdir(exist_ok=True)
    safe_name = re.sub(r'[^\w]', '', keyword)
    screenshot_path = OUTPUT_DIR / f"instagram_{safe_name}.png"

    # 1. 激活Edge并打开tag页面
    print(f"[1/3] 打开 #{tag} ...")
    run_as(f'''
    tell application "Microsoft Edge"
        activate
        open location "https://www.instagram.com/explore/tags/{tag}/"
    end tell
    ''')
    time.sleep(4)

    # 2. 等待用户点击
    print(f"\n[2/3] 请在浏览器中点击一个用户进入TA的主页！")
    print("等待9秒...")
    for i in range(9, 0, -1):
        print(f"  {i}秒...", end='\r')
        time.sleep(1)
    print()

    # 3. 截图 - 交互式选择窗口
    print(f"\n[3/3] 请点击Edge浏览器窗口进行截图...")
    subprocess.run(f"screencapture -w '{screenshot_path}'", shell=True)
    print(f"✅ 截图保存: {screenshot_path}")

    # 更新HTML
    if TEMPLATE_HTML.exists():
        c = TEMPLATE_HTML.read_text()
        # 查找并替换图片src
        new_c = re.sub(r'src="instagram_[^"]+\.png"', f'src="{screenshot_path.name}"', c)
        if new_c != c:
            TEMPLATE_HTML.write_text(new_c)
            print("✅ HTML已更新")

    print(f"\n完成！打开 {TEMPLATE_HTML} 查看效果")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法: python3 instagram_screenshot.py '关键词'")
        sys.exit(1)
    main(sys.argv[1])
