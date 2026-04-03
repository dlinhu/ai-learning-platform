# 简单对话Agent / Simple Conversational Agent

## Overview / 概述

Build a conversational agent that maintains context across multiple interactions using LangChain. / 构建能够在多次交互中保持上下文的对话Agent。

## Key Knowledge Points / 核心知识点

### 1. 对话历史管理 / Conversation History Management

**English:** Use RunnableWithMessageHistory to manage conversation history for context-aware conversations.

**中文:** 使用RunnableWithMessageHistory管理对话历史，实现上下文感知的对话。

**Key Concepts / 核心概念:**
- RunnableWithMessageHistory / 消息历史包装器
- ChatMessageHistory / 聊天消息历史
- Session management / 会话管理

**Example / 示例:**
```python
chain_with_history = RunnableWithMessageHistory(
    chain, get_chat_history,
    input_messages_key='input',
    history_messages_key='history'
)
# → Wrap chain with message history

```

---

### 2. 提示模板设计 / Prompt Template Design

**English:** Use ChatPromptTemplate and MessagesPlaceholder to design prompts that include historical messages.

**中文:** 使用ChatPromptTemplate和MessagesPlaceholder设计包含历史消息的提示模板。

**Key Concepts / 核心概念:**
- ChatPromptTemplate / 聊天提示模板
- MessagesPlaceholder / 消息占位符
- System message / 系统消息

**Example / 示例:**
```python
prompt = ChatPromptTemplate.from_messages([
    ('system', 'You are a helpful AI assistant.'),
    MessagesPlaceholder(variable_name='history'),
    ('human', '{input}')
])
# → Create prompt template with history placeholder

```

---

## Summary / 总结

This lesson covered key AI Agent concepts. Practice these techniques to build better intelligent systems.

本课程涵盖了关键AI Agent技术。练习这些技术以构建更好的智能系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own agents / 构建自己的Agent
3. Explore advanced patterns / 探索高级模式
