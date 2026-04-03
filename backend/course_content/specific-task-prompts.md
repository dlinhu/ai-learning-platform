# Specific Task Prompts / 特定任务提示

## Overview / 概述

Learn prompt design techniques for specific tasks like summarization, translation, and classification. / 学习特定任务如摘要、翻译、分类的提示设计技术。

## Key Knowledge Points / 核心知识点

### 1. Summarization Prompts / 摘要提示

**English:** Summarization prompts are designed for generating text summaries, including length control, key point extraction, and format specification.

**中文:** 摘要提示设计用于生成文本摘要，包括长度控制、重点提取、格式规范等要素。

**Key Concepts / 核心概念:**
- Length control / 长度控制
- Key point extraction / 重点提取
- Format specification / 格式规范

**Example / 示例:**
```
Summarize the following text in 3 bullet points, focusing on the main arguments:
{text}
→ Concise bullet-point summary

```

---

### 2. Translation Prompts / 翻译提示

**English:** Translation prompts are designed for high-quality translation, including source/target language specification, style preservation, and terminology consistency.

**中文:** 翻译提示设计用于高质量翻译，包括源语言和目标语言指定、风格保持、术语一致性等。

**Key Concepts / 核心概念:**
- Language specification / 语言指定
- Style preservation / 风格保持
- Terminology consistency / 术语一致性

**Example / 示例:**
```
Translate from English to Chinese. Maintain formal business tone. Keep technical terms in English.
Text: {text}
→ Professional translation with preserved terms

```

---

### 3. Classification Prompts / 分类提示

**English:** Classification prompts are designed to assign inputs to predefined categories, including category definition, boundary specification, and example provision.

**中文:** 分类提示设计用于将输入分配到预定义类别，包括类别定义、边界说明、示例提供等。

**Key Concepts / 核心概念:**
- Category definition / 类别定义
- Boundary specification / 边界说明
- Example provision / 示例提供

**Example / 示例:**
```
Classify the email into one of:
- Urgent
- Normal
- Low priority

Email: {email}
Category:
→ Single category classification

```

---

## Summary / 总结

This lesson covered the key concepts and techniques for effective prompt engineering. Practice these techniques to improve your AI interactions.

本课程涵盖了有效提示工程的关键概念和技术。练习这些技术以提高您的AI交互能力。

## Next Steps / 下一步

1. Practice with real examples / 使用真实示例练习
2. Experiment with different techniques / 尝试不同技术
3. Build your own prompt library / 构建您自己的提示库
