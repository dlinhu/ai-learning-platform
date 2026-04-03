# Few-Shot Learning / 少样本学习

## Overview / 概述

Learn few-shot learning techniques that enable AI models to perform tasks with minimal examples. / 学习少样本学习技术，让AI模型通过少量示例执行任务。

## Key Knowledge Points / 核心知识点

### 1. Basic Few-Shot Learning / 基础少样本学习

**English:** Basic few-shot learning enables models to quickly learn and generalize to new tasks with minimal labeled examples, without requiring large training datasets.

**中文:** 基础少样本学习通过提供少量标注示例，让模型快速学习并泛化到新任务，无需大量训练数据。

**Key Concepts / 核心概念:**
- Example-based learning / 示例学习
- Quick adaptation / 快速适应
- Minimal data / 最少数据

**Example / 示例:**
```
Examples:
Text: I love this! → Positive
Text: This is terrible → Negative
Text: {input} → ?
→ Classification based on examples

```

---

### 2. In-Context Learning / 上下文学习

**English:** In-context learning allows models to adapt to new tasks based solely on examples provided in the prompt, without fine-tuning model parameters.

**中文:** 上下文学习允许模型仅根据提示中提供的示例适应新任务，无需微调模型参数。

**Key Concepts / 核心概念:**
- No fine-tuning / 无需微调
- Prompt-based adaptation / 提示适应
- Flexible learning / 灵活学习

**Example / 示例:**
```
Task: Convert to pig latin
hello → ellohay
apple → appleay
{input} → ?
→ Learned transformation rule

```

---

### 3. Multi-Task Few-Shot / 多任务少样本

**English:** Multi-task few-shot learning designs prompt templates that enable a single model to perform multiple related tasks, improving efficiency and generalization.

**中文:** 多任务少样本学习设计一个提示模板，让单个模型执行多个相关任务，提高效率和泛化能力。

**Key Concepts / 核心概念:**
- Task switching / 任务切换
- Shared examples / 共享示例
- Multi-purpose prompts / 多用途提示

**Example / 示例:**
```
Perform the specified task:
Text: Bonjour
Task: language → French
Text: {input}
Task: {task} → ?
→ Task-specific output

```

---

## Summary / 总结

This lesson covered the key concepts and techniques for effective prompt engineering. Practice these techniques to improve your AI interactions.

本课程涵盖了有效提示工程的关键概念和技术。练习这些技术以提高您的AI交互能力。

## Next Steps / 下一步

1. Practice with real examples / 使用真实示例练习
2. Experiment with different techniques / 尝试不同技术
3. Build your own prompt library / 构建您自己的提示库
