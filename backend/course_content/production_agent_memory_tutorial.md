# Redis 记忆系统 / Redis Memory System

## Overview / 概述

Build production-ready memory systems for AI agents using Redis with short-term and long-term memory. / 使用Redis构建生产级AI Agent记忆系统，包括短期和长期记忆。

## Key Knowledge Points / 核心知识点

### 1. 双记忆架构 / Dual-Memory Architecture

**English:** Short-term memory manages conversation context, long-term memory uses RedisVL for semantic search storage of persistent knowledge.

**中文:** 短期记忆管理对话上下文，长期记忆使用RedisVL进行语义搜索存储持久知识。

**Key Concepts / 核心概念:**
- Short-term memory / 短期记忆
- Long-term memory / 长期记忆
- RedisVL / Redis向量库
- Semantic search / 语义搜索

**Example / 示例:**
```python
class MemoryType(str, Enum):
    EPISODIC = 'episodic'  # User experiences
    SEMANTIC = 'semantic'   # General knowledge
# → Define memory types for agent

```

---

### 2. Redis 检查点 / Redis Checkpointer

**English:** Use RedisSaver to implement state persistence for LangGraph workflows.

**中文:** 使用RedisSaver实现LangGraph工作流的状态持久化。

**Key Concepts / 核心概念:**
- RedisSaver / Redis保存器
- State persistence / 状态持久化
- Thread management / 线程管理
- Session recovery / 会话恢复

**Example / 示例:**
```python
from langgraph.checkpoint.redis import RedisSaver
redis_saver = RedisSaver(redis_client=redis_client)
redis_saver.setup()
# → Setup Redis checkpointer for state persistence

```

---

### 3. 向量记忆存储 / Vector Memory Storage

**English:** Use RedisVL to create vector indexes for semantic search and deduplication of memories.

**中文:** 使用RedisVL创建向量索引，实现记忆的语义搜索和去重。

**Key Concepts / 核心概念:**
- Vector index / 向量索引
- Embedding storage / 嵌入存储
- Deduplication / 去重
- Similarity search / 相似性搜索

**Example / 示例:**
```python
memory_schema = IndexSchema.from_dict({
    'index': {'name': 'agent_memories'},
    'fields': [{'name': 'embedding', 'type': 'vector', 'attrs': {'dims': 1536}}]
})
# → Create memory vector index schema

```

---

## Summary / 总结

This lesson covered key production deployment concepts. Practice these techniques to build robust production systems.

本课程涵盖了关键的生产部署技术。练习这些技术以构建健壮的生产系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own production agents / 构建自己的生产Agent
3. Explore advanced patterns / 探索高级模式
