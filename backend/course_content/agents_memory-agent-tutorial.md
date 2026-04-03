# 记忆增强Agent / Memory-Enhanced Agent

## Overview / 概述

Build AI agents with three types of memory: semantic, episodic, and procedural using LangGraph and LangMem. / 构建具有三种记忆类型的AI Agent：语义记忆、情景记忆和程序记忆。

## Key Knowledge Points / 核心知识点

### 1. 三种记忆类型 / Three Memory Types

**English:** Semantic memory stores facts and knowledge, episodic memory remembers specific interactions, procedural memory learns and improves behavioral patterns.

**中文:** 语义记忆存储事实知识，情景记忆记住特定交互，程序记忆学习和改进行为模式。

**Key Concepts / 核心概念:**
- Semantic Memory / 语义记忆
- Episodic Memory / 情景记忆
- Procedural Memory / 程序记忆

**Example / 示例:**
```python
# Semantic: store facts about contacts
# Episodic: remember past email examples
# Procedural: improve prompts based on feedback
# → Three types of agent memory

```

---

### 2. LangMem 工具 / LangMem Tools

**English:** Use create_manage_memory_tool and create_search_memory_tool to manage agent memory.

**中文:** 使用create_manage_memory_tool和create_search_memory_tool管理Agent记忆。

**Key Concepts / 核心概念:**
- manage_memory / 管理记忆
- search_memory / 搜索记忆
- InMemoryStore / 内存存储

**Example / 示例:**
```python
manage_memory_tool = create_manage_memory_tool(namespace=('assistant', '{user_id}', 'collection'))
search_memory_tool = create_search_memory_tool(namespace=('assistant', '{user_id}', 'collection'))
# → Create LangMem memory tools

```

---

## Summary / 总结

This lesson covered key AI Agent concepts. Practice these techniques to build better intelligent systems.

本课程涵盖了关键AI Agent技术。练习这些技术以构建更好的智能系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own agents / 构建自己的Agent
3. Explore advanced patterns / 探索高级模式
