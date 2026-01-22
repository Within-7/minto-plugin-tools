---
name: mcp-minimal
description: Minimal MCP client for connecting to remote MCP services via SSE. Simple interface to interact with MCP tools.
license: MIT
compatibility: opencode
metadata:
  version: "1.0"
  author: within-7
  category: integration
---

# MCP Minimal Skill

Minimal MCP client plugin for connecting to and interacting with remote MCP services via Server-Sent Events (SSE).

## What I Do

- **Connect to MCP Services**: Establish SSE connection to remote MCP servers
- **Call MCP Tools**: Invoke remote tools and receive responses
- **Simple Interface**: Natural language interaction with MCP capabilities
- **Service Discovery**: Automatically discover available tools from connected services

## When to Use Me

User wants to:
- Connect to remote MCP services (e.g., global-data-mcp-hello)
- Call MCP tools using natural language
- Test MCP service connectivity
- Interact with MCP-powered services without manual configuration

## How It Works

### Connection Model

This plugin uses SSE (Server-Sent Events) to communicate with remote MCP services:

```
Minto (Client) <--SSE--> MCP Server (e.g., http://13.58.80.11:32086/sse)
```

### Configuration

MCP services are configured in `~/.minto.json`:

```json
{
  "mcpServers": {
    "global-data-mcp-hello": {
      "type": "sse",
      "url": "http://13.58.80.11:32086/sse",
      "enabled": true
    }
  }
}
```

### Usage Patterns

**Natural Language (Recommended)**:
```
User: "Ping the MCP service"
Minto: [Automatically calls global-data-mcp-hello:ping]

User: "调用 global-data-mcp-hello 的 ping 工具"
Minto: [Calls specified tool with context]
```

**Direct Tool Invocation**:
```
global-data-mcp-hello:ping
global-data-mcp-hello:list_tools
```

## Available Services

### global-data-mcp-hello

- **Type**: SSE
- **URL**: `http://13.58.80.11:32086/sse`
- **Tools**:
  - `ping(msg)`: Echo service for testing connectivity

### Adding New Services

To add a new MCP service, update `~/.minto.json`:

```json
{
  "mcpServers": {
    "my-mcp-service": {
      "type": "sse",
      "url": "https://my-service.com/mcp",
      "enabled": true,
      "headers": {
        "Authorization": "Bearer ${TOKEN}"
      }
    }
  }
}
```

## Examples

### Basic Usage

```bash
# Test connectivity
"测试 MCP 连接"
"Ping global-data-mcp-hello"

# Call specific tools
"调用 MCP 的 ping 工具，参数是 hello"
"使用 global-data-mcp-hello 服务"
```

### Advanced Usage

```bash
# List available tools
"列出 MCP 服务的所有工具"

# Get service information
"查看 MCP 服务状态"

# Custom parameters
"调用 ping，消息内容是测试连接"
```

## MCP Server Types

This plugin supports multiple MCP transport types:

| Type | Description | Config Fields |
|------|-------------|---------------|
| **sse** | Server-Sent Events | `url` |
| **stdio** | Local process | `command`, `args` |
| **websocket** | WebSocket connection | `url`, `headers` |
| **http** | RESTful API | `baseUrl`, `timeout` |

## Troubleshooting

### Connection Issues

If MCP tools fail to connect:

1. **Check service status**: Verify the MCP server is running
2. **Validate URL**: Ensure the SSE endpoint is correct
3. **Network access**: Confirm firewall allows connections
4. **Authentication**: Check if credentials are required

### Debug Commands

```bash
# Test service manually (if curl available)
curl -I http://13.58.80.11:32086/sse

# Check Minto configuration
cat ~/.minto.json | grep -A 10 mcpServers

# View MCP logs (if available)
tail -f ~/.minto/logs/mcp.log
```

## Architecture

```
┌─────────────────────────────────────┐
│           Minto (Client)            │
│  ┌───────────────────────────────┐  │
│  │   mcp-minimal Plugin          │  │
│  │  - Natural Language Parsing  │  │
│  │  - Tool Discovery            │  │
│  │  - SSE Connection Management │  │
│  └───────────────────────────────┘  │
│             │                         │
│             │ SSE                    │
│             ▼                         │
│  ┌───────────────────────────────┐  │
│  │   Remote MCP Server           │  │
│  │  (global-data-mcp-hello)      │  │
│  │  - Tool Registry              │  │
│  │  - Request/Response Handling  │  │
│  │  - Business Logic             │  │
│  └───────────────────────────────┘  │
└─────────────────────────────────────┘
```

## Notes

- This plugin provides **client-side** MCP connectivity
- The actual MCP server runs independently (remote or local)
- Multiple MCP services can be configured simultaneously
- Tool discovery is automatic upon connection
- All interactions use natural language - no special syntax needed

## See Also

- [MCP Specification](https://modelcontextprotocol.io)
- [SSE Documentation](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events)
- Minto MCP Configuration Guide
