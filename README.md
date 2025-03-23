# GitHub API MCP Server

用于GitHub搜索API的MCP。

## 环境要求

- [uv](https://docs.astral.sh/uv/) - 一个项目管理工具，可以很方便管理依赖。

## 使用方法

1、安装依赖

```
uv PyGithub python-dotenv
```

2、在Client里配置Server

```json
{
  "mcpServers": {
    "github_server": {
      "command": "uv",
      "args": [
        "--directory",
        "D:/blog/github-mcp-server",
        "run",
        "github_server.py"
      ]
    }
  }
}

```

3、在Client里使用
