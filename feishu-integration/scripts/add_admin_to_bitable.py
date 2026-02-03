#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import requests
import json

APP_ID = "cli_a9e4652af5f89cca"
APP_SECRET = "4OazKFCmZTT4cjlwK0ecAhr3eAaJ7dhH"
APP_TOKEN = "OJYHb0j3ba2ACDs5HjBc9ERRnPb"
YOUR_USER_ID = "ou_31ec8c3772b60ed46d16ed23e4eda331"

def get_token():
    url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    payload = {
        "app_id": APP_ID,
        "app_secret": APP_SECRET
    }
    resp = requests.post(url, json=payload)
    data = resp.json()
    if data.get("code") == 0:
        return data.get("tenant_access_token")
    else:
        print(f"获取token失败: {data}")
        return None

def enable_advanced_permission(token):
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "app": {
            "app_settings": {
                "enable_advanced_permissions": True
            }
        }
    }
    resp = requests.put(url, headers=headers, json=payload)
    print(f"\n1. 开启高级权限:")
    print(f"状态码: {resp.status_code}")
    print(f"响应: {resp.json()}")
    return resp.json().get("code") == 0

def create_admin_role(token):
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/roles"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "role_name": "管理员",
        "description": "完全管理权限"
    }
    resp = requests.post(url, headers=headers, json=payload)
    print(f"\n2. 创建管理员角色:")
    print(f"状态码: {resp.status_code}")
    data = resp.json()
    print(f"响应: {json.dumps(data, ensure_ascii=False, indent=2)}")
    
    if data.get("code") == 0:
        role_id = data.get("data", {}).get("role", {}).get("role_id")
        print(f"✅ 角色创建成功，role_id: {role_id}")
        return role_id
    else:
        print(f"❌ 角色创建失败")
        return None

def add_user_to_role(token, role_id, user_id):
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{APP_TOKEN}/roles/{role_id}/members"
    headers = {
        "Authorization": f"Bearer {token}",
        "Content-Type": "application/json"
    }
    payload = {
        "member_type": "user",
        "member_id": user_id,
        "member_id_type": "open_id"
    }
    resp = requests.post(url, headers=headers, json=payload)
    print(f"\n3. 添加用户到角色:")
    print(f"状态码: {resp.status_code}")
    print(f"响应: {resp.json()}")
    return resp.json().get("code") == 0

if __name__ == "__main__":
    print("=" * 60)
    print("飞书多维表格 - 添加管理员")
    print(f"表格: {APP_TOKEN}")
    print(f"用户: {YOUR_USER_ID}")
    print("=" * 60)
    
    # 获取token
    token = get_token()
    if not token:
        print("❌ 无法获取access_token，退出")
        exit(1)
    print(f"✅ 获取token成功")
    
    # 开启高级权限
    success = enable_advanced_permission(token)
    if not success:
        print("⚠️  开启高级权限失败，可能已经开启或有其他问题，继续...")
    
    # 创建管理员角色
    role_id = create_admin_role(token)
    if not role_id:
        print("❌ 创建角色失败，退出")
        exit(1)
    
    # 添加用户到角色
    success = add_user_to_role(token, role_id, YOUR_USER_ID)
    if success:
        print("\n" + "=" * 60)
        print("✅ 成功！你已被添加为表格管理员")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("❌ 添加用户到角色失败")
        print("=" * 60)