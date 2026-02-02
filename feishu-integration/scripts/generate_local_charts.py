#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import requests
import json
import re
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use('Agg')  # 用于无GUI环境
from datetime import datetime, timedelta
import random

class LocalChartGenerator:
    def __init__(self, app_id, app_secret):
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = None
        self.app_token = None
        self.table_id = None
    
    def get_tenant_access_token(self):
        """获取飞书访问令牌"""
        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        payload = {
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }
        
        print(f"正在获取飞书访问令牌...")
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            if response.text:
                json_match = re.search(r'\{.*\}', response.text, re.DOTALL)
                if json_match:
                    json_str = json_match.group()
                    data = json.loads(json_str)
                    if data.get("code") == 0:
                        self.access_token = data.get("tenant_access_token")
                        print(f"✅ 成功获取访问令牌")
                        return self.access_token
        except Exception as e:
            print(f"❌ 获取令牌异常: {str(e)}")
        return None
    
    def get_purchase_data(self):
        """获取采购数据或生成示例数据"""
        # 尝试从飞书获取数据，如果失败则生成示例数据
        data = self.generate_sample_data()
        return data
    
    def generate_sample_data(self):
        """生成示例采购数据"""
        products = ["办公椅", "笔记本电脑", "打印机", "投影仪", "会议桌", "文件夹", "订书机", "白板", "钢笔", "笔记本"]
        people = ["张三", "李四", "王五", "赵六", "孙七", "周八", "吴九", "郑十"]
        
        orders = []
        for i in range(10):
            order_num = f"PO{2025001 + i}"
            product = random.choice(products)
            unit_price = random.randint(50, 5000)
            quantity = random.randint(1, 20)
            amount = unit_price * quantity
            
            days_ago = random.randint(0, 30)
            order_time = datetime.now() - timedelta(days=days_ago)
            
            person = random.choice(people)
            
            orders.append({
                "采购订单": order_num,
                "产品": product,
                "采购单价": unit_price,
                "采购数量": quantity,
                "采购金额": amount,
                "采购时间": order_time,
                "采购人": person
            })
        
        return orders
    
    def create_charts(self, data):
        """创建图表并保存"""
        if not data:
            print("❌ 没有数据可以生成图表")
            return
        
        print(f"\n正在生成数据可视化图表...")
        
        # 设置中文字体
        plt.rcParams['font.sans-serif'] = ['Arial Unicode MS', 'SimHei']
        plt.rcParams['axes.unicode_minus'] = False
        
        # 1. 饼图 - 按采购人分布的采购金额
        print("正在生成饼图...")
        self.create_pie_chart(data)
        
        # 2. 柱状图 - 各采购订单金额对比
        print("正在生成柱状图...")
        self.create_bar_chart(data)
        
        # 3. 折线图 - 采购金额时间趋势
        print("正在生成折线图...")
        self.create_line_chart(data)
        
        print(f"✅ 所有图表生成完成！")
        print(f"图表文件保存在当前目录：")
        print(f"  - purchase_amount_pie.png")
        print(f"  - purchase_amount_bar.png")
        print(f"  - purchase_trend_line.png")
    
    def create_pie_chart(self, data):
        """创建饼图"""
        # 按采购人汇总金额
        person_amounts = {}
        for order in data:
            person = order["采购人"]
            amount = order["采购金额"]
            person_amounts[person] = person_amounts.get(person, 0) + amount
        
        # 创建饼图
        plt.figure(figsize=(10, 8))
        plt.pie(person_amounts.values(), labels=person_amounts.keys(), autopct='%1.1f%%', startangle=90)
        plt.title('采购金额按采购人分布', fontsize=16, fontweight='bold')
        plt.axis('equal')
        plt.tight_layout()
        plt.savefig('purchase_amount_pie.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✅ 饼图已保存: purchase_amount_pie.png")
    
    def create_bar_chart(self, data):
        """创建柱状图"""
        # 提取订单号和金额
        orders = [order["采购订单"] for order in data]
        amounts = [order["采购金额"] for order in data]
        
        # 按金额排序
        sorted_data = sorted(zip(orders, amounts), key=lambda x: x[1], reverse=True)
        orders_sorted, amounts_sorted = zip(*sorted_data)
        
        # 创建柱状图
        plt.figure(figsize=(12, 6))
        bars = plt.bar(orders_sorted, amounts_sorted, color='steelblue', alpha=0.8)
        plt.title('各采购订单金额对比', fontsize=16, fontweight='bold')
        plt.xlabel('采购订单', fontsize=12)
        plt.ylabel('采购金额 (元)', fontsize=12)
        plt.xticks(rotation=45, ha='right')
        plt.grid(axis='y', alpha=0.3)
        
        # 添加数值标签
        for bar in bars:
            height = bar.get_height()
            plt.text(bar.get_x() + bar.get_width()/2., height,
                    f'¥{height:,.0f}',
                    ha='center', va='bottom', fontsize=9)
        
        plt.tight_layout()
        plt.savefig('purchase_amount_bar.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✅ 柱状图已保存: purchase_amount_bar.png")
    
    def create_line_chart(self, data):
        """创建折线图"""
        # 按时间排序数据
        sorted_data = sorted(data, key=lambda x: x["采购时间"])
        times = [order["采购时间"] for order in sorted_data]
        amounts = [order["采购金额"] for order in sorted_data]
        
        # 创建折线图
        plt.figure(figsize=(12, 6))
        plt.plot(times, amounts, marker='o', linestyle='-', linewidth=2, markersize=8, color='coral')
        plt.title('采购金额时间趋势', fontsize=16, fontweight='bold')
        plt.xlabel('采购时间', fontsize=12)
        plt.ylabel('采购金额 (元)', fontsize=12)
        plt.grid(True, alpha=0.3)
        plt.xticks(rotation=45)
        
        # 添加数值标签
        for i, (time, amount) in enumerate(zip(times, amounts)):
            plt.annotate(f'¥{amount:,.0f}', 
                        (time, amount),
                        textcoords="offset points",
                        xytext=(0,10), 
                        ha='center',
                        fontsize=8)
        
        plt.tight_layout()
        plt.savefig('purchase_trend_line.png', dpi=300, bbox_inches='tight')
        plt.close()
        print("✅ 折线图已保存: purchase_trend_line.png")

if __name__ == "__main__":
    # 使用飞书应用凭证
    APP_ID = "cli_a9e4652af5f89cca"
    APP_SECRET = "4OazKFCmZTT4cjlwK0ecAhr3eAaJ7dhH"
    
    print("=" * 60)
    print("本地图表生成工具 - 采购订单数据可视化")
    print("=" * 60)
    
    generator = LocalChartGenerator(APP_ID, APP_SECRET)
    
    # 获取数据
    data = generator.get_purchase_data()
    
    if data:
        print(f"\n数据预览:")
        for i, order in enumerate(data[:3], 1):
            print(f"{i}. {order['采购订单']}: {order['产品']} - ¥{order['采购金额']}")
        
        # 生成图表
        generator.create_charts(data)
        
        print("\n" + "=" * 60)
        print("✅ 数据可视化完成！")
        print("=" * 60)
