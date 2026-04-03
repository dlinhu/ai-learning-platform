# Basic Prompt Structures Tutorial / 基础提示结构教程

## Overview / 概述

This tutorial focuses on two fundamental types of prompt structures:
本教程专注于两种基本的提示结构类型：

1. **Single-turn prompts / 单轮提示**
2. **Multi-turn prompts (conversations) / 多轮提示（对话）**

We'll use OpenAI's GPT model and LangChain to demonstrate these concepts.
我们将使用OpenAI的GPT模型和LangChain来演示这些概念。

## Motivation / 学习动机

Understanding different prompt structures is crucial for effective communication with AI models. Single-turn prompts are useful for quick, straightforward queries, while multi-turn prompts enable more complex, context-aware interactions. Mastering these structures allows for more versatile and effective use of AI in various applications.

理解不同的提示结构对于与AI模型有效沟通至关重要。单轮提示适用于快速、直接的查询，而多轮提示则支持更复杂、具有上下文感知的交互。掌握这些结构可以在各种应用中更灵活、更有效地使用AI。

## Key Components / 关键组件

1. **Single-turn Prompts / 单轮提示**: One-shot interactions with the language model / 与语言模型的一次性交互
2. **Multi-turn Prompts / 多轮提示**: Series of interactions that maintain context / 维护上下文的一系列交互
3. **Prompt Templates / 提示模板**: Reusable structures for consistent prompting / 用于一致性提示的可复用结构
4. **Conversation Chains / 对话链**: Maintaining context across multiple interactions / 在多次交互中维护上下文

---

## Setup / 环境设置

First, let's import the necessary libraries and set up our environment.
首先，让我们导入必要的库并设置环境。

```python
import os
from langchain_openai import ChatOpenAI
from langchain.prompts import PromptTemplate
from langchain.chains import ConversationChain
from langchain.memory import ConversationBufferMemory

from dotenv import load_dotenv
load_dotenv()

os.environ["OPENAI_API_KEY"] = os.getenv('OPENAI_API_KEY')
llm = ChatOpenAI(model="gpt-4o-mini")
```

---

## 1. Single-turn Prompts / 单轮提示

Single-turn prompts are one-shot interactions with the language model. They consist of a single input (prompt) and generate a single output (response).

单轮提示是与语言模型的一次性交互。它们由单个输入（提示）组成，并生成单个输出（响应）。

### Example / 示例

```python
single_turn_prompt = "What are the three primary colors?"
print(llm.invoke(single_turn_prompt).content)
```

**Output / 输出:**
```
The three primary colors are red, blue, and yellow. These colors cannot be created by mixing other colors together and are the foundation for creating a wide range of other colors through mixing.
```

### Using PromptTemplate / 使用提示模板

Now, let's use a PromptTemplate to create a more structured single-turn prompt:
现在，让我们使用PromptTemplate创建一个更结构化的单轮提示：

```python
structured_prompt = PromptTemplate(
    input_variables=["topic"],
    template="Provide a brief explanation of {topic} and list its three main components."
)

chain = structured_prompt | llm
print(chain.invoke({"topic": "color theory"}).content)
```

---

## 2. Multi-turn Prompts / 多轮提示

Multi-turn prompts involve a series of interactions with the language model, allowing for more complex and context-aware conversations.

多轮提示涉及与语言模型的一系列交互，允许更复杂、具有上下文感知的对话。

### Example / 示例

```python
conversation = ConversationChain(
    llm=llm, 
    verbose=True,
    memory=ConversationBufferMemory()
)

print(conversation.predict(input="Hi, I'm learning about space. Can you tell me about planets?"))
print(conversation.predict(input="What's the largest planet in our solar system?"))
print(conversation.predict(input="How does its size compare to Earth?"))
```

---

## Comparison: Single-turn vs Multi-turn / 对比：单轮 vs 多轮

Let's compare how single-turn and multi-turn prompts handle a series of related questions:
让我们比较单轮和多轮提示如何处理一系列相关问题：

```python
# Single-turn prompts
prompts = [
    "What is the capital of France?",
    "What is its population?",
    "What is the city's most famous landmark?"
]

print("Single-turn responses:")
for prompt in prompts:
    print(f"Q: {prompt}")
    print(f"A: {llm.invoke(prompt).content}\n")

# Multi-turn prompts
print("Multi-turn responses:")
conversation = ConversationChain(llm=llm, memory=ConversationBufferMemory())
for prompt in prompts:
    print(f"Q: {prompt}")
    print(f"A: {conversation.predict(input=prompt)}\n")
```

### Results / 结果

**Single-turn / 单轮:**
- Q: What is the capital of France? → A: The capital of France is Paris.
- Q: What is its population? → A: Could you please specify which location... (Model doesn't know "its" refers to Paris / 模型不知道"its"指的是巴黎)
- Q: What is the city's most famous landmark? → A: To provide an accurate answer, I need to know which city... (No context / 无上下文)

**Multi-turn / 多轮:**
- Q: What is the capital of France? → A: The capital of France is Paris!...
- Q: What is its population? → A: As of my last update, the population of Paris is approximately 2.1 million... (Context maintained / 上下文已维护)
- Q: What is the city's most famous landmark? → A: The most famous landmark in Paris is undoubtedly the Eiffel Tower!... (Context aware / 上下文感知)

---

## Conclusion / 总结

This tutorial has introduced you to the basics of single-turn and multi-turn prompt structures. We've seen how:
本教程介绍了单轮和多轮提示结构的基础知识。我们已经了解了：

1. **Single-turn prompts / 单轮提示** are useful for quick, isolated queries / 适用于快速、独立的查询
2. **Multi-turn prompts / 多轮提示** maintain context across a conversation, allowing for more complex interactions / 在对话中维护上下文，允许更复杂的交互
3. **PromptTemplates / 提示模板** can be used to create structured, reusable prompts / 可用于创建结构化、可复用的提示
4. **Conversation chains / 对话链** in LangChain help manage context in multi-turn interactions / 在LangChain中帮助管理多轮交互中的上下文

Understanding these different prompt structures allows you to choose the most appropriate approach for various tasks and create more effective interactions with AI language models.

理解这些不同的提示结构，可以为各种任务选择最合适的方法，并与AI语言模型创建更有效的交互。
