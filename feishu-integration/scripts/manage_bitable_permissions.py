#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

"""
飞书多维表格用户编辑权限管理工具
使用飞书官方SDK: lark-oapi
"""

import json
import sys

try:
    import lark_oapi as lark
    from lark_oapi.api.drive.v1 import CreatePermissionMemberRequest, BaseMember
except ImportError:
    print("❌ 缺少飞书SDK，请先安装:")
    print("pip install lark-oapi")
    sys.exit(1)


class FeishuPermissionManager:
    """飞书多维表格用户编辑权限管理工具（使用官方SDK）"""
    
    def __init__(self, app_id, app_secret):
        self.app_id = app_id
        self.app_secret = app_secret
        self.client = lark.Client.builder() \
            .app_id(app_id) \
            .app_secret(app_secret) \
            .log_level(lark.LogLevel.INFO) \
            .build()
    
    def add_member(self, token, member_id, perm="edit", member_type="openid", need_notification=True):
        """
        添加成员到多维表格
        
        Args:
            token: 多维表格的 app_token
            member_id: 成员ID（open_id 或 union_id 或 user_id）
            perm: 权限类型
                - "view": 查看权限
                - "edit": 编辑权限
                - "full_access": 完全管理权限
            member_type: 成员类型
                - "openid": open_id
                - "unionid": union_id
                - "userid": user_id
            need_notification: 是否发送通知
        
        Returns:
            bool: 成功返回True，失败返回False
        """
        # 构造请求对象
        request = CreatePermissionMemberRequest.builder() \
            .token(token) \
            .type("bitable") \
            .need_notification(need_notification) \
            .request_body(BaseMember.builder()
                .member_type(member_type)
                .member_id(member_id)
                .perm(perm)
                .build()) \
            .build()
        
        # 发起请求
        response = self.client.drive.v1.permission_member.create(request)
        
        # 处理结果
        if not response.success():
            print(f"❌ 添加成员失败:")
            print(f"   错误码: {response.code}")
            print(f"   错误信息: {response.msg}")
            print(f"   日志ID: {response.get_log_id()}")
            
            # 打印详细错误信息
            try:
                error_data = json.loads(response.raw.content)
                print(f"   详细错误: {json.dumps(error_data, indent=4, ensure_ascii=False)}")
            except:
                pass
            
            return False
        
        print(f"✅ 成功添加成员!")
        print(f"   成员ID: {member_id}")
        print(f"   权限: {perm}")
        
        return True
    
    def batch_add_members(self, token, members, need_notification=True):
        """
        批量添加成员到多维表格
        
        Args:
            token: 多维表格的 app_token
            members: 成员列表，每个成员是包含 member_id, perm, member_type 的字典
            need_notification: 是否发送通知
        
        Returns:
            dict: {"success": 成功数量, "failed": 失败数量, "results": 结果列表}
        """
        results = {
            "success": 0,
            "failed": 0,
            "results": []
        }
        
        print(f"\n正在批量添加 {len(members)} 个成员...")
        
        for i, member in enumerate(members, 1):
            member_id = member.get("member_id")
            perm = member.get("perm", "edit")
            member_type = member.get("member_type", "openid")
            
            print(f"\n[{i}/{len(members)}] 添加成员: {member_id}")
            
            success = self.add_member(token, member_id, perm, member_type, need_notification)
            
            results["results"].append({
                "member_id": member_id,
                "success": success
            })
            
            if success:
                results["success"] += 1
            else:
                results["failed"] += 1
        
        return results


def main():
    """主函数 - 交互式命令行工具"""
    
    # 配置信息
    APP_ID = "cli_a9e4652af5f89cca"
    APP_SECRET = "4OazKFCmZTT4cjlwK0ecAhr3eAaJ7dhH"
    
    print("=" * 70)
    print("飞书多维表格 - 用户编辑权限管理工具")
    print("使用飞书官方SDK")
    print("=" * 70)
    
    # 初始化客户端
    manager = FeishuPermissionManager(APP_ID, APP_SECRET)
    
    # 获取表格信息
    print("\n请输入表格信息:")
    APP_TOKEN = input("表格 APP_TOKEN: ").strip()
    
    if not APP_TOKEN:
        print("❌ APP_TOKEN 不能为空")
        sys.exit(1)
    
    # 选择操作类型
    print("\n请选择操作:")
    print("1. 添加单个成员")
    print("2. 批量添加成员")
    
    choice = input("\n请输入选择 (1/2): ").strip()
    
    if choice == "1":
        # 添加单个成员
        print("\n请输入成员信息:")
        member_id = input("成员 Open ID: ").strip()
        
        if not member_id:
            print("❌ 成员ID不能为空")
            sys.exit(1)
        
        print("\n请选择权限类型:")
        print("1. 查看权限 (view)")
        print("2. 编辑权限 (edit)")
        print("3. 完全管理权限 (full_access)")
        
        perm_choice = input("请输入选择 (1/2/3, 默认2): ").strip()
        if perm_choice == "1":
            perm = "view"
        elif perm_choice == "3":
            perm = "full_access"
        else:
            perm = "edit"
        
        # 添加成员
        if manager.add_member(APP_TOKEN, member_id, perm):
            print(f"\n{'=' * 70}")
            print("✅ 成员添加成功!")
            print(f"{'=' * 70}")
        else:
            print(f"\n{'=' * 70}")
            print("❌ 成员添加失败")
            print(f"{'=' * 70}")
    
    elif choice == "2":
        # 批量添加成员
        print("\n请输入成员信息 (每行一个成员ID，格式: member_id,perm)")
        print("示例: ou_xxxxx,edit")
        print("输入完成后按 Ctrl+D (Mac/Linux) 或 Ctrl+Z (Windows) 结束输入")
        
        members = []
        try:
            while True:
                line = input()
                line = line.strip()
                if not line:
                    continue
                
                parts = line.split(',')
                if len(parts) >= 1:
                    member_id = parts[0].strip()
                    perm = parts[1].strip() if len(parts) > 1 else "edit"
                    
                    members.append({
                        "member_id": member_id,
                        "perm": perm,
                        "member_type": "openid"
                    })
        except EOFError:
            pass
        
        if not members:
            print("❌ 未输入任何成员")
            sys.exit(1)
        
        # 批量添加
        results = manager.batch_add_members(APP_TOKEN, members)
        
        # 输出结果
        print(f"\n{'=' * 70}")
        print("批量添加完成!")
        print(f"成功: {results['success']} 个")
        print(f"失败: {results['failed']} 个")
        print(f"{'=' * 70}")
    
    else:
        print("❌ 无效的选择")
        sys.exit(1)


if __name__ == "__main__":
    main()
