# Fusion Retrieval / 融合检索

## Overview / 概述

Learn fusion retrieval techniques that combine multiple retrieval methods for better results. / 学习融合检索技术，结合多种检索方法获得更好结果。

## Key Knowledge Points / 核心知识点

### 1. Multi-Method Fusion / 多方法融合

**English:** Fusion retrieval combines vector retrieval, keyword retrieval, and other methods, ranking comprehensively to improve retrieval quality.

**中文:** 融合检索结合向量检索、关键词检索等多种方法，综合排序提高检索质量。

**Key Concepts / 核心概念:**
- Vector retrieval / 向量检索
- Keyword retrieval / 关键词检索
- Result fusion / 结果融合

**Example / 示例:**
```python
vector_results = vector_store.search(query)
keyword_results = bm25_search(query)
fused_results = reciprocal_rank_fusion(
    [vector_results, keyword_results]
)
# → Combine multiple retrieval methods

```

---

### 2. Reciprocal Rank Fusion / 倒数排名融合

**English:** RRF algorithm calculates comprehensive scores based on reciprocal ranks from each method, simply and effectively fusing multiple retrieval results.

**中文:** RRF算法根据各方法的排名倒数计算综合分数，简单有效地融合多种检索结果。

**Key Concepts / 核心概念:**
- Rank aggregation / 排名聚合
- Score combination / 分数组合
- Simple effective / 简单有效

**Example / 示例:**
```python
def rrf(rankings, k=60):
    scores = {}
    for ranking in rankings:
        for i, doc in enumerate(ranking):
            scores[doc] = scores.get(doc, 0) + 1/(k + i + 1)
    return sorted(scores.items(), key=lambda x: -x[1])
# → Simple and effective fusion algorithm

```

---

## Summary / 总结

This lesson covered key RAG techniques. Practice these concepts to build better retrieval systems.

本课程涵盖了关键RAG技术。练习这些概念以构建更好的检索系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Compare different approaches / 比较不同方法
3. Optimize for your use case / 针对您的场景优化
