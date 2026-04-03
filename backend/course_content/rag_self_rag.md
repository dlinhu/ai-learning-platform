# Self RAG / 自我RAG

## Overview / 概述

Learn Self-RAG that enables models to reflect on and improve their own retrieval and generation. / 学习自我RAG，让模型反思并改进自己的检索和生成过程。

## Key Knowledge Points / 核心知识点

### 1. Self-Reflection / 自我反思

**English:** Self-RAG enables models to evaluate retrieval relevance and generation quality for self-improvement.

**中文:** Self-RAG让模型评估检索内容的相关性和生成答案的质量，进行自我改进。

**Key Concepts / 核心概念:**
- Relevance assessment / 相关性评估
- Quality evaluation / 质量评估
- Self-improvement / 自我改进

**Example / 示例:**
```python
1. Retrieve documents
2. Assess relevance: Is this relevant?
3. Generate answer
4. Evaluate: Is this supported by context?
5. Refine if needed
# → Iterative self-improvement loop

```

---

### 2. Adaptive Retrieval / 自适应检索

**English:** Decide whether retrieval is needed based on question complexity, avoiding unnecessary retrieval operations.

**中文:** 根据问题复杂度决定是否需要检索，避免不必要的检索操作。

**Key Concepts / 核心概念:**
- Need assessment / 需求评估
- Efficiency optimization / 效率优化
- Dynamic decision / 动态决策

**Example / 示例:**
```python
question = "What is 2+2?"
decision = "No retrieval needed"  # Simple question

question = "What are the latest AI trends?"
decision = "Retrieval needed"  # Requires current info
# → Dynamic retrieval decision based on question type

```

---

## Summary / 总结

This lesson covered key RAG techniques. Practice these concepts to build better retrieval systems.

本课程涵盖了关键RAG技术。练习这些概念以构建更好的检索系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Compare different approaches / 比较不同方法
3. Optimize for your use case / 针对您的场景优化
