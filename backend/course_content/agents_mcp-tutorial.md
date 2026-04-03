# MCP 模型上下文协议 / Model Context Protocol

## Overview / 概述

Learn MCP (Model Context Protocol) for standardizing AI model integration with external resources and tools. / 学习MCP协议，标准化AI模型与外部资源和工具的集成。

## Key Knowledge Points / 核心知识点

### 1. MCP 架构 / MCP Architecture

**English:** MCP follows a client-server architecture with three main components: Host (AI application), Client (connector), and Server (capability provider).

**中文:** MCP采用客户端-服务器架构，包含Host（AI应用）、Client（连接器）和Server（能力提供者）三个主要组件。

**Key Concepts / 核心概念:**
- Host / 主机
- Client / 客户端
- Server / 服务器
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

**English:** MCP supports dynamic tool discovery, allowing AI to automatically discover and use tools provided by servers.

**中文:** MCP支持动态工具发现，AI可以自动发现和使用服务器提供的工具。

**Key Concepts / 核心概念:**
- Tool discovery / 工具发现
- Dynamic execution / 动态执行
- Stdio connection / 标准输入输出连接

**Example / 示例:**
```python
tools = await session.list_tools()
result = await session.call_tool(tool_name, arguments)
# → Discover and execute MCP tools

```

---

## Summary / 总结

This lesson covered key AI Agent concepts. Practice these techniques to build better intelligent systems.

本课程涵盖了关键AI Agent技术。练习这些技术以构建更好的智能系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own agents / 构建自己的Agent
3. Explore advanced patterns / 探索高级模式
