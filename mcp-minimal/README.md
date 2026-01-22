# MCP Minimal Plugin

Minimal MCP client plugin for Minto - provides seamless integration with remote MCP services via Server-Sent Events (SSE).

## Quick Start

### Installation

1. **Clone or copy this plugin to your Minto plugins directory**:

```bash
# Option 1: Copy directly
cp -r /Users/mac/Desktop/minto-plugin-tools/mcp-minimal ~/.minto/plugins/

# Option 2: Create symlink
ln -s /Users/mac/Desktop/minto-plugin-tools/mcp-minimal ~/.minto/plugins/mcp-minimal
```

2. **Configure MCP services in `~/.minto.json`**:

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

3. **Restart Minto** to load the plugin.

### Usage

Once installed, use natural language to interact with MCP services:

```bash
# Test connectivity
"Ping the MCP service"
"测试 global-data-mcp-hello 连接"

# Call specific tools
"调用 MCP 的 ping 工具"
"使用 global-data-mcp-hello 服务"
```

## Features

- ✅ **SSE Support**: Connect to remote MCP servers via Server-Sent Events
- ✅ **Natural Language**: Interact using plain language - no special syntax
- ✅ **Auto Discovery**: Automatically discovers available tools from connected services
- ✅ **Multiple Services**: Configure and use multiple MCP services simultaneously
- ✅ **Error Handling**: Graceful handling of connection issues

## Plugin Structure

```
mcp-minimal/
├── plugin.json          # Plugin metadata
├── skills/
│   └── SKILL.md         # Core skill documentation
└── README.md            # This file
```

## Configuration

### Adding MCP Services

Edit `~/.minto.json` to add new MCP services:

```json
{
  "mcpServers": {
    "service-name": {
      "type": "sse|stdio|websocket|http",
      "url": "https://service-url.com/mcp",
      "enabled": true,
      "headers": {
        "Authorization": "Bearer ${TOKEN}"
      }
    }
  }
}
```

### Service Types

| Type | Description | Example |
|------|-------------|---------|
| **sse** | Server-Sent Events | `http://13.58.80.11:32086/sse` |
| **stdio** | Local command | `{ "command": "python", "args": ["server.py"] }` |
| **websocket** | WebSocket | `wss://service.com/mcp` |
| **http** | REST API | `https://api.service.com/mcp` |

## Examples

### Basic Ping Test

```bash
# Natural language
"Ping global-data-mcp-hello"

# Direct invocation
global-data-mcp-hello:ping
```

### Custom Parameters

```bash
# With message
"调用 ping 工具，参数是 hello world"
"Ping with message: test connection"
```

### Service Discovery

```bash
# List available tools
"列出 MCP 服务的所有工具"
"查看 global-data-mcp-hello 有哪些工具"
```

## Troubleshooting

### Connection Failed

**Problem**: "MCP error -32001: Request timed out"

**Solutions**:
1. Verify the MCP server is running
2. Check the URL is correct and accessible
3. Ensure no firewall blocking the connection
4. Try `curl -I <url>` to test connectivity

### Service Not Found

**Problem**: "MCP tool not found"

**Solutions**:
1. Check service is `enabled: true` in config
2. Verify service name matches exactly
3. Restart Minto to reload configuration
4. Check `~/.minto.json` syntax is valid

### Debug Mode

Enable verbose logging in Minto:

```json
{
  "logging": {
    "level": "debug"
  }
}
```

## Architecture

```
User Input (Natural Language)
         │
         ▼
┌─────────────────┐
│  Minto Core     │
│  (Parser)       │
└─────────────────┘
         │
         ▼
┌─────────────────────────────┐
│  mcp-minimal Plugin         │
│  - Route to appropriate MCP │
│  - Handle SSE connections   │
│  - Parse responses          │
└─────────────────────────────┘
         │
         │ SSE / HTTP
         ▼
┌─────────────────────────────┐
│  Remote MCP Server          │
│  (global-data-mcp-hello)    │
│  - Tool execution           │
│  - Business logic           │
└─────────────────────────────┘
```

## Contributing

To add new MCP services or extend functionality:

1. Update `skills/SKILL.md` with new capabilities
2. Add examples to this README
3. Test with various MCP service types
4. Document any breaking changes

## License

MIT License - see LICENSE file for details

## Author

within-7

## Version History

- **1.0.0** (2026-01-22): Initial release
  - SSE support
  - Natural language interface
  - Multi-service configuration
