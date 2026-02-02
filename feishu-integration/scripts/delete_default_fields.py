#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import requests
import json
import re

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
            
            if not response.text:
                print("❌ 服务器返回空响应")
                return None
            
            json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                data = json.loads(json_str)
                
                if data.get("code") == 0:
                    self.access_token = data.get("tenant_access_token")
                    print(f"✅ 成功获取访问令牌")
                    return self.access_token
                else:
                    print(f"❌ 获取令牌失败: {data.get('msg')}")
                    return None
            else:
                print(f"❌ 未找到有效JSON响应")
                return None
                
        except Exception as e:
            print(f"❌ 请求异常: {str(e)}")
            return None
    
    def get_bitable_by_name(self, name):
        """根据名称获取多维表格"""
        if not self.access_token:
            self.get_tenant_access_token()
        
        # 直接使用已知的应用token，或者手动输入
        print(f"\n提示：请确保已创建名为 '{name}' 的多维表格")
        print(f"如果查找失败，可以手动输入表格的app_token")
        
        # 先尝试获取token，如果失败则提示手动输入
        url = "https://open.feishu.cn/open-apis/bitable/v1/apps"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        print(f"\n正在查找多维表格: {name}")
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            
            print(f"响应状态码: {response.status_code}")
            print(f"响应内容: {response.text[:300]}")
            
            if response.status_code != 200:
                print(f"❌ API请求失败，状态码: {response.status_code}")
                print(f"提示：请检查飞书应用是否有 '多维表格' 相关权限")
                return None
            
            if not response.text:
                print("❌ 服务器返回空响应")
                return None
            
            # 尝试直接解析JSON
            try:
                data = response.json()
            except json.JSONDecodeError:
                # 使用正则表达式提取JSON
                json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                if json_match:
                    json_str = json_match.group()
                    data = json.loads(json_str)
                else:
                    print(f"❌ 未找到有效JSON响应")
                    return None
                
            if data.get("code") == 0:
                apps = data.get("data", {}).get("items", [])
                print(f"找到 {len(apps)} 个多维表格")
                
                for app in apps:
                    app_name = app.get("name", "")
                    print(f"检查表格: {app_name}")
                    if app_name == name:
                        self.app_token = app.get("app_token")
                        print(f"✅ 找到多维表格: {name}")
                        print(f"表格Token: {self.app_token}")
                        return self.app_token
                
                print(f"❌ 未找到名为 '{name}' 的多维表格")
                print(f"可用的表格: {[app.get('name') for app in apps]}")
                return None
            else:
                print(f"❌ 获取多维表格列表失败: {data.get('msg')}")
                return None
                
        except Exception as e:
            print(f"❌ 请求异常: {str(e)}")
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
            
            if not response.text:
                print("❌ 服务器返回空响应")
                return None
            
            json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                data = json.loads(json_str)
                
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
            else:
                print(f"❌ 未找到有效JSON响应")
                return None
                
        except Exception as e:
            print(f"❌ 请求异常: {str(e)}")
            return None
    
    def get_all_fields(self):
        """获取所有字段"""
        if not self.app_token or not self.table_id:
            print("❌ 缺少必要的token信息")
            return None
        
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables/{self.table_id}/fields"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        print(f"\n正在获取所有字段...")
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            
            if not response.text:
                print("❌ 服务器返回空响应")
                return None
            
            json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                data = json.loads(json_str)
                
                if data.get("code") == 0:
                    fields = data.get("data", {}).get("items", [])
                    print(f"✅ 获取到 {len(fields)} 个字段")
                    return fields
                else:
                    print(f"❌ 获取字段失败: {data.get('msg')}")
                    return None
            else:
                print(f"❌ 未找到有效JSON响应")
                return None
                
        except Exception as e:
            print(f"❌ 请求异常: {str(e)}")
            return None
    
    def delete_default_fields(self):
        """删除默认字段（文本、单选、日期、附件）"""
        fields = self.get_all_fields()
        if not fields:
            return False
        
        print(f"\n正在删除默认字段...")
        
        # 默认字段名称
        default_field_names = ["文本", "单选", "日期", "附件"]
        
        deleted_count = 0
        for field in fields:
            field_name = field.get("field_name")
            field_id = field.get("field_id")
            
            if field_name in default_field_names:
                print(f"删除字段: {field_name} (ID: {field_id})")
                
                url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables/{self.table_id}/fields/{field_id}"
                headers = {
                    "Authorization": f"Bearer {self.access_token}",
                    "Content-Type": "application/json"
                }
                
                try:
                    response = requests.delete(url, headers=headers, timeout=10)
                    
                    if response.text:
                        json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                        if json_match:
                            json_str = json_match.group()
                            data = json.loads(json_str)
                            
                            if data.get("code") == 0:
                                print(f"✅ 成功删除字段: {field_name}")
                                deleted_count += 1
                            else:
                                print(f"⚠️  删除字段失败: {field_name} - {data.get('msg')}")
                    
                except Exception as e:
                    print(f"❌ 删除字段异常: {str(e)}")
        
        print(f"\n✅ 成功删除 {deleted_count} 个默认字段")
        return deleted_count > 0

if __name__ == "__main__":
    # 使用提供的飞书应用凭证
    APP_ID = "cli_a9e4652af5f89cca"
    APP_SECRET = "4OazKFCmZTT4cjlwK0ecAhr3eAaJ7dhH"
    
    print("=" * 60)
    print("飞书多维表格默认字段删除工具")
    print("=" * 60)
    
    client = FeishuClient(APP_ID, APP_SECRET)
    
    # 查找"采购订单"表格
    app_token = client.get_bitable_by_name("采购订单")
    
    if app_token:
        # 获取数据表
        table_id = client.get_tables()
        
        if table_id:
            # 删除默认字段
            success = client.delete_default_fields()
            
            print("\n" + "=" * 60)
            if success:
                print("✅ 默认字段删除完成！")
                print("已删除字段: 文本、单选、日期、附件")
            else:
                print("❌ 默认字段删除失败")
            print("=" * 60)
        else:
            print("\n" + "=" * 60)
            print("❌ 获取数据表失败")
            print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("❌ 未找到'采购订单'多维表格")
        print("提示: 请先运行 create_purchase_order_bitable.py 创建表格")
        print("=" * 60)
