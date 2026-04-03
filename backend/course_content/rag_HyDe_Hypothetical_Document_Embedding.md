# HyDe / 假设文档嵌入

## Overview / 概述

Learn Hypothetical Document Embedding (HyDe) that generates hypothetical documents to improve retrieval. / 学习假设文档嵌入技术，通过生成假设文档提高检索效果。

## Key Knowledge Points / 核心知识点

### 1. Hypothetical Document Generation / 假设文档生成

**English:** HyDe has LLM generate a hypothetical ideal answer document, then uses this document for retrieval to improve relevance.

**中文:** HyDe让LLM生成一个假设的理想答案文档，然后用这个文档进行检索，提高检索相关性。

**Key Concepts / 核心概念:**
- Hypothetical answer / 假设答案
- Document generation / 文档生成
- Enhanced retrieval / 增强检索

**Example / 示例:**
```python
query = "What causes climate change?"
hypothetical_doc = llm.generate("Write an answer about climate change causes")
embedding = embed(hypothetical_doc)
results = vector_store.search(embedding)
# → Use hypothetical document for better retrieval

```

---

### 2. Semantic Bridging / 语义桥接

**English:** Hypothetical document acts as semantic bridge between query and real documents, addressing vocabulary mismatch.

**中文:** 假设文档作为查询和真实文档之间的语义桥梁，弥补词汇不匹配问题。

**Key Concepts / 核心概念:**
- Vocabulary mismatch / 词汇不匹配
- Semantic similarity / 语义相似性
- Bridge mechanism / 桥接机制

**Example / 示例:**
```python
Query: "How to fix slow computer?"
Hypothetical: "To improve computer performance, you can..."
This bridges to documents about "system optimization", "RAM upgrade", etc.
# → Hypothetical document expands semantic coverage

```

---

## Summary / 总结

This lesson covered key RAG techniques. Practice these concepts to build better retrieval systems.

本课程涵盖了关键RAG技术。练习这些概念以构建更好的检索系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Compare different approaches / 比较不同方法
3. Optimize for your use case / 针对您的场景优化
