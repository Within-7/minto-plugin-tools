#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
飞书 MCP 服务器
使用 FastMCP 框架实现的飞书 API 集成
"""

import os
import requests
from typing import Optional
from fastmcp import FastMCP

# 创建 MCP 服务器
mcp = FastMCP("feishu-integration")

# 飞书配置
APP_ID = os.getenv("FEISHU_APP_ID", "")
APP_SECRET = os.getenv("FEISHU_APP_SECRET", "")


class FeishuAPI:
    """飞书 API 客户端"""

    def __init__(self):
        self.app_id = APP_ID
        self.app_secret = APP_SECRET
        self._token = None

    def get_token(self) -> str:
        """获取访问令牌"""
        if self._token:
            return self._token

        if not self.app_id or not self.app_secret:
            raise ValueError("FEISHU_APP_ID and FEISHU_APP_SECRET environment variables are required")

        url = "https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal"
        payload = {
            "app_id": self.app_id,
            "app_secret": self.app_secret
        }

        response = requests.post(url, json=payload, timeout=10)
        data = response.json()

        if data.get("code") != 0:
            raise Exception(f"获取令牌失败: {data.get('msg')}")

        self._token = data.get("tenant_access_token")
        return self._token

    def get_headers(self) -> dict:
        """获取请求头"""
        return {
            "Authorization": f"Bearer {self.get_token()}",
            "Content-Type": "application/json"
        }


# 创建全局 API 客户端
api = FeishuAPI()


@mcp.tool()
def get_tenant_access_token() -> str:
    """获取飞书访问令牌"""
    token = api.get_token()
    return f"✅ 成功获取访问令牌: {token[:20]}..."


@mcp.tool()
def create_bitable(name: str, folder_token: str = "") -> str:
    """
    创建飞书多维表格应用

    Args:
        name: 多维表格名称
        folder_token: 文件夹token（可选，空字符串表示根目录）
    """
    url = "https://open.feishu.cn/open-apis/bitable/v1/apps"
    payload = {
        "name": name,
        "folder_token": folder_token
    }

    response = requests.post(url, headers=api.get_headers(), json=payload, timeout=10)
    data = response.json()

    if data.get("code") != 0:
        raise Exception(f"创建多维表格失败: {data.get('msg')}")

    app_token = data.get("data", {}).get("app", {}).get("app_token")
    app_url = f"https://feishu.cn/base/{app_token}"

    return f"✅ 成功创建多维表格\n应用Token: {app_token}\n应用链接: {app_url}"


@mcp.tool()
def get_tables(app_token: str) -> str:
    """
    获取多维表格中的所有数据表

    Args:
        app_token: 多维表格应用token
    """
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables"

    response = requests.get(url, headers=api.get_headers(), timeout=10)
    data = response.json()

    if data.get("code") != 0:
        raise Exception(f"获取数据表失败: {data.get('msg')}")

    tables = data.get("data", {}).get("items", [])

    result = f"✅ 获取到 {len(tables)} 个数据表:\n"
    for table in tables:
        result += f"- {table.get('table_id')}: {table.get('name')}\n"

    return result


@mcp.tool()
def add_table_field(app_token: str, table_id: str, field_name: str, field_type: int) -> str:
    """
    为数据表添加字段

    Args:
        app_token: 多维表格应用token
        table_id: 数据表ID
        field_name: 字段名称
        field_type: 字段类型（1=文本，2=数字，3=单选，4=多选，5=日期，7=附件，11=电话，12=邮箱，13=网址，15=进度）
    """
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/fields"
    payload = {
        "field_name": field_name,
        "type": field_type
    }

    response = requests.post(url, headers=api.get_headers(), json=payload, timeout=10)
    data = response.json()

    if data.get("code") != 0:
        raise Exception(f"添加字段失败: {data.get('msg')}")

    return f"✅ 成功添加字段: {field_name}"


@mcp.tool()
def add_record(app_token: str, table_id: str, fields: dict) -> str:
    """
    向数据表添加记录

    Args:
        app_token: 多维表格应用token
        table_id: 数据表ID
        fields: 记录字段数据，键值对形式
    """
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records"
    payload = {"fields": fields}

    response = requests.post(url, headers=api.get_headers(), json=payload, timeout=10)
    data = response.json()

    if data.get("code") != 0:
        raise Exception(f"添加记录失败: {data.get('msg')}")

    return f"✅ 成功添加记录"


@mcp.tool()
def get_records(app_token: str, table_id: str, page_size: int = 20) -> str:
    """
    获取数据表中的记录

    Args:
        app_token: 多维表格应用token
        table_id: 数据表ID
        page_size: 每页记录数（默认20）
    """
    import json
    url = f"https://open.feishu.cn/open-apis/bitable/v1/apps/{app_token}/tables/{table_id}/records"
    params = {"page_size": page_size}

    response = requests.get(url, headers=api.get_headers(), params=params, timeout=10)
    data = response.json()

    if data.get("code") != 0:
        raise Exception(f"获取记录失败: {data.get('msg')}")

    records = data.get("data", {}).get("items", [])

    return f"✅ 获取到 {len(records)} 条记录:\n{json.dumps(records, ensure_ascii=False, indent=2)}"


@mcp.tool()
def add_collaborator(app_token: str, member_type: str, member_id: str, perm_type: str) -> str:
    """
    添加协作者到多维表格

    Args:
        app_token: 多维表格应用token
        member_type: 成员类型（user=用户，group=用户组）
        member_id: 成员ID（open_id 或 union_id）
        perm_type: 权限类型（view=查看，edit=编辑，full_access=完全管理）
    """
    url = "https://open.feishu.cn/open-apis/permission/v2/permissions/add_member"

    # 使用 form-data 格式
    payload = {
        "resource_type": "bitable",
        "resource_id": app_token,
        "perm_type": perm_type,
        "member_type": member_type,
        "member_id": member_id
    }

    headers = {
        "Authorization": f"Bearer {api.get_token()}",
        "Content-Type": "application/x-www-form-urlencoded; charset=utf-8"
    }

    response = requests.post(url, headers=headers, data=payload, timeout=10)
    data = response.json()

    if data.get("code") != 0:
        raise Exception(f"添加协作者失败: {data.get('msg')} (code: {data.get('code')})")

    return f"✅ 成功添加协作者: {member_id} ({perm_type})"


@mcp.tool()
def get_user_by_email(email: str) -> str:
    """
    通过邮箱获取用户信息

    Args:
        email: 用户邮箱
    """
    url = "https://open.feishu.cn/open-apis/contact/v3/users/get_by_email"
    payload = {
        "emails": [email],
        "include_resigned": False
    }

    response = requests.post(url, headers=api.get_headers(), json=payload, timeout=10)
    data = response.json()

    if data.get("code") != 0:
        raise Exception(f"获取用户失败: {data.get('msg')}")

    user_list = data.get("data", {}).get("user_list", [])
    if not user_list:
        raise Exception(f"未找到用户: {email}")

    user = user_list[0]
    return f"✅ 找到用户:\n姓名: {user.get('name', 'N/A')}\nOpen ID: {user.get('open_id')}\n邮箱: {email}"


@mcp.resource("feishu://config")
def get_config() -> str:
    """获取当前飞书配置信息"""
    import json
    config = {
        "app_id": f"{APP_ID[:10]}..." if APP_ID else "Not configured",
        "has_secret": bool(APP_SECRET),
        "has_token": bool(api._token)
    }
    return json.dumps(config, ensure_ascii=False, indent=2)


if __name__ == "__main__":
    # 运行 MCP 服务器
    mcp.run()
