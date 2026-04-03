# Llama Firewall 入门 / Llama Firewall Introduction

## Overview / 概述

Get started with Llama Firewall for agent security. / 开始使用Llama Firewall保护Agent安全。

## Key Knowledge Points / 核心知识点

### 1. Llama Firewall 基础 / Llama Firewall Basics

**English:** Use Llama Firewall to build agent security layers and filter malicious inputs.

**中文:** 使用Llama Firewall构建Agent安全防护层，过滤恶意输入。

**Key Concepts / 核心概念:**
- Firewall / 防火墙
- Input filtering / 输入过滤
- Security layer / 安全层
- Threat detection / 威胁检测

**Example / 示例:**
```python
from llamafirewall import Firewall
firewall = Firewall()
if firewall.is_safe(user_input):
    agent.process(user_input)
# → Check input safety with Llama Firewall

```

---

## Summary / 总结

This lesson covered key production deployment concepts. Practice these techniques to build robust production systems.

本课程涵盖了关键的生产部署技术。练习这些技术以构建健壮的生产系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own production agents / 构建自己的生产Agent
3. Explore advanced patterns / 探索高级模式
