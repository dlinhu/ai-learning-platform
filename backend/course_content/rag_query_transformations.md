# Query Transformations / 查询转换

## Overview / 概述

Learn query transformation techniques that improve retrieval by modifying or expanding user queries. / 学习查询转换技术，通过修改或扩展用户查询提高检索效果。

## Key Knowledge Points / 核心知识点

### 1. Query Expansion / 查询扩展

**English:** Query expansion enhances original queries by generating multiple related queries or adding synonyms to improve recall.

**中文:** 查询扩展通过生成多个相关查询或添加同义词来增强原始查询，提高召回率。

**Key Concepts / 核心概念:**
- Multi-query generation / 多查询生成
- Synonym expansion / 同义词扩展
- Recall improvement / 召回率提升

**Example / 示例:**
```python
original_query = "climate change effects"
expanded_queries = [
    "What are the impacts of climate change?",
    "How does global warming affect the environment?",
    "Consequences of climate change"
]
# → Generate multiple related queries for better retrieval

```

---

### 2. Query Rewriting / 查询重写

**English:** Query rewriting transforms vague or complex queries into clearer, more retrievable forms.

**中文:** 查询重写将模糊或复杂的查询转换为更清晰、更易检索的形式。

**Key Concepts / 核心概念:**
- Query clarification / 查询澄清
- Intent understanding / 意图理解
- Optimization / 优化

**Example / 示例:**
```python
original = "it doesn't work"
rewritten = "What are common troubleshooting steps for [specific product] when it fails to start?"
# → Transform vague query to specific one

```

---

## Summary / 总结

This lesson covered key RAG techniques. Practice these concepts to build better retrieval systems.

本课程涵盖了关键RAG技术。练习这些概念以构建更好的检索系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Compare different approaches / 比较不同方法
3. Optimize for your use case / 针对您的场景优化
