# 检索增强生成 / Retrieval Augmented Generation

## Overview / 概述

Learn RAG fundamentals, architectures, and optimization strategies. / 学习RAG基础、架构和优化策略。

## Key Knowledge Points / 核心知识点

### 1. RAG 基础架构 / RAG Fundamentals

**English:** Core architecture of RAG systems: collaboration between retriever, reranker, and generator.

**中文:** RAG系统的核心架构：检索器、重排序器和生成器的协同工作。

**Key Concepts / 核心概念:**
- Retriever / 检索器
- Reranker / 重排序器
- Generator / 生成器
- Pipeline / 流水线

**Example / 示例:**
```python
class RAGSystem:
    def __init__(self):
        self.retriever = DenseRetriever()
        self.reranker = CrossEncoderReranker()
        self.generator = LLMGenerator()
    def query(self, q):
        docs = self.retriever.retrieve(q)
        ranked = self.reranker.rerank(q, docs)
        return self.generator.generate(q, ranked)
# → Implement RAG system architecture

```

---

### 2. 稠密段落检索 / Dense Passage Retrieval

**English:** Efficient passage retrieval using dual-encoder architecture.

**中文:** 使用双编码器架构进行高效的段落检索。

**Key Concepts / 核心概念:**
- Dual Encoder / 双编码器
- Passage Embedding / 段落嵌入
- Query Encoding / 查询编码
- FAISS Index / FAISS索引

**Example / 示例:**
```python
class DualEncoder:
    def encode_query(self, query): return self.query_encoder(query)
    def encode_passage(self, passage): return self.passage_encoder(passage)
    def retrieve(self, query, index, k=10):
        q_emb = self.encode_query(query)
        return index.search(q_emb, k)
# → Implement dual encoder for DPR

```

---

### 3. 混合检索策略 / Hybrid Retrieval Strategies

**English:** Combining advantages of sparse retrieval (BM25) and dense retrieval.

**中文:** 结合稀疏检索（BM25）和稠密检索的优势。

**Key Concepts / 核心概念:**
- BM25 / BM25算法
- Dense Retrieval / 稠密检索
- Score Fusion / 分数融合
- Reciprocal Rank / 倒数排名

**Example / 示例:**
```python
def hybrid_retrieve(query, sparse_idx, dense_idx, alpha=0.5):
    sparse_results = bm25_search(query, sparse_idx)
    dense_results = dense_search(query, dense_idx)
    return reciprocal_rank_fusion(sparse_results, dense_results, alpha)
# → Implement hybrid retrieval

```

---

## Summary / 总结

This lesson covered key context engineering concepts. Practice these techniques to build robust context systems.

本课程涵盖了关键的上下文工程技术。练习这些技术以构建健壮的上下文系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own context systems / 构建自己的上下文系统
3. Explore advanced patterns / 探索高级模式
