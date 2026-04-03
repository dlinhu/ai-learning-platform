# LangGraph 入门教程 / Introduction to LangGraph

## Overview / 概述

Learn LangGraph fundamentals including StateGraph, nodes, edges, and workflow visualization. / 学习LangGraph基础，包括StateGraph、节点、边和工作流可视化。

## Key Knowledge Points / 核心知识点

### 1. StateGraph 工作流 / StateGraph Workflow

**English:** LangGraph uses StateGraph to create graph-based workflows where each node represents a function or computational step, and edges define the flow between nodes.

**中文:** LangGraph使用StateGraph创建基于图的工作流，每个节点代表一个函数或计算步骤，边定义节点之间的流程。

**Key Concepts / 核心概念:**
- StateGraph / 状态图
- Nodes / 节点
- Edges / 边
- Workflow / 工作流

**Example / 示例:**
```python
workflow = StateGraph(State)
workflow.add_node('classification_node', classification_node)
workflow.add_edge('classification_node', 'entity_extraction')
app = workflow.compile()
# → Create and compile a LangGraph workflow

```

---

### 2. 状态管理 / State Management

**English:** Use TypedDict to define state classes for passing and updating data between workflow nodes.

**中文:** 使用TypedDict定义状态类，在工作流节点之间传递和更新数据。

**Key Concepts / 核心概念:**
- TypedDict / 类型字典
- State / 状态
- Data flow / 数据流

**Example / 示例:**
```python
class State(TypedDict):
    text: str
    classification: str
    entities: List[str]
    summary: str
# → Define workflow state with TypedDict

```

---

## Summary / 总结

This lesson covered key AI Agent concepts. Practice these techniques to build better intelligent systems.

本课程涵盖了关键AI Agent技术。练习这些技术以构建更好的智能系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own agents / 构建自己的Agent
3. Explore advanced patterns / 探索高级模式
