# Dull Fantasy Game MCP

Simple MCP server used to learn about MCP,
both through local MCP Inspector and tying into Claude Desktop.

## Claude Desktop configuration

```json
"DullFantasyGame": {
    "command": "/usr/local/bin/uv",
    "args": [
        "--directory",
        "/abs/path/to/fantasy-game-mcp",
        "run",
        "main.py"
    ]
}
```