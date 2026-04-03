# 混合 Agent 教程 / Hybrid Agent Tutorial

## Overview / 概述

Build hybrid agents combining local and cloud capabilities. / 构建结合本地和云端能力的混合Agent。

## Key Knowledge Points / 核心知识点

### 1. 混合 Agent 架构 / Hybrid Agent Architecture

**English:** Combine advantages of local LLMs and cloud APIs to balance cost and performance.

**中文:** 结合本地LLM和云端API的优势，实现成本和性能的平衡。

**Key Concepts / 核心概念:**
- Hybrid architecture / 混合架构
- Local LLM / 本地LLM
- Cloud API / 云端API
- Cost optimization / 成本优化

**Example / 示例:**
```python
class HybridAgent:
    def __init__(self):
        self.local_llm = OllamaLLM(model='llama3')
        self.cloud_llm = ChatOpenAI(model='gpt-4o')
# → Create hybrid agent with local and cloud LLMs

```

---

## Summary / 总结

This lesson covered key production deployment concepts. Practice these techniques to build robust production systems.

本课程涵盖了关键的生产部署技术。练习这些技术以构建健壮的生产系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own production agents / 构建自己的生产Agent
3. Explore advanced patterns / 探索高级模式
