# 自我改进Agent / Self-Improving Agent

## Overview / 概述

Build agents that can learn from feedback and improve their behavior over time. / 构建能够从反馈中学习并随时间改进行为的Agent。

## Key Knowledge Points / 核心知识点

### 1. 反馈学习 / Feedback Learning

**English:** Agent learns from user feedback and adjusts its behavior and response strategies.

**中文:** Agent从用户反馈中学习，调整其行为和响应策略。

**Key Concepts / 核心概念:**
- User feedback / 用户反馈
- Behavior adjustment / 行为调整
- Learning loop / 学习循环

**Example / 示例:**
```python
feedback = 'The response was too verbose'
improved_prompt = optimizer.invoke({
    'trajectories': [(conversation, {'feedback': feedback})],
    'prompts': current_prompts
})
# → Learn from feedback to improve prompts

```

---

### 2. 提示优化 / Prompt Optimization

**English:** Use optimizer to automatically improve agent's system prompts based on feedback.

**中文:** 使用优化器根据反馈自动改进Agent的系统提示。

**Key Concepts / 核心概念:**
- Prompt optimizer / 提示优化器
- Trajectory analysis / 轨迹分析
- Continuous improvement / 持续改进

**Example / 示例:**
```python
optimizer = create_multi_prompt_optimizer(llm)
result = optimizer.invoke({'trajectories': trajectories, 'prompts': prompts})
improved_prompt = next(p['prompt'] for p in result if p['name'] == 'response')
# → Optimize prompts based on feedback

```

---

## Summary / 总结

This lesson covered key AI Agent concepts. Practice these techniques to build better intelligent systems.

本课程涵盖了关键AI Agent技术。练习这些技术以构建更好的智能系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own agents / 构建自己的Agent
3. Explore advanced patterns / 探索高级模式
