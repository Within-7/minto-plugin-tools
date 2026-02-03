#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import requests
import json

class FeishuClient:
    def __init__(self, app_id, app_secret):
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = None
    
    def get_tenant_access_token(self):
        """获取 tenant_access_token"""
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        payload = {
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }
        
        print(f"正在请求飞书API获取token...")
        print(f"API地址: {url}")
        print(f"App ID: {self.app_id}")
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            data = response.json()
            
            print(f"\n响应状态码: {response.status_code}")
            print(f"响应内容: {json.dumps(data, ensure_ascii=False, indent=2)}")
            
            if data.get("code") == 0:
                self.access_token = data.get("tenant_access_token")
                print(f"\n✅ 成功获取 tenant_access_token")
                print(f"Token: {self.access_token[:20]}...")
                return self.access_token
            else:
                print(f"\n❌ 获取token失败: {data.get('msg')}")
                return None
                
        except Exception as e:
            print(f"\n❌ 请求异常: {str(e)}")
            return None

if __name__ == "__main__":
    # 使用提供的飞书应用凭证
    APP_ID = "cli_a9e4652af5f89cca"
    APP_SECRET = "4OazKFCmZTT4cjlwK0ecAhr3eAaJ7dhH"
    
    print("=" * 60)
    print("飞书API连接测试")
    print("=" * 60)
    
    client = FeishuClient(APP_ID, APP_SECRET)
    token = client.get_tenant_access_token()
    
    print("\n" + "=" * 60)
    if token:
        print("✅ 飞书配置验证成功！")
    else:
        print("❌ 飞书配置验证失败，请检查 App ID 和 Secret")
    print("=" * 60)
