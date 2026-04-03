# Constrained & Guided Generation / 约束引导生成

## Overview / 概述

Learn constrained and guided generation techniques for controlled AI outputs. / 学习约束引导生成技术，实现可控的AI输出。

## Key Knowledge Points / 核心知识点

### 1. Output Constraints / 输出约束

**English:** Output constraints control model output scope and structure by defining format, length, and content limitations.

**中文:** 输出约束通过定义格式、长度、内容等限制，控制模型生成的输出范围和结构。

**Key Concepts / 核心概念:**
- Format constraints / 格式约束
- Length constraints / 长度约束
- Content constraints / 内容约束

**Example / 示例:**
```
Output must be valid JSON with keys: name, age, email.
→ {
  "name": "John",
  "age": 30,
  "email": "john@example.com"
}

```

---

### 2. Guided Generation / 引导生成

**English:** Guided generation uses structured prompts, templates, and grammar constraints to guide models to generate content as expected.

**中文:** 引导生成使用结构化提示、模板、语法约束等方法，引导模型按预期方式生成内容。

**Key Concepts / 核心概念:**
- Structured prompts / 结构化提示
- Grammar constraints / 语法约束
- Template guidance / 模板引导

**Example / 示例:**
```
Generate a sentence following this pattern:
[Adjective] [Noun] [Verb] [Adverb]
→ The quick fox runs swiftly.

```

---

## Summary / 总结

This lesson covered the key concepts and techniques for effective prompt engineering. Practice these techniques to improve your AI interactions.

本课程涵盖了有效提示工程的关键概念和技术。练习这些技术以提高您的AI交互能力。

## Next Steps / 下一步

1. Practice with real examples / 使用真实示例练习
2. Experiment with different techniques / 尝试不同技术
3. Build your own prompt library / 构建您自己的提示库
