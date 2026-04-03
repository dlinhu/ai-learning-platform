# 任务导向Agent / Task-Oriented Agent

## Overview / 概述

Build agents that can perform specific tasks like summarization and translation using structured tools. / 构建能够使用结构化工具执行特定任务（如摘要和翻译）的Agent。

## Key Knowledge Points / 核心知识点

### 1. Structured Tools / 结构化工具

**English:** Use StructuredTool to wrap custom functions as agent tools with name, description, and input schema.

**中文:** 使用StructuredTool将自定义函数包装为Agent可用的工具，包含名称、描述和输入模式。

**Key Concepts / 核心概念:**
- StructuredTool / 结构化工具
- Input schema / 输入模式
- Tool description / 工具描述

**Example / 示例:**
```python
tools = [
    StructuredTool.from_function(
        func=summarize,
        name='Summarize',
        description='Useful for summarizing text',
        args_schema=TextInput
    )
]
# → Create structured tool from function

```

---

### 2. Agent Executor / Agent执行器

**English:** AgentExecutor manages agent execution, controlling iteration count and stopping conditions.

**中文:** AgentExecutor管理Agent的执行，控制迭代次数和停止条件。

**Key Concepts / 核心概念:**
- AgentExecutor / Agent执行器
- max_iterations / 最大迭代次数
- early_stopping_method / 提前停止方法

**Example / 示例:**
```python
agent_executor = AgentExecutor(
    agent=agent,
    tools=tools,
    verbose=True,
    max_iterations=3,
    early_stopping_method='force'
)
# → Configure agent executor with limits

```

---

## Summary / 总结

This lesson covered key AI Agent concepts. Practice these techniques to build better intelligent systems.

本课程涵盖了关键AI Agent技术。练习这些技术以构建更好的智能系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own agents / 构建自己的Agent
3. Explore advanced patterns / 探索高级模式
