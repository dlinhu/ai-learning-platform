# Reranking / 重排序

## Overview / 概述

Learn reranking techniques that improve retrieval relevance by reassessing and reordering retrieved documents. / 学习重排序技术，通过重新评估和排序检索文档提高检索相关性。

## Key Knowledge Points / 核心知识点

### 1. Reranking Concept / 重排序概念

**English:** Reranking reassesses and reorders initial retrieval results using more sophisticated models for better relevance judgment.

**中文:** 重排序是对初始检索结果进行重新评估和排序，使用更复杂的模型提高相关性判断。

**Key Concepts / 核心概念:**
- Relevance scoring / 相关性评分
- Document reordering / 文档重排序
- Quality improvement / 质量提升

**Example / 示例:**
```python
1. Initial retrieval with vector search
2. Score each document with LLM/CrossEncoder
3. Sort by relevance score
4. Return top K documents
# → Two-stage retrieval with reranking

```

---

### 2. LLM vs Cross-Encoder / LLM与交叉编码器

**English:** LLM reranking uses language models for scoring, Cross-Encoder uses specially trained relevance models, each with advantages.

**中文:** LLM重排序使用语言模型评分，Cross-Encoder使用专门训练的相关性模型，各有优势。

**Key Concepts / 核心概念:**
- LLM scoring / LLM评分
- Cross-Encoder / 交叉编码器
- Trade-offs / 权衡取舍

**Example / 示例:**
```python
cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')
scores = cross_encoder.predict([[query, doc] for doc in docs])
# → Fast and accurate relevance scoring

```

---

## Summary / 总结

This lesson covered key RAG techniques. Practice these concepts to build better retrieval systems.

本课程涵盖了关键RAG技术。练习这些概念以构建更好的检索系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Compare different approaches / 比较不同方法
3. Optimize for your use case / 针对您的场景优化
