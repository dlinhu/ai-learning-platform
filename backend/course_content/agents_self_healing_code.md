# 自愈代码Agent / Self-Healing Code Agent

## Overview / 概述

Build an agent that can detect runtime errors, generate fixes, and maintain a memory of bug patterns using vector databases. / 构建能够检测运行时错误、生成修复并维护bug模式记忆的Agent。

## Key Knowledge Points / 核心知识点

### 1. 错误检测与修复 / Error Detection & Fix

**English:** Agent detects runtime errors, uses LLM to generate fix code, and validates the fix.

**中文:** Agent检测运行时错误，使用LLM生成修复代码，并验证修复效果。

**Key Concepts / 核心概念:**
- Error detection / 错误检测
- Code generation / 代码生成
- Patch validation / 补丁验证

**Example / 示例:**
```python
try:
    result = function(*arguments)
except Exception as e:
    error_description = str(e)
    new_code = llm.invoke(f'Fix this function: {function_string}, Error: {error_description}')
# → Detect error and generate fix

```

---

### 2. 向量数据库记忆 / Vector Database Memory

**English:** Use ChromaDB to store bug reports and find similar historical bugs and fixes through semantic search.

**中文:** 使用ChromaDB存储bug报告，通过语义搜索找到相似的历史bug和修复方案。

**Key Concepts / 核心概念:**
- ChromaDB / 向量数据库
- Bug patterns / Bug模式
- Semantic search / 语义搜索

**Example / 示例:**
```python
collection.add(ids=[id], documents=[bug_report])
results = collection.query(query_texts=[new_bug], n_results=10)
# → Store and query bug patterns

```

---

## Summary / 总结

This lesson covered key AI Agent concepts. Practice these techniques to build better intelligent systems.

本课程涵盖了关键AI Agent技术。练习这些技术以构建更好的智能系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own agents / 构建自己的Agent
3. Explore advanced patterns / 探索高级模式
