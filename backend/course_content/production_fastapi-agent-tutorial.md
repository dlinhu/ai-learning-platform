# FastAPI Agent 部署 / FastAPI Agent Deployment

## Overview / 概述

Deploy AI agents as production APIs using FastAPI with synchronous and streaming endpoints. / 使用FastAPI将AI Agent部署为生产API，包括同步和流式端点。

## Key Knowledge Points / 核心知识点

### 1. FastAPI Agent 服务 / FastAPI Agent Service

**English:** Create agent API services using FastAPI with Pydantic model validation and automatic documentation generation.

**中文:** 使用FastAPI创建Agent API服务，支持Pydantic模型验证和自动文档生成。

**Key Concepts / 核心概念:**
- FastAPI / FastAPI框架
- Pydantic models / Pydantic模型
- Auto documentation / 自动文档
- Type validation / 类型验证

**Example / 示例:**
```python
@app.post('/agent', response_model=QueryResponse)
def query_agent(request: QueryRequest):
    return QueryResponse(response=agent.generate_response(request.query))
# → Create FastAPI agent endpoint

```

---

### 2. 流式响应 / Streaming Responses

**English:** Implement streaming transmission of agent responses using Server-Sent Events (SSE).

**中文:** 使用Server-Sent Events (SSE)实现Agent响应的流式传输。

**Key Concepts / 核心概念:**
- SSE / 服务器发送事件
- StreamingResponse / 流式响应
- Token streaming / Token流式传输
- EventSourceResponse / 事件源响应

**Example / 示例:**
```python
@app.post('/agent/stream')
async def stream_agent(request: QueryRequest):
    return StreamingResponse(event_generator(), media_type='text/event-stream')
# → Create streaming agent endpoint

```

---

### 3. API 认证 / API Authentication

**English:** Add API Key authentication and request validation for agent APIs.

**中文:** 为Agent API添加API Key认证和请求验证。

**Key Concepts / 核心概念:**
- API Key / API密钥
- Header validation / 请求头验证
- Dependency injection / 依赖注入
- Error handling / 错误处理

**Example / 示例:**
```python
async def verify_api_key(x_api_key: str = Header(None)):
    if x_api_key != os.environ.get('API_KEY'):
        raise HTTPException(status_code=403)
# → Verify API key in request header

```

---

## Summary / 总结

This lesson covered key production deployment concepts. Practice these techniques to build robust production systems.

本课程涵盖了关键的生产部署技术。练习这些技术以构建健壮的生产系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own production agents / 构建自己的生产Agent
3. Explore advanced patterns / 探索高级模式
