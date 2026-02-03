#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import requests
import json
import re

def test_feishu_permissions():
    """测试飞书应用权限"""
    APP_ID = "cli_a9e4652af5f89cca"
    APP_SECRET = "4OazKFCmZTT4cjlwK0ecAhr3eAaJ7dhH"
    
    print("=" * 60)
    print("飞书应用权限测试工具")
    print("=" * 60)
    
    # 1. 测试获取访问令牌
    print("\n1. 测试获取访问令牌...")
    token_url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
    token_payload = {
        "app_id": APP_ID,
        "app_secret": APP_SECRET
    }
    
    try:
        response = requests.post(token_url, json=token_payload, timeout=10)
        print(f"响应状态码: {response.status_code}")
        
        if response.text:
            json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                data = json.loads(json_str)
                
                if data.get("code") == 0:
                    access_token = data.get("tenant_access_token")
                    print(f"✅ 成功获取访问令牌")
                    print(f"Token: {access_token[:20]}...")
                else:
                    print(f"❌ 获取令牌失败: {data.get('msg')}")
                    return None
            else:
                print(f"❌ 未找到有效JSON响应")
                return None
        else:
            print(f"❌ 服务器返回空响应")
            return None
    except Exception as e:
        print(f"❌ 请求异常: {str(e)}")
        return None
    
    # 2. 测试获取多维表格列表
    print("\n2. 测试获取多维表格列表...")
    apps_url = "https://open.feishu.cn/open-apis/bitable/v1/apps"
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }
    
    try:
        response = requests.get(apps_url, headers=headers, timeout=10)
        print(f"响应状态码: {response.status_code}")
        
        if response.status_code == 404:
            print(f"❌ 无法访问多维表格API (404)")
            print(f"可能缺少权限: bitable:app:readonly")
        elif response.text:
            json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                data = json.loads(json_str)
                
                if data.get("code") == 0:
                    apps = data.get("data", {}).get("items", [])
                    print(f"✅ 成功获取多维表格列表，共 {len(apps)} 个表格")
                    for app in apps:
                        print(f"  - {app.get('name')}")
                else:
                    print(f"❌ 获取表格列表失败: {data.get('msg')}")
                    print(f"错误代码: {data.get('code')}")
    except Exception as e:
        print(f"❌ 请求异常: {str(e)}")
    
    # 3. 测试创建应用
    print("\n3. 测试创建多维表格应用...")
    create_url = "https://open.feishu.cn/open-apis/bitable/v1/apps"
    create_payload = {
        "name": "测试应用权限",
        "folder_token": ""
    }
    
    try:
        response = requests.post(create_url, headers=headers, json=create_payload, timeout=10)
        print(f"响应状态码: {response.status_code}")
        print(f"响应内容: {response.text[:300]}")
        
        if response.text:
            json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                data = json.loads(json_str)
                
                if data.get("code") == 0:
                    app_token = data.get("data", {}).get("app", {}).get("app_token")
                    print(f"✅ 成功创建测试应用！")
                    print(f"应用Token: {app_token}")
                    print(f"✅ 您的应用具有完整的创建权限！")
                    
                    # 清理测试应用
                    print(f"\n清理测试应用...")
                    delete_url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}"
                    delete_response = requests.delete(delete_url, headers=headers, timeout=10)
                    print(f"删除响应状态码: {delete_response.status_code}")
                    print(f"✅ 测试完成并已清理测试应用")
                else:
                    print(f"❌ 创建应用失败: {data.get('msg')}")
                    print(f"错误代码: {data.get('code')}")
                    print(f"可能缺少权限: bitable:app")
    except Exception as e:
        print(f"❌ 请求异常: {str(e)}")
    
    print("\n" + "=" * 60)
    print("权限测试完成")
    print("=" * 60)

if __name__ == "__main__":
    test_feishu_permissions()
