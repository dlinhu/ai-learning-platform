# 记忆系统 / Memory Systems

## Overview / 概述

Learn short-term and long-term memory architectures for AI agents. / 学习AI Agent的短期和长期记忆架构。

## Key Knowledge Points / 核心知识点

### 1. 短期记忆 / Short-Term Memory

**English:** Manage current conversation context with sliding window and priority queue strategies.

**中文:** 管理当前对话上下文，包括滑动窗口和优先级队列策略。

**Key Concepts / 核心概念:**
- Sliding Window / 滑动窗口
- Token Budget / Token预算
- Priority Queue / 优先级队列
- Context Overflow / 上下文溢出

**Example / 示例:**
```python
class ShortTermMemory:
    def __init__(self, max_tokens=4000):
        self.messages = []
        self.max_tokens = max_tokens
    def add(self, msg):
        self.messages.append(msg)
        self._trim_if_needed()
# → Implement short-term memory with token limit

```

---

### 2. 长期记忆 / Long-Term Memory

**English:** Persist memories using vector storage, supporting semantic search and memory retrieval.

**中文:** 使用向量存储持久化记忆，支持语义搜索和记忆检索。

**Key Concepts / 核心概念:**
- Vector Store / 向量存储
- Memory Persistence / 记忆持久化
- Semantic Search / 语义搜索
- Memory Consolidation / 记忆巩固

**Example / 示例:**
```python
class LongTermMemory:
    def __init__(self, vector_store):
        self.store = vector_store
    def store_memory(self, memory):
        embedding = embed(memory)
        self.store.add(embedding, metadata=memory)
    def recall(self, query, k=5):
        return self.store.search(embed(query), k)
# → Implement long-term memory with vector store

```

---

### 3. 记忆类型 / Memory Types

**English:** Episodic memory (user experiences), semantic memory (general knowledge), procedural memory (skills).

**中文:** 情景记忆（用户经历）、语义记忆（通用知识）、程序记忆（技能）。

**Key Concepts / 核心概念:**
- Episodic Memory / 情景记忆
- Semantic Memory / 语义记忆
- Procedural Memory / 程序记忆
- Memory Classification / 记忆分类

**Example / 示例:**
```python
class MemoryType(Enum):
    EPISODIC = 'episodic'    # User experiences
    SEMANTIC = 'semantic'     # General knowledge
    PROCEDURAL = 'procedural' # Skills and procedures
# → Define memory type classification

```

---

## Summary / 总结

This lesson covered key context engineering concepts. Practice these techniques to build robust context systems.

本课程涵盖了关键的上下文工程技术。练习这些技术以构建健壮的上下文系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own context systems / 构建自己的上下文系统
3. Explore advanced patterns / 探索高级模式
