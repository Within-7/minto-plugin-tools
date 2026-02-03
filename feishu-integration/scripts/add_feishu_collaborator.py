#!/usr/bin/env python3
# -*- encoding: utf-8 -*-

import requests
import json

class FeishuCollaboratorClient:
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
        
        print("正在获取飞书访问令牌...")
        
        try:
            response = requests.post(url, json=payload, timeout=10)
            data = response.json()
            
            if data.get("code") == 0:
                self.access_token = data.get("tenant_access_token")
                print("✅ 成功获取访问令牌")
                return self.access_token
            else:
                print(f"❌ 获取令牌失败: {data.get('msg')}")
                return None
                
        except Exception as e:
            print(f"❌ 请求异常: {str(e)}")
            return None
    
    def add_collaborator_via_permission_api(self, app_token, member_id, member_type="user", perm="view"):
        """通过权限API V2添加协作者"""
        if not self.access_token:
            self.get_tenant_access_token()
        
        # 使用权限API V2
        url = "https://open.feishu.cn/open-apis/permission/v2/permissions/add_member"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"
        }
        
        # 构建表单数据
        payload = {
            "resource_type": "bitable",  # 多维表格
            "resource_id": app_token,    # 表格的app_token
            "perm_type": perm,           # view/edit/full_access
            "member_type": member_type,  # user/group/department/role
            "member_id": member_id       # 成员ID
        }
        
        print(f"\n正在通过权限API V2添加协作者...")
        print(f"请求URL: {url}")
        print(f"请求参数: {payload}")
        
        try:
            response = requests.post(url, headers=headers, data=payload, timeout=10)
            
            print(f"\n响应状态码: {response.status_code}")
            print(f"原始响应内容: {response.text[:500]}")
            
            data = response.json()
            print(f"解析后的JSON: {json.dumps(data, ensure_ascii=False, indent=2)}")
            
            if data.get("code") == 0:
                print(f"✅ 成功添加协作者！")
                return True
            else:
                error_code = data.get("code")
                error_msg = data.get("msg")
                print(f"❌ 添加协作者失败")
                print(f"错误码: {error_code}")
                print(f"错误信息: {error_msg}")
                
                # 常见错误提示
                if error_code == 99991663:
                    print("提示: 应用没有 '添加协作者' 权限，需要在飞书开放平台开通:")
                    print("  - permission:permission.member.create")
                    print("  - 或者权限包: '分享云文档'")
                elif error_code == 99991401:
                    print("提示: app_token 不正确或应用无权访问该表格")
                elif error_code == 7104:
                    print("提示: member_id 格式不正确，应该是 open_id (ou_xxxxx)")
                
                return False
                
        except Exception as e:
            print(f"❌ 请求异常: {str(e)}")
            import traceback
            print(f"详细错误信息:\n{traceback.format_exc()}")
            return False
    
    def get_app_roles_v2(self, app_token):
        """尝试使用高级权限V2 API获取角色列表"""
        if not self.access_token:
            self.get_tenant_access_token()
        
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/app_roles"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        print(f"\n尝试使用高级权限V2 API获取角色列表...")
        print(f"请求URL: {url}")
        
        try:
            response = requests.get(url, headers=headers, timeout=10)
            data = response.json()
            
            print(f"响应状态码: {response.status_code}")
            print(f"解析后的JSON: {json.dumps(data, ensure_ascii=False, indent=2)}")
            
            if data.get("code") == 0:
                roles = data.get("data", {}).get("items", [])
                print(f"✅ 获取到 {len(roles)} 个角色")
                return roles
            else:
                print(f"❌ 高级权限API不可用: {data.get('msg')}")
                return None
                
        except Exception as e:
            print(f"❌ 请求异常: {str(e)}")
            return None
    
    def add_collaborator_to_role(self, app_token, role_id, member_id, member_type="user", member_id_type="open_id"):
        """添加协作者到高级权限角色"""
        if not self.access_token:
            self.get_tenant_access_token()
        
        url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/app_roles/{role_id}/members"
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Content-Type": "application/json"
        }
        
        payload = {
            "member_type": member_type,
            "member_id": member_id,
            "member_id_type": member_id_type
        }
        
        print(f"\n正在添加协作者到高级权限角色...")
        print(f"请求URL: {url}")
        print(f"请求体: {json.dumps(payload, ensure_ascii=False, indent=2)}")
        
        try:
            response = requests.post(url, headers=headers, json=payload, timeout=10)
            
            print(f"\n响应状态码: {response.status_code}")
            data = response.json()
            print(f"解析后的JSON: {json.dumps(data, ensure_ascii=False, indent=2)}")
            
            if data.get("code") == 0:
                result = data.get("data", {}).get("result")
                if result:
                    print(f"✅ 成功添加协作者！")
                    return True
                else:
                    print(f"❌ 添加失败: {data.get('data', {}).get('msg')}")
                    return False
            else:
                print(f"❌ 添加协作者失败: {data.get('msg')}")
                return False
                
        except Exception as e:
            print(f"❌ 请求异常: {str(e)}")
            return False

if __name__ == "__main__":
    # 使用提供的飞书应用凭证
    APP_ID = "cli_a9e4652af5f89cca"
    APP_SECRET = "4OazKFCmZTT4cjlwK0ecAhr3eAaJ7dhH"
    
    # 要添加的协作者信息
    MEMBER_ID = "ou_31ec8c3772b60ed46d16ed23e4eda331"  # 你的 open_id
    APP_TOKEN = "MaHdbMV0WaZfwJsIUqwclxfgnQg"
    
    print("=" * 60)
    print("飞书多维表格协作者添加工具")
    print("=" * 60)
    
    client = FeishuCollaboratorClient(APP_ID, APP_SECRET)
    
    # 策略1: 尝试使用高级权限API
    print("\n策略1: 尝试使用高级权限API...")
    roles = client.get_app_roles_v2(APP_TOKEN)
    
    if roles:
        print(f"\n可用角色列表:")
        for i, role in enumerate(roles):
            role_id = role.get("role_id")
            role_name = role.get("role_name")
            print(f"{i+1}. {role_name} (ID: {role_id})")
        
        # 默认添加到第一个角色
        if roles:
            selected_role = roles[0]
            role_id = selected_role.get("role_id")
            role_name = selected_role.get("role_name")
            
            print(f"\n选择角色: {role_name}")
            success = client.add_collaborator_to_role(APP_TOKEN, role_id, MEMBER_ID)
            
            if success:
                print(f"\n{'=' * 60}")
                print("✅ 协作者添加完成！")
                print(f"{'=' * 60}")
                exit(0)
    
    # 策略2: 使用权限API V2
    print(f"\n策略2: 使用权限API V2...")
    print("请选择权限类型:")
    print("1. 查看权限 (view)")
    print("2. 编辑权限 (edit)")
    print("3. 完全管理权限 (full_access)")
    
    perm_choice = input("请输入选择 (1/2/3，默认1): ").strip()
    if perm_choice == "2":
        perm = "edit"
    elif perm_choice == "3":
        perm = "full_access"
    else:
        perm = "view"
    
    print(f"\n选择的权限: {perm}")
    success = client.add_collaborator_via_permission_api(APP_TOKEN, MEMBER_ID, member_type="user", perm=perm)
    
    if success:
        print(f"\n{'=' * 60}")
        print("✅ 协作者添加完成！")
        print(f"{'=' * 60}")
    else:
        print(f"\n{'=' * 60}")
        print("❌ 协作者添加失败")
        print("提示: 请确保飞书应用已添加相关权限")
        print(f"{'=' * 60}")