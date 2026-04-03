# Zero-Shot Prompting / 零样本提示

## Overview / 概述

Learn zero-shot prompting techniques that allow AI models to perform tasks without specific examples. / 学习零样本提示技术，让AI模型在没有具体示例的情况下执行任务。

## Key Knowledge Points / 核心知识点

### 1. Direct Task Specification / 直接任务指定

**English:** Direct task specification is the core method of zero-shot prompting, clearly defining task requirements for the model to understand and execute without examples.

**中文:** 直接任务指定是零样本提示的核心方法，通过清晰定义任务要求让模型理解并执行，无需提供示例。

**Key Concepts / 核心概念:**
- Clear instructions / 清晰指令
- No examples needed / 无需示例
- Task definition / 任务定义

**Example / 示例:**
```
Classify the sentiment as Positive, Negative, or Neutral.
Text: {text}
Sentiment:
→ Direct classification without examples

```

---

### 2. Format Specification / 格式规范

**English:** Format specification provides output format guidelines in prompts to help models respond in a structured way for zero-shot tasks.

**中文:** 格式规范通过在提示中提供输出格式指南，帮助模型以结构化方式响应零样本任务。

**Key Concepts / 核心概念:**
- Output structure / 输出结构
- Format templates / 格式模板
- Structured response / 结构化响应

**Example / 示例:**
```
Generate a news article with:
Headline: [...]
Lead: [...]
Body: [...]
Conclusion: [...]
→ Structured article output

```

---

### 3. Multi-step Reasoning / 多步推理

**English:** Multi-step reasoning breaks down complex tasks into simpler zero-shot steps, improving overall model performance and accuracy.

**中文:** 多步推理将复杂任务分解为简单的零样本步骤，提高模型的整体性能和准确性。

**Key Concepts / 核心概念:**
- Task decomposition / 任务分解
- Step-by-step analysis / 逐步分析
- Complex problem solving / 复杂问题解决

**Example / 示例:**
```
Analyze the text:
1. Main Argument
2. Supporting Evidence
3. Counterarguments
→ Structured analysis output

```

---

## Summary / 总结

This lesson covered the key concepts and techniques for effective prompt engineering. Practice these techniques to improve your AI interactions.

本课程涵盖了有效提示工程的关键概念和技术。练习这些技术以提高您的AI交互能力。

## Next Steps / 下一步

1. Practice with real examples / 使用真实示例练习
2. Experiment with different techniques / 尝试不同技术
3. Build your own prompt library / 构建您自己的提示库
