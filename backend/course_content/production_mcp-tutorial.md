# MCP 生产集成 / MCP Production Integration

## Overview / 概述

Implement MCP protocol for production AI agents with custom servers and tool discovery. / 实现MCP协议用于生产AI Agent，包括自定义服务器和工具发现。

## Key Knowledge Points / 核心知识点

### 1. MCP 服务器开发 / MCP Server Development

**English:** Develop custom MCP servers using @mcp.tool decorator to expose agent tools.

**中文:** 开发自定义MCP服务器，使用@mcp.tool装饰器暴露Agent工具。

**Key Concepts / 核心概念:**
- @mcp.tool decorator / 工具装饰器
- Server configuration / 服务器配置
- Tool exposure / 工具暴露
- JSON-RPC 2.0

**Example / 示例:**
```python
@mcp.tool()
async def get_crypto_price(crypto_id: str) -> str:
    return f'Price of {crypto_id}'
# → Define MCP tool with decorator

```

---

### 2. 工具发现与执行 / Tool Discovery & Execution

**English:** Implement dynamic tool discovery where agents can automatically discover and use tools provided by MCP servers.

**中文:** 实现动态工具发现，Agent可以自动发现和使用MCP服务器提供的工具。

**Key Concepts / 核心概念:**
- Tool discovery / 工具发现
- Dynamic execution / 动态执行
- Stdio connection / 标准输入输出连接
- Session management / 会话管理

**Example / 示例:**
```python
async with ClientSession(read, write) as session:
    await session.initialize()
    tools = await session.list_tools()
# → Discover available MCP tools

```

---

## Summary / 总结

This lesson covered key production deployment concepts. Practice these techniques to build robust production systems.

本课程涵盖了关键的生产部署技术。练习这些技术以构建健壮的生产系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own production agents / 构建自己的生产Agent
3. Explore advanced patterns / 探索高级模式
