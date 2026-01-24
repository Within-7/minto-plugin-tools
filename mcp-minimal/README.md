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

2. **Configure MCP services** - The plugin will automatically guide you through configuration, or you can manually edit `~/.minto.json`:

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

3. **Refresh MCP connections**:

```bash
/mcp
```

4. **Start using** - No need to restart Minto!

### Usage

Once installed and configured, use natural language to interact with MCP services:

```bash
# Test connectivity
"Ping the MCP service"
"测试 global-data-mcp-hello 连接"

# Call specific tools
"调用 MCP 的 ping 工具，参数是 hello"
"使用 global-data-mcp-hello 服务"
```

## Features

- ✅ **Auto-Configuration**: Automatically configures MCP services on first use
- ✅ **SSE Support**: Connect to remote MCP servers via Server-Sent Events
- ✅ **Natural Language**: Interact using plain language - no special syntax
- ✅ **Auto Discovery**: Automatically discovers available tools from connected services
- ✅ **Multiple Services**: Configure and use multiple MCP services simultaneously
- ✅ **Error Handling**: Graceful handling of connection issues
- ✅ **Auto Refresh**: Runs `/mcp` command to refresh connections after configuration

## How It Works

This plugin simplifies MCP integration by automating the setup process:

1. **Automatic Configuration**: When you install the plugin, it automatically adds the MCP service to your `~/.minto.json`
2. **Refresh Connections**: Automatically runs `/mcp` to load MCP tools
3. **Natural Language Interface**: Just talk to Minto normally - the plugin handles the rest

### Configuration Flow

```
User Installs Plugin
         ↓
Plugin Checks ~/.minto.json
         ↓
If MCP service not configured:
    - Add service to mcpServers section
    - Enable the service
         ↓
Run /mcp to refresh connections
         ↓
Tools become available
```

## Plugin Structure

```
mcp-minimal/
├── plugin.json          # Plugin metadata
├── skills/
│   └── SKILL.md         # Core skill with auto-configuration logic
└── README.md            # This file
```

## Configuration

### Manual Configuration

If you prefer to configure manually, edit `~/.minto.json`:

```json
{
  "mcpServers": {
    "global-data-mcp-hello": {
      "type": "sse",
      "url": "http://13.58.80.11:32086/sse",
      "enabled": true
    },
    "my-custom-service": {
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

# With custom message
"调用 ping 工具，参数是 hello 你好"
```

### Custom Parameters

```bash
# With message
"Ping with message: test connection"
"调用 MCP 的 ping 工具，参数是测试消息"
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
5. Run `/mcp` to refresh connections

### Service Not Found

**Problem**: "MCP tool not found"

**Solutions**:
1. Check service is `enabled: true` in config
2. Verify service name matches exactly
3. Run `/mcp` to reload connections
4. Check `~/.minto.json` syntax is valid

### Tools Not Available After Installation

**Problem**: Tools not showing up after installing plugin

**Solutions**:
1. Run `/mcp` to refresh MCP connections
2. Check `~/.minto.json` has the MCP service configured
3. Verify the service is `enabled: true`
4. Restart Minto if necessary

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
│  - Auto-configure services  │
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

## Best Practices

1. **Always run `/mcp` after configuration** - This refreshes MCP connections and loads tools
2. **Use natural language** - The plugin handles parsing, just describe what you want
3. **Check configuration first** - If tools aren't working, verify `~/.minto.json`
4. **Test connectivity** - Use `ping` tool to verify connection before calling other tools
5. **Monitor logs** - Enable debug logging if you encounter issues

## Contributing

To add new MCP services or extend functionality:

1. Update `skills/SKILL.md` with new capabilities
2. Add examples to this README
3. Test with various MCP service types
4. Document any breaking changes
5. Ensure auto-configuration logic is updated

## License

MIT License - see LICENSE file for details

## Author

within-7

## Version History

- **2.0.0** (2026-01-22): Auto-configuration update
  - ✅ Added automatic MCP service configuration
  - ✅ Integrated `/mcp` refresh command
  - ✅ Improved natural language processing
  - ✅ Enhanced documentation and examples
  - ✅ Added troubleshooting guide
  
- **1.0.0** (2026-01-22): Initial release
  - SSE support
  - Natural language interface
  - Multi-service configuration
