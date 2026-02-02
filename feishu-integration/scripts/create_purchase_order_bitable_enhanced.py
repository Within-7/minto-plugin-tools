#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import requests
import json
import re
from datetime import datetime

class FeishuPurchaseOrderClient:
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
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            print(f"响应状态码: {response.status_code}")
            
            if not response.text:
                print("❌ 服务器返回空响应")
                return None
            
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
    
    def delete_all_default_records(self):
        """删除所有默认的空记录"""
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables/{self.table_id}/records"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        try:
            # 获取所有记录
            response = requests.get(url, headers=headers, timeout=10)
            if response.text:
                json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                if json_match:
                    json_str = json_match.group()
                    data = json.loads(json_str)
                    if data.get("code") == 0:
                        records = data.get("data", {}).get("items", [])
                        
                        if not records:
                            print("✅ 没有默认记录需要删除")
                            return
                        
                        print(f"发现 {len(records)} 条默认记录，正在删除...")
                        deleted_count = 0
                        
                        # 删除所有记录
                        for record in records:
                            record_id = record.get("record_id")
                            delete_url = f"{url}/{record_id}"
                            delete_response = requests.delete(delete_url, headers=headers, timeout=10)
                            
                            if delete_response.status_code == 200:
                                deleted_count += 1
                        
                        print(f"✅ 共删除 {deleted_count} 条默认记录")
                        
        except Exception as e:
            print(f"删除默认记录时出错: {str(e)}")
    
    def delete_all_default_fields(self):
        """删除所有默认字段（前10个）"""
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables/{self.table_id}/fields"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.text:
                json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                if json_match:
                    json_str = json_match.group()
                    data = json.loads(json_str)
                    if data.get("code") == 0:
                        fields = data.get("data", {}).get("items", [])
                        
                        # 删除前10个字段（默认字段）
                        deleted_count = 0
                        for i, field in enumerate(fields[:10]):  # 只处理前10个
                            field_id = field.get("field_id")
                            field_name = field.get("field_name", f"字段{i+1}")
                            
                            delete_url = f"{url}/{field_id}"
                            delete_response = requests.delete(delete_url, headers=headers, timeout=10)
                            
                            if delete_response.status_code == 200:
                                print(f"✅ 删除默认字段 {i+1}/10: {field_name}")
                                deleted_count += 1
                            else:
                                print(f"⚠️  删除字段失败: {field_name}")
                        
                        print(f"✅ 共删除 {deleted_count} 个默认字段")
                        
        except Exception as e:
            print(f"删除默认字段时出错: {str(e)}")
    
    def delete_default_fields(self):
        """删除默认字段"""
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables/{self.table_id}/fields"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            if response.text:
                json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                if json_match:
                    json_str = json_match.group()
                    data = json.loads(json_str)
                    if data.get("code") == 0:
                        fields = data.get("data", {}).get("items", [])
                        default_names = ["文本", "单选", "日期", "附件", "多选", "号码", "复选框"]
                        
                        for field in fields:
                            field_name = field.get("field_name")
                            field_id = field.get("field_id")
                            if field_name in default_names:
                                delete_url = f"{url}/{field_id}"
                                requests.delete(delete_url, headers=headers, timeout=10)
                                print(f"✅ 删除默认字段: {field_name}")
        except Exception as e:
            print(f"删除默认字段时出错: {str(e)}")
    
    def create_table_fields(self):
        """创建完整的采购订单字段"""
        if not self.app_token or not self.table_id:
            print("❌ 缺少必要的token信息")
            return False
        
        print(f"\n正在删除默认字段和记录...")
        self.delete_all_default_records()  # 先删除默认记录
        self.delete_all_default_fields()   # 再删除默认字段
        
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables/{self.table_id}/fields"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        # 定义完整的采购订单字段（20个字段）
        fields = [
            {
                "field_name": "订单编号",
                "type": 1
            },
            {
                "field_name": "采购主题",
                "type": 1
            },
            {
                "field_name": "供应商名称",
                "type": 1
            },
            {
                "field_name": "供应商联系人",
                "type": 1
            },
            {
                "field_name": "供应商电话",
                "type": 1
            },
            {
                "field_name": "采购物品",
                "type": 1
            },
            {
                "field_name": "规格型号",
                "type": 1
            },
            {
                "field_name": "单位",
                "type": 1
            },
            {
                "field_name": "采购数量",
                "type": 2
            },
            {
                "field_name": "单价",
                "type": 2
            },
            {
                "field_name": "采购金额",
                "type": 2
            },
            {
                "field_name": "申请部门",
                "type": 1
            },
            {
                "field_name": "采购申请人",
                "type": 1
            },
            {
                "field_name": "采购时间",
                "type": 5
            },
            {
                "field_name": "要求交货日期",
                "type": 5
            },
            {
                "field_name": "实际交货日期",
                "type": 5
            },
            {
                "field_name": "付款方式",
                "type": 1
            },
            {
                "field_name": "订单状态",
                "type": 1
            },
            {
                "field_name": "审批人",
                "type": 1
            },
            {
                "field_name": "备注说明",
                "type": 1
            }
        ]
        
        print(f"\n正在创建{len(fields)}个采购订单字段...")
        
        success_count = 0
        for i, field in enumerate(fields, 1):
            try:
                response = requests.post(url, headers=headers, json=field, timeout=10)
                print(f"[{i}/{len(fields)}] 创建字段 '{field['field_name']}' - 状态码: {response.status_code}")
                
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
        
        print(f"\n字段创建完成: {success_count}/{len(fields)} 成功")
        return success_count == len(fields)
    
    def add_sample_records(self):
        """添加示例采购订单数据"""
        if not self.app_token or not self.table_id:
            print("❌ 缺少必要的token信息")
            return False
        
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{self.app_token}/tables/{self.table_id}/records"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        # 生成示例数据
        records = [
            {
                "订单编号": "PO202401001",
                "采购主题": "办公电脑采购",
                "供应商名称": "北京科技有限公司",
                "供应商联系人": "张经理",
                "供应商电话": "13800138001",
                "采购物品": "笔记本电脑",
                "规格型号": "ThinkPad X1 Carbon",
                "单位": "台",
                "采购数量": 10,
                "单价": 8500,
                "采购金额": 85000,
                "申请部门": "技术部",
                "采购申请人": "李明",
                "采购时间": 1705776000000,
                "要求交货日期": 1706208000000,
                "实际交货日期": 1706121600000,
                "付款方式": "货到付款",
                "订单状态": "已完成",
                "审批人": "王总",
                "备注说明": "急需配置，请尽快发货"
            },
            {
                "订单编号": "PO202401002",
                "采购主题": "办公室家具采购",
                "供应商名称": "上海家具有限公司",
                "供应商联系人": "刘经理",
                "供应商电话": "13900139002",
                "采购物品": "办公椅",
                "规格型号": "人体工学椅H5",
                "单位": "把",
                "采购数量": 50,
                "单价": 1200,
                "采购金额": 60000,
                "申请部门": "行政部",
                "采购申请人": "陈芳",
                "采购时间": 1705862400000,
                "要求交货日期": 1706294400000,
                "实际交货日期": 1706294400000,
                "付款方式": "月结30天",
                "订单状态": "已完成",
                "审批人": "赵总",
                "备注说明": "需要安装服务"
            },
            {
                "订单编号": "PO202401003",
                "采购主题": "网络设备采购",
                "供应商名称": "深圳网络设备公司",
                "供应商联系人": "周工",
                "供应商电话": "13700137003",
                "采购物品": "企业路由器",
                "规格型号": "AR6280",
                "单位": "台",
                "采购数量": 2,
                "单价": 15000,
                "采购金额": 30000,
                "申请部门": "技术部",
                "采购申请人": "王强",
                "采购时间": 1705948800000,
                "要求交货日期": 1706380800000,
                "实际交货日期": 0,
                "付款方式": "预付50%",
                "订单状态": "采购中",
                "审批人": "王总",
                "备注说明": "需要技术支持，含3年质保"
            },
            {
                "订单编号": "PO202401004",
                "采购主题": "打印纸采购",
                "供应商名称": "广州办公用品公司",
                "供应商联系人": "吴经理",
                "供应商电话": "13600136004",
                "采购物品": "A4打印纸",
                "规格型号": "70g 500张/包",
                "单位": "包",
                "采购数量": 200,
                "单价": 25,
                "采购金额": 5000,
                "申请部门": "行政部",
                "采购申请人": "陈芳",
                "采购时间": 1706035200000,
                "要求交货日期": 1706467200000,
                "实际交货日期": 0,
                "付款方式": "货到付款",
                "订单状态": "已批准",
                "审批人": "赵总",
                "备注说明": "每月定期采购"
            },
            {
                "订单编号": "PO202401005",
                "采购主题": "会议桌采购",
                "供应商名称": "东莞家具制造厂",
                "供应商联系人": "郑经理",
                "供应商电话": "13500135005",
                "采购物品": "大会议桌",
                "规格型号": "定制 4米×1.2米",
                "单位": "张",
                "采购数量": 1,
                "单价": 18000,
                "采购金额": 18000,
                "申请部门": "行政部",
                "采购申请人": "陈芳",
                "采购时间": 1706121600000,
                "要求交货日期": 1706726400000,
                "实际交货日期": 0,
                "付款方式": "预付30%，尾款货到付清",
                "订单状态": "待审批",
                "审批人": "",
                "备注说明": "需要现场测量尺寸"
            },
            {
                "订单编号": "PO202401006",
                "采购主题": "服务器设备采购",
                "供应商名称": "杭州系统集成公司",
                "供应商联系人": "孙工程师",
                "供应商电话": "13400134006",
                "采购物品": "机架式服务器",
                "规格型号": "Dell R740",
                "单位": "台",
                "采购数量": 3,
                "单价": 45000,
                "采购金额": 135000,
                "申请部门": "技术部",
                "采购申请人": "李明",
                "采购时间": 1706208000000,
                "要求交货日期": 1706812800000,
                "实际交货日期": 0,
                "付款方式": "分期付款",
                "订单状态": "待审批",
                "审批人": "",
                "备注说明": "包含安装调试服务，需提供培训"
            },
            {
                "订单编号": "PO202401007",
                "采购主题": "空调设备采购",
                "供应商名称": "珠海电器公司",
                "供应商联系人": "钱经理",
                "供应商电话": "13300133007",
                "采购物品": "中央空调",
                "规格型号": "5匹风管机",
                "单位": "台",
                "采购数量": 8,
                "单价": 12000,
                "采购金额": 96000,
                "申请部门": "行政部",
                "采购申请人": "陈芳",
                "采购时间": 1706294400000,
                "要求交货日期": 1706899200000,
                "实际交货日期": 0,
                "付款方式": "货到付款",
                "订单状态": "已取消",
                "审批人": "赵总",
                "备注说明": "预算不足，暂缓采购"
            },
            {
                "订单编号": "PO202401008",
                "采购主题": "投影仪采购",
                "供应商名称": "北京科技有限公司",
                "供应商联系人": "张经理",
                "供应商电话": "13800138001",
                "采购物品": "高清投影仪",
                "规格型号": "Epson X500",
                "单位": "台",
                "采购数量": 5,
                "单价": 6000,
                "采购金额": 30000,
                "申请部门": "培训部",
                "采购申请人": "林华",
                "采购时间": 1706380800000,
                "要求交货日期": 1706985600000,
                "实际交货日期": 0,
                "付款方式": "月结",
                "订单状态": "已批准",
                "审批人": "王总",
                "备注说明": "用于培训教室，需要高清效果"
            }
        ]
        
        print(f"\n正在添加{len(records)}条示例采购订单...")
        
        success_count = 0
        for i, record in enumerate(records, 1):
            payload = {"fields": record}
            try:
                response = requests.post(url, headers=headers, json=payload, timeout=10)
                
                if response.text:
                    json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                    if json_match:
                        json_str = json_match.group()
                        data = json.loads(json_str)
                        if data.get("code") == 0:
                            print(f"[{i}/{len(records)}] ✅ 成功添加订单: {record['订单编号']} - {record['采购主题']}")
                            success_count += 1
                        else:
                            print(f"[{i}/{len(records)}] ⚠️  添加订单失败: {record['订单编号']} - {data.get('msg')}")
                    
            except Exception as e:
                print(f"❌ 添加记录异常: {str(e)}")
        
        print(f"\n数据添加完成: {success_count}/{len(records)} 成功")
        return success_count == len(records)

if __name__ == "__main__":
    # 配置飞书应用凭证
    APP_ID = "cli_a9e4652af5f89cca"
    APP_SECRET = "4OazKFCmZTT4cjlwK0ecAhr3eAaJ7dhH"
    
    print("=" * 80)
    print("飞书采购订单多维表格创建工具（完整版）")
    print("=" * 80)
    
    client = FeishuPurchaseOrderClient(APP_ID, APP_SECRET)
    
    # 创建多维表格
    app_token = client.create_bitable("采购订单管理系统")
    
    if app_token:
        # 获取默认数据表
        table_id = client.get_tables()
        
        if table_id:
            # 创建字段（20个字段）
            fields_created = client.create_table_fields()
            
            # 添加示例数据（8条记录）
            if fields_created:
                client.add_sample_records()
        
        print("\n" + "=" * 80)
        print("✅ 采购订单管理系统创建完成！")
        print("=" * 80)
        table_url = f"https://feishu.cn/base/{app_token}"
        print(f"📊 表格链接: {table_url}")
        print(f"📈 数据规模: 8行 x 20列")
        print("\n📋 字段列表:")
        print("1. 订单编号 - 采购订单唯一编号")
        print("2. 采购主题 - 采购项目名称")
        print("3. 供应商名称 - 供应商公司名称")
        print("4. 供应商联系人 - 供应商联系人姓名")
        print("5. 供应商电话 - 供应商联系电话")
        print("6. 采购物品 - 采购的物品名称")
        print("7. 规格型号 - 物品规格型号")
        print("8. 单位 - 计量单位（个/台/套等）")
        print("9. 采购数量 - 采购数量")
        print("10. 单价 - 采购单价（元）")
        print("11. 采购金额 - 总金额=单价×数量")
        print("12. 申请部门 - 申请采购的部门")
        print("13. 采购申请人 - 申请人姓名")
        print("14. 采购时间 - 申请采购日期")
        print("15. 要求交货日期 - 期望的交货日期")
        print("16. 实际交货日期 - 实际交货日期")
        print("17. 付款方式 - 货到付款/月结/预付等")
        print("18. 订单状态 - 待审批/已批准/采购中/已完成/已取消")
        print("19. 审批人 - 订单审批人")
        print("20. 备注说明 - 其他说明信息")
        print("\n💡 提示: 可以在飞书中打开表格，添加协作者进行协作编辑")
        print("=" * 80)
    else:
        print("\n" + "=" * 80)
        print("❌ 多维表格创建失败")
        print("提示: 请确保飞书应用已添加 '多维表格' 相关权限")
        print("=" * 80)
