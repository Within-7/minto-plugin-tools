#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import requests
import json

class FeishuClient:
    def __init__(self, app_id, app_secret):
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = None
        self.app_token = None
        self.table_id = None
    
    def get_tenant_access_token(self):
        """获取 tenant_access_token"""
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        payload = {
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }
        
        print(f"正在获取飞书访问令牌...")
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            data = response.json()
            
            if data.get("code") == 0:
                self.access_token = data.get("tenant_access_token")
                print(f"✅ 成功获取访问令牌")
                return self.access_token
            else:
                print(f"❌ 获取令牌失败: {data.get('msg')}")
                return None
                
        except Exception as e:
            print(f"❌ 请求异常: {str(e)}")
            return None
    
    def create_bitable(self, title):
        """创建多维表格"""
        if not self.access_token:
            self.get_tenant_access_token()
        
        url = "https://open.feishu.cn/open-apis/bitable/v1/apps"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "name": title,
            "folder_token": ""  # 空字符串表示创建在根目录
        }
        
        print(f"\n正在创建多维表格: {title}")
        print(f"API地址: {url}")
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            data = response.json()
            
            print(f"\n响应状态码: {response.status_code}")
            print(f"响应内容: {json.dumps(data, ensure_ascii=False, indent=2)}")
            
            if data.get("code") == 0:
                self.app_token = data.get("data", {}).get("app", {}).get("app_token")
                print(f"\n✅ 成功创建多维表格！")
                print(f"表格Token: {self.app_token}")
                return self.app_token
            else:
                print(f"\n❌ 创建表格失败: {data.get('msg')}")
                return None
                
        except Exception as e:
            print(f"\n❌ 请求异常: {str(e)}")
            return None
    
    def get_tables(self):
        """获取表格中的所有数据表"""
        if not self.app_token:
            print("❌ 未找到表格token")
            return None
        
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        print(f"\n正在获取数据表信息...")
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            data = response.json()
            
            if data.get("code") == 0:
                tables = data.get("data", {}).get("items", [])
                if tables:
                    self.table_id = tables[0].get("table_id")
                    print(f"✅ 获取到默认数据表ID: {self.table_id}")
                    return self.table_id
                else:
                    print("❌ 未找到数据表")
                    return None
            else:
                print(f"❌ 获取数据表失败: {data.get('msg')}")
                return None
                
        except Exception as e:
            print(f"❌ 请求异常: {str(e)}")
            return None
    
    def add_table_fields(self):
        """添加表格字段"""
        if not self.app_token or not self.table_id:
            print("❌ 缺少必要的token信息")
            return False
        
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables/{self.table_id}/fields"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        # 定义三个字段：名字、标题、阅读量
        fields = [
            {
                "field_name": "名字",
                "type": 1  # 文本类型
            },
            {
                "field_name": "标题", 
                "type": 1  # 文本类型
            },
            {
                "field_name": "阅读量",
                "type": 2  # 数字类型
            }
        ]
        
        print(f"\n正在添加表格字段...")
        
        # 逐个添加字段
        for field in fields:
            try:
                response = requests.post(url, headers=headers, json=field, timeout=10)
                data = response.json()
                
                if data.get("code") == 0:
                    print(f"✅ 成功添加字段: {field['field_name']}")
                else:
                    print(f"⚠️  添加字段失败: {field['field_name']} - {data.get('msg')}")
                    
            except Exception as e:
                print(f"❌ 添加字段异常: {str(e)}")
        
        return True
    
    def add_record(self, name, title, views):
        """添加一条记录"""
        if not self.app_token or not self.table_id:
            print("❌ 缺少必要的token信息")
            return False
        
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables/{self.table_id}/records"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "fields": {
                "名字": name,
                "标题": title,
                "阅读量": views
            }
        }
        
        print(f"\n正在添加记录: {name} - {title} - {views}")
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            data = response.json()
            
            if data.get("code") == 0:
                print(f"✅ 成功添加记录")
                return True
            else:
                print(f"❌ 添加记录失败: {data.get('msg')}")
                return False
                
        except Exception as e:
            print(f"❌ 请求异常: {str(e)}")
            return False
    
    def add_owner_permission(self, user_id):
        """添加表格所有者权限（添加自己为管理员）"""
        if not self.app_token:
            print("❌ 缺少app_token")
            return False
        
        url = "https://open.feishu.cn/open-apis/permission/v2/permissions/add_member"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"
        }
        
        payload = {
            "resource_type": "bitable",
            "resource_id": self.app_token,
            "perm_type": "full_access",  # 完全管理权限
            "member_type": "user",
            "member_id": user_id
        }
        
        print(f"\n正在添加表格所有者权限...")
        print(f"用户ID: {user_id}")
        
        try:
            response = requests.post(url, headers=headers, data=payload, timeout=10)
            data = response.json()
            
            if data.get("code") == 0:
                print(f"✅ 成功添加所有者权限！")
                return True
            else:
                print(f"❌ 添加权限失败: {data.get('msg')}")
                if data.get("code") == 99991663:
                    print("提示: 应用需要开通 '添加协作者' 权限")
                return False
                
        except Exception as e:
            print(f"❌ 请求异常: {str(e)}")
            return False

if __name__ == "__main__":
    # 使用提供的飞书应用凭证
    APP_ID = "cli_a9e4652af5f89cca"
    APP_SECRET = "4OazKFCmZTT4cjlwK0ecAhr3eAaJ7dhH"
    
    # 你的飞书用户ID（需要替换为你的真实 open_id）
    # 可以通过飞书开放平台获取，或者使用你之前提到的ID
    YOUR_USER_ID = "ou_31ec8c3772b60ed46d16ed23e4eda331"  # 你的 open_id
    
    print("=" * 60)
    print("飞书多维表格创建工具")
    print("=" * 60)
    
    client = FeishuClient(APP_ID, APP_SECRET)
    
    # 创建多维表格
    app_token = client.create_bitable("测试表格")
    
    if app_token:
        # 添加自己为表格管理员（解决权限问题）
        client.add_owner_permission(YOUR_USER_ID)
        
        # 获取默认数据表
        table_id = client.get_tables()
        
        if table_id:
            # 添加字段
            client.add_table_fields()
            
            # 添加示例数据
            print("\n添加示例数据...")
            client.add_record("张三", "测试文章1", 1000)
            client.add_record("李四", "测试文章2", 2500)
            client.add_record("王五", "测试文章3", 5800)
        
        print("\n" + "=" * 60)
        print("✅ 多维表格创建完成！")
        table_url = f"https://feishu.cn/base/{app_token}"
        print(f"表格链接: {table_url}")
        print("💡 你已被添加为表格管理员，拥有完全编辑权限")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("❌ 多维表格创建失败")
        print("提示: 请确保飞书应用已添加 '多维表格' 相关权限")
        print("=" * 60)
