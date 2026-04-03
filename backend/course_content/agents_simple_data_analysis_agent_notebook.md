# 数据分析Agent / Data Analysis Agent

## Overview / 概述

Create an AI-powered data analysis agent that can interpret and answer questions about datasets using natural language. / 创建能够用自然语言解释和回答数据集问题的AI数据分析Agent。

## Key Knowledge Points / 核心知识点

### 1. Pandas DataFrame Agent / Pandas数据框Agent

**English:** Use create_pandas_dataframe_agent to create agents that can analyze dataframes with natural language queries.

**中文:** 使用create_pandas_dataframe_agent创建能够分析数据框的Agent，支持自然语言查询。

**Key Concepts / 核心概念:**
- create_pandas_dataframe_agent / Pandas Agent创建
- Natural language queries / 自然语言查询
- Data analysis / 数据分析

**Example / 示例:**
```python
agent = create_pandas_dataframe_agent(
    ChatOpenAI(model='gpt-4o'),
    df,
    verbose=True,
    allow_dangerous_code=True
)
# → Create Pandas DataFrame agent

```

---

### 2. 自然语言数据查询 / Natural Language Data Queries

**English:** Agent can convert natural language questions into Python code to perform data analysis.

**中文:** Agent可以将自然语言问题转换为Python代码执行数据分析。

**Key Concepts / 核心概念:**
- Query translation / 查询转换
- Code generation / 代码生成
- Result interpretation / 结果解释

**Example / 示例:**
```python
agent.run({'input': 'What is the average price of cars sold?'})
# Agent generates: df['Price'].mean()
# → Natural language to data analysis

```

---

## Summary / 总结

This lesson covered key AI Agent concepts. Practice these techniques to build better intelligent systems.

本课程涵盖了关键AI Agent技术。练习这些技术以构建更好的智能系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own agents / 构建自己的Agent
3. Explore advanced patterns / 探索高级模式
