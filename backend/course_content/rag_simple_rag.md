# Simple RAG / 基础RAG系统

## Overview / 概述

Learn the fundamentals of Retrieval-Augmented Generation systems including document processing, chunking, vector storage, and retrieval. / 学习检索增强生成系统的基础知识，包括文档处理、分块、向量存储和检索。

## Key Knowledge Points / 核心知识点

### 1. RAG System Components / RAG系统组件

**English:** RAG systems consist of document loaders, text splitters, embedding models, vector stores, and retrievers, implementing the complete flow from documents to retrieval.

**中文:** RAG系统由文档加载器、文本分割器、嵌入模型、向量存储和检索器组成，实现从文档到检索的完整流程。

**Key Concepts / 核心概念:**
- Document Loading / 文档加载
- Text Chunking / 文本分块
- Vector Store / 向量存储
- Retriever / 检索器

**Example / 示例:**
```python
loader = PyPDFLoader(path)
documents = loader.load()
text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)
texts = text_splitter.split_documents(documents)
vectorstore = FAISS.from_documents(texts, embeddings)
# → Complete RAG pipeline from document to vector store

```

---

### 2. Vector Store Creation / 向量存储创建

**English:** Create efficient vector stores using FAISS and OpenAI embeddings for fast similarity search.

**中文:** 使用FAISS和OpenAI嵌入创建高效的向量存储，支持快速相似性搜索。

**Key Concepts / 核心概念:**
- FAISS / Facebook AI相似性搜索
- OpenAI Embeddings / OpenAI嵌入
- Similarity Search / 相似性搜索

**Example / 示例:**
```python
embeddings = OpenAIEmbeddings()
vectorstore = FAISS.from_documents(texts, embeddings)
retriever = vectorstore.as_retriever(search_kwargs={'k': 2})
# → Create retriever returning top 2 results

```

---

## Summary / 总结

This lesson covered key RAG techniques. Practice these concepts to build better retrieval systems.

本课程涵盖了关键RAG技术。练习这些概念以构建更好的检索系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Compare different approaches / 比较不同方法
3. Optimize for your use case / 针对您的场景优化
