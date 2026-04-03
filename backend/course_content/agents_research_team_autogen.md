# AutoGen研究团队 / AutoGen Research Team

## Overview / 概述

Build a research team using Microsoft AutoGen framework for multi-agent collaboration. / 使用Microsoft AutoGen框架构建研究团队进行多Agent协作。

## Key Knowledge Points / 核心知识点

### 1. AutoGen框架 / AutoGen Framework

**English:** Microsoft AutoGen provides multi-agent conversation framework, supporting automatic dialogue and collaboration between agents.

**中文:** Microsoft AutoGen提供多Agent对话框架，支持Agent之间的自动对话和协作。

**Key Concepts / 核心概念:**
- AutoGen / AutoGen框架
- Multi-agent conversation / 多Agent对话
- Assistant Agent / 助手Agent

**Example / 示例:**
```python
assistant = AssistantAgent('assistant', llm_config=llm_config)
user_proxy = UserProxyAgent('user_proxy', code_execution_config=...)
user_proxy.initiate_chat(assistant, message='Research topic...')
# → Set up AutoGen agents for research

```

---

## Summary / 总结

This lesson covered key AI Agent concepts. Practice these techniques to build better intelligent systems.

本课程涵盖了关键AI Agent技术。练习这些技术以构建更好的智能系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own agents / 构建自己的Agent
3. Explore advanced patterns / 探索高级模式
