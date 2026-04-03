# RAPTOR / 递归摘要树

## Overview / 概述

Learn RAPTOR (Recursive Abstractive Processing for Tree-Organized Retrieval) that builds hierarchical document summaries. / 学习RAPTOR递归摘要树技术，构建层次化文档摘要。

## Key Knowledge Points / 核心知识点

### 1. Hierarchical Summarization / 层次化摘要

**English:** RAPTOR recursively builds document summary trees, from bottom-level documents to top-level summaries, supporting multi-granularity retrieval.

**中文:** RAPTOR递归地构建文档摘要树，从底层文档到高层摘要，支持多粒度检索。

**Key Concepts / 核心概念:**
- Tree structure / 树结构
- Recursive summarization / 递归摘要
- Multi-granularity / 多粒度

**Example / 示例:**
```python
Level 0: Original documents
Level 1: Summaries of document clusters
Level 2: Summaries of Level 1 summaries
...
Query: search across all levels
# → Hierarchical retrieval from fine to coarse granularity

```

---

### 2. Cluster-based Summarization / 聚类摘要

**English:** Cluster similar documents then generate summaries, preserving topic coherence and improving retrieval efficiency.

**中文:** 将相似文档聚类后生成摘要，保留主题连贯性，提高检索效率。

**Key Concepts / 核心概念:**
- Document clustering / 文档聚类
- Topic coherence / 主题连贯
- Efficient retrieval / 高效检索

**Example / 示例:**
```python
1. Embed all documents
2. Cluster by similarity
3. Generate summary for each cluster
4. Recursively cluster summaries
5. Build tree structure
# → Build hierarchical summary tree from documents

```

---

## Summary / 总结

This lesson covered key RAG techniques. Practice these concepts to build better retrieval systems.

本课程涵盖了关键RAG技术。练习这些概念以构建更好的检索系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Compare different approaches / 比较不同方法
3. Optimize for your use case / 针对您的场景优化
