# CRAG / 纠正性RAG

## Overview / 概述

Learn Corrective RAG (CRAG) that corrects retrieval errors through document evaluation and knowledge refinement. / 学习纠正性RAG，通过文档评估和知识精炼纠正检索错误。

## Key Knowledge Points / 核心知识点

### 1. Document Evaluation / 文档评估

**English:** CRAG evaluates retrieved document relevance to decide whether to use, discard, or supplement knowledge.

**中文:** CRAG评估检索文档的相关性，决定是使用、丢弃还是补充知识。

**Key Concepts / 核心概念:**
- Relevance scoring / 相关性评分
- Decision making / 决策制定
- Quality control / 质量控制

**Example / 示例:**
```python
1. Retrieve documents
2. Evaluate: relevant or not?
3. If relevant → use
4. If irrelevant → web search
5. If ambiguous → combine both
# → Corrective retrieval with fallback options

```

---

### 2. Knowledge Refinement / 知识精炼

**English:** Extract key information from relevant documents, filter irrelevant content, improve answer quality.

**中文:** 从相关文档中提取关键信息，过滤无关内容，提高答案质量。

**Key Concepts / 核心概念:**
- Information extraction / 信息提取
- Content filtering / 内容过滤
- Quality enhancement / 质量增强

**Example / 示例:**
```python
relevant_docs = evaluate_documents(retrieved_docs)
refined_knowledge = extract_key_points(relevant_docs)
answer = generate_with_context(query, refined_knowledge)
# → Extract and refine knowledge for better answers

```

---

## Summary / 总结

This lesson covered key RAG techniques. Practice these concepts to build better retrieval systems.

本课程涵盖了关键RAG技术。练习这些概念以构建更好的检索系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Compare different approaches / 比较不同方法
3. Optimize for your use case / 针对您的场景优化
