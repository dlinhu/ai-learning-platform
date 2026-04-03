# Semantic Chunking / 语义分块

## Overview / 概述

Learn semantic chunking techniques that create context-aware text segments based on meaning rather than fixed sizes. / 学习语义分块技术，基于语义而非固定大小创建上下文感知的文本片段。

## Key Knowledge Points / 核心知识点

### 1. Semantic Chunking Concept / 语义分块概念

**English:** Semantic chunking splits text based on semantic similarity, maintaining semantic coherence and avoiding breaks in the middle of sentences.

**中文:** 语义分块根据文本的语义相似性进行分割，保持语义连贯性，避免在句子中间断开。

**Key Concepts / 核心概念:**
- Semantic coherence / 语义连贯性
- Breakpoint detection / 断点检测
- Context preservation / 上下文保持

**Example / 示例:**
```python
text_splitter = SemanticChunker(
    OpenAIEmbeddings(),
    breakpoint_threshold_type='percentile',
    breakpoint_threshold_amount=90
)
docs = text_splitter.create_documents([content])
# → Create semantically coherent chunks

```

---

### 2. Breakpoint Types / 断点类型

**English:** Three breakpoint types: percentile, standard deviation, and interquartile range for determining text split points.

**中文:** 三种断点类型：百分位数、标准差、四分位距，用于确定文本分割点。

**Key Concepts / 核心概念:**
- Percentile / 百分位数
- Standard Deviation / 标准差
- Interquartile Range / 四分位距

**Example / 示例:**
```python
# Percentile: splits at differences > X percentile
# Standard deviation: splits at differences > X std
# Interquartile: uses IQR for split points
# → Different methods for semantic boundary detection

```

---

## Summary / 总结

This lesson covered key RAG techniques. Practice these concepts to build better retrieval systems.

本课程涵盖了关键RAG技术。练习这些概念以构建更好的检索系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Compare different approaches / 比较不同方法
3. Optimize for your use case / 针对您的场景优化
