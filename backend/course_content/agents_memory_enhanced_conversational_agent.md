# 记忆增强对话Agent / Memory-Enhanced Conversational Agent

## Overview / 概述

Build conversational agents with enhanced memory capabilities for better context retention. / 构建具有增强记忆能力的对话Agent以更好地保持上下文。

## Key Knowledge Points / 核心知识点

### 1. 长期记忆存储 / Long-term Memory Storage

**English:** Use vector storage for long-term memory, supporting semantic search to retrieve relevant historical information.

**中文:** 使用向量存储实现长期记忆，支持语义搜索检索相关历史信息。

**Key Concepts / 核心概念:**
- Vector storage / 向量存储
- Long-term memory / 长期记忆
- Semantic retrieval / 语义检索

**Example / 示例:**
```python
store.put(('assistant', user_id, 'memories'), memory_id, memory_content)
relevant_memories = store.search(('assistant', user_id, 'memories'), query=user_input)
# → Store and retrieve long-term memories

```

---

### 2. 记忆整合 / Memory Integration

**English:** Integrate retrieved memories into current conversation context for personalized responses.

**中文:** 将检索到的记忆整合到当前对话上下文中，提供个性化响应。

**Key Concepts / 核心概念:**
- Memory integration / 记忆整合
- Personalization / 个性化
- Context enrichment / 上下文丰富

**Example / 示例:**
```python
memories = store.search(namespace, query=current_input)
context = f'Relevant memories: {memories}\nCurrent input: {current_input}'
response = llm.invoke(context)
# → Integrate memories into conversation

```

---

## Summary / 总结

This lesson covered key AI Agent concepts. Practice these techniques to build better intelligent systems.

本课程涵盖了关键AI Agent技术。练习这些技术以构建更好的智能系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own agents / 构建自己的Agent
3. Explore advanced patterns / 探索高级模式
