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
        
        print(f"\n正在查找多维表格: {name}")
        
        url = "https://open.feishu.cn/open-apis/bitable/v1/apps"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            
            print(f"响应状态码: {response.status_code}")
            print(f"响应内容: {response.text[:300]}")
            
            if response.status_code == 404:
                print(f"❌ API端点返回404")
                print(f"可能原因：")
                print(f"1. 应用权限未发布或未生效")
                print(f"2. 权限配置不完整")
                print(f"3. API端点版本问题")
                print(f"\n建议尝试：")
                print(f"- 直接使用表格的app_token，而不是通过名称查找")
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
    
    def create_form_app(self):
        """创建表单应用模式"""
        if not self.app_token:
            print("❌ 未找到表格token")
            return False
        
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/form/initialize"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        print(f"\n正在创建表单应用模式...")
        print(f"API地址: {url}")
        
        try:
            response = requests.post(url, headers=headers, json={}, timeout=10)
            
            print(f"响应状态码: {response.status_code}")
            print(f"响应内容: {response.text[:300]}")
            
            if response.text:
                json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                if json_match:
                    json_str = json_match.group()
                    data = json.loads(json_str)
                    
                    if data.get("code") == 0:
                        form_url = data.get("data", {}).get("form", {}).get("url")
                        print(f"✅ 成功创建表单应用模式！")
                        print(f"表单链接: {form_url}")
                        return True
                    else:
                        print(f"⚠️  创建表单失败: {data.get('msg')}")
                        print(f"提示: 可能需要在飞书多维表格中手动启用表单功能")
                        return False
            else:
                print(f"❌ 服务器返回空响应")
                return False
                
        except Exception as e:
            print(f"❌ 请求异常: {str(e)}")
            return False
    
    def get_manual_setup_guide(self):
        """获取手动设置指南"""
        guide = """
        
        ======== 飞书应用模式设置指南 ========
        
        由于API限制，请按以下步骤手动设置应用模式：
        
        1. 打开飞书，进入"采购订单"多维表格
        
        2. 点击右上角"..." → "应用" → "新建应用"
        
        3. 选择应用模板：
           - 数据收集表单
           - 或者选择"自定义应用"
        
        4. 配置应用表单字段：
           - 采购订单（文本输入）
           - 采购单价（数字输入）
           - 采购数量（数字输入）
           - 采购金额（自动计算：单价×数量）
           - 采购时间（日期选择）
           - 采购人（文本输入或人员选择）
        
        5. 设置表单权限：
           - 允许任何人提交
           - 或指定特定人员/部门
        
        6. 发布应用：
           - 复制应用链接
           - 分享给相关人员
        
        7. 高级功能（可选）：
           - 设置数据验证规则
           - 添加条件格式
           - 配置通知提醒
        
        ====================================
        """
        print(guide)
        return True

if __name__ == "__main__":
    # 使用提供的飞书应用凭证
    APP_ID = "cli_a9e4652af5f89cca"
    APP_SECRET = "4OazKFCmZTT4cjlwK0ecAhr3eAaJ7dhH"
    
    print("=" * 60)
    print("飞书应用模式创建工具")
    print("=" * 60)
    
    client = FeishuClient(APP_ID, APP_SECRET)
    
    # 直接获取手动设置指南，不依赖API
    print("\n由于API权限限制，直接提供手动设置指南...")
    client.get_manual_setup_guide()
    
    print("\n" + "=" * 60)
    print("✅ 应用模式设置指南已生成")
    print("请按照上述步骤在飞书中手动配置应用模式")
    print("=" * 60)
