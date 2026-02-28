#!/usr/bin/env node

import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
  ListResourcesRequestSchema,
  ReadResourceRequestSchema
} from '@modelcontextprotocol/sdk/types.js';
import axios from 'axios';

class FeishuMCPServer {
  constructor() {
    this.server = new Server(
      {
        name: 'feishu-mcp-server',
        version: '1.0.0',
      },
      {
        capabilities: {
          tools: {},
          resources: {},
        },
      }
    );

    this.appId = process.env.FEISHU_APP_ID || '';
    this.appSecret = process.env.FEISHU_APP_SECRET || '';
    this.accessToken = null;

    this.setupHandlers();
  }

  setupHandlers() {
    // List available tools
    this.server.setRequestHandler(ListToolsRequestSchema, async () => ({
      tools: [
        {
          name: 'get_tenant_access_token',
          description: '获取飞书 tenant_access_token（访问令牌）',
          inputSchema: {
            type: 'object',
            properties: {},
            required: [],
          },
        },
        {
          name: 'create_bitable',
          description: '创建飞书多维表格应用',
          inputSchema: {
            type: 'object',
            properties: {
              name: {
                type: 'string',
                description: '多维表格名称',
              },
              folder_token: {
                type: 'string',
                description: '文件夹token（可选，空字符串表示根目录）',
              },
            },
            required: ['name'],
          },
        },
        {
          name: 'get_tables',
          description: '获取多维表格中的所有数据表',
          inputSchema: {
            type: 'object',
            properties: {
              app_token: {
                type: 'string',
                description: '多维表格应用token',
              },
            },
            required: ['app_token'],
          },
        },
        {
          name: 'add_table_field',
          description: '为数据表添加字段',
          inputSchema: {
            type: 'object',
            properties: {
              app_token: {
                type: 'string',
                description: '多维表格应用token',
              },
              table_id: {
                type: 'string',
                description: '数据表ID',
              },
              field_name: {
                type: 'string',
                description: '字段名称',
              },
              field_type: {
                type: 'number',
                description: '字段类型：1=文本，2=数字，3=单选，4=多选，5=日期，7=附件，11=电话，12=邮箱，13=网址，15=进度',
              },
            },
            required: ['app_token', 'table_id', 'field_name', 'field_type'],
          },
        },
        {
          name: 'add_record',
          description: '向数据表添加记录',
          inputSchema: {
            type: 'object',
            properties: {
              app_token: {
                type: 'string',
                description: '多维表格应用token',
              },
              table_id: {
                type: 'string',
                description: '数据表ID',
              },
              fields: {
                type: 'object',
                description: '记录字段数据，键值对形式',
              },
            },
            required: ['app_token', 'table_id', 'fields'],
          },
        },
        {
          name: 'get_records',
          description: '获取数据表中的记录',
          inputSchema: {
            type: 'object',
            properties: {
              app_token: {
                type: 'string',
                description: '多维表格应用token',
              },
              table_id: {
                type: 'string',
                description: '数据表ID',
              },
              page_size: {
                type: 'number',
                description: '每页记录数（默认20）',
              },
            },
            required: ['app_token', 'table_id'],
          },
        },
        {
          name: 'add_collaborator',
          description: '添加协作者到多维表格',
          inputSchema: {
            type: 'object',
            properties: {
              app_token: {
                type: 'string',
                description: '多维表格应用token',
              },
              member_type: {
                type: 'string',
                description: '成员类型：user（用户）、group（用户组）',
                enum: ['user', 'group'],
              },
              member_id: {
                type: 'string',
                description: '成员ID（open_id 或 union_id）',
              },
              perm_type: {
                type: 'string',
                description: '权限类型：view（查看）、edit（编辑）、full_access（完全管理）',
                enum: ['view', 'edit', 'full_access'],
              },
            },
            required: ['app_token', 'member_type', 'member_id', 'perm_type'],
          },
        },
        {
          name: 'get_user_by_email',
          description: '通过邮箱获取用户信息',
          inputSchema: {
            type: 'object',
            properties: {
              email: {
                type: 'string',
                description: '用户邮箱',
              },
            },
            required: ['email'],
          },
        },
      ],
    }));

    // List available resources
    this.server.setRequestHandler(ListResourcesRequestSchema, async () => ({
      resources: [
        {
          uri: 'feishu://config',
          name: 'Feishu Configuration',
          description: '当前飞书配置信息',
          mimeType: 'application/json',
        },
      ],
    }));

    // Read resource
    this.server.setRequestHandler(ReadResourceRequestSchema, async (request) => {
      const uri = request.params.uri;

      if (uri === 'feishu://config') {
        return {
          contents: [
            {
              uri,
              mimeType: 'application/json',
              text: JSON.stringify(
                {
                  app_id: this.appId ? `${this.appId.slice(0, 10)}...` : 'Not configured',
                  has_secret: !!this.appSecret,
                  has_token: !!this.accessToken,
                },
                null,
                2
              ),
            },
          ],
        };
      }

      throw new Error(`Resource not found: ${uri}`);
    });

    // Handle tool calls
    this.server.setRequestHandler(CallToolRequestSchema, async (request) => {
      const { name, arguments: args } = request.params;

      try {
        switch (name) {
          case 'get_tenant_access_token':
            return await this.getTenantAccessToken();

          case 'create_bitable':
            return await this.createBitable(args.name, args.folder_token);

          case 'get_tables':
            return await this.getTables(args.app_token);

          case 'add_table_field':
            return await this.addTableField(
              args.app_token,
              args.table_id,
              args.field_name,
              args.field_type
            );

          case 'add_record':
            return await this.addRecord(args.app_token, args.table_id, args.fields);

          case 'get_records':
            return await this.getRecords(args.app_token, args.table_id, args.page_size);

          case 'add_collaborator':
            return await this.addCollaborator(
              args.app_token,
              args.member_type,
              args.member_id,
              args.perm_type
            );

          case 'get_user_by_email':
            return await this.getUserByEmail(args.email);

          default:
            throw new Error(`Unknown tool: ${name}`);
        }
      } catch (error) {
        return {
          content: [
            {
              type: 'text',
              text: `Error: ${error.message}`,
            },
          ],
          isError: true,
        };
      }
    });
  }

  async ensureAccessToken() {
    if (!this.accessToken) {
      await this.getTenantAccessTokenInternal();
    }
  }

  async getTenantAccessTokenInternal() {
    if (!this.appId || !this.appSecret) {
      throw new Error('FEISHU_APP_ID and FEISHU_APP_SECRET environment variables are required');
    }

    const url = 'https://open.feishu.cn/open-apis/auth/v3/tenant_access_token/internal';
    const response = await axios.post(url, {
      app_id: this.appId,
      app_secret: this.appSecret,
    });

    if (response.data.code !== 0) {
      throw new Error(`Failed to get access token: ${response.data.msg}`);
    }

    this.accessToken = response.data.tenant_access_token;
    return this.accessToken;
  }

  async getTenantAccessToken() {
    const token = await this.getTenantAccessTokenInternal();
    return {
      content: [
        {
          type: 'text',
          text: `✅ 成功获取访问令牌: ${token.slice(0, 20)}...`,
        },
      ],
    };
  }

  async createBitable(name, folder_token = '') {
    await this.ensureAccessToken();

    const url = 'https://open.feishu.cn/open-apis/bitable/v1/apps';
    const response = await axios.post(
      url,
      { name, folder_token },
      {
        headers: {
          Authorization: `Bearer ${this.accessToken}`,
          'Content-Type': 'application/json',
        },
      }
    );

    if (response.data.code !== 0) {
      throw new Error(`Failed to create bitable: ${response.data.msg}`);
    }

    const appToken = response.data.data.app.app_token;
    const appUrl = `https://feishu.cn/base/${appToken}`;

    return {
      content: [
        {
          type: 'text',
          text: `✅ 成功创建多维表格\n应用Token: ${appToken}\n应用链接: ${appUrl}`,
        },
      ],
    };
  }

  async getTables(appToken) {
    await this.ensureAccessToken();

    const url = `https://open.feishu.cn/open-apis/bitable/v1/apps/${appToken}/tables`;
    const response = await axios.get(url, {
      headers: {
        Authorization: `Bearer ${this.accessToken}`,
        'Content-Type': 'application/json',
      },
    });

    if (response.data.code !== 0) {
      throw new Error(`Failed to get tables: ${response.data.msg}`);
    }

    const tables = response.data.data.items || [];

    return {
      content: [
        {
          type: 'text',
          text: `✅ 获取到 ${tables.length} 个数据表:\n${tables.map(t => `- ${t.table_id}: ${t.name}`).join('\n')}`,
        },
      ],
    };
  }

  async addTableField(appToken, tableId, fieldName, fieldType) {
    await this.ensureAccessToken();

    const url = `https://open.feishu.cn/open-apis/bitable/v1/apps/${appToken}/tables/${tableId}/fields`;
    const response = await axios.post(
      url,
      { field_name: fieldName, type: fieldType },
      {
        headers: {
          Authorization: `Bearer ${this.accessToken}`,
          'Content-Type': 'application/json',
        },
      }
    );

    if (response.data.code !== 0) {
      throw new Error(`Failed to add field: ${response.data.msg}`);
    }

    return {
      content: [
        {
          type: 'text',
          text: `✅ 成功添加字段: ${fieldName}`,
        },
      ],
    };
  }

  async addRecord(appToken, tableId, fields) {
    await this.ensureAccessToken();

    const url = `https://open.feishu.cn/open-apis/bitable/v1/apps/${appToken}/tables/${tableId}/records`;
    const response = await axios.post(
      url,
      { fields },
      {
        headers: {
          Authorization: `Bearer ${this.accessToken}`,
          'Content-Type': 'application/json',
        },
      }
    );

    if (response.data.code !== 0) {
      throw new Error(`Failed to add record: ${response.data.msg}`);
    }

    return {
      content: [
        {
          type: 'text',
          text: `✅ 成功添加记录`,
        },
      ],
    };
  }

  async getRecords(appToken, tableId, pageSize = 20) {
    await this.ensureAccessToken();

    const url = `https://open.feishu.cn/open-apis/bitable/v1/apps/${appToken}/tables/${tableId}/records`;
    const response = await axios.get(url, {
      headers: {
        Authorization: `Bearer ${this.accessToken}`,
        'Content-Type': 'application/json',
      },
      params: { page_size: pageSize },
    });

    if (response.data.code !== 0) {
      throw new Error(`Failed to get records: ${response.data.msg}`);
    }

    const records = response.data.data.items || [];

    return {
      content: [
        {
          type: 'text',
          text: `✅ 获取到 ${records.length} 条记录:\n${JSON.stringify(records, null, 2)}`,
        },
      ],
    };
  }

  async addCollaborator(appToken, memberType, memberId, permType) {
    await this.ensureAccessToken();

    const url = 'https://open.feishu.cn/open-apis/permission/v2/permissions/add_member';
    const params = new URLSearchParams({
      resource_type: 'bitable',
      resource_id: appToken,
      perm_type: permType,
      member_type: memberType,
      member_id: memberId,
    });

    const response = await axios.post(url, params, {
      headers: {
        Authorization: `Bearer ${this.accessToken}`,
        'Content-Type': 'application/x-www-form-urlencoded; charset=utf-8',
      },
    });

    if (response.data.code !== 0) {
      throw new Error(`Failed to add collaborator: ${response.data.msg} (code: ${response.data.code})`);
    }

    return {
      content: [
        {
          type: 'text',
          text: `✅ 成功添加协作者: ${memberId} (${permType})`,
        },
      ],
    };
  }

  async getUserByEmail(email) {
    await this.ensureAccessToken();

    const url = 'https://open.feishu.cn/open-apis/contact/v3/users/get_by_email';
    const response = await axios.post(
      url,
      { emails: [email], include_resigned: false },
      {
        headers: {
          Authorization: `Bearer ${this.accessToken}`,
          'Content-Type': 'application/json',
        },
      }
    );

    if (response.data.code !== 0) {
      throw new Error(`Failed to get user: ${response.data.msg}`);
    }

    const userList = response.data.data.user_list || [];
    if (userList.length === 0) {
      throw new Error(`User not found: ${email}`);
    }

    const user = userList[0];
    return {
      content: [
        {
          type: 'text',
          text: `✅ 找到用户:\n姓名: ${user.name || 'N/A'}\nOpen ID: ${user.open_id}\n邮箱: ${email}`,
        },
      ],
    };
  }

  async run() {
    const transport = new StdioServerTransport();
    await this.server.connect(transport);
    console.error('Feishu MCP server running on stdio');
  }
}

// Start server
const server = new FeishuMCPServer();
server.run().catch(console.error);
