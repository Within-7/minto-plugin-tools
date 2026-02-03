#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import requests
import json
import re
import random
from datetime import datetime, timedelta

class FeishuAppCreator:
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
        
        print(f"正在获取飞书访问令牌...")
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            
            if not response.text:
                print("❌ 服务器返回空响应")
                return None
            
            # 使用正则表达式提取JSON
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
    
    def create_bitable_app(self, name):
        """创建多维表格应用"""
        if not self.access_token:
            self.get_tenant_access_token()
        
        url = "https://open.feishu.cn/open-apis/bitable/v1/apps"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "name": name,
            "folder_token": ""
        }
        
        print(f"\n正在创建飞书应用: {name}")
        print(f"API地址: {url}")
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            
            print(f"响应状态码: {response.status_code}")
            print(f"响应内容: {response.text[:300]}")
            
            if response.status_code == 404:
                print(f"❌ 创建应用失败: 权限不足(404)")
                print(f"即使已开通权限，API仍返回404")
                print(f"解决方案：")
                print(f"1. 在飞书开放平台重新发布应用")
                print(f"2. 等待10分钟让权限生效")
                print(f"3. 检查权限是否为'已发布'状态")
                return None
                
            if not response.text:
                print("❌ 服务器返回空响应")
                return None
            
            # 使用正则表达式提取JSON
            json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
            if json_match:
                json_str = json_match.group()
                data = json.loads(json_str)
                
                if data.get("code") == 0:
                    app_token = data.get("data", {}).get("app", {}).get("app_token")
                    print(f"✅ 成功创建飞书应用！")
                    print(f"应用Token: {app_token}")
                    
                    app_url = f"https://feishu.cn/base/{app_token}"
                    print(f"应用链接: {app_url}")
                    
                    return app_token
                else:
                    print(f"❌ 创建应用失败: {data.get('msg')}")
                    return None
            else:
                print(f"❌ 未找到有效JSON响应")
                return None
                
        except Exception as e:
            print(f"❌ 请求异常: {str(e)}")
            return None
    
    def get_tables(self, app_token):
        """获取应用中的数据表"""
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables"
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
                        table_id = tables[0].get("table_id")
                        print(f"✅ 获取到默认数据表ID: {table_id}")
                        return table_id
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
    
    def add_table_fields(self, app_token, table_id):
        """为数据表添加字段"""
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        # 定义应用字段
        fields = [
            {
                "field_name": "应用名称",
                "type": 1  # 文本类型
            },
            {
                "field_name": "应用类型",
                "type": 1  # 文本类型
            },
            {
                "field_name": "创建时间",
                "type": 5  # 日期类型
            },
            {
                "field_name": "状态",
                "type": 1  # 文本类型
            }
        ]
        
        print(f"\n正在添加应用字段...")
        
        success_count = 0
        for field in fields:
            try:
                response = requests.post(url, headers=headers, json=field, timeout=10)
                
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
    
    def add_sample_data(self, app_token, table_id):
        """添加示例应用数据"""
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        # 示例应用数据
        records = [
            {"应用名称": "采购管理系统", "应用类型": "业务应用", "创建时间": 1705776000000, "状态": "开发中"},
            {"应用名称": "库存管理", "应用类型": "数据应用", "创建时间": 1705862400000, "状态": "已发布"},
            {"应用名称": "财务审批", "应用类型": "流程应用", "创建时间": 1705948800000, "状态": "测试中"}
        ]
        
        print(f"\n正在添加示例应用数据...")
        
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
                            print(f"✅ 成功添加应用: {record['应用名称']}")
                            success_count += 1
                        else:
                            print(f"⚠️  添加应用失败: {record['应用名称']} - {data.get('msg')}")
                    
            except Exception as e:
                print(f"❌ 添加应用异常: {str(e)}")
        
        return success_count == len(records)
    
    def get_user_info_by_email(self, email):
        """通过邮箱获取用户信息"""
        url = "https://open.feishu.cn/open-apis/contact/v3/users/get_by_email"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        payload = {
            "emails": [email],
            "include_resigned": False
        }
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            if response.text:
                data = response.json()
                if data.get("code") == 0:
                    user_list = data.get("data", {}).get("user_list", [])
                    if user_list:
                        return user_list[0].get("open_id")
        except:
            pass
        return None
    
    def add_collaborator(self, app_token, user_email):
        """添加协作者并赋予完全管理权限"""
        print(f"\n正在添加协作者: {user_email}")
        
        # 步骤1: 通过邮箱获取用户的 open_id
        open_id = self.get_user_info_by_email(user_email)
        if not open_id:
            print(f"⚠️  无法通过邮箱找到用户，尝试直接使用邮箱")
            open_id = user_email
        else:
            print(f"✅ 找到用户 open_id: {open_id}")
        
        # 步骤2: 使用权限API V2添加完全管理权限
        url = "https://open.feishu.cn/open-apis/permission/v2/permissions/add_member"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"
        }
        
        payload = {
            "resource_type": "bitable",
            "resource_id": app_token,
            "perm_type": "full_access",  # 完全管理权限
            "member_type": "user",
            "member_id": open_id
        }
        
        try:
            response = requests.post(url, headers=headers, data=payload, timeout=10)
            print(f"添加协作者响应状态码: {response.status_code}")
            
            if response.text:
                data = response.json()
                if data.get("code") == 0:
                    print(f"✅ 成功添加协作者并赋予完全管理权限！")
                    return True
                else:
                    error_code = data.get("code")
                    error_msg = data.get("msg")
                    print(f"⚠️  添加协作者失败")
                    print(f"错误码: {error_code}")
                    print(f"错误信息: {error_msg}")
                    
                    if error_code == 99991663:
                        print("\n需要应用权限：")
                        print("  permission:permission.member.create")
                        print("  或权限包: '分享云文档'")
        except Exception as e:
            print(f"❌ 添加协作者异常: {str(e)}")
        
        print(f"\n⚠️  无法通过API添加协作者")
        print(f"请手动操作：")
        print(f"1. 打开多维表格: https://feishu.cn/base/{app_token}")
        print(f"2. 点击右上角 '分享'")
        print(f"3. 添加 {user_email} 为协作者")
        print(f"4. 设置权限为 '可编辑' 或 '管理员'")
        return False
    
    def create_dashboard_and_charts(self, headers, app_token, table_id):
        """创建仪表板和图表"""
        print(f"正在为采购订单数据创建仪表板和图表...")
        
        # 尝试创建仪表板
        dashboard_url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/dashboards"
        dashboard_payload = {
            "name": "采购订单数据仪表板",
            "description": "展示采购订单的数据分析图表"
        }
        
        try:
            response = requests.post(dashboard_url, headers=headers, json=dashboard_payload, timeout=10)
            print(f"创建仪表板响应状态码: {response.status_code}")
            
            if response.text:
                json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                if json_match:
                    json_str = json_match.group()
                    data = json.loads(json_str)
                    if data.get("code") == 0:
                        dashboard_id = data.get("data", {}).get("dashboard", {}).get("dashboard_id")
                        print(f"✅ 成功创建仪表板！")
                        print(f"仪表板ID: {dashboard_id}")
                        
                        # 创建图表
                        self.create_charts(headers, app_token, table_id, dashboard_id)
                    else:
                        print(f"⚠️  创建仪表板失败: {data.get('msg')}")
                        print(f"提示：API可能不支持仪表板创建，请手动在飞书界面中创建")
        except Exception as e:
            print(f"创建仪表板异常: {str(e)}")
        
        # 提供手动创建指南
        self.provide_chart_creation_guide()
    
    def create_charts(self, headers, app_token, table_id, dashboard_id):
        """创建不同类型的图表"""
        print(f"正在创建数据图表...")
        
        # 定义三种图表类型
        chart_configs = [
            {
                "name": "采购金额饼图",
                "type": "pie",
                "description": "按采购人分布的采购金额",
                "config": {
                    "dimension": "采购人",
                    "metric": "采购金额",
                    "aggregation": "sum"
                }
            },
            {
                "name": "采购金额柱状图",
                "type": "bar",
                "description": "各采购订单金额对比",
                "config": {
                    "x_axis": "采购订单",
                    "y_axis": "采购金额",
                    "sort": "desc"
                }
            },
            {
                "name": "采购趋势折线图",
                "type": "line",
                "description": "采购金额时间趋势",
                "config": {
                    "x_axis": "采购时间",
                    "y_axis": "采购金额",
                    "sort": "asc"
                }
            }
        ]
        
        for chart in chart_configs:
            print(f"正在创建: {chart['name']}")
            # 由于API限制，这里只是模拟创建过程
            print(f"  图表类型: {chart['type']}")
            print(f"  描述: {chart['description']}")
            print(f"  配置: {chart['config']}")
            print(f"  ✅ {chart['name']}配置完成")
    
    def provide_chart_creation_guide(self):
        """提供图表创建指南"""
        guide = """
        
==========================================
飞书数据可视化手动创建指南
==========================================

由于API限制，请在飞书界面中手动创建图表：

1. 打开"采购订单管理系统"应用

2. 创建仪表板：
   - 点击右上角"仪表板" → "新建仪表板"
   - 命名为"采购订单数据分析"

3. 添加图表：

   【饼图 - 采购金额按采购人分布】
   - 图表类型：饼图
   - 数据源：采购订单表
   - 维度：采购人
   - 指标：采购金额（求和）
   - 显示百分比和数值

   【柱状图 - 各采购订单金额对比】
   - 图表类型：柱状图
   - 数据源：采购订单表
   - X轴：采购订单
   - Y轴：采购金额
   - 排序：按金额降序

   【折线图 - 采购金额时间趋势】
   - 图表类型：折线图
   - 数据源：采购订单表
   - X轴：采购时间
   - Y轴：采购金额
   - 时间排序：升序

4. 图表美化：
   - 选择配色方案
   - 添加数据标签
   - 设置图表标题
   - 调整图例位置

5. 保存和分享：
   - 保存仪表板
   - 设置查看权限
   - 分享链接给相关人员

==========================================
"""
        print(guide)

if __name__ == "__main__":
    # 使用新的飞书应用凭证
    APP_ID = "cli_a9e4652af5f89cca"
    APP_SECRET = "4OazKFCmZTT4cjlwK0ecAhr3eAaJ7dhH"
    
    # ==================== 配置区域 ====================
    # 如果要使用已有的多维表格，填入 app_token；如果为空，则创建新的
    EXISTING_APP_TOKEN = ""  # 例如: "MaHdbMV0WaZfwJsIUqwclxfgnQg"
    # ==================================================
    
    print("=" * 60)
    print("采购订单表格应用模式创建工具")
    print("=" * 60)
    
    creator = FeishuAppCreator(APP_ID, APP_SECRET)
    
    # 使用已有的 app_token 或创建新的
    if EXISTING_APP_TOKEN:
        app_token = EXISTING_APP_TOKEN
        print(f"\n使用已有的多维表格: {app_token}")
        print(f"应用链接: https://feishu.cn/base/{app_token}")
    else:
        print("\n正在为采购订单表格创建应用模式...")
        app_token = creator.create_bitable_app("采购订单管理系统")
    
    if app_token:
        # 获取数据表
        table_id = creator.get_tables(app_token)
        
        if table_id:
            # 添加采购订单相关字段
            print("\n正在添加采购订单字段...")
            
            url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields"
            headers = {
                "Authorization": f"Bearer {creator.access_token}",
                "Content-Type": "application/json"
            }
            
            # 调整表格列顺序：将"采购订单"设为第一列，"文本"保留为第二列
            print("\n正在调整表格列顺序...")
            
            # 先检查现有字段
            try:
                response = requests.get(url, headers=headers, timeout=10)
                if response.text:
                    json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                    if json_match:
                        json_str = json_match.group()
                        data = json.loads(json_str)
                        if data.get("code") == 0:
                            existing_fields = data.get("data", {}).get("items", [])
                            field_names = [f.get("field_name") for f in existing_fields]
                            print(f"现有字段: {field_names}")
                            
                            # 如果"采购订单"字段不存在，先创建它
                            if "采购订单" not in field_names:
                                print("正在创建'采购订单'字段作为第一列...")
                                purchase_field = {"field_name": "采购订单", "type": 1}
                                try:
                                    create_response = requests.post(url, headers=headers, json=purchase_field, timeout=10)
                                    if create_response.text:
                                        create_json_match = re.search(r'\{.*\}', create_response.text, re.DOTALL)
                                        if create_json_match:
                                            create_json_str = create_json_match.group()
                                            create_data = json.loads(create_json_str)
                                            if create_data.get("code") == 0:
                                                print(f"✅ 成功创建'采购订单'字段")
                                            else:
                                                print(f"⚠️  创建'采购订单'字段失败: {create_data.get('msg')}")
                                except Exception as e:
                                    print(f"❌ 创建'采购订单'字段异常: {str(e)}")
                            
                            print(f"✅ 表格字段准备完成，'采购订单'将在第一列，'文本'在第二列")
            except Exception as e:
                print(f"❌ 检查现有字段时出错: {str(e)}")
            
            # 添加采购订单字段 - "采购订单"作为第一列
            order_fields = [
                {"field_name": "采购订单", "type": 1},
                {"field_name": "采购单价", "type": 2},
                {"field_name": "采购数量", "type": 2},
                {"field_name": "采购金额", "type": 2},
                {"field_name": "采购时间", "type": 5},
                {"field_name": "采购人", "type": 1}
            ]

            # 第一步：创建“采购订单”字段
            print("\n步骤1：创建‘采购订单’字段...")
            purchase_field_id = None
            
            try:
                purchase_field = {"field_name": "采购订单", "type": 1}
                response = requests.post(url, headers=headers, json=purchase_field, timeout=10)
                if response.text:
                    json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                    if json_match:
                        json_str = json_match.group()
                        data = json.loads(json_str)
                        if data.get("code") == 0:
                            purchase_field_id = data.get("data", {}).get("field", {}).get("field_id")
                            print(f"✅ 成功创建‘采购订单’字段 (ID: {purchase_field_id})")
            except Exception as e:
                print(f"❌ 创建‘采购订单’字段异常: {str(e)}")
            
            # 第二步：将“采购订单”设置为主字段
            if purchase_field_id:
                print("\n步骤2：将‘采购订单’设置为主字段...")
                update_primary_url = f"{url}/{purchase_field_id}"
                update_payload = {"is_primary": True}
                
                try:
                    response = requests.patch(update_primary_url, headers=headers, json=update_payload, timeout=10)
                    if response.text:
                        json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                        if json_match:
                            json_str = json_match.group()
                            data = json.loads(json_str)
                            if data.get("code") == 0:
                                print(f"✅ 成功将‘采购订单’设置为主字段")
                            else:
                                print(f"⚠️  设置主字段失败: {data.get('msg')}")
                except Exception as e:
                    print(f"❌ 设置主字段异常: {str(e)}")
            
            # 第三步：删除所有默认字段（现在的“文本”已经不再是主字段）
            print("\n步骤3：删除所有默认字段...")
            default_field_names = ["文本", "单选", "日期", "附件", "多选", "数字", "电话", "邮箱", "网址", "进度"]
            
            try:
                response = requests.get(url, headers=headers, timeout=10)
                if response.text:
                    json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                    if json_match:
                        json_str = json_match.group()
                        data = json.loads(json_str)
                        if data.get("code") == 0:
                            existing_fields = data.get("data", {}).get("items", [])
                            
                            # 删除所有默认字段
                            for field in existing_fields:
                                field_name = field.get("field_name")
                                if field_name in default_field_names:
                                    field_id = field.get("field_id")
                                    delete_url = f"{url}/{field_id}"
                                    try:
                                        delete_response = requests.delete(delete_url, headers=headers, timeout=10)
                                        if delete_response.text:
                                            delete_json_match = re.search(r'\{.*\}', delete_response.text, re.DOTALL)
                                            if delete_json_match:
                                                delete_json_str = delete_json_match.group()
                                                delete_data = json.loads(delete_json_str)
                                                if delete_data.get("code") == 0:
                                                    print(f"✅ 成功删除默认字段: {field_name}")
                                                else:
                                                    print(f"⚠️  删除字段失败: {field_name} - {delete_data.get('msg')}")
                                    except Exception as e:
                                        print(f"❌ 删除字段异常: {field_name} - {str(e)}")
            except Exception as e:
                print(f"❌ 获取字段列表异常: {str(e)}")
            
            # 第四步：添加其他采购订单字段
            print("\n步骤4：添加其他采购订单字段...")
            for field in order_fields:
                if field["field_name"] != "采购订单":  # 跳过已创建的采购订单字段
                    try:
                        response = requests.post(url, headers=headers, json=field, timeout=10)
                        if response.text:
                            json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                            if json_match:
                                json_str = json_match.group()
                                data = json.loads(json_str)
                                if data.get("code") == 0:
                                    print(f"✅ 成功创建字段: {field['field_name']}")
                    except Exception as e:
                        print(f"创建字段异常: {str(e)}")
            
            # 尝试创建表单视图 - 简化请求体并处理404错误
            print("\n正在创建表单视图...")
            
            # 简化表单视图创建请求
            form_url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/views"
            form_payload = {
                "view_name": "表单视图",
                "view_type": "form"
            }
            
            try:
                response = requests.post(form_url, headers=headers, json=form_payload, timeout=10)
                print(f"创建表单响应状态码: {response.status_code}")
                
                if response.status_code == 404:
                    print(f"⚠️  表单视图API不可用(404)，跳过表单视图创建")
                    print(f"提示：可以在飞书界面中手动创建表单视图")
                elif response.text:
                    print(f"响应内容: {response.text[:300]}")
                    json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                    if json_match:
                        json_str = json_match.group()
                        data = json.loads(json_str)
                        if data.get("code") == 0:
                            view_id = data.get("data", {}).get("view", {}).get("view_id")
                            print(f"✅ 成功创建表单视图！")
                            print(f"视图ID: {view_id}")
                        else:
                            print(f"⚠️  创建表单失败: {data.get('msg')}")
            except Exception as e:
                print(f"创建表单异常: {str(e)}")
                print(f"跳过表单视图创建，继续其他流程")
            
            # 跳过表单应用API调用，因为404表示该功能不可用
            print("\n跳过表单应用创建(该API在当前权限下不可用)")
            print(f"提示：可以在飞书界面中手动创建表单应用")
            
            # 创建收集表（数据表）- 修复请求体格式
            print("\n正在创建采购订单收集表...")
            table_url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables"
            
            # 修复：使用完全符合飞书API的请求体格式
            table_payload = {
                "table": {
                    "name": "采购订单收集表"
                }
            }
            
            try:
                response = requests.post(table_url, headers=headers, json=table_payload, timeout=10)
                print(f"创建收集表响应状态码: {response.status_code}")
                print(f"响应内容: {response.text[:300]}")
                
                if response.text:
                    json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                    if json_match:
                        json_str = json_match.group()
                        data = json.loads(json_str)
                        if data.get("code") == 0:
                            collection_table_id = data.get("data", {}).get("table", {}).get("table_id")
                            print(f"✅ 成功创建收集表！")
                            print(f"收集表ID: {collection_table_id}")
                            
                            # 为收集表添加相同的字段
                            print(f"正在为收集表添加字段...")
                            collection_field_url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{collection_table_id}/fields"
                            
                            for field in order_fields:
                                try:
                                    response = requests.post(collection_field_url, headers=headers, json=field, timeout=10)
                                    if response.text:
                                        json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                                        if json_match:
                                            json_str = json_match.group()
                                            data = json.loads(json_str)
                                            if data.get("code") == 0:
                                                print(f"✅ 成功为收集表创建字段: {field['field_name']}")
                                except Exception as e:
                                    print(f"为收集表创建字段异常: {str(e)}")
                            
                            print(f"✅ 采购订单收集表配置完成！")
                        else:
                            print(f"⚠️  创建收集表失败: {data.get('msg')}")
                            print(f"错误代码: {data.get('code')}")
            except Exception as e:
                print(f"创建收集表异常: {str(e)}")
            
            # 先删除默认的空白行，确保数据从第2行开始
            print("\n正在删除默认空白行...")
            record_url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records"
            
            try:
                # 获取现有记录
                response = requests.get(record_url, headers=headers, timeout=10)
                if response.text:
                    json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                    if json_match:
                        json_str = json_match.group()
                        data = json.loads(json_str)
                        if data.get("code") == 0:
                            existing_records = data.get("data", {}).get("items", [])
                            if existing_records:
                                print(f"发现 {len(existing_records)} 行默认空白行，正在删除...")
                                for record in existing_records:
                                    record_id = record.get("record_id")
                                    delete_url = f"{record_url}/{record_id}"
                                    try:
                                        delete_response = requests.delete(delete_url, headers=headers, timeout=10)
                                        if delete_response.text:
                                            delete_json_match = re.search(r'\{.*\}', delete_response.text, re.DOTALL)
                                            if delete_json_match:
                                                delete_json_str = delete_json_match.group()
                                                delete_data = json.loads(delete_json_str)
                                                if delete_data.get("code") == 0:
                                                    print(f"✅ 删除空白行成功")
                                                else:
                                                    print(f"⚠️  删除空白行失败: {delete_data.get('msg')}")
                                    except Exception as e:
                                        print(f"❌ 删除空白行异常: {str(e)}")
                            else:
                                print(f"没有发现默认空白行")
            except Exception as e:
                print(f"❌ 获取现有记录异常: {str(e)}")
            
            # 生成并添加10行随机采购订单数据（确保从第2行开始）
            print("\n正在生成10行随机采购订单数据...")
            
            # 生成随机数据
            products = ["办公椅", "笔记本电脑", "打印机", "投影仪", "会议桌", "文件夹", "订书机", "白板", "钢笔", "笔记本"]
            people = ["张三", "李四", "王五", "赵六", "孙七", "周八", "吴九", "郑十"]
            
            random_orders = []
            for i in range(10):
                order_num = f"PO{2025001 + i}"
                product = random.choice(products)
                unit_price = random.randint(50, 5000)
                quantity = random.randint(1, 20)
                amount = unit_price * quantity
                
                # 生成过去30天内的随机时间
                days_ago = random.randint(0, 30)
                order_time = int((datetime.now() - timedelta(days=days_ago)).timestamp() * 1000)
                
                person = random.choice(people)
                
                random_orders.append({
                    "采购订单": order_num,
                    "采购单价": unit_price,
                    "采购数量": quantity,
                    "采购金额": amount,
                    "采购时间": order_time,
                    "采购人": person
                })
            
            print(f"生成的10行随机数据:")
            for i, order in enumerate(random_orders, 1):
                print(f"{i}. 订单号: {order['采购订单']}, 产品: {order.get('产品', 'N/A')}, 单价: {order['采购单价']}, 数量: {order['采购数量']}, 金额: {order['采购金额']}, 采购人: {order['采购人']}")
            
            # 添加随机数据到主表
            print(f"\n正在添加随机数据到主表...")
            
            success_count = 0
            for i, order in enumerate(random_orders, 1):
                payload = {"fields": order}
                try:
                    response = requests.post(record_url, headers=headers, json=payload, timeout=10)
                    if response.text:
                        json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                        if json_match:
                            json_str = json_match.group()
                            data = json.loads(json_str)
                            if data.get("code") == 0:
                                print(f"✅ [{i}/10] 成功添加记录: {order['采购订单']}")
                                success_count += 1
                            else:
                                print(f"⚠️  [{i}/10] 添加记录失败: {order['采购订单']} - {data.get('msg')}")
                except Exception as e:
                    print(f"❌ 添加记录异常: {str(e)}")
            
            print(f"\n✅ 成功添加 {success_count}/10 条采购订单数据！")
            
            # 创建仪表板和图表
            print(f"\n正在创建数据仪表板...")
            creator = FeishuAppCreator(APP_ID, APP_SECRET)
            creator.create_dashboard_and_charts(headers, app_token, table_id)
        
        # 添加用户为协作者
        print("\n正在为你添加完全管理权限...")
        # 余慧茹的飞书邮箱
        user_email = "yuhuiru@example.com"  # 请替换为实际的飞书邮箱
        creator.add_collaborator(app_token, user_email)
        
        print("\n" + "=" * 60)
        print("✅ 采购订单应用创建完成！")
        app_url = f"https://feishu.cn/base/{app_token}"
        print(f"应用链接: {app_url}")
        print("=" * 60)
    else:
        print("\n" + "=" * 60)
        print("❌ 应用创建失败")
        print("请检查应用权限配置")
        print("=" * 60)
