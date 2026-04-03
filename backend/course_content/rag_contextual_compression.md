# Contextual Compression / 上下文压缩

## Overview / 概述

Learn contextual compression techniques that extract and compress relevant information from retrieved documents. / 学习上下文压缩技术，从检索文档中提取和压缩相关信息。

## Key Knowledge Points / 核心知识点

### 1. Compression Concept / 压缩概念

**English:** Contextual compression extracts query-relevant parts from retrieved documents, reducing noise and improving relevance.

**中文:** 上下文压缩从检索文档中提取与查询相关的部分，减少噪声并提高相关性。

**Key Concepts / 核心概念:**
- Relevant extraction / 相关提取
- Noise reduction / 噪声减少
- Context optimization / 上下文优化

**Example / 示例:**
```python
compressor = LLMChainExtractor.from_llm(llm)
compression_retriever = ContextualCompressionRetriever(
    base_compressor=compressor,
    base_retriever=base_retriever
)
# → Extract only relevant parts from documents

```

---

## Summary / 总结

This lesson covered key RAG techniques. Practice these concepts to build better retrieval systems.

本课程涵盖了关键RAG技术。练习这些概念以构建更好的检索系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Compare different approaches / 比较不同方法
3. Optimize for your use case / 针对您的场景优化
