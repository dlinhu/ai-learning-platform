# PydanticAI 对话Agent / PydanticAI Conversational Agent

## Overview / 概述

Build conversational agents using PydanticAI framework with type safety and validation. / 使用PydanticAI框架构建具有类型安全和验证的对话Agent。

## Key Knowledge Points / 核心知识点

### 1. PydanticAI Agent / PydanticAI Agent

**English:** PydanticAI provides a type-safe agent framework, combining Pydantic's validation and type-safety principles.

**中文:** PydanticAI提供类型安全的Agent框架，结合Pydantic的验证和类型安全原则。

**Key Concepts / 核心概念:**
- Type safety / 类型安全
- Validation / 验证
- Pydantic integration / Pydantic集成

**Example / 示例:**
```python
agent = Agent(
    model='openai:gpt-4o-mini',
    system_prompt='You are a helpful AI assistant.'
)
# → Create PydanticAI agent

```

---

### 2. 消息存储与检索 / Message Storage & Retrieval

**English:** Use ModelMessagesTypeAdapter for message serialization and deserialization storage.

**中文:** 使用ModelMessagesTypeAdapter进行消息的序列化和反序列化存储。

**Key Concepts / 核心概念:**
- ModelMessagesTypeAdapter / 消息类型适配器
- JSON serialization / JSON序列化
- Message history / 消息历史

**Example / 示例:**
```python
messages = ModelMessagesTypeAdapter.validate_json(msg_group)
store[session_id].append(run_result.new_messages_json())
# → Store and retrieve messages in JSON format

```

---

## Summary / 总结

This lesson covered key AI Agent concepts. Practice these techniques to build better intelligent systems.

本课程涵盖了关键AI Agent技术。练习这些技术以构建更好的智能系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own agents / 构建自己的Agent
3. Explore advanced patterns / 探索高级模式
