# 工具集成 / Tool Integration

## Overview / 概述

Learn tool discovery, binding, and execution for AI agents. / 学习AI Agent的工具发现、绑定和执行。

## Key Knowledge Points / 核心知识点

### 1. 工具发现 / Tool Discovery

**English:** Dynamically discover available tools including API endpoints, functions, and external services.

**中文:** 动态发现可用工具，包括API端点、函数和外部服务。

**Key Concepts / 核心概念:**
- Dynamic Discovery / 动态发现
- Tool Registry / 工具注册表
- API Introspection / API内省
- Service Discovery / 服务发现

**Example / 示例:**
```python
class ToolRegistry:
    def __init__(self):
        self.tools = {}
    def register(self, name, func, schema):
        self.tools[name] = {'func': func, 'schema': schema}
    def discover(self, query):
        return [t for t in self.tools if matches(query, t)]
# → Implement tool discovery registry

```

---

### 2. 工具绑定 / Tool Binding

**English:** Bind tools to LLM supporting function calling and parameter validation.

**中文:** 将工具绑定到LLM，支持函数调用和参数验证。

**Key Concepts / 核心概念:**
- Function Calling / 函数调用
- Parameter Validation / 参数验证
- Schema Binding / 模式绑定
- Type Coercion / 类型转换

**Example / 示例:**
```python
def bind_tool(llm, tool_schema):
    return llm.bind_tools([tool_schema])

tool_schema = {
    'name': 'search',
    'parameters': {'query': {'type': 'string'}}
}
# → Bind tool to LLM with schema

```

---

### 3. 工具执行 / Tool Execution

**English:** Safely execute tool calls including error handling and result parsing.

**中文:** 安全执行工具调用，包括错误处理和结果解析。

**Key Concepts / 核心概念:**
- Safe Execution / 安全执行
- Error Handling / 错误处理
- Result Parsing / 结果解析
- Timeout Management / 超时管理

**Example / 示例:**
```python
async def execute_tool(tool, params, timeout=30):
    try:
        result = await asyncio.wait_for(
            tool(**params), timeout=timeout
        )
        return {'success': True, 'result': result}
    except Exception as e:
        return {'success': False, 'error': str(e)}
# → Implement safe tool execution

```

---

## Summary / 总结

This lesson covered key context engineering concepts. Practice these techniques to build robust context systems.

本课程涵盖了关键的上下文工程技术。练习这些技术以构建健壮的上下文系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own context systems / 构建自己的上下文系统
3. Explore advanced patterns / 探索高级模式
