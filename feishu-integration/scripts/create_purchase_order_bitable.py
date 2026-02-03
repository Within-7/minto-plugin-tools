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
            print(f"响应状态码: {response.status_code}")
            
            if not response.text:
                print("❌ 服务器返回空响应")
                return None
            
            # 使用正则表达式提取JSON
            json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                data = json.loads(json_str)
            else:
                print(f"❌ 未找到有效JSON响应")
                return None
            
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
            "folder_token": ""
        }
        
        print(f"\n正在创建多维表格: {title}")
        print(f"API地址: {url}")
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            print(f"响应状态码: {response.status_code}")
            
            if not response.text:
                print("❌ 服务器返回空响应")
                return None
            
            # 使用正则表达式提取JSON
            json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                data = json.loads(json_str)
            else:
                print(f"❌ 未找到有效JSON响应")
                return None
            
            if data.get("code") == 0:
                self.app_token = data.get("data", {}).get("app", {}).get("app_token")
                print(f"✅ 成功创建多维表格！")
                print(f"表格Token: {self.app_token}")
                return self.app_token
            else:
                print(f"❌ 创建表格失败: {data.get('msg')}")
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
            
            # 使用正则表达式提取JSON
            json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                data = json.loads(json_str)
            else:
                print(f"❌ 未找到有效JSON响应")
                return None
            
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
    
    def create_table_fields(self):
        """创建表格字段"""
        if not self.app_token or not self.table_id:
            print("❌ 缺少必要的token信息")
            return False
        
        # 先删除默认字段（文本、单选、日期、附件）
        print(f"\n正在删除默认字段...")
        self.delete_default_fields()
        
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables/{self.table_id}/fields"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        # 定义6个字段
        fields = [
            {
                "field_name": "采购订单",
                "type": 1  # 文本类型
            },
            {
                "field_name": "采购单价",
                "type": 2  # 数字类型
            },
            {
                "field_name": "采购数量",
                "type": 2  # 数字类型
            },
            {
                "field_name": "采购金额",
                "type": 2  # 数字类型
            },
            {
                "field_name": "采购时间",
                "type": 5  # 日期类型
            },
            {
                "field_name": "采购人",
                "type": 1  # 文本类型
            }
        ]
        
        print(f"\n正在创建表格字段...")
        
        success_count = 0
        for field in fields:
            try:
                response = requests.post(url, headers=headers, json=field, timeout=10)
                print(f"创建字段 '{field['field_name']}' - 状态码: {response.status_code}")
                
                if response.text:
                    json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                    if json_match:
                        json_str = json_match.group()
                        data = json.loads(json_str)
                        if data.get("code") == 0:
                            print(f"✅ 成功创建字段: {field['field_name']}")
                            success_count += 1
                        else:
                            print(f"⚠️  创建字段失败: {field['field_name']} - {data.get('msg')}")
                    
            except Exception as e:
                print(f"❌ 创建字段异常: {str(e)}")
        
        return success_count == len(fields)
    
    def delete_default_fields(self):
        """删除默认字段"""
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables/{self.table_id}/fields"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        # 获取所有字段
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.text:
                json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                if json_match:
                    json_str = json_match.group()
                    data = json.loads(json_str)
                    if data.get("code") == 0:
                        fields = data.get("data", {}).get("items", [])
                        default_names = ["文本", "单选", "日期", "附件"]
                        
                        for field in fields:
                            field_name = field.get("field_name")
                            field_id = field.get("field_id")
                            if field_name in default_names:
                                delete_url = f"{url}/{field_id}"
                                requests.delete(delete_url, headers=headers, timeout=10)
                                print(f"✅ 删除默认字段: {field_name}")
        except Exception as e:
            print(f"删除默认字段时出错: {str(e)}")
    
    def add_sample_records(self):
        """添加6行示例数据"""
        if not self.app_token or not self.table_id:
            print("❌ 缺少必要的token信息")
            return False
        
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables/{self.table_id}/records"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        # 6行示例数据
        records = [
            {"采购单价": 100, "采购订单": "PO001", "采购金额": 500, "采购数量": 5, "采购时间": 1705776000000, "采购人": "张三"},
            {"采购单价": 200, "采购订单": "PO002", "采购金额": 800, "采购数量": 4, "采购时间": 1705862400000, "采购人": "李四"},
            {"采购单价": 150, "采购订单": "PO003", "采购金额": 900, "采购数量": 6, "采购时间": 1705948800000, "采购人": "王五"},
            {"采购单价": 300, "采购订单": "PO004", "采购金额": 1200, "采购数量": 4, "采购时间": 1706035200000, "采购人": "赵六"},
            {"采购单价": 250, "采购订单": "PO005", "采购金额": 1250, "采购数量": 5, "采购时间": 1706121600000, "采购人": "孙七"},
            {"采购单价": 180, "采购订单": "PO006", "采购金额": 1080, "采购数量": 6, "采购时间": 1706208000000, "采购人": "周八"}
        ]
        
        print(f"\n正在添加6行示例数据...")
        
        success_count = 0
        for record in records:
            payload = {"fields": record}
            try:
                response = requests.post(url, headers=headers, json=payload, timeout=10)
                
                if response.text:
                    json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                    if json_match:
                        json_str = json_match.group()
                        data = json.loads(json_str)
                        if data.get("code") == 0:
                            print(f"✅ 成功添加记录: {record['采购订单']}")
                            success_count += 1
                        else:
                            print(f"⚠️  添加记录失败: {record['采购订单']} - {data.get('msg')}")
                    
            except Exception as e:
                print(f"❌ 添加记录异常: {str(e)}")
        
        return success_count == len(records)

if __name__ == "__main__":
    # 使用提供的飞书应用凭证
    APP_ID = "cli_a9e4652af5f89cca"
    APP_SECRET = "4OazKFCmZTT4cjlwK0ecAhr3eAaJ7dhH"
    
    print("=" * 60)
    print("飞书采购订单多维表格创建工具")
    print("=" * 60)
    
    client = FeishuClient(APP_ID, APP_SECRET)
    
    # 创建多维表格
    app_token = client.create_bitable("采购订单")
    
    if app_token:
        # 获取默认数据表
        table_id = client.get_tables()
        
        if table_id:
            # 创建字段
            client.create_table_fields()
            
            # 添加6行数据
            client.add_sample_records()
        
        print("\n" + "=" * 60)
        print("✅ 采购订单多维表格创建完成！")
        table_url = f"https://feishu.cn/base/{app_token}"
        print(f"表格链接: {table_url}")
        print("表格结构: 6行 x 6列")
        print("列名: 采购单价, 采购订单, 采购金额, 采购数量, 采购时间, 采购人")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("❌ 多维表格创建失败")
        print("提示: 请确保飞书应用已添加 '多维表格' 相关权限")
        print("=" * 60)
