# Prompt Templates & Variables / 提示模板与变量

## Overview / 概述

Learn prompt templates and variable techniques using Jinja2 for dynamic prompt generation. / 学习使用Jinja2的提示模板和变量技术进行动态提示生成。

## Key Knowledge Points / 核心知识点

### 1. Template Basics / 模板基础

**English:** Template basics involve creating reusable prompt templates with variable placeholders, supporting dynamic content injection and formatting.

**中文:** 模板基础涉及使用变量占位符创建可复用的提示模板，支持动态内容注入和格式化。

**Key Concepts / 核心概念:**
- Variable placeholders / 变量占位符
- Reusability / 可复用性
- Dynamic content / 动态内容

**Example / 示例:**
```
Hello {{name}}, please explain {{topic}}.
→ Personalized prompt with injected values

```

---

### 2. Jinja2 Syntax / Jinja2语法

**English:** Jinja2 syntax includes variable interpolation, conditional statements, loops, filters, and other advanced template features.

**中文:** Jinja2语法包括变量插值、条件语句、循环、过滤器等高级模板功能。

**Key Concepts / 核心概念:**
- Variable interpolation / 变量插值
- Conditionals / 条件语句
- Loops / 循环
- Filters / 过滤器

**Example / 示例:**
```
{% for item in items %}
{{item}}: {{item|length}} chars
{% endfor %}
→ Formatted list with filters applied

```

---

## Summary / 总结

This lesson covered the key concepts and techniques for effective prompt engineering. Practice these techniques to improve your AI interactions.

本课程涵盖了有效提示工程的关键概念和技术。练习这些技术以提高您的AI交互能力。

## Next Steps / 下一步

1. Practice with real examples / 使用真实示例练习
2. Experiment with different techniques / 尝试不同技术
3. Build your own prompt library / 构建您自己的提示库
