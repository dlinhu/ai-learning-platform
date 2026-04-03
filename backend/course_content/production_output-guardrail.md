# 输出护栏 / Output Guardrails

## Overview / 概述

Implement output guardrails to ensure safe and appropriate agent responses. / 实现输出护栏确保Agent响应安全适当。

## Key Knowledge Points / 核心知识点

### 1. 输出护栏实现 / Output Guardrail Implementation

**English:** Implement output guardrails to filter sensitive information, inappropriate content, and potentially harmful responses.

**中文:** 实现输出护栏过滤敏感信息、不当内容和潜在有害响应。

**Key Concepts / 核心概念:**
- Output filtering / 输出过滤
- Content moderation / 内容审核
- PII protection / 个人信息保护
- Response validation / 响应验证

**Example / 示例:**
```python
@output_guardrail
def check_output(response):
    if contains_pii(response):
        return redact_pii(response)
    return response
# → Implement output guardrail for PII protection

```

---

## Summary / 总结

This lesson covered key production deployment concepts. Practice these techniques to build robust production systems.

本课程涵盖了关键的生产部署技术。练习这些技术以构建健壮的生产系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own production agents / 构建自己的生产Agent
3. Explore advanced patterns / 探索高级模式
