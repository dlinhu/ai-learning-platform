# Context Engineering 提示词工程思维导图

## 第一模块：Prompts 提示词工程

### Day 1: 原子 + 零/少样本
- **原子 Prompt** - 最基本的提示单元
  - TASK + CONSTRAINTS + OUTPUT 结构
  - 分子提示基础
- **最小 Prompt** - 最简提示模板
- **零样本 (Zero-shot)** - 无示例直接推理
- **少样本 (Few-shot)** - 通过示例学习
- **分子 Context** - 上下文组织

### Day 2: CoT + 角色 + 约束 + 自洽
- **扩展上下文** - 上下文窗口管理
- **思维链 (CoT)** - Chain of Thought 推理
- **角色/Persona** - 角色扮演提示
- **约束生成** - Constrained Guided Generation
- **自洽 (Self-Consistency)** - 多路径一致性

### Day 3: 指令 + 任务分解 + 提示链
- **指令工程** - 清晰指令设计
- **任务分解** - Task Decomposition
- **提示链** - Prompt Chaining/Sequencing

### Day 4: 记忆 + 控制循环 + 认知
- **记忆单元 (Cells of Context)** - 上下文记忆组织
- **控制循环** - 多步控制流程
- **认知工具** - Cognitive Tools 模板

### Day 5: 提示编程 + 优化 + Schema
- **提示编程** - 类代码推理
- **Prompt 程序** - 组合式提示
- **Prompt 优化** - Optimization Techniques
- **评估** - Evaluating Prompt Effectiveness
- **Schema 设计** - 输出结构化设计
- **参考** - Cognitive Patterns & Patterns

---

## 学习路径图

```
提示词工程 (Prompts)
│
├── 基础原子
│   ├── 原子 Prompt (TASK+CONSTRAINTS+OUTPUT)
│   ├── 最小 Prompt
│   ├── 零样本 (Zero-shot)
│   └── 少样本 (Few-shot)
│
├── 进阶技巧
│   ├── 思维链 (CoT)
│   ├── 角色扮演 (Role/Persona)
│   ├── 约束生成 (Constraints)
│   ├── 自洽 (Self-Consistency)
│   └── 扩展上下文
│
├── 复杂任务
│   ├── 指令工程
│   ├── 任务分解
│   └── 提示链
│
├── 上下文管理
│   ├── 记忆单元
│   ├── 控制循环
│   └── 认知工具
│
└── 工程化
    ├── 提示编程
    ├── Prompt 程序
    ├── 优化技巧
    ├── 效果评估
    └── Schema 设计
```

---

## 核心概念关系图

| 概念 | 英文 | 核心作用 |
|------|------|----------|
| 原子 Prompt | Atoms | 最小提示单元 |
| 零样本 | Zero-shot | 无示例推理 |
| 少样本 | Few-shot | 示例学习 |
| 思维链 | CoT | 推理步骤显式化 |
| 角色 | Role | 身份设定增强 |
| 约束 | Constraints | 输出格式控制 |
| 自洽 | Self-Consistency | 多路径验证 |
| 任务分解 | Decomposition | 复杂任务拆分 |
| 提示链 | Chaining | 多步串联 |
| 记忆单元 | Cells | 上下文组织 |
| 控制循环 | Control Loops | 迭代优化 |
| Schema | Schema | 结构化输出 |

---

## 进阶路径

```
Junior (基础)
    ↓
原子 → 零/少样本 → 指令 → 任务分解
    ↓
Senior (进阶)
    ↓
CoT → 角色 → 约束 → 自洽 → 提示链
    ↓
Professor (高级)
    ↓
提示编程 → 优化 → 评估 → Schema 设计
```
