# AI学习平台综合练习题集

## Comprehensive Practice Questions for AI Learning Platform

---

**生成时间 / Generated**: 2026-03-17 00:57:11

**总题数 / Total Questions**: 236

**模块数 / Total Modules**: 5

---

## 目录 / Table of Contents

1. [Prompts 提示词工程](#Prompts-提示词工程) (92题)
2. [RAG 检索增强生成](#RAG-检索增强生成) (32题)
3. [Agent 智能体](#Agent-智能体) (56题)
4. [PROD 生产落地](#PROD-生产落地) (29题)
5. [Context Engineering 上下文工程](#Context-Engineering-上下文工程) (27题)

---

## Prompts 提示词工程

### 模块概述 / Module Overview

本模块包含 92 道练习题，涵盖该领域的核心知识点。

---

### 单选题 / Single Choice (41题)

#### 1. 原子提示的三个核心要素是什么？

- A. 输入、处理、输出
- B. TASK、CONSTRAINTS、OUTPUT
- C. 问题、分析、答案
- D. 数据、模型、结果

**答案**: B

**解析**: 原子提示包含三个核心要素：TASK(任务描述)、CONSTRAINTS(约束条件)、OUTPUT(输出格式)。这三个要素缺一不可，共同构成完整的提示指令。

**知识点**: 原子提示 (Atomic Prompting)

**课程**: 原子 + 零/少样本

**难度**: ⭐

---

#### 2. 在原子提示中，TASK要素的作用是什么？

- A. 限制模型行为边界
- B. 明确告诉模型要做什么
- C. 指定输出结果格式
- D. 提供示例参考

**答案**: B

**解析**: TASK(任务描述)的作用是明确告诉模型要做什么，让模型清楚理解任务目标。

**知识点**: 原子提示 (Atomic Prompting)

**课程**: 原子 + 零/少样本

**难度**: ⭐

---

#### 3. 以下哪个是好的原子提示示例？

- A. 帮我写点东西
- B. 写一篇文章
- C. 任务：写一篇关于AI的短文；约束：100字以内，包含3个要点；输出：带编号的要点列表
- D. 写一篇AI文章，字数不限

**答案**: C

**解析**: 选项C包含了完整的三个要素：任务(写短文)、约束(100字、3要点)、输出格式(编号列表)，是一个标准的原子提示。

**知识点**: 原子提示 (Atomic Prompting)

**课程**: 原子 + 零/少样本

**难度**: ⭐⭐

---

#### 4. OUTPUT要素主要解决什么问题？

- A. 告诉模型做什么
- B. 限制模型行为
- C. 指定期望的结果格式
- D. 提供背景信息

**答案**: C

**解析**: OUTPUT(输出格式)要素用于指定期望的结果格式，让模型知道应该以什么样的形式输出答案。

**知识点**: 原子提示 (Atomic Prompting)

**课程**: 原子 + 零/少样本

**难度**: ⭐

---

#### 5. 零样本学习的主要特点是什么？

- A. 需要大量训练数据
- B. 不需要示例就能完成任务
- C. 必须提供多个示例
- D. 只能处理简单任务

**答案**: B

**解析**: 零样本学习的核心特点是不需要示例，模型仅通过任务描述就能完成任务，依赖预训练知识和泛化能力。

**知识点**: 零样本学习 (Zero-shot Learning)

**课程**: 原子 + 零/少样本

**难度**: ⭐

---

#### 6. 零样本学习最适合什么类型的任务？

- A. 复杂推理任务
- B. 简单分类任务
- C. 需要特定格式的任务
- D. 多步骤任务

**答案**: B

**解析**: 零样本学习最适合简单、直接的任务，如简单分类。复杂任务通常需要示例或思维链来提高效果。

**知识点**: 零样本学习 (Zero-shot Learning)

**课程**: 原子 + 零/少样本

**难度**: ⭐

---

#### 7. 少样本学习中，通常建议使用多少个示例？

- A. 1个
- B. 2-5个
- C. 10个以上
- D. 越多越好

**答案**: B

**解析**: 少样本学习通常建议使用2-5个示例。示例太少可能不够，太多会占用上下文且可能干扰模型。

**知识点**: 少样本学习 (Few-shot Learning)

**课程**: 原子 + 零/少样本

**难度**: ⭐

---

#### 8. 少样本学习示例应该具备什么特点？

- A. 越复杂越好
- B. 代表性强、格式一致
- C. 随机选择即可
- D. 数量最重要

**答案**: B

**解析**: 少样本学习的示例应该具有代表性，能覆盖不同情况，且格式保持一致，帮助模型建立正确的任务理解。

**知识点**: 少样本学习 (Few-shot Learning)

**课程**: 原子 + 零/少样本

**难度**: ⭐⭐

---

#### 9. 思维链(CoT)技术最早由谁提出？

- A. OpenAI
- B. Google
- C. Anthropic
- D. Meta

**答案**: B

**解析**: 思维链(Chain of Thought)技术由Google在2022年提出，是一种让模型逐步展示推理过程的技术。

**知识点**: 思维链 (Chain of Thought, CoT)

**课程**: CoT + 角色 + 约束 + 自洽

**难度**: ⭐

---

#### 10. 以下哪个是激活思维链的常用触发语？

- A. 请快速回答
- B. 让我们一步一步思考
- C. 简短回答
- D. 只给答案

**答案**: B

**解析**: '让我们一步一步思考'是激活思维链的常用触发语，让模型在给出最终答案前先输出中间推理步骤。

**知识点**: 思维链 (Chain of Thought, CoT)

**课程**: CoT + 角色 + 约束 + 自洽

**难度**: ⭐

---

#### 11. Zero-shot CoT和Few-shot CoT的主要区别是什么？

- A. 使用不同的模型
- B. 是否提供推理示例
- C. 输出格式不同
- D. 任务类型不同

**答案**: B

**解析**: Zero-shot CoT只使用触发语激活推理，Few-shot CoT则提供推理示例来引导模型的推理方式。

**知识点**: 思维链 (Chain of Thought, CoT)

**课程**: CoT + 角色 + 约束 + 自洽

**难度**: ⭐⭐

---

#### 12. 单轮提示的主要特点是什么？

- A. 维护对话上下文
- B. 一次性交互，无上下文记忆
- C. 需要ConversationChain
- D. 自动存储历史

**答案**: B

**解析**: 单轮提示是一次性交互，每次调用都是独立的，不维护上下文记忆。

**知识点**: Single-turn Prompts / 单轮提示

**课程**: Basic Prompt Structures / 基础提示结构

**难度**: ⭐

---

#### 13. 以下哪个是单轮提示的典型应用场景？

- A. 客户服务聊天机器人
- B. 快速事实查询
- C. 多步骤推理
- D. 教学对话系统

**答案**: B

**解析**: 单轮提示适合快速、独立的事实查询，不需要上下文的场景。

**知识点**: Single-turn Prompts / 单轮提示

**课程**: Basic Prompt Structures / 基础提示结构

**难度**: ⭐

---

#### 14. PromptTemplate的主要作用是什么？

- A. 存储对话历史
- B. 创建可复用的结构化提示
- C. 自动生成答案
- D. 管理API调用

**答案**: B

**解析**: PromptTemplate用于创建可复用的结构化提示，支持变量参数化。

**知识点**: Prompt Templates / 提示模板

**课程**: Basic Prompt Structures / 基础提示结构

**难度**: ⭐

---

#### 15. 在PromptTemplate中，input_variables参数的作用是什么？

- A. 指定输出格式
- B. 定义模板中的变量名
- C. 设置模型参数
- D. 配置记忆类型

**答案**: B

**解析**: input_variables定义了模板中可以替换的变量名列表。

**知识点**: Prompt Templates / 提示模板

**课程**: Basic Prompt Structures / 基础提示结构

**难度**: ⭐⭐

---

#### 16. 多轮提示与单轮提示的主要区别是什么？

- A. 使用不同的模型
- B. 维护对话上下文
- C. 响应速度更快
- D. 不需要API调用

**答案**: B

**解析**: 多轮提示的主要特点是维护对话上下文，允许追问和上下文感知的对话。

**知识点**: Multi-turn Prompts / 多轮提示

**课程**: Basic Prompt Structures / 基础提示结构

**难度**: ⭐

---

#### 17. ConversationBufferMemory的作用是什么？

- A. 生成对话内容
- B. 存储完整对话历史
- C. 优化模型性能
- D. 管理API密钥

**答案**: B

**解析**: ConversationBufferMemory存储完整的对话历史，用于维护多轮对话的上下文。

**知识点**: Conversation Memory / 对话记忆

**课程**: Basic Prompt Structures / 基础提示结构

**难度**: ⭐

---

#### 18. ConversationBufferMemory对于很长的对话有什么潜在问题？

- A. 响应变慢
- B. 可能超出token限制
- C. 无法存储历史
- D. 不支持中文

**答案**: B

**解析**: ConversationBufferMemory存储所有历史，对于很长的对话可能超出模型的token限制。

**知识点**: Conversation Memory / 对话记忆

**课程**: Basic Prompt Structures / 基础提示结构

**难度**: ⭐⭐

---

#### 19. ConversationChain需要配合什么组件才能维护上下文？

- A. PromptTemplate
- B. Memory组件
- C. Vector Store
- D. Embeddings

**答案**: B

**解析**: ConversationChain需要配合Memory组件（如ConversationBufferMemory）才能维护对话上下文。

**知识点**: ConversationChain / 对话链

**课程**: Basic Prompt Structures / 基础提示结构

**难度**: ⭐

---

#### 20. ConversationChain的verbose=True参数有什么作用？

- A. 提高响应速度
- B. 显示内部处理过程
- C. 增加token限制
- D. 启用记忆功能

**答案**: B

**解析**: verbose=True会显示ConversationChain内部的提示处理过程，便于调试。

**知识点**: ConversationChain / 对话链

**课程**: Basic Prompt Structures / 基础提示结构

**难度**: ⭐⭐

---

#### 21. 零样本提示的主要特点是什么？

- A. 需要大量训练数据
- B. 不需要示例就能完成任务
- C. 必须提供多个示例
- D. 只能处理简单任务

**答案**: B

**解析**: 零样本提示的核心特点是不需要示例，模型仅通过任务描述就能完成任务。

**知识点**: Direct Task Specification / 直接任务指定

**课程**: Zero-Shot Prompting / 零样本提示

**难度**: ⭐

---

#### 22. 格式规范的主要作用是什么？

- A. 提高模型速度
- B. 帮助模型以结构化方式响应
- C. 减少token使用
- D. 增加示例数量

**答案**: B

**解析**: 格式规范通过提供输出格式指南，帮助模型以结构化方式响应任务。

**知识点**: Format Specification / 格式规范

**课程**: Zero-Shot Prompting / 零样本提示

**难度**: ⭐

---

#### 23. 少样本学习通常建议使用多少个示例？

- A. 1个
- B. 2-5个
- C. 10个以上
- D. 越多越好

**答案**: B

**解析**: 少样本学习通常建议使用2-5个示例，过多会占用上下文且可能干扰模型。

**知识点**: Basic Few-Shot Learning / 基础少样本学习

**课程**: Few-Shot Learning / 少样本学习

**难度**: ⭐

---

#### 24. 思维链提示的核心思想是什么？

- A. 快速给出答案
- B. 让模型展示推理过程
- C. 减少token使用
- D. 简化问题

**答案**: B

**解析**: 思维链提示的核心是让模型在给出最终答案前先输出中间推理步骤。

**知识点**: Basic CoT Prompting / 基础思维链

**课程**: Chain of Thought (CoT) Prompting / 思维链提示

**难度**: ⭐

---

#### 25. 以下哪个是激活思维链的常用触发语？

- A. 请快速回答
- B. 让我们一步一步思考
- C. 简短回答
- D. 只给答案

**答案**: B

**解析**: '让我们一步一步思考'是激活思维链的常用触发语。

**知识点**: Basic CoT Prompting / 基础思维链

**课程**: Chain of Thought (CoT) Prompting / 思维链提示

**难度**: ⭐

---

#### 26. 角色提示的主要作用是什么？

- A. 减少token使用
- B. 引导模型以特定视角响应
- C. 加快响应速度
- D. 简化提示

**答案**: B

**解析**: 角色提示通过指定角色身份，引导模型以特定专业视角和风格响应。

**知识点**: Role Assignment / 角色分配

**课程**: Role Prompting / 角色提示

**难度**: ⭐

---

#### 27. 自一致性的主要目的是什么？

- A. 加快响应速度
- B. 提高响应可靠性
- C. 减少token使用
- D. 简化提示

**答案**: B

**解析**: 自一致性通过多条推理路径选择最一致的答案，提高响应的可靠性。

**知识点**: Self-Consistency Concept / 自一致性概念

**课程**: Self-Consistency / 自一致性

**难度**: ⭐

---

#### 28. 提示链的主要作用是什么？

- A. 加快处理速度
- B. 将复杂任务分解为子任务
- C. 减少API调用
- D. 简化单个提示

**答案**: B

**解析**: 提示链将复杂任务分解为多个顺序执行的子任务，每个子任务处理一部分工作。

**知识点**: Prompt Chaining Concept / 提示链概念

**课程**: Prompt Chaining & Sequencing / 提示链与序列

**难度**: ⭐

---

#### 29. 任务分解的主要目的是什么？

- A. 增加任务数量
- B. 将复杂任务变为可管理的子任务
- C. 减少工作量
- D. 简化提示

**答案**: B

**解析**: 任务分解的主要目的是将复杂任务拆分为更小、更易管理的子任务。

**知识点**: Decomposition Strategies / 分解策略

**课程**: Task Decomposition Prompts / 任务分解提示

**难度**: ⭐

---

#### 30. 提示模板的主要优势是什么？

- A. 减少代码量
- B. 可复用性和一致性
- C. 加快执行速度
- D. 简化逻辑

**答案**: B

**解析**: 提示模板的主要优势是可复用性和一致性，可以多次使用同一模板生成不同内容的提示。

**知识点**: Template Basics / 模板基础

**课程**: Prompt Templates & Variables / 提示模板与变量

**难度**: ⭐

---

#### 31. 格式化的主要目的是什么？

- A. 减少token
- B. 提高可读性
- C. 加快速度
- D. 增加复杂度

**答案**: B

**解析**: 格式化的主要目的是提高提示的可读性，让模型更容易理解任务要求。

**知识点**: Formatting Principles / 格式化原则

**课程**: Prompt Formatting & Structure / 提示格式与结构

**难度**: ⭐

---

#### 32. 提示长度管理的主要挑战是什么？

- A. 语法错误
- B. 平衡信息完整性和上下文窗口限制
- C. 格式问题
- D. 语言障碍

**答案**: B

**解析**: 提示长度管理的主要挑战是在信息完整性和上下文窗口限制之间找到平衡。

**知识点**: Length Management / 长度管理

**课程**: Prompt Length & Complexity Management / 提示长度与复杂度管理

**难度**: ⭐

---

#### 33. 以下哪个不是常见的性能指标？

- A. 准确性
- B. 一致性
- C. 代码行数
- D. Token效率

**答案**: C

**解析**: 常见的性能指标包括准确性、一致性、响应时间、Token效率，不包括代码行数。

**知识点**: Performance Metrics / 性能指标

**课程**: Prompt Optimization Techniques / 提示优化技术

**难度**: ⭐

---

#### 34. 以下哪个是有效的防御策略？

- A. 忽略所有输入
- B. 输入验证和输出过滤
- C. 禁用所有功能
- D. 增加响应时间

**答案**: B

**解析**: 输入验证和输出过滤是有效的防御策略，可以在不影响功能的情况下提高安全性。

**知识点**: Defense Strategies / 防御策略

**课程**: Prompt Security & Safety / 提示安全与防护

**难度**: ⭐

---

#### 35. 以下哪个是词汇歧义的例子？

- A. 'I saw the man with the telescope'
- B. 'Bank (river vs. financial)'
- C. 'The horse raced past the barn fell'
- D. 'Time flies like an arrow'

**答案**: B

**解析**: 词汇歧义是指同一个词有多种含义，如'bank'可以指河岸或银行。

**知识点**: Ambiguity Sources / 歧义来源

**课程**: Ambiguity & Clarity / 消歧与清晰度

**难度**: ⭐⭐

---

#### 36. 引导生成的主要目的是什么？

- A. 加快生成速度
- B. 引导模型按预期方式生成
- C. 减少token使用
- D. 简化提示

**答案**: B

**解析**: 引导生成的主要目的是使用结构化提示、模板、语法约束等方法，引导模型按预期方式生成内容。

**知识点**: Guided Generation / 引导生成

**课程**: Constrained & Guided Generation / 约束引导生成

**难度**: ⭐

---

#### 37. 偏见缓解的主要目的是什么？

- A. 提高速度
- B. 确保公平对待所有群体
- C. 减少成本
- D. 简化流程

**答案**: B

**解析**: 偏见缓解的主要目的是识别和减少提示中的偏见，确保AI输出公平对待所有群体。

**知识点**: Bias Mitigation / 偏见缓解

**课程**: Ethical Prompt Engineering / 伦理提示工程

**难度**: ⭐

---

#### 38. 以下哪个是有效的评估方法？

- A. 随机猜测
- B. A/B测试
- C. 忽略结果
- D. 只测试一次

**答案**: B

**解析**: A/B测试是一种有效的评估方法，可以比较不同提示版本的效果差异。

**知识点**: Evaluation Methods / 评估方法

**课程**: Evaluating Prompt Effectiveness / 提示效果评估

**难度**: ⭐

---

#### 39. 多语言提示的主要挑战是什么？

- A. 语法错误
- B. 语言检测和跨语言一致性
- C. 格式问题
- D. 速度慢

**答案**: B

**解析**: 多语言提示的主要挑战包括准确检测语言和确保跨语言的一致性。

**知识点**: Multilingual Strategies / 多语言策略

**课程**: Multilingual Prompting / 多语言提示

**难度**: ⭐

---

#### 40. 负面提示的主要作用是什么？

- A. 增加输出内容
- B. 指定要避免的内容
- C. 加快生成速度
- D. 简化提示

**答案**: B

**解析**: 负面提示的主要作用是通过明确指出不应包含的内容，引导模型避免特定输出。

**知识点**: Negative Constraints / 负面约束

**课程**: Negative Prompting / 负面提示

**难度**: ⭐

---

#### 41. 摘要提示通常需要包含什么？

- A. 完整原文
- B. 长度控制和重点提取
- C. 所有细节
- D. 翻译要求

**答案**: B

**解析**: 摘要提示通常需要包含长度控制、重点提取、格式规范等要素。

**知识点**: Summarization Prompts / 摘要提示

**课程**: Specific Task Prompts / 特定任务提示

**难度**: ⭐

---

### 多选题 / Multiple Choice (20题)

#### 1. 原子提示的优点包括哪些？

- A. 结构清晰
- B. 易于验证
- C. 可复用
- D. 自动执行

**答案**: A,B,C

**解析**: 原子提示具有结构清晰、易于验证结果、可复用等优点。但它本身不能自动执行，需要模型来处理。

**知识点**: 原子提示 (Atomic Prompting)

**课程**: 原子 + 零/少样本

**难度**: ⭐⭐

---

#### 2. 零样本学习的优点有哪些？

- A. 简单直接
- B. 节省token
- C. 适合快速测试
- D. 效果一定最好

**答案**: A,B,C

**解析**: 零样本学习的优点包括简单直接、节省token(不需要示例)、适合快速测试。但效果不一定最好，复杂任务可能需要示例。

**知识点**: 零样本学习 (Zero-shot Learning)

**课程**: 原子 + 零/少样本

**难度**: ⭐⭐

---

#### 3. 设计少样本学习示例时应该注意什么？

- A. 示例格式一致
- B. 示例内容正确
- C. 覆盖不同情况
- D. 示例越难越好

**答案**: A,B,C

**解析**: 设计示例时应注意：格式一致、内容正确、覆盖不同情况。示例难度应与实际任务匹配，不是越难越好。

**知识点**: 少样本学习 (Few-shot Learning)

**课程**: 原子 + 零/少样本

**难度**: ⭐⭐

---

#### 4. 思维链技术适合哪些类型的任务？

- A. 数学计算
- B. 逻辑推理
- C. 简单分类
- D. 多步骤问题

**答案**: A,B,D

**解析**: 思维链适合需要推理的任务：数学计算、逻辑推理、多步骤问题。简单分类任务通常不需要CoT。

**知识点**: 思维链 (Chain of Thought, CoT)

**课程**: CoT + 角色 + 约束 + 自洽

**难度**: ⭐⭐

---

#### 5. 单轮提示的优点包括哪些？

- A. 简单直接
- B. 无需管理状态
- C. 适合快速查询
- D. 自动维护上下文

**答案**: A,B,C

**解析**: 单轮提示简单直接、无需管理状态、适合快速查询。但它不会自动维护上下文。

**知识点**: Single-turn Prompts / 单轮提示

**课程**: Basic Prompt Structures / 基础提示结构

**难度**: ⭐⭐

---

#### 6. 多轮提示适合哪些场景？

- A. 客户服务聊天机器人
- B. 交互式教学系统
- C. 快速事实查询
- D. 多步骤问题解决

**答案**: A,B,D

**解析**: 多轮提示适合需要上下文的场景：客户服务、教学系统、多步骤问题。快速事实查询适合单轮提示。

**知识点**: Multi-turn Prompts / 多轮提示

**课程**: Basic Prompt Structures / 基础提示结构

**难度**: ⭐⭐

---

#### 7. ConversationChain的常用参数包括哪些？

- A. llm - 语言模型
- B. memory - 记忆组件
- C. verbose - 详细输出
- D. temperature - 温度参数

**答案**: A,B,C

**解析**: ConversationChain常用参数：llm(语言模型)、memory(记忆组件)、verbose(详细输出)。temperature是模型参数。

**知识点**: ConversationChain / 对话链

**课程**: Basic Prompt Structures / 基础提示结构

**难度**: ⭐⭐

---

#### 8. 多步推理的优点包括哪些？

- A. 提高准确性
- B. 处理复杂任务
- C. 减少步骤
- D. 增加透明度

**答案**: A,B,D

**解析**: 多步推理可以提高准确性、处理复杂任务、增加推理透明度。

**知识点**: Multi-step Reasoning / 多步推理

**课程**: Zero-Shot Prompting / 零样本提示

**难度**: ⭐⭐

---

#### 9. 多任务少样本学习的优点包括？

- A. 提高效率
- B. 更好的泛化
- C. 减少重复
- D. 单一模型多功能

**答案**: A,B,D

**解析**: 多任务少样本学习可以提高效率、改善泛化能力、让单一模型执行多种功能。

**知识点**: Multi-Task Few-Shot / 多任务少样本

**课程**: Few-Shot Learning / 少样本学习

**难度**: ⭐⭐

---

#### 10. 思维链相比标准提示的优势包括？

- A. 提高准确性
- B. 增加可解释性
- C. 便于验证
- D. 减少token

**答案**: A,B,C

**解析**: 思维链提高准确性、增加可解释性、便于验证推理过程，但会增加token使用。

**知识点**: CoT vs Standard Prompting / 思维链与标准提示对比

**课程**: Chain of Thought (CoT) Prompting / 思维链提示

**难度**: ⭐⭐

---

#### 11. 链设计需要考虑哪些因素？

- A. 任务分解方式
- B. 子任务接口
- C. 错误处理
- D. 中间结果存储

**答案**: A,B,C,D

**解析**: 链设计需要考虑任务分解、接口定义、错误处理、中间存储等多个因素。

**知识点**: Chain Design / 链设计

**课程**: Prompt Chaining & Sequencing / 提示链与序列

**难度**: ⭐⭐

---

#### 12. Jinja2支持哪些模板功能？

- A. 变量插值
- B. 条件语句
- C. 循环
- D. 过滤器

**答案**: A,B,C,D

**解析**: Jinja2支持变量插值、条件语句、循环、过滤器等高级模板功能。

**知识点**: Jinja2 Syntax / Jinja2语法

**课程**: Prompt Templates & Variables / 提示模板与变量

**难度**: ⭐

---

#### 13. 提示的结构元素包括哪些？

- A. 任务描述
- B. 上下文
- C. 示例
- D. 输出格式

**答案**: A,B,C,D

**解析**: 提示的结构元素包括任务描述、上下文、示例、输出格式、约束条件等。

**知识点**: Structural Elements / 结构元素

**课程**: Prompt Formatting & Structure / 提示格式与结构

**难度**: ⭐

---

#### 14. 提示优化策略包括哪些？

- A. 迭代改进
- B. A/B测试
- C. 反馈循环
- D. 随机修改

**答案**: A,B,C

**解析**: 提示优化策略包括迭代改进、A/B测试、反馈循环等系统化方法，不包括随机修改。

**知识点**: Optimization Strategies / 优化策略

**课程**: Prompt Optimization Techniques / 提示优化技术

**难度**: ⭐

---

#### 15. 常见的安全威胁包括哪些？

- A. 提示注入
- B. 越狱攻击
- C. 数据泄露
- D. 性能下降

**答案**: A,B,C

**解析**: 常见的安全威胁包括提示注入、越狱攻击、数据泄露等。性能下降不是安全威胁。

**知识点**: Security Threats / 安全威胁

**课程**: Prompt Security & Safety / 提示安全与防护

**难度**: ⭐

---

#### 16. 常见的输出约束类型包括？

- A. 格式约束
- B. 长度约束
- C. 内容约束
- D. 颜色约束

**答案**: A,B,C

**解析**: 常见的输出约束包括格式约束、长度约束、内容约束等。颜色约束不是常见的输出约束。

**知识点**: Output Constraints / 输出约束

**课程**: Constrained & Guided Generation / 约束引导生成

**难度**: ⭐

---

#### 17. 伦理提示工程的原则包括哪些？

- A. 公平性
- B. 透明性
- C. 隐私保护
- D. 利润最大化

**答案**: A,B,C

**解析**: 伦理原则包括公平性、透明性、隐私保护、避免伤害等，不包括利润最大化。

**知识点**: Ethical Principles / 伦理原则

**课程**: Ethical Prompt Engineering / 伦理提示工程

**难度**: ⭐

---

#### 18. 常见的评估指标包括哪些？

- A. 准确性
- B. 一致性
- C. 相关性
- D. 代码行数

**答案**: A,B,C

**解析**: 常见的评估指标包括准确性、一致性、相关性、完整性等。代码行数不是提示评估指标。

**知识点**: Evaluation Metrics / 评估指标

**课程**: Evaluating Prompt Effectiveness / 提示效果评估

**难度**: ⭐

---

#### 19. 负面提示适用于哪些场景？

- A. 内容过滤
- B. 风格控制
- C. 安全限制
- D. 增加创意

**答案**: A,B,C

**解析**: 负面提示适用于内容过滤、风格控制、安全限制等需要排除特定输出的场景。

**知识点**: Use Cases / 使用场景

**课程**: Negative Prompting / 负面提示

**难度**: ⭐

---

#### 20. 分类提示需要包含哪些要素？

- A. 类别定义
- B. 边界说明
- C. 示例提供
- D. 翻译规则

**答案**: A,B,C

**解析**: 分类提示需要包含类别定义、边界说明、示例提供等要素。翻译规则不是分类提示的要素。

**知识点**: Classification Prompts / 分类提示

**课程**: Specific Task Prompts / 特定任务提示

**难度**: ⭐

---

### 判断题 / True or False (19题)

#### 1. 原子提示中，约束条件是可选的，不是必须的。

**答案**: 错误

**解析**: 原子提示的三个要素(TASK、CONSTRAINTS、OUTPUT)都是必须的，约束条件用于限制模型的行为边界，确保输出符合预期。

**知识点**: 原子提示 (Atomic Prompting)

**课程**: 原子 + 零/少样本

**难度**: ⭐

---

#### 2. 零样本学习比少样本学习效果一定更好。

**答案**: 错误

**解析**: 零样本学习不一定比少样本学习效果好。对于复杂任务，少样本学习通常效果更好，因为示例能帮助模型更好地理解任务。

**知识点**: 零样本学习 (Zero-shot Learning)

**课程**: 原子 + 零/少样本

**难度**: ⭐

---

#### 3. 少样本学习中的示例越多，效果一定越好。

**答案**: 错误

**解析**: 示例不是越多越好。过多示例会占用上下文空间，增加成本，且可能干扰模型理解。通常2-5个效果最佳。

**知识点**: 少样本学习 (Few-shot Learning)

**课程**: 原子 + 零/少样本

**难度**: ⭐

---

#### 4. 思维链技术对所有类型的任务都有帮助。

**答案**: 错误

**解析**: 思维链主要对需要推理的复杂任务有帮助，如数学问题、逻辑推理。对于简单任务，使用CoT反而会增加不必要的复杂度。

**知识点**: 思维链 (Chain of Thought, CoT)

**课程**: CoT + 角色 + 约束 + 自洽

**难度**: ⭐⭐

---

#### 5. 单轮提示适合用于需要记住之前对话内容的场景。

**答案**: 错误

**解析**: 单轮提示不维护上下文，不适合需要记住之前对话内容的场景。这种场景应该使用多轮提示。

**知识点**: Single-turn Prompts / 单轮提示

**课程**: Basic Prompt Structures / 基础提示结构

**难度**: ⭐

---

#### 6. PromptTemplate可以使用管道操作符(|)与LLM连接。

**答案**: 正确

**解析**: LangChain支持使用管道操作符将PromptTemplate与LLM连接：template | llm

**知识点**: Prompt Templates / 提示模板

**课程**: Basic Prompt Structures / 基础提示结构

**难度**: ⭐⭐

---

#### 7. 在多轮对话中，追问时需要重复之前提到的上下文信息。

**答案**: 错误

**解析**: 多轮对话的优势正是可以追问而无需重复上下文，对话记忆会保存之前的信息。

**知识点**: Multi-turn Prompts / 多轮提示

**课程**: Basic Prompt Structures / 基础提示结构

**难度**: ⭐

---

#### 8. ConversationBufferMemory是LangChain中唯一的记忆类型。

**答案**: 错误

**解析**: LangChain有多种记忆类型，如ConversationBufferWindowMemory、ConversationSummaryMemory等。

**知识点**: Conversation Memory / 对话记忆

**课程**: Basic Prompt Structures / 基础提示结构

**难度**: ⭐

---

#### 9. ConversationChain在最新版本的LangChain中已被弃用。

**答案**: 正确

**解析**: ConversationChain在LangChain 0.2.7中已被弃用，建议使用RunnableWithMessageHistory。

**知识点**: ConversationChain / 对话链

**课程**: Basic Prompt Structures / 基础提示结构

**难度**: ⭐⭐

---

#### 10. 零样本学习依赖模型的预训练知识和泛化能力。

**答案**: 正确

**解析**: 零样本学习依赖模型在预训练中获得的知识和泛化能力来处理新任务。

**知识点**: Direct Task Specification / 直接任务指定

**课程**: Zero-Shot Prompting / 零样本提示

**难度**: ⭐

---

#### 11. 上下文学习需要对模型进行微调。

**答案**: 错误

**解析**: 上下文学习的优势正是无需微调，模型仅根据提示中的示例适应新任务。

**知识点**: In-Context Learning / 上下文学习

**课程**: Few-Shot Learning / 少样本学习

**难度**: ⭐

---

#### 12. 思维链技术对所有类型的任务都有帮助。

**答案**: 错误

**解析**: 思维链主要对需要推理的复杂任务有帮助，简单任务使用CoT反而增加不必要的复杂度。

**知识点**: Advanced CoT Techniques / 高级思维链技术

**课程**: Chain of Thought (CoT) Prompting / 思维链提示

**难度**: ⭐⭐

---

#### 13. 角色设计越详细，响应越精准。

**答案**: 正确

**解析**: 详细的角色描述包括专业背景、性格特征、沟通风格等，有助于获得更精准的响应。

**知识点**: Persona Design / 角色设计

**课程**: Role Prompting / 角色提示

**难度**: ⭐

---

#### 14. 自一致性需要将温度参数设为0。

**答案**: 错误

**解析**: 自一致性需要一定的随机性来生成不同的推理路径，通常设置温度参数大于0。

**知识点**: Implementation Strategy / 实施策略

**课程**: Self-Consistency / 自一致性

**难度**: ⭐⭐

---

#### 15. 分解提示应该包含输出格式规范。

**答案**: 正确

**解析**: 分解提示应该包含分解规则和输出格式，以便模型生成结构化的分解结果。

**知识点**: Decomposition Prompts / 分解提示

**课程**: Task Decomposition Prompts / 任务分解提示

**难度**: ⭐

---

#### 16. 复杂度管理可以通过任务分解来实现。

**答案**: 正确

**解析**: 复杂度管理可以通过分解任务、简化指令、使用模板等方式降低提示的复杂度。

**知识点**: Complexity Management / 复杂度管理

**课程**: Prompt Length & Complexity Management / 提示长度与复杂度管理

**难度**: ⭐

---

#### 17. 提供示例是消除歧义的有效方法。

**答案**: 正确

**解析**: 提供示例可以帮助模型理解期望的输出格式和内容，从而消除歧义。

**知识点**: Clarity Techniques / 清晰度技术

**课程**: Ambiguity & Clarity / 消歧与清晰度

**难度**: ⭐

---

#### 18. 文化考量在多语言提示中很重要。

**答案**: 正确

**解析**: 文化考量涉及理解不同语言和文化背景下的表达习惯、禁忌、偏好等，对多语言提示很重要。

**知识点**: Cultural Considerations / 文化考量

**课程**: Multilingual Prompting / 多语言提示

**难度**: ⭐

---

#### 19. 翻译提示需要指定源语言和目标语言。

**答案**: 正确

**解析**: 翻译提示需要明确指定源语言和目标语言，以确保正确的翻译方向。

**知识点**: Translation Prompts / 翻译提示

**课程**: Specific Task Prompts / 特定任务提示

**难度**: ⭐

---


## RAG 检索增强生成

### 模块概述 / Module Overview

本模块包含 32 道练习题，涵盖该领域的核心知识点。

---

### 单选题 / Single Choice (17题)

#### 1. RAG的全称是什么？

- A. Retrieval-Augmented Generation
- B. Reading and Generation
- C. Random Access Generation
- D. Rule-based AI Generation

**答案**: A

**解析**: RAG全称是Retrieval-Augmented Generation（检索增强生成），是一种结合信息检索和文本生成的技术。

**知识点**: RAG基本原理

**课程**: RAG 原理 + Simple RAG

**难度**: ⭐

---

#### 2. RAG的主要作用是什么？

- A. 训练新模型
- B. 减少幻觉，提高准确性
- C. 加快推理速度
- D. 减少存储空间

**答案**: B

**解析**: RAG通过检索相关文档作为上下文，可以有效减少模型幻觉，提高答案的准确性和可追溯性。

**知识点**: RAG基本原理

**课程**: RAG 原理 + Simple RAG

**难度**: ⭐

---

#### 3. RAG系统的主要组件不包括以下哪个？

- A. 文档加载器
- B. 文本分割器
- C. 图像处理器
- D. 向量存储

**答案**: C

**解析**: RAG系统主要处理文本，核心组件包括文档加载器、文本分割器、嵌入模型、向量存储和检索器。

**知识点**: RAG System Components / RAG系统组件

**课程**: Simple RAG / 基础RAG系统

**难度**: ⭐

---

#### 4. FAISS的主要作用是什么？

- A. 文档加载
- B. 向量相似性搜索
- C. 文本生成
- D. 图像处理

**答案**: B

**解析**: FAISS是Facebook开发的向量相似性搜索库，用于高效的向量检索。

**知识点**: Vector Store Creation / 向量存储创建

**课程**: Simple RAG / 基础RAG系统

**难度**: ⭐

---

#### 5. 语义分块相比固定大小分块的主要优势是什么？

- A. 更快的处理速度
- B. 保持语义连贯性
- C. 更小的存储空间
- D. 更简单的实现

**答案**: B

**解析**: 语义分块的主要优势是根据语义相似性分割，保持语义连贯性。

**知识点**: Semantic Chunking Concept / 语义分块概念

**课程**: Semantic Chunking / 语义分块

**难度**: ⭐

---

#### 6. 重排序的主要目的是什么？

- A. 加快检索速度
- B. 提高检索相关性
- C. 减少存储空间
- D. 简化代码

**答案**: B

**解析**: 重排序的主要目的是通过更复杂的模型重新评估文档相关性，提高检索质量。

**知识点**: Reranking Concept / 重排序概念

**课程**: Reranking / 重排序

**难度**: ⭐

---

#### 7. 查询扩展的主要目的是什么？

- A. 减少查询数量
- B. 提高召回率
- C. 加快检索速度
- D. 减少存储

**答案**: B

**解析**: 查询扩展通过生成多个相关查询提高召回率，找到更多相关文档。

**知识点**: Query Expansion / 查询扩展

**课程**: Query Transformations / 查询转换

**难度**: ⭐

---

#### 8. 上下文压缩的主要作用是什么？

- A. 增加文档数量
- B. 提取相关部分减少噪声
- C. 加快处理速度
- D. 增加上下文长度

**答案**: B

**解析**: 上下文压缩从检索文档中提取与查询相关的部分，减少噪声并提高相关性。

**知识点**: Compression Concept / 压缩概念

**课程**: Contextual Compression / 上下文压缩

**难度**: ⭐

---

#### 9. Self-RAG的核心特点是什么？

- A. 更快的检索
- B. 自我反思和改进
- C. 更大的存储
- D. 更简单的实现

**答案**: B

**解析**: Self-RAG的核心特点是让模型评估检索和生成质量，进行自我改进。

**知识点**: Self-Reflection / 自我反思

**课程**: Self RAG / 自我RAG

**难度**: ⭐

---

#### 10. CRAG对不相关文档的处理方式是什么？

- A. 直接使用
- B. 丢弃并可能使用网络搜索
- C. 忽略
- D. 重新生成

**答案**: B

**解析**: CRAG会评估文档相关性，对不相关文档丢弃并可能使用网络搜索补充知识。

**知识点**: Document Evaluation / 文档评估

**课程**: CRAG / 纠正性RAG

**难度**: ⭐

---

#### 11. Graph RAG的主要优势是什么？

- A. 更快的检索速度
- B. 提供结构化知识和语义理解
- C. 更小的存储空间
- D. 更简单的实现

**答案**: B

**解析**: Graph RAG将知识图谱与向量检索结合，提供结构化知识和语义理解。

**知识点**: Knowledge Graph Integration / 知识图谱集成

**课程**: Graph RAG / 图RAG

**难度**: ⭐

---

#### 12. HyDe的核心思想是什么？

- A. 直接使用查询检索
- B. 生成假设文档用于检索
- C. 增加检索数量
- D. 使用多个嵌入模型

**答案**: B

**解析**: HyDe的核心思想是让LLM生成假设的理想答案文档，然后用这个文档进行检索。

**知识点**: Hypothetical Document Generation / 假设文档生成

**课程**: HyDe / 假设文档嵌入

**难度**: ⭐

---

#### 13. RAPTOR的主要特点是什么？

- A. 单层检索
- B. 层次化摘要树
- C. 固定分块
- D. 线性处理

**答案**: B

**解析**: RAPTOR的主要特点是递归地构建文档摘要树，支持多粒度检索。

**知识点**: Hierarchical Summarization / 层次化摘要

**课程**: RAPTOR / 递归摘要树

**难度**: ⭐

---

#### 14. RRF算法的主要优点是什么？

- A. 复杂度高
- B. 简单有效
- C. 需要训练
- D. 只支持两种方法

**答案**: B

**解析**: RRF算法根据排名倒数计算综合分数，简单有效地融合多种检索结果。

**知识点**: Reciprocal Rank Fusion / 倒数排名融合

**课程**: Fusion Retrieval / 融合检索

**难度**: ⭐

---

#### 15. 自适应检索的核心是什么？

- A. 固定检索策略
- B. 根据查询特征调整策略
- C. 增加检索数量
- D. 减少检索时间

**答案**: B

**解析**: 自适应检索的核心是根据查询的复杂度、类型等特征选择最适合的检索策略。

**知识点**: Query Analysis / 查询分析

**课程**: Adaptive Retrieval / 自适应检索

**难度**: ⭐

---

#### 16. 多模态RAG如何处理图像？

- A. 忽略图像
- B. 生成图像描述用于检索
- C. 只存储图像
- D. 删除图像

**答案**: B

**解析**: 多模态RAG使用视觉模型为图像生成描述，使图像内容可被检索。

**知识点**: Image Understanding / 图像理解

**课程**: Multi-Modal RAG / 多模态RAG

**难度**: ⭐

---

#### 17. CSV RAG如何处理表格数据？

- A. 直接存储原始文件
- B. 转换为适合检索的格式
- C. 只读取第一行
- D. 忽略表格结构

**答案**: B

**解析**: CSV RAG将表格数据转换为适合检索的格式，支持结构化查询和自然语言查询。

**知识点**: Tabular Data Processing / 表格数据处理

**课程**: CSV RAG / CSV表格RAG

**难度**: ⭐

---

### 多选题 / Multiple Choice (3题)

#### 1. RAG系统的核心组件包括哪些？

- A. 向量数据库
- B. Embedding模型
- C. 大语言模型
- D. 图形处理器

**答案**: A,B,C

**解析**: RAG系统核心组件包括：向量数据库(存储向量)、Embedding模型(文本向量化)、大语言模型(生成答案)。

**知识点**: RAG基本原理

**课程**: RAG 原理 + Simple RAG

**难度**: ⭐⭐

---

#### 2. 语义分块支持哪些断点类型？

- A. 百分位数
- B. 标准差
- C. 固定长度
- D. 四分位距

**答案**: A,B,D

**解析**: 语义分块支持百分位数、标准差、四分位距三种断点类型。

**知识点**: Breakpoint Types / 断点类型

**课程**: Semantic Chunking / 语义分块

**难度**: ⭐

---

#### 3. 融合检索可以结合哪些方法？

- A. 向量检索
- B. 关键词检索
- C. 图像检索
- D. 语义检索

**答案**: A,B,D

**解析**: 融合检索可以结合向量检索、关键词检索、语义检索等多种文本检索方法。

**知识点**: Multi-Method Fusion / 多方法融合

**课程**: Fusion Retrieval / 融合检索

**难度**: ⭐

---

### 判断题 / True or False (10题)

#### 1. RAG需要重新训练语言模型才能使用新知识。

**答案**: 错误

**解析**: RAG的优势之一就是不需要重新训练模型，只需更新知识库文档即可使用新知识。

**知识点**: RAG基本原理

**课程**: RAG 原理 + Simple RAG

**难度**: ⭐

---

#### 2. OpenAI Embeddings可以将文本转换为向量表示。

**答案**: 正确

**解析**: OpenAI Embeddings模型可以将文本转换为高维向量，用于相似性计算和检索。

**知识点**: Vector Store Creation / 向量存储创建

**课程**: Simple RAG / 基础RAG系统

**难度**: ⭐

---

#### 3. Cross-Encoder比LLM重排序更快。

**答案**: 正确

**解析**: Cross-Encoder是专门训练的轻量级模型，通常比调用LLM API更快。

**知识点**: LLM vs Cross-Encoder / LLM与交叉编码器

**课程**: Reranking / 重排序

**难度**: ⭐

---

#### 4. 查询重写可以将模糊查询转换为更具体的查询。

**答案**: 正确

**解析**: 查询重写的目的就是将模糊或复杂的查询转换为更清晰、更易检索的形式。

**知识点**: Query Rewriting / 查询重写

**课程**: Query Transformations / 查询转换

**难度**: ⭐

---

#### 5. 自适应检索可以根据问题复杂度决定是否需要检索。

**答案**: 正确

**解析**: 自适应检索会评估问题是否需要检索，避免不必要的检索操作。

**知识点**: Adaptive Retrieval / 自适应检索

**课程**: Self RAG / 自我RAG

**难度**: ⭐

---

#### 6. 知识精炼可以提高答案质量。

**答案**: 正确

**解析**: 知识精炼从相关文档中提取关键信息，过滤无关内容，提高答案质量。

**知识点**: Knowledge Refinement / 知识精炼

**课程**: CRAG / 纠正性RAG

**难度**: ⭐

---

#### 7. 多跳推理可以回答需要连接多个知识点的问题。

**答案**: 正确

**解析**: 多跳推理通过知识图谱的关系链连接多个知识点，回答复杂问题。

**知识点**: Multi-hop Reasoning / 多跳推理

**课程**: Graph RAG / 图RAG

**难度**: ⭐

---

#### 8. 假设文档可以解决词汇不匹配问题。

**答案**: 正确

**解析**: 假设文档作为语义桥梁，弥补查询词和文档词不一致的问题。

**知识点**: Semantic Bridging / 语义桥接

**课程**: HyDe / 假设文档嵌入

**难度**: ⭐

---

#### 9. 聚类摘要可以保留主题连贯性。

**答案**: 正确

**解析**: 将相似文档聚类后生成摘要，可以保留主题连贯性，提高检索效率。

**知识点**: Cluster-based Summarization / 聚类摘要

**课程**: RAPTOR / 递归摘要树

**难度**: ⭐

---

#### 10. 表格可以转换为文本进行检索。

**答案**: 正确

**解析**: 从文档中提取的表格可以转换为结构化格式或文本描述进行检索。

**知识点**: Table Extraction / 表格提取

**课程**: Multi-Modal RAG / 多模态RAG

**难度**: ⭐

---


## Agent 智能体

### 模块概述 / Module Overview

本模块包含 56 道练习题，涵盖该领域的核心知识点。

---

### 单选题 / Single Choice (25题)

#### 1. AI Agent与普通LLM的主要区别是什么？

- A. 参数量更大
- B. 能够自主决策和执行行动
- C. 响应速度更快
- D. 只能回答问题

**答案**: B

**解析**: AI Agent的核心特点是能够自主决策、感知环境、执行行动，而普通LLM只能被动回答问题。

**知识点**: AI Agent定义

**课程**: Agent 概念 + Organs + Function Calling

**难度**: ⭐

---

#### 2. 以下哪个不是Agent的典型组件？

- A. 感知模块
- B. 决策模块
- C. 执行模块
- D. 训练模块

**答案**: D

**解析**: Agent的典型组件包括感知、决策、执行、记忆等模块。训练模块不是Agent运行时的组件。

**知识点**: AI Agent定义

**课程**: Agent 概念 + Organs + Function Calling

**难度**: ⭐⭐

---

#### 3. ReAct模式中的'ReAct'代表什么？

- A. Read and Act
- B. Reasoning and Acting
- C. Request and Action
- D. Response and Activity

**答案**: B

**解析**: ReAct代表Reasoning and Acting（推理与行动），是一种结合推理和行动的Agent模式。

**知识点**: ReAct模式

**课程**: 简单对话 + ReAct Agent

**难度**: ⭐

---

#### 4. ReAct模式的主要优势是什么？

- A. 执行速度最快
- B. 推理过程可解释
- C. 不需要工具
- D. 只能处理简单任务

**答案**: B

**解析**: ReAct模式的主要优势是推理过程清晰可见，每一步思考都有记录，便于理解和调试。

**知识点**: ReAct模式

**课程**: 简单对话 + ReAct Agent

**难度**: ⭐⭐

---

#### 5. MCP协议是由哪家公司提出的？

- A. OpenAI
- B. Google
- C. Anthropic
- D. Microsoft

**答案**: C

**解析**: MCP(Model Context Protocol)是由Anthropic在2024年11月提出的开放协议。

**知识点**: MCP协议概述

**课程**: MCP 模型上下文协议

**难度**: ⭐

---

#### 6. MCP协议的主要目的是什么？

- A. 训练新模型
- B. 标准化LLM与工具的交互
- C. 加快推理速度
- D. 减少存储需求

**答案**: B

**解析**: MCP协议的目的是标准化LLM与外部数据源、工具的交互方式，被称为AI模型的'万能插座'。

**知识点**: MCP协议概述

**课程**: MCP 模型上下文协议

**难度**: ⭐

---

#### 7. LangGraph是由哪个团队开发的？

- A. OpenAI
- B. LangChain
- C. Anthropic
- D. Google

**答案**: B

**解析**: LangGraph是由LangChain团队开发的Agent编排框架，基于图状态机构建。

**知识点**: LangGraph概述

**课程**: LangGraph

**难度**: ⭐

---

#### 8. LangGraph的核心概念是什么？

- A. 链式结构
- B. StateGraph(状态图)
- C. 线性流程
- D. 单一节点

**答案**: B

**解析**: LangGraph的核心概念是StateGraph(状态图)，图由节点和边组成，状态在节点间传递和更新。

**知识点**: LangGraph概述

**课程**: LangGraph

**难度**: ⭐

---

#### 9. LangGraph中用于定义节点之间流程的是什么？

- A. 状态
- B. 边
- C. 节点
- D. 变量

**答案**: B

**解析**: 在LangGraph中，边(Edges)定义节点之间的流程和条件路由。

**知识点**: StateGraph 工作流 / StateGraph Workflow

**课程**: LangGraph 入门教程 / Introduction to LangGraph

**难度**: ⭐

---

#### 10. MCP架构中的Host指的是什么？

- A. MCP服务器
- B. AI应用程序
- C. 数据库
- D. API端点

**答案**: B

**解析**: Host是AI应用程序（如Claude Desktop），需要访问外部资源。

**知识点**: MCP 架构 / MCP Architecture

**课程**: MCP 模型上下文协议 / Model Context Protocol

**难度**: ⭐

---

#### 11. 哪个LangMem工具用于搜索记忆？

- A. manage_memory_tool
- B. search_memory_tool
- C. create_memory_tool
- D. delete_memory_tool

**答案**: B

**解析**: search_memory_tool用于搜索存储的记忆内容。

**知识点**: LangMem 工具 / LangMem Tools

**课程**: 记忆增强Agent / Memory-Enhanced Agent

**难度**: ⭐

---

#### 12. RunnableWithMessageHistory的主要作用是什么？

- A. 生成回复
- B. 管理对话历史
- C. 调用API
- D. 解析JSON

**答案**: B

**解析**: RunnableWithMessageHistory用于管理对话历史，实现上下文感知。

**知识点**: 对话历史管理 / Conversation History Management

**课程**: 简单对话Agent / Simple Conversational Agent

**难度**: ⭐

---

#### 13. PydanticAI的主要优势是什么？

- A. 更快的执行速度
- B. 类型安全和验证
- C. 更小的内存占用
- D. 更简单的API

**答案**: B

**解析**: PydanticAI的主要优势是结合Pydantic的类型安全和验证能力。

**知识点**: PydanticAI Agent / PydanticAI Agent

**课程**: PydanticAI 对话Agent / PydanticAI Conversational Agent

**难度**: ⭐

---

#### 14. create_pandas_dataframe_agent的主要功能是什么？

- A. 创建数据可视化
- B. 创建能分析数据框的Agent
- C. 清洗数据
- D. 导出数据

**答案**: B

**解析**: create_pandas_dataframe_agent创建能够分析Pandas数据框的Agent。

**知识点**: Pandas DataFrame Agent / Pandas数据框Agent

**课程**: 数据分析Agent / Data Analysis Agent

**难度**: ⭐

---

#### 15. StructuredTool需要定义什么？

- A. 只有名称
- B. 名称、描述和输入模式
- C. 只有函数
- D. 只有描述

**答案**: B

**解析**: StructuredTool需要定义名称、描述和输入模式(args_schema)。

**知识点**: Structured Tools / 结构化工具

**课程**: 任务导向Agent / Task-Oriented Agent

**难度**: ⭐

---

#### 16. 多Agent协作系统的主要优势是什么？

- A. 更快的执行速度
- B. 结合不同专业知识解决复杂问题
- C. 更少的内存占用
- D. 更简单的代码

**答案**: B

**解析**: 多Agent协作系统可以结合不同专业领域的知识来解决复杂问题。

**知识点**: Agent协作模式 / Agent Collaboration Pattern

**课程**: 多Agent协作系统 / Multi-Agent Collaboration System

**难度**: ⭐

---

#### 17. 自愈代码Agent如何生成修复？

- A. 使用预定义规则
- B. 使用LLM生成修复代码
- C. 随机生成
- D. 从互联网搜索

**答案**: B

**解析**: 自愈代码Agent使用LLM根据错误信息生成修复代码。

**知识点**: 错误检测与修复 / Error Detection & Fix

**课程**: 自愈代码Agent / Self-Healing Code Agent

**难度**: ⭐

---

#### 18. 自我改进Agent如何学习？

- A. 从预定义规则
- B. 从用户反馈
- C. 从随机尝试
- D. 从代码分析

**答案**: B

**解析**: 自我改进Agent从用户反馈中学习并调整行为。

**知识点**: 反馈学习 / Feedback Learning

**课程**: 自我改进Agent / Self-Improving Agent

**难度**: ⭐

---

#### 19. 长期记忆存储使用什么技术实现语义搜索？

- A. 关系数据库
- B. 向量存储
- C. 文件系统
- D. 缓存

**答案**: B

**解析**: 长期记忆存储使用向量存储实现语义搜索功能。

**知识点**: 长期记忆存储 / Long-term Memory Storage

**课程**: 记忆增强对话Agent / Memory-Enhanced Conversational Agent

**难度**: ⭐

---

#### 20. 客户支持Agent如何处理复杂咨询？

- A. 忽略
- B. 自动回复
- C. 升级给人工
- D. 删除

**答案**: C

**解析**: 复杂咨询会被升级给人工客服处理。

**知识点**: 客户咨询处理 / Customer Inquiry Handling

**课程**: 客户支持Agent / Customer Support Agent

**难度**: ⭐

---

#### 21. AutoGen是哪个公司开发的？

- A. Google
- B. Microsoft
- C. OpenAI
- D. Meta

**答案**: B

**解析**: AutoGen是Microsoft开发的多Agent对话框架。

**知识点**: AutoGen框架 / AutoGen Framework

**课程**: AutoGen研究团队 / AutoGen Research Team

**难度**: ⭐

---

#### 22. Swarm架构中Agent如何协作？

- A. 竞争
- B. 各自独立
- C. 协作分工
- D. 随机

**答案**: C

**解析**: Swarm架构中Agent协作分工，每个负责不同阶段。

**知识点**: Swarm架构 / Swarm Architecture

**课程**: 博客写作Swarm / Blog Writer Swarm

**难度**: ⭐

---

#### 23. 科学论文Agent提取哪些关键信息？

- A. 只有标题
- B. 方法、结果和结论
- C. 只有作者
- D. 只有参考文献

**答案**: B

**解析**: 科学论文Agent提取方法、结果和结论等关键信息。

**知识点**: 论文分析 / Paper Analysis

**课程**: 科学论文Agent / Scientific Paper Agent

**难度**: ⭐

---

#### 24. 旅行规划Agent根据什么生成行程？

- A. 随机选择
- B. 用户偏好和约束
- C. 固定模板
- D. 价格排序

**答案**: B

**解析**: 旅行规划Agent根据用户偏好和约束条件生成行程。

**知识点**: 行程规划 / Itinerary Planning

**课程**: 旅行规划Agent / Travel Planner Agent

**难度**: ⭐

---

#### 25. 音乐作曲Agent根据什么生成创作建议？

- A. 随机生成
- B. 风格和参数
- C. 固定模板
- D. 用户年龄

**答案**: B

**解析**: 音乐作曲Agent根据风格和参数生成创作建议。

**知识点**: 音乐创作辅助 / Music Composition Assistance

**课程**: 音乐作曲Agent / Music Compositor Agent

**难度**: ⭐

---

### 多选题 / Multiple Choice (5题)

#### 1. AI Agent具有哪些核心特性？

- A. 自主性
- B. 反应性
- C. 主动性
- D. 社交性

**答案**: A,B,C,D

**解析**: AI Agent具有四大核心特性：自主性(独立决策)、反应性(响应环境)、主动性(追求目标)、社交性(与其他Agent协作)。

**知识点**: AI Agent定义

**课程**: Agent 概念 + Organs + Function Calling

**难度**: ⭐⭐

---

#### 2. ReAct模式的三个核心步骤是什么？

- A. Thought(思考)
- B. Action(行动)
- C. Observation(观察)
- D. Training(训练)

**答案**: A,B,C

**解析**: ReAct模式包含三个核心步骤：Thought(思考当前状态)、Action(执行行动)、Observation(获取结果)，形成TAO循环。

**知识点**: ReAct模式

**课程**: 简单对话 + ReAct Agent

**难度**: ⭐⭐

---

#### 3. MCP Server可以提供哪些类型的资源？

- A. Tools(工具)
- B. Resources(资源)
- C. Prompts(提示模板)
- D. Models(模型)

**答案**: A,B,C

**解析**: MCP Server可以提供Tools(可调用的函数)、Resources(可访问的数据)、Prompts(预定义的提示模板)。

**知识点**: MCP协议概述

**课程**: MCP 模型上下文协议

**难度**: ⭐⭐

---

#### 4. LangGraph支持哪些控制流？

- A. 循环
- B. 分支
- C. 并行
- D. 只支持线性

**答案**: A,B,C

**解析**: LangGraph支持循环、分支、并行等复杂控制流，这是相比传统链式结构的优势。

**知识点**: LangGraph概述

**课程**: LangGraph

**难度**: ⭐⭐

---

#### 5. Agent的三种记忆类型包括哪些？

- A. 语义记忆
- B. 情景记忆
- C. 程序记忆
- D. 临时记忆

**答案**: A,B,C

**解析**: Agent的三种记忆类型是语义记忆、情景记忆和程序记忆。

**知识点**: 三种记忆类型 / Three Memory Types

**课程**: 记忆增强Agent / Memory-Enhanced Agent

**难度**: ⭐

---

### 判断题 / True or False (18题)

#### 1. Agent只能单独工作，不能与其他Agent协作。

**答案**: 错误

**解析**: Agent具有社交性，可以与其他Agent协作完成复杂任务，这是多Agent系统的基础。

**知识点**: AI Agent定义

**课程**: Agent 概念 + Organs + Function Calling

**难度**: ⭐

---

#### 2. ReAct模式中，Agent可以跳过思考步骤直接行动。

**答案**: 错误

**解析**: ReAct模式强调每次行动前都要思考，跳过思考可能导致错误的行动选择。

**知识点**: ReAct模式

**课程**: 简单对话 + ReAct Agent

**难度**: ⭐

---

#### 3. MCP协议是闭源的，只能由Anthropic使用。

**答案**: 错误

**解析**: MCP是一个开放协议，任何人都可以开发兼容的Server和Client，促进工具生态发展。

**知识点**: MCP协议概述

**课程**: MCP 模型上下文协议

**难度**: ⭐

---

#### 4. LangGraph中的状态是不可变的，不能被修改。

**答案**: 错误

**解析**: LangGraph中的状态可以被节点修改，但应该通过reducer函数进行增量更新，而不是直接修改。

**知识点**: LangGraph概述

**课程**: LangGraph

**难度**: ⭐⭐

---

#### 5. TypedDict可以用于定义LangGraph工作流的状态类。

**答案**: 正确

**解析**: TypedDict用于定义状态类，在工作流节点之间传递和更新数据。

**知识点**: 状态管理 / State Management

**课程**: LangGraph 入门教程 / Introduction to LangGraph

**难度**: ⭐

---

#### 6. MCP支持动态工具发现。

**答案**: 正确

**解析**: MCP支持动态工具发现，AI可以自动发现和使用服务器提供的工具。

**知识点**: 工具发现与执行 / Tool Discovery & Execution

**课程**: MCP 模型上下文协议 / Model Context Protocol

**难度**: ⭐

---

#### 7. MessagesPlaceholder用于在提示模板中插入历史消息。

**答案**: 正确

**解析**: MessagesPlaceholder在提示模板中为历史消息预留位置。

**知识点**: 提示模板设计 / Prompt Template Design

**课程**: 简单对话Agent / Simple Conversational Agent

**难度**: ⭐

---

#### 8. ModelMessagesTypeAdapter用于消息的序列化和反序列化。

**答案**: 正确

**解析**: ModelMessagesTypeAdapter用于将消息转换为JSON格式存储和从JSON恢复。

**知识点**: 消息存储与检索 / Message Storage & Retrieval

**课程**: PydanticAI 对话Agent / PydanticAI Conversational Agent

**难度**: ⭐

---

#### 9. Agent可以将自然语言问题转换为Python代码执行数据分析。

**答案**: 正确

**解析**: Agent能够理解自然语言问题并生成相应的Python代码进行分析。

**知识点**: 自然语言数据查询 / Natural Language Data Queries

**课程**: 数据分析Agent / Data Analysis Agent

**难度**: ⭐

---

#### 10. AgentExecutor可以控制Agent的最大迭代次数。

**答案**: 正确

**解析**: AgentExecutor通过max_iterations参数控制最大迭代次数。

**知识点**: Agent Executor / Agent执行器

**课程**: 任务导向Agent / Task-Oriented Agent

**难度**: ⭐

---

#### 11. Agent之间通过共享上下文列表传递信息。

**答案**: 正确

**解析**: Agent之间通过共享的上下文列表传递消息和信息。

**知识点**: 上下文传递 / Context Passing

**课程**: 多Agent协作系统 / Multi-Agent Collaboration System

**难度**: ⭐

---

#### 12. ChromaDB用于存储bug报告并进行语义搜索。

**答案**: 正确

**解析**: ChromaDB存储bug报告，通过语义搜索找到相似的历史bug。

**知识点**: 向量数据库记忆 / Vector Database Memory

**课程**: 自愈代码Agent / Self-Healing Code Agent

**难度**: ⭐

---

#### 13. 提示优化器可以自动改进Agent的系统提示。

**答案**: 正确

**解析**: 提示优化器根据反馈轨迹自动改进系统提示。

**知识点**: 提示优化 / Prompt Optimization

**课程**: 自我改进Agent / Self-Improving Agent

**难度**: ⭐

---

#### 14. 记忆整合可以提供个性化的响应。

**答案**: 正确

**解析**: 将历史记忆整合到当前上下文可以提供更个性化的响应。

**知识点**: 记忆整合 / Memory Integration

**课程**: 记忆增强对话Agent / Memory-Enhanced Conversational Agent

**难度**: ⭐

---

#### 15. 论文评分系统可以评估多个维度。

**答案**: 正确

**解析**: 论文评分系统可以评估内容、结构、语法等多个维度。

**知识点**: 自动评分流程 / Automated Grading Process

**课程**: 论文评分系统 / Essay Grading System

**难度**: ⭐

---

#### 16. 新闻摘要Agent可以生成简洁的新闻摘要。

**答案**: 正确

**解析**: 新闻摘要Agent分析新闻内容并生成简洁摘要。

**知识点**: 新闻摘要生成 / News Summary Generation

**课程**: 新闻摘要Agent / News TLDR Agent

**难度**: ⭐

---

#### 17. 播客生成Agent可以生成对话脚本。

**答案**: 正确

**解析**: 播客生成Agent可以生成包含对话的播客脚本。

**知识点**: 播客内容生成 / Podcast Content Generation

**课程**: 播客生成Agent / Podcast Generator Agent

**难度**: ⭐

---

#### 18. 网络搜索摘要Agent可以聚合多个搜索结果。

**答案**: 正确

**解析**: Agent可以聚合多个搜索结果并生成综合摘要。

**知识点**: 网络搜索集成 / Internet Search Integration

**课程**: 网络搜索摘要Agent / Internet Search & Summarize Agent

**难度**: ⭐

---


## PROD 生产落地

### 模块概述 / Module Overview

本模块包含 29 道练习题，涵盖该领域的核心知识点。

---

### 单选题 / Single Choice (15题)

#### 1. StateGraph在生产环境中的主要优势是什么？

- A. 更快的执行速度
- B. 状态持久化和恢复
- C. 更简单的代码
- D. 更少的内存占用

**答案**: B

**解析**: StateGraph支持状态持久化和恢复，适合生产环境。

**知识点**: StateGraph 生产架构 / StateGraph Production Architecture

**课程**: LangGraph 生产级教程 / LangGraph Production Tutorial

**难度**: ⭐

---

#### 2. A2A协议的主要目的是什么？

- A. 加密通信
- B. Agent间标准化通信
- C. 数据存储
- D. 用户界面

**答案**: B

**解析**: A2A协议定义了Agent之间通信的标准格式。

**知识点**: A2A 协议架构 / A2A Protocol Architecture

**课程**: Agent-to-Agent 通信协议 / Agent-to-Agent Communication Protocol

**难度**: ⭐

---

#### 3. 向量记忆存储的主要优势是什么？

- A. 更快的写入速度
- B. 语义搜索能力
- C. 更小的存储空间
- D. 更简单的查询

**答案**: B

**解析**: 向量存储支持语义搜索，可以找到相似的记忆。

**知识点**: 向量记忆存储 / Vector Memory Storage

**课程**: Redis 记忆系统 / Redis Memory System

**难度**: ⭐

---

#### 4. MCP服务器使用什么装饰器暴露工具？

- A. @tool
- B. @mcp.tool
- C. @expose
- D. @api

**答案**: B

**解析**: MCP服务器使用@mcp.tool装饰器暴露工具。

**知识点**: MCP 服务器开发 / MCP Server Development

**课程**: MCP 生产集成 / MCP Production Integration

**难度**: ⭐

---

#### 5. FastAPI的主要优势是什么？

- A. 自动文档生成
- B. 类型验证
- C. 高性能异步
- D. 以上都是

**答案**: D

**解析**: FastAPI具有自动文档、类型验证和高性能异步等优势。

**知识点**: FastAPI Agent 服务 / FastAPI Agent Service

**课程**: FastAPI Agent 部署 / FastAPI Agent Deployment

**难度**: ⭐

---

#### 6. API Key通常放在哪个请求头中？

- A. Authorization
- B. X-API-Key
- C. Content-Type
- D. Accept

**答案**: B

**解析**: API Key通常放在X-API-Key请求头中。

**知识点**: API 认证 / API Authentication

**课程**: FastAPI Agent 部署 / FastAPI Agent Deployment

**难度**: ⭐

---

#### 7. Ollama的主要优势是什么？

- A. 更快的响应
- B. 数据隐私和成本控制
- C. 更好的模型
- D. 更简单的API

**答案**: B

**解析**: Ollama允许本地运行模型，保护数据隐私并控制成本。

**知识点**: Ollama 本地推理 / Ollama Local Inference

**课程**: Ollama 本地部署 / Ollama Local Deployment

**难度**: ⭐

---

#### 8. Streamlit的主要用途是什么？

- A. 数据分析
- B. 快速构建Web UI
- C. 机器学习
- D. 数据库管理

**答案**: B

**解析**: Streamlit用于快速构建Web应用界面。

**知识点**: Streamlit UI 开发 / Streamlit UI Development

**课程**: Streamlit 聊天机器人 / Streamlit Chatbot

**难度**: ⭐

---

#### 9. 微调的主要目的是什么？

- A. 减少模型大小
- B. 提高特定任务性能
- C. 加快推理速度
- D. 减少训练时间

**答案**: B

**解析**: 微调用于提高模型在特定任务或领域的性能。

**知识点**: Agent 微调技术 / Agent Fine-tuning Techniques

**课程**: Agent 微调指南 / Agent Fine-tuning Guide

**难度**: ⭐

---

#### 10. Llama Firewall的主要功能是什么？

- A. 加速推理
- B. 安全防护和输入过滤
- C. 数据存储
- D. 模型训练

**答案**: B

**解析**: Llama Firewall用于Agent安全防护和输入过滤。

**知识点**: Llama Firewall 基础 / Llama Firewall Basics

**课程**: Llama Firewall 入门 / Llama Firewall Introduction

**难度**: ⭐

---

#### 11. 输出护栏的主要目的是什么？

- A. 加快响应速度
- B. 确保响应安全和适当
- C. 减少响应长度
- D. 增加响应多样性

**答案**: B

**解析**: 输出护栏确保Agent响应安全适当。

**知识点**: 输出护栏实现 / Output Guardrail Implementation

**课程**: 输出护栏 / Output Guardrails

**难度**: ⭐

---

#### 12. 可观测性的主要目的是什么？

- A. 加快执行速度
- B. 监控和诊断系统行为
- C. 减少内存使用
- D. 简化代码

**答案**: B

**解析**: 可观测性用于监控和诊断系统行为。

**知识点**: Agent 可观测性 / Agent Observability

**课程**: Qualifire 可观测性 / Qualifire Observability

**难度**: ⭐

---

#### 13. Web内容提取的主要目的是什么？

- A. 加快网页加载
- B. 获取结构化数据
- C. 提高SEO排名
- D. 减少带宽使用

**答案**: B

**解析**: Web内容提取用于从网页获取结构化数据。

**知识点**: Web 内容提取 / Web Content Extraction

**课程**: 搜索提取爬取 / Search Extract Crawl

**难度**: ⭐

---

#### 14. Ollama模型拉取命令是什么？

- A. ollama download
- B. ollama pull
- C. ollama get
- D. ollama fetch

**答案**: B

**解析**: 使用ollama pull命令下载模型。

**知识点**: Ollama 基础操作 / Ollama Basic Operations

**课程**: Ollama 基础用法 / Ollama Basic Usage

**难度**: ⭐

---

#### 15. 多步骤Agent的主要特点是什么？

- A. 更快的执行
- B. 执行复杂多步骤任务
- C. 更少的内存使用
- D. 更简单的代码

**答案**: B

**解析**: 多步骤Agent能够执行复杂的多步骤任务。

**知识点**: 多步骤 Agent 设计 / Multi-Step Agent Design

**课程**: 多步骤 Agent 教程 / Multi-Step Agent Tutorial

**难度**: ⭐

---

### 多选题 / Multiple Choice (1题)

#### 1. Agent记忆系统包括哪些类型？

- A. 短期记忆
- B. 长期记忆
- C. 临时记忆
- D. 缓存记忆

**答案**: A,B

**解析**: Agent记忆系统包括短期记忆和长期记忆。

**知识点**: 双记忆架构 / Dual-Memory Architecture

**课程**: Redis 记忆系统 / Redis Memory System

**难度**: ⭐

---

### 判断题 / True or False (13题)

#### 1. 条件边可以根据状态决定工作流的下一步。

**答案**: 正确

**解析**: 条件边允许根据当前状态动态决定工作流路径。

**知识点**: 节点与边设计 / Node and Edge Design

**课程**: LangGraph 生产级教程 / LangGraph Production Tutorial

**难度**: ⭐

---

#### 2. RedisSaver用于持久化LangGraph工作流状态。

**答案**: 正确

**解析**: RedisSaver是LangGraph的检查点保存器，用于状态持久化。

**知识点**: Redis 检查点 / Redis Checkpointer

**课程**: Redis 记忆系统 / Redis Memory System

**难度**: ⭐

---

#### 3. MCP支持动态工具发现。

**答案**: 正确

**解析**: MCP支持动态工具发现，Agent可以自动发现可用工具。

**知识点**: 工具发现与执行 / Tool Discovery & Execution

**课程**: MCP 生产集成 / MCP Production Integration

**难度**: ⭐

---

#### 4. SSE用于实现Agent响应的流式传输。

**答案**: 正确

**解析**: Server-Sent Events用于实现流式响应传输。

**知识点**: 流式响应 / Streaming Responses

**课程**: FastAPI Agent 部署 / FastAPI Agent Deployment

**难度**: ⭐

---

#### 5. LangSmith可以用于追踪Agent执行流程。

**答案**: 正确

**解析**: LangSmith提供完整的追踪和监控功能。

**知识点**: 追踪与监控 / Tracing & Monitoring

**课程**: LangSmith 追踪基础 / LangSmith Tracing Basics

**难度**: ⭐

---

#### 6. Tavily API专为AI Agent设计。

**答案**: 正确

**解析**: Tavily是专为AI Agent优化的搜索API。

**知识点**: Web 搜索集成 / Web Search Integration

**课程**: Web Agent 教程 / Web Agent Tutorial

**难度**: ⭐

---

#### 7. IntellAgent可以评估Agent的准确性和响应时间。

**答案**: 正确

**解析**: IntellAgent提供多种性能指标评估。

**知识点**: Agent 性能评估 / Agent Performance Evaluation

**课程**: IntellAgent 评估 / IntellAgent Evaluation

**难度**: ⭐

---

#### 8. 提示注入是Agent安全的主要威胁之一。

**答案**: 正确

**解析**: 提示注入是Agent面临的主要安全威胁。

**知识点**: 安全漏洞评估 / Security Vulnerability Assessment

**课程**: Agent 安全评估 / Agent Security Evaluation

**难度**: ⭐

---

#### 9. 输入护栏可以检测提示注入攻击。

**答案**: 正确

**解析**: 输入护栏用于检测和阻止各种恶意输入。

**知识点**: 输入护栏实现 / Input Guardrail Implementation

**课程**: 输入护栏 / Input Guardrails

**难度**: ⭐

---

#### 10. 工具安全配置可以防止工具滥用。

**答案**: 正确

**解析**: 工具安全配置包括访问控制和执行限制。

**知识点**: 工具安全配置 / Tool Security Configuration

**课程**: 工具安全 / Tools Security

**难度**: ⭐

---

#### 11. 混合Agent可以平衡成本和性能。

**答案**: 正确

**解析**: 混合Agent结合本地和云端优势，优化成本和性能。

**知识点**: 混合 Agent 架构 / Hybrid Agent Architecture

**课程**: 混合 Agent 教程 / Hybrid Agent Tutorial

**难度**: ⭐

---

#### 12. 向量化支持语义搜索功能。

**答案**: 正确

**解析**: 向量化将文本转换为向量，支持语义搜索。

**知识点**: 向量化处理 / Vectorization Processing

**课程**: 向量化教程 / Vectorize Tutorial

**难度**: ⭐

---

#### 13. LangChain可以与Ollama集成使用本地LLM。

**答案**: 正确

**解析**: LangChain通过ChatOllama类支持Ollama集成。

**知识点**: LangChain Ollama 集成 / LangChain Ollama Integration

**课程**: LangChain + Ollama Agent / LangChain + Ollama Agent

**难度**: ⭐

---


## Context Engineering 上下文工程

### 模块概述 / Module Overview

本模块包含 27 道练习题，涵盖该领域的核心知识点。

---

### 单选题 / Single Choice (9题)

#### 1. 上下文组装方程 C = A(c₁, c₂, ..., cₙ) 中的 A 代表什么？

- A. 算法
- B. 组装函数
- C. 上下文
- D. 参数

**答案**: B

**解析**: A代表Assembly Function（组装函数），用于组合上下文组件。

**知识点**: 上下文组装方程 / Context Assembly Equation

**课程**: 数学基础 / Mathematical Foundations

**难度**: ⭐

---

#### 2. 语义检索引擎主要使用什么技术？

- A. 关键词匹配
- B. 向量嵌入和相似度
- C. 正则表达式
- D. 数据库索引

**答案**: B

**解析**: 语义检索使用向量嵌入和语义相似度进行检索。

**知识点**: 语义检索引擎 / Semantic Retrieval Engine

**课程**: 上下文检索与生成 / Context Retrieval & Generation

**难度**: ⭐

---

#### 3. 上下文压缩的主要目的是什么？

- A. 增加信息量
- B. 减少长度保留关键信息
- C. 加快处理速度
- D. 提高准确性

**答案**: B

**解析**: 上下文压缩旨在减少长度同时保留关键信息。

**知识点**: 上下文压缩 / Context Compression

**课程**: 上下文处理 / Context Processing

**难度**: ⭐

---

#### 4. 稠密段落检索使用什么架构？

- A. 单编码器
- B. 双编码器
- C. 三编码器
- D. 无编码器

**答案**: B

**解析**: DPR使用双编码器分别编码查询和段落。

**知识点**: 稠密段落检索 / Dense Passage Retrieval

**课程**: 检索增强生成 / Retrieval Augmented Generation

**难度**: ⭐

---

#### 5. 短期记忆管理的主要策略是什么？

- A. 数据库存储
- B. 滑动窗口和Token预算
- C. 文件系统
- D. 网络传输

**答案**: B

**解析**: 短期记忆使用滑动窗口和Token预算策略管理上下文。

**知识点**: 短期记忆 / Short-Term Memory

**课程**: 记忆系统 / Memory Systems

**难度**: ⭐

---

#### 6. 工具绑定的主要作用是什么？

- A. 加快执行速度
- B. 支持函数调用和参数验证
- C. 减少内存使用
- D. 简化代码

**答案**: B

**解析**: 工具绑定支持函数调用和参数验证。

**知识点**: 工具绑定 / Tool Binding

**课程**: 工具集成 / Tool Integration

**难度**: ⭐

---

#### 7. Agent通信协议不包括以下哪种？

- A. 消息传递
- B. 共享记忆
- C. 直接调用
- D. 黑板模式

**答案**: C

**解析**: Agent通信通过消息传递、共享记忆或黑板模式。

**知识点**: Agent 通信协议 / Agent Communication Protocols

**课程**: 多Agent系统 / Multi-Agent Systems

**难度**: ⭐

---

#### 8. 吸引子动力学中的吸引子代表什么？

- A. 数据点
- B. 稳定状态
- C. 随机噪声
- D. 错误状态

**答案**: B

**解析**: 吸引子代表场中的稳定状态。

**知识点**: 吸引子动力学 / Attractor Dynamics

**课程**: 场论整合 / Field Theory Integration

**难度**: ⭐

---

#### 9. 元学习的主要特点是什么？

- A. 学习更多数据
- B. 学习如何学习
- C. 学习更快
- D. 学习更少

**答案**: B

**解析**: 元学习是学习如何学习的过程。

**知识点**: 元学习 / Meta-Learning

**课程**: 元递归系统 / Meta-Recursive Systems

**难度**: ⭐

---

### 多选题 / Multiple Choice (7题)

#### 1. 上下文工程的四大支柱包括哪些？

- A. 形式化
- B. 优化
- C. 信息论
- D. 深度学习

**答案**: A,B,C

**解析**: 四大支柱是形式化、优化、信息论和贝叶斯推断。

**知识点**: 四大支柱 / Four Pillars

**课程**: 数学基础 / Mathematical Foundations

**难度**: ⭐

---

#### 2. RAG系统的核心组件包括哪些？

- A. 检索器
- B. 重排序器
- C. 生成器
- D. 分类器

**答案**: A,B,C

**解析**: RAG系统由检索器、重排序器和生成器组成。

**知识点**: RAG 基础架构 / RAG Fundamentals

**课程**: 检索增强生成 / Retrieval Augmented Generation

**难度**: ⭐

---

#### 3. 记忆类型包括哪些？

- A. 情景记忆
- B. 语义记忆
- C. 程序记忆
- D. 临时记忆

**答案**: A,B,C

**解析**: 三种主要记忆类型是情景、语义和程序记忆。

**知识点**: 记忆类型 / Memory Types

**课程**: 记忆系统 / Memory Systems

**难度**: ⭐

---

#### 4. Agent协调模式包括哪些？

- A. 层级式
- B. 对等式
- C. 混合式
- D. 独立式

**答案**: A,B,C

**解析**: 协调模式包括层级式、对等式和混合式。

**知识点**: Agent 协调模式 / Agent Coordination Patterns

**课程**: 多Agent系统 / Multi-Agent Systems

**难度**: ⭐

---

#### 5. 上下文系统评估指标包括哪些？

- A. 准确性
- B. 相关性
- C. 连贯性
- D. 代码行数

**答案**: A,B,C

**解析**: 评估指标包括准确性、相关性和连贯性。

**知识点**: 评估指标 / Evaluation Metrics

**课程**: 评估方法论 / Evaluation Methodologies

**难度**: ⭐

---

#### 6. 可解释性方法包括哪些？

- A. 注意力可视化
- B. 特征归因
- C. 反事实分析
- D. 数据加密

**答案**: A,B,C

**解析**: 可解释性方法包括注意力可视化、特征归因和反事实分析。

**知识点**: 可解释性方法 / Interpretability Methods

**课程**: 可解释性 / Interpretability

**难度**: ⭐

---

#### 7. 跨模态上下文整合涉及哪些模态？

- A. 文本
- B. 图像
- C. 音频
- D. 代码

**答案**: A,B,C

**解析**: 跨模态整合包括文本、图像、音频等多种模态。

**知识点**: 跨模态上下文 / Cross-Modal Context

**课程**: 跨模态整合 / Cross-Modal Integration

**难度**: ⭐

---

### 判断题 / True or False (11题)

#### 1. Software 3.0范式包括Prompts、Programming和Protocols三个层次。

**答案**: 正确

**解析**: Software 3.0的三大范式是Prompts（模板）、Programming（算法）、Protocols（编排）。

**知识点**: Software 3.0 范式 / Software 3.0 Paradigm

**课程**: 数学基础 / Mathematical Foundations

**难度**: ⭐

---

#### 2. 动态上下文组装需要考虑上下文窗口限制。

**答案**: 正确

**解析**: 动态组装需要优化信息密度并遵守上下文窗口限制。

**知识点**: 动态上下文组装 / Dynamic Context Assembly

**课程**: 上下文检索与生成 / Context Retrieval & Generation

**难度**: ⭐

---

#### 3. 上下文生命周期管理包括初始化、更新和清理。

**答案**: 正确

**解析**: 生命周期管理覆盖上下文的完整生命周期。

**知识点**: 上下文生命周期 / Context Lifecycle

**课程**: 上下文管理 / Context Management

**难度**: ⭐

---

#### 4. 混合检索结合了稀疏检索和稠密检索的优势。

**答案**: 正确

**解析**: 混合检索融合BM25和稠密检索的结果。

**知识点**: 混合检索策略 / Hybrid Retrieval Strategies

**课程**: 检索增强生成 / Retrieval Augmented Generation

**难度**: ⭐

---

#### 5. 长期记忆使用向量存储支持语义搜索。

**答案**: 正确

**解析**: 长期记忆通过向量嵌入支持语义搜索和检索。

**知识点**: 长期记忆 / Long-Term Memory

**课程**: 记忆系统 / Memory Systems

**难度**: ⭐

---

#### 6. 工具发现可以动态发现可用的API端点和函数。

**答案**: 正确

**解析**: 工具发现支持动态发现各种可用工具。

**知识点**: 工具发现 / Tool Discovery

**课程**: 工具集成 / Tool Integration

**难度**: ⭐

---

#### 7. 神经场论将上下文视为连续语义场。

**答案**: 正确

**解析**: 神经场论使用连续场表示上下文。

**知识点**: 神经场基础 / Neural Field Foundations

**课程**: 场论整合 / Field Theory Integration

**难度**: ⭐

---

#### 8. 自改进循环通过反馈持续改进系统性能。

**答案**: 正确

**解析**: 自改进循环利用反馈持续优化系统。

**知识点**: 自改进循环 / Self-Improvement Loops

**课程**: 元递归系统 / Meta-Recursive Systems

**难度**: ⭐

---

#### 9. 量子语义使用量子概念建模语义歧义。

**答案**: 正确

**解析**: 量子语义利用量子力学概念处理语义问题。

**知识点**: 量子语义基础 / Quantum Semantics Foundations

**课程**: 量子语义 / Quantum Semantics

**难度**: ⭐

---

#### 10. 协作演化通过群体协作提升整体能力。

**答案**: 正确

**解析**: 协作演化使Agent群体通过协作提升能力。

**知识点**: 协作演化模式 / Collaborative Evolution Patterns

**课程**: 协作演化 / Collaborative Evolution

**难度**: ⭐

---

#### 11. 上下文工程的未来方向包括自适应上下文和神经符号整合。

**答案**: 正确

**解析**: 这些是上下文工程的前沿研究方向。

**知识点**: 前沿研究方向 / Frontier Research Directions

**课程**: 未来方向 / Future Directions

**难度**: ⭐

---


---

## 答案速查表 / Quick Answer Key


### Prompts 提示词工程

1. B
2. B
3. 错误
4. TASK|CONSTRAINTS|OUTPUT|任务|约束|输出
5. C
6. A,B,C
7. 限制,边界,范围,控制,符合预期
8. C
9. B
10. 错误
11. B
12. 泛化|预训练|generalization|pre-training
13. A,B,C
14. 简单,快速,测试,token,基础
15. B
16. 错误
17. B
18. A,B,C
19. 示例|例子|example|样本
20. 示例,理解,模式,学习,参考
21. B
22. B
23. 错误
24. A,B,D
25. 推理|中间|思考|reasoning|intermediate
26. 推理,可见,准确,复杂,验证
27. B
28. B
29. 错误
30. B
31. 输入|输出|input|output
32. A,B,C
33. B
34. B
35. 正确
36. 变量|variable|input_variables
37. B
38. A,B,D
39. 错误
40. 上下文,追问,对话,记忆,连贯
41. B
42. B
43. 错误
44. 完整|全部|complete|all
45. B
46. B
47. 正确
48. A,B,C
49. B
50. 正确
51. B
52. A,B,D
53. B
54. 错误
55. A,B,D
56. B
57. B
58. 错误
59. A,B,C
60. B
61. 正确
62. B
63. 错误
64. B
65. A,B,C,D
66. B
67. 正确
68. B
69. A,B,C,D
70. B
71. A,B,C,D
72. B
73. 正确
74. A,B,C
75. C
76. A,B,C
77. B
78. B
79. 正确
80. A,B,C
81. B
82. A,B,C
83. B
84. A,B,C
85. B
86. B
87. 正确
88. B
89. A,B,C
90. B
91. 正确
92. A,B,C

### RAG 检索增强生成

1. A
2. B
3. 错误
4. A,B,C
5. 检索|生成|retrieve|generate|搜索
6. 更新,成本,追溯,幻觉,知识
7. C
8. B
9. 正确
10. B
11. A,B,D
12. B
13. 正确
14. B
15. 正确
16. B
17. B
18. 正确
19. B
20. 正确
21. B
22. 正确
23. B
24. 正确
25. B
26. 正确
27. A,B,D
28. B
29. B
30. B
31. 正确
32. B

### Agent 智能体

1. B
2. A,B,C,D
3. 错误
4. D
5. 工具|Tool|API|函数
6. 独立,决策,人工,自动,目标
7. B
8. A,B,C
9. 错误
10. B
11. TAO|Thought-Action-Observation|思考-行动-观察
12. 循环,终止,无限,限制,安全
13. C
14. B
15. A,B,C
16. 错误
17. Client-Server|客户端-服务器|CS
18. 标准,复用,一次,兼容,生态
19. B
20. B
21. A,B,C
22. 错误
23. 条件|conditional
24. 保存,恢复,暂停,人机,检查点
25. B
26. 正确
27. B
28. 正确
29. A,B,C
30. B
31. B
32. 正确
33. B
34. 正确
35. B
36. 正确
37. B
38. 正确
39. B
40. 正确
41. B
42. 正确
43. B
44. 正确
45. B
46. 正确
47. C
48. B
49. C
50. 正确
51. B
52. 正确
53. B
54. 正确
55. B
56. 正确

### PROD 生产落地

1. B
2. 正确
3. B
4. A,B
5. 正确
6. B
7. B
8. 正确
9. D
10. 正确
11. B
12. 正确
13. B
14. 正确
15. B
16. 正确
17. B
18. 正确
19. B
20. 正确
21. B
22. 正确
23. B
24. 正确
25. B
26. 正确
27. B
28. 正确
29. B

### Context Engineering 上下文工程

1. B
2. A,B,C
3. 正确
4. B
5. 正确
6. B
7. 正确
8. A,B,C
9. B
10. 正确
11. B
12. 正确
13. A,B,C
14. 正确
15. B
16. A,B,C
17. C
18. 正确
19. B
20. A,B,C
21. B
22. 正确
23. 正确
24. A,B,C
25. 正确
26. A,B,C
27. 正确


---

## 学习建议 / Study Tips

1. **先学习课程内容**: 在做练习题之前，确保已经学习相关课程内容。
2. **独立思考**: 尝试自己回答问题，再看答案和解析。
3. **记录错题**: 将做错的题目记录下来，定期复习。
4. **理解原理**: 不要只记住答案，要理解背后的原理。

---

## 统计信息 / Statistics

| 模块 | 单选题 | 多选题 | 判断题 | 总计 |
|------|--------|--------|--------|------|
| Prompts 提示词工程 | 41 | 20 | 19 | 92 |
| RAG 检索增强生成 | 17 | 3 | 10 | 32 |
| Agent 智能体 | 25 | 5 | 18 | 56 |
| PROD 生产落地 | 15 | 1 | 13 | 29 |
| Context Engineering 上下文工程 | 9 | 7 | 11 | 27 |
| **总计** | **107** | **36** | **71** | **236** |


---

*本文档由AI学习平台自动生成 / This document is auto-generated by AI Learning Platform*
