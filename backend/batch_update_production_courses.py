import os
import sys

backend_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, backend_dir)

from app.utils.database import SessionLocal
from app.models.models import Module, Lesson, KnowledgePoint, Term, LessonTerm, PracticeQuestion

PRODUCTION_COURSES_DATA = {
    "langgraph_tutorial.ipynb": {
        "title": "LangGraph 生产级教程 / LangGraph Production Tutorial",
        "summary": "Learn LangGraph for building production-ready agent workflows with state management and graph-based architectures. / 学习LangGraph构建生产级Agent工作流，包括状态管理和图架构。",
        "knowledge_points": [
            {
                "title": "StateGraph 生产架构 / StateGraph Production Architecture",
                "description": "在生产环境中使用StateGraph构建可扩展的Agent工作流，支持状态持久化和恢复。",
                "description_en": "Build scalable agent workflows in production using StateGraph with state persistence and recovery support.",
                "importance": 3,
                "key_concepts": ["StateGraph / 状态图", "State persistence / 状态持久化", "Workflow recovery / 工作流恢复", "Production scaling / 生产扩展"],
                "examples": [{"title": "Production StateGraph", "prompt": "from langgraph.checkpoint.memory import MemorySaver\ncheckpointer = MemorySaver()\napp = workflow.compile(checkpointer=checkpointer)", "response": "Compile workflow with checkpointer for persistence"}]
            },
            {
                "title": "节点与边设计 / Node and Edge Design",
                "description": "设计生产级节点和条件边，实现复杂的Agent决策流程。",
                "description_en": "Design production-grade nodes and conditional edges for complex agent decision flows.",
                "importance": 3,
                "key_concepts": ["Conditional edges / 条件边", "Node functions / 节点函数", "Error handling / 错误处理", "Flow control / 流程控制"],
                "examples": [{"title": "Conditional Routing", "prompt": "workflow.add_conditional_edges(\n    'agent',\n    should_continue,\n    {'continue': 'action', 'end': END}\n)", "response": "Add conditional routing based on state"}]
            }
        ],
        "terms": [
            {"term": "StateGraph", "term_cn": "状态图", "definition": "LangGraph中用于管理工作流状态的核心组件", "definition_en": "Core component in LangGraph for managing workflow state"},
            {"term": "Checkpointer", "term_cn": "检查点", "definition": "用于持久化工作流状态的组件", "definition_en": "Component for persisting workflow state"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "StateGraph在生产环境中的主要优势是什么？", "options": ["A. 更快的执行速度", "B. 状态持久化和恢复", "C. 更简单的代码", "D. 更少的内存占用"], "answer": "B", "explanation": "StateGraph支持状态持久化和恢复，适合生产环境。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "条件边可以根据状态决定工作流的下一步。", "answer": "正确", "explanation": "条件边允许根据当前状态动态决定工作流路径。", "difficulty": 1}
        ]
    },
    "a2a_tutorial.ipynb": {
        "title": "Agent-to-Agent 通信协议 / Agent-to-Agent Communication Protocol",
        "summary": "Learn A2A protocol for enabling seamless communication between AI agents. / 学习A2A协议实现AI Agent之间的无缝通信。",
        "knowledge_points": [
            {
                "title": "A2A 协议架构 / A2A Protocol Architecture",
                "description": "A2A协议定义了Agent之间通信的标准格式，包括消息结构、路由和发现机制。",
                "description_en": "A2A protocol defines standard formats for inter-agent communication, including message structure, routing, and discovery mechanisms.",
                "importance": 3,
                "key_concepts": ["Agent discovery / Agent发现", "Message routing / 消息路由", "Protocol standards / 协议标准", "Interoperability / 互操作性"],
                "examples": [{"title": "A2A Message", "prompt": "message = A2AMessage(\n    sender='agent_a',\n    receiver='agent_b',\n    content={'task': 'analyze', 'data': payload}\n)", "response": "Create A2A protocol message"}]
            }
        ],
        "terms": [
            {"term": "A2A Protocol", "term_cn": "Agent-to-Agent协议", "definition": "Agent之间通信的标准协议", "definition_en": "Standard protocol for communication between agents"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "A2A协议的主要目的是什么？", "options": ["A. 加密通信", "B. Agent间标准化通信", "C. 数据存储", "D. 用户界面"], "answer": "B", "explanation": "A2A协议定义了Agent之间通信的标准格式。", "difficulty": 1}
        ]
    },
    "agent_memory_tutorial.ipynb": {
        "title": "Redis 记忆系统 / Redis Memory System",
        "summary": "Build production-ready memory systems for AI agents using Redis with short-term and long-term memory. / 使用Redis构建生产级AI Agent记忆系统，包括短期和长期记忆。",
        "knowledge_points": [
            {
                "title": "双记忆架构 / Dual-Memory Architecture",
                "description": "短期记忆管理对话上下文，长期记忆使用RedisVL进行语义搜索存储持久知识。",
                "description_en": "Short-term memory manages conversation context, long-term memory uses RedisVL for semantic search storage of persistent knowledge.",
                "importance": 3,
                "key_concepts": ["Short-term memory / 短期记忆", "Long-term memory / 长期记忆", "RedisVL / Redis向量库", "Semantic search / 语义搜索"],
                "examples": [{"title": "Memory Types", "prompt": "class MemoryType(str, Enum):\n    EPISODIC = 'episodic'  # User experiences\n    SEMANTIC = 'semantic'   # General knowledge", "response": "Define memory types for agent"}]
            },
            {
                "title": "Redis 检查点 / Redis Checkpointer",
                "description": "使用RedisSaver实现LangGraph工作流的状态持久化。",
                "description_en": "Use RedisSaver to implement state persistence for LangGraph workflows.",
                "importance": 3,
                "key_concepts": ["RedisSaver / Redis保存器", "State persistence / 状态持久化", "Thread management / 线程管理", "Session recovery / 会话恢复"],
                "examples": [{"title": "Redis Checkpointer", "prompt": "from langgraph.checkpoint.redis import RedisSaver\nredis_saver = RedisSaver(redis_client=redis_client)\nredis_saver.setup()", "response": "Setup Redis checkpointer for state persistence"}]
            },
            {
                "title": "向量记忆存储 / Vector Memory Storage",
                "description": "使用RedisVL创建向量索引，实现记忆的语义搜索和去重。",
                "description_en": "Use RedisVL to create vector indexes for semantic search and deduplication of memories.",
                "importance": 2,
                "key_concepts": ["Vector index / 向量索引", "Embedding storage / 嵌入存储", "Deduplication / 去重", "Similarity search / 相似性搜索"],
                "examples": [{"title": "Memory Index", "prompt": "memory_schema = IndexSchema.from_dict({\n    'index': {'name': 'agent_memories'},\n    'fields': [{'name': 'embedding', 'type': 'vector', 'attrs': {'dims': 1536}}]\n})", "response": "Create memory vector index schema"}]
            }
        ],
        "terms": [
            {"term": "RedisVL", "term_cn": "Redis向量库", "definition": "Redis的向量搜索库，用于语义搜索", "definition_en": "Redis vector library for semantic search"},
            {"term": "Episodic Memory", "term_cn": "情景记忆", "definition": "存储用户特定经历和偏好的记忆", "definition_en": "Memory storing user-specific experiences and preferences"},
            {"term": "Semantic Memory", "term_cn": "语义记忆", "definition": "存储通用知识和事实的记忆", "definition_en": "Memory storing general knowledge and facts"}
        ],
        "questions": [
            {"kp_index": 0, "type": "multiple_choice", "question": "Agent记忆系统包括哪些类型？", "options": ["A. 短期记忆", "B. 长期记忆", "C. 临时记忆", "D. 缓存记忆"], "answer": "A,B", "explanation": "Agent记忆系统包括短期记忆和长期记忆。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "RedisSaver用于持久化LangGraph工作流状态。", "answer": "正确", "explanation": "RedisSaver是LangGraph的检查点保存器，用于状态持久化。", "difficulty": 1},
            {"kp_index": 2, "type": "single_choice", "question": "向量记忆存储的主要优势是什么？", "options": ["A. 更快的写入速度", "B. 语义搜索能力", "C. 更小的存储空间", "D. 更简单的查询"], "answer": "B", "explanation": "向量存储支持语义搜索，可以找到相似的记忆。", "difficulty": 1}
        ]
    },
    "mcp-tutorial.ipynb": {
        "title": "MCP 生产集成 / MCP Production Integration",
        "summary": "Implement MCP protocol for production AI agents with custom servers and tool discovery. / 实现MCP协议用于生产AI Agent，包括自定义服务器和工具发现。",
        "knowledge_points": [
            {
                "title": "MCP 服务器开发 / MCP Server Development",
                "description": "开发自定义MCP服务器，使用@mcp.tool装饰器暴露Agent工具。",
                "description_en": "Develop custom MCP servers using @mcp.tool decorator to expose agent tools.",
                "importance": 3,
                "key_concepts": ["@mcp.tool decorator / 工具装饰器", "Server configuration / 服务器配置", "Tool exposure / 工具暴露", "JSON-RPC 2.0"],
                "examples": [{"title": "MCP Tool", "prompt": "@mcp.tool()\nasync def get_crypto_price(crypto_id: str) -> str:\n    return f'Price of {crypto_id}'", "response": "Define MCP tool with decorator"}]
            },
            {
                "title": "工具发现与执行 / Tool Discovery & Execution",
                "description": "实现动态工具发现，Agent可以自动发现和使用MCP服务器提供的工具。",
                "description_en": "Implement dynamic tool discovery where agents can automatically discover and use tools provided by MCP servers.",
                "importance": 3,
                "key_concepts": ["Tool discovery / 工具发现", "Dynamic execution / 动态执行", "Stdio connection / 标准输入输出连接", "Session management / 会话管理"],
                "examples": [{"title": "Tool Discovery", "prompt": "async with ClientSession(read, write) as session:\n    await session.initialize()\n    tools = await session.list_tools()", "response": "Discover available MCP tools"}]
            }
        ],
        "terms": [
            {"term": "MCP Server", "term_cn": "MCP服务器", "definition": "通过MCP协议暴露能力的轻量级程序", "definition_en": "Lightweight program exposing capabilities via MCP protocol"},
            {"term": "Tool Discovery", "term_cn": "工具发现", "definition": "动态发现可用工具的过程", "definition_en": "Process of dynamically discovering available tools"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "MCP服务器使用什么装饰器暴露工具？", "options": ["A. @tool", "B. @mcp.tool", "C. @expose", "D. @api"], "answer": "B", "explanation": "MCP服务器使用@mcp.tool装饰器暴露工具。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "MCP支持动态工具发现。", "answer": "正确", "explanation": "MCP支持动态工具发现，Agent可以自动发现可用工具。", "difficulty": 1}
        ]
    },
    "fastapi-agent-tutorial.ipynb": {
        "title": "FastAPI Agent 部署 / FastAPI Agent Deployment",
        "summary": "Deploy AI agents as production APIs using FastAPI with synchronous and streaming endpoints. / 使用FastAPI将AI Agent部署为生产API，包括同步和流式端点。",
        "knowledge_points": [
            {
                "title": "FastAPI Agent 服务 / FastAPI Agent Service",
                "description": "使用FastAPI创建Agent API服务，支持Pydantic模型验证和自动文档生成。",
                "description_en": "Create agent API services using FastAPI with Pydantic model validation and automatic documentation generation.",
                "importance": 3,
                "key_concepts": ["FastAPI / FastAPI框架", "Pydantic models / Pydantic模型", "Auto documentation / 自动文档", "Type validation / 类型验证"],
                "examples": [{"title": "FastAPI Endpoint", "prompt": "@app.post('/agent', response_model=QueryResponse)\ndef query_agent(request: QueryRequest):\n    return QueryResponse(response=agent.generate_response(request.query))", "response": "Create FastAPI agent endpoint"}]
            },
            {
                "title": "流式响应 / Streaming Responses",
                "description": "使用Server-Sent Events (SSE)实现Agent响应的流式传输。",
                "description_en": "Implement streaming transmission of agent responses using Server-Sent Events (SSE).",
                "importance": 3,
                "key_concepts": ["SSE / 服务器发送事件", "StreamingResponse / 流式响应", "Token streaming / Token流式传输", "EventSourceResponse / 事件源响应"],
                "examples": [{"title": "Streaming Endpoint", "prompt": "@app.post('/agent/stream')\nasync def stream_agent(request: QueryRequest):\n    return StreamingResponse(event_generator(), media_type='text/event-stream')", "response": "Create streaming agent endpoint"}]
            },
            {
                "title": "API 认证 / API Authentication",
                "description": "为Agent API添加API Key认证和请求验证。",
                "description_en": "Add API Key authentication and request validation for agent APIs.",
                "importance": 2,
                "key_concepts": ["API Key / API密钥", "Header validation / 请求头验证", "Dependency injection / 依赖注入", "Error handling / 错误处理"],
                "examples": [{"title": "API Key Auth", "prompt": "async def verify_api_key(x_api_key: str = Header(None)):\n    if x_api_key != os.environ.get('API_KEY'):\n        raise HTTPException(status_code=403)", "response": "Verify API key in request header"}]
            }
        ],
        "terms": [
            {"term": "FastAPI", "term_cn": "FastAPI框架", "definition": "现代高性能Python Web框架", "definition_en": "Modern high-performance Python web framework"},
            {"term": "SSE", "term_cn": "服务器发送事件", "definition": "服务器向客户端推送实时数据的技术", "definition_en": "Technology for server to push real-time data to client"},
            {"term": "Pydantic", "term_cn": "Pydantic库", "definition": "Python数据验证库，使用类型注解", "definition_en": "Python data validation library using type annotations"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "FastAPI的主要优势是什么？", "options": ["A. 自动文档生成", "B. 类型验证", "C. 高性能异步", "D. 以上都是"], "answer": "D", "explanation": "FastAPI具有自动文档、类型验证和高性能异步等优势。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "SSE用于实现Agent响应的流式传输。", "answer": "正确", "explanation": "Server-Sent Events用于实现流式响应传输。", "difficulty": 1},
            {"kp_index": 2, "type": "single_choice", "question": "API Key通常放在哪个请求头中？", "options": ["A. Authorization", "B. X-API-Key", "C. Content-Type", "D. Accept"], "answer": "B", "explanation": "API Key通常放在X-API-Key请求头中。", "difficulty": 1}
        ]
    },
    "langsmith_basics.ipynb": {
        "title": "LangSmith 追踪基础 / LangSmith Tracing Basics",
        "summary": "Learn LangSmith for tracing, debugging, and monitoring AI agent applications. / 学习LangSmith用于追踪、调试和监控AI Agent应用。",
        "knowledge_points": [
            {
                "title": "追踪与监控 / Tracing & Monitoring",
                "description": "使用LangSmith追踪Agent执行流程，监控性能和调试问题。",
                "description_en": "Use LangSmith to trace agent execution flow, monitor performance, and debug issues.",
                "importance": 3,
                "key_concepts": ["Trace / 追踪", "Span / 跨度", "Run tree / 运行树", "Performance monitoring / 性能监控"],
                "examples": [{"title": "LangSmith Setup", "prompt": "os.environ['LANGSMITH_TRACING'] = 'true'\nos.environ['LANGSMITH_API_KEY'] = 'your_key'", "response": "Enable LangSmith tracing"}]
            }
        ],
        "terms": [
            {"term": "LangSmith", "term_cn": "LangSmith平台", "definition": "LangChain的追踪和监控平台", "definition_en": "LangChain's tracing and monitoring platform"},
            {"term": "Trace", "term_cn": "追踪", "definition": "记录Agent执行过程的完整路径", "definition_en": "Complete path recording of agent execution process"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "LangSmith可以用于追踪Agent执行流程。", "answer": "正确", "explanation": "LangSmith提供完整的追踪和监控功能。", "difficulty": 1}
        ]
    },
    "ollama_tutorial.ipynb": {
        "title": "Ollama 本地部署 / Ollama Local Deployment",
        "summary": "Deploy AI agents locally using Ollama for on-premises LLM inference. / 使用Ollama本地部署AI Agent进行本地LLM推理。",
        "knowledge_points": [
            {
                "title": "Ollama 本地推理 / Ollama Local Inference",
                "description": "使用Ollama在本地运行开源LLM，实现数据隐私和成本控制。",
                "description_en": "Use Ollama to run open-source LLMs locally for data privacy and cost control.",
                "importance": 3,
                "key_concepts": ["Local inference / 本地推理", "Model management / 模型管理", "Privacy control / 隐私控制", "Cost optimization / 成本优化"],
                "examples": [{"title": "Ollama Usage", "prompt": "from langchain_ollama import ChatOllama\nllm = ChatOllama(model='llama3.2')\nresponse = llm.invoke('Hello!')", "response": "Use Ollama for local LLM inference"}]
            }
        ],
        "terms": [
            {"term": "Ollama", "term_cn": "Ollama工具", "definition": "本地运行开源LLM的工具", "definition_en": "Tool for running open-source LLMs locally"},
            {"term": "On-premises", "term_cn": "本地部署", "definition": "在本地服务器运行而非云端", "definition_en": "Running on local servers instead of cloud"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "Ollama的主要优势是什么？", "options": ["A. 更快的响应", "B. 数据隐私和成本控制", "C. 更好的模型", "D. 更简单的API"], "answer": "B", "explanation": "Ollama允许本地运行模型，保护数据隐私并控制成本。", "difficulty": 1}
        ]
    },
    "web-agent-tutorial.ipynb": {
        "title": "Web Agent 教程 / Web Agent Tutorial",
        "summary": "Build agents that can search and interact with the web using Tavily API. / 构建能够使用Tavily API搜索和交互网络的Agent。",
        "knowledge_points": [
            {
                "title": "Web 搜索集成 / Web Search Integration",
                "description": "使用Tavily API集成网络搜索能力，让Agent获取实时信息。",
                "description_en": "Use Tavily API to integrate web search capabilities for agents to get real-time information.",
                "importance": 3,
                "key_concepts": ["Tavily API / Tavily接口", "Web search / 网络搜索", "Real-time data / 实时数据", "Search tools / 搜索工具"],
                "examples": [{"title": "Tavily Search", "prompt": "from langchain_tavily import TavilySearch\ntool = TavilySearch(max_results=5)\nresults = tool.invoke('latest AI news')", "response": "Use Tavily for web search"}]
            }
        ],
        "terms": [
            {"term": "Tavily", "term_cn": "Tavily搜索", "definition": "专为AI Agent设计的搜索API", "definition_en": "Search API designed for AI agents"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "Tavily API专为AI Agent设计。", "answer": "正确", "explanation": "Tavily是专为AI Agent优化的搜索API。", "difficulty": 1}
        ]
    },
    "building-chatbot-notebook.ipynb": {
        "title": "Streamlit 聊天机器人 / Streamlit Chatbot",
        "summary": "Build interactive chatbot UIs using Streamlit for AI agents. / 使用Streamlit为AI Agent构建交互式聊天机器人UI。",
        "knowledge_points": [
            {
                "title": "Streamlit UI 开发 / Streamlit UI Development",
                "description": "使用Streamlit快速构建Agent聊天界面，支持消息历史和会话管理。",
                "description_en": "Use Streamlit to quickly build agent chat interfaces with message history and session management.",
                "importance": 2,
                "key_concepts": ["Streamlit / Streamlit框架", "Chat interface / 聊天界面", "Session state / 会话状态", "Message history / 消息历史"],
                "examples": [{"title": "Streamlit Chat", "prompt": "import streamlit as st\nst.chat_message('user').write(prompt)\nst.chat_message('assistant').write(response)", "response": "Create chat interface with Streamlit"}]
            }
        ],
        "terms": [
            {"term": "Streamlit", "term_cn": "Streamlit框架", "definition": "Python快速Web应用开发框架", "definition_en": "Python framework for rapid web app development"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "Streamlit的主要用途是什么？", "options": ["A. 数据分析", "B. 快速构建Web UI", "C. 机器学习", "D. 数据库管理"], "answer": "B", "explanation": "Streamlit用于快速构建Web应用界面。", "difficulty": 1}
        ]
    },
    "intellagent-evaluation-tutorial.ipynb": {
        "title": "IntellAgent 评估 / IntellAgent Evaluation",
        "summary": "Evaluate AI agent performance using IntellAgent framework. / 使用IntellAgent框架评估AI Agent性能。",
        "knowledge_points": [
            {
                "title": "Agent 性能评估 / Agent Performance Evaluation",
                "description": "使用IntellAgent评估Agent的准确性、响应时间和任务完成率。",
                "description_en": "Use IntellAgent to evaluate agent accuracy, response time, and task completion rate.",
                "importance": 2,
                "key_concepts": ["Performance metrics / 性能指标", "Evaluation framework / 评估框架", "Benchmarking / 基准测试", "Quality assurance / 质量保证"],
                "examples": [{"title": "Agent Evaluation", "prompt": "from intellagent import evaluate\nresults = evaluate(agent, test_cases)\nprint(results.accuracy, results.latency)", "response": "Evaluate agent performance"}]
            }
        ],
        "terms": [
            {"term": "IntellAgent", "term_cn": "IntellAgent框架", "definition": "AI Agent性能评估框架", "definition_en": "AI agent performance evaluation framework"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "IntellAgent可以评估Agent的准确性和响应时间。", "answer": "正确", "explanation": "IntellAgent提供多种性能指标评估。", "difficulty": 1}
        ]
    },
    "fine_tuning_agents_guide.ipynb": {
        "title": "Agent 微调指南 / Agent Fine-tuning Guide",
        "summary": "Learn techniques for fine-tuning AI agents for specific tasks. / 学习针对特定任务微调AI Agent的技术。",
        "knowledge_points": [
            {
                "title": "Agent 微调技术 / Agent Fine-tuning Techniques",
                "description": "使用任务特定数据微调Agent模型，提高特定领域的性能。",
                "description_en": "Fine-tune agent models using task-specific data to improve performance in specific domains.",
                "importance": 3,
                "key_concepts": ["Fine-tuning / 微调", "Domain adaptation / 领域适应", "Task-specific data / 任务特定数据", "Model customization / 模型定制"],
                "examples": [{"title": "Fine-tuning Setup", "prompt": "from openai import OpenAI\nclient.fine_tuning.jobs.create(\n    training_file='train.jsonl',\n    model='gpt-4o-mini'\n)", "response": "Create fine-tuning job"}]
            }
        ],
        "terms": [
            {"term": "Fine-tuning", "term_cn": "微调", "definition": "使用特定数据调整预训练模型", "definition_en": "Adjusting pre-trained models with specific data"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "微调的主要目的是什么？", "options": ["A. 减少模型大小", "B. 提高特定任务性能", "C. 加快推理速度", "D. 减少训练时间"], "answer": "B", "explanation": "微调用于提高模型在特定任务或领域的性能。", "difficulty": 1}
        ]
    },
    "agent-security-evaluation-tutorial.ipynb": {
        "title": "Agent 安全评估 / Agent Security Evaluation",
        "summary": "Evaluate and secure AI agents against potential vulnerabilities. / 评估和保护AI Agent免受潜在漏洞影响。",
        "knowledge_points": [
            {
                "title": "安全漏洞评估 / Security Vulnerability Assessment",
                "description": "识别和评估Agent的安全漏洞，包括提示注入和数据泄露风险。",
                "description_en": "Identify and assess agent security vulnerabilities including prompt injection and data leakage risks.",
                "importance": 3,
                "key_concepts": ["Prompt injection / 提示注入", "Data leakage / 数据泄露", "Security testing / 安全测试", "Vulnerability assessment / 漏洞评估"],
                "examples": [{"title": "Security Test", "prompt": "security_report = evaluate_security(agent)\nprint(security_report.vulnerabilities)", "response": "Run security evaluation on agent"}]
            }
        ],
        "terms": [
            {"term": "Prompt Injection", "term_cn": "提示注入", "definition": "恶意输入试图操纵Agent行为", "definition_en": "Malicious input attempting to manipulate agent behavior"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "提示注入是Agent安全的主要威胁之一。", "answer": "正确", "explanation": "提示注入是Agent面临的主要安全威胁。", "difficulty": 1}
        ]
    },
    "hello-llama.ipynb": {
        "title": "Llama Firewall 入门 / Llama Firewall Introduction",
        "summary": "Get started with Llama Firewall for agent security. / 开始使用Llama Firewall保护Agent安全。",
        "knowledge_points": [
            {
                "title": "Llama Firewall 基础 / Llama Firewall Basics",
                "description": "使用Llama Firewall构建Agent安全防护层，过滤恶意输入。",
                "description_en": "Use Llama Firewall to build agent security layers and filter malicious inputs.",
                "importance": 3,
                "key_concepts": ["Firewall / 防火墙", "Input filtering / 输入过滤", "Security layer / 安全层", "Threat detection / 威胁检测"],
                "examples": [{"title": "Llama Firewall", "prompt": "from llamafirewall import Firewall\nfirewall = Firewall()\nif firewall.is_safe(user_input):\n    agent.process(user_input)", "response": "Check input safety with Llama Firewall"}]
            }
        ],
        "terms": [
            {"term": "Llama Firewall", "term_cn": "Llama防火墙", "definition": "Agent安全防护框架", "definition_en": "Agent security protection framework"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "Llama Firewall的主要功能是什么？", "options": ["A. 加速推理", "B. 安全防护和输入过滤", "C. 数据存储", "D. 模型训练"], "answer": "B", "explanation": "Llama Firewall用于Agent安全防护和输入过滤。", "difficulty": 1}
        ]
    },
    "input-guardrail.ipynb": {
        "title": "输入护栏 / Input Guardrails",
        "summary": "Implement input guardrails to protect AI agents from malicious inputs. / 实现输入护栏保护AI Agent免受恶意输入。",
        "knowledge_points": [
            {
                "title": "输入护栏实现 / Input Guardrail Implementation",
                "description": "实现输入护栏检测和阻止恶意提示、注入攻击和不当内容。",
                "description_en": "Implement input guardrails to detect and block malicious prompts, injection attacks, and inappropriate content.",
                "importance": 3,
                "key_concepts": ["Input validation / 输入验证", "Content filtering / 内容过滤", "Attack prevention / 攻击预防", "Safety checks / 安全检查"],
                "examples": [{"title": "Input Guardrail", "prompt": "@guardrail\ndef check_input(user_input):\n    if contains_injection(user_input):\n        raise SecurityError('Potential injection detected')", "response": "Implement input guardrail"}]
            }
        ],
        "terms": [
            {"term": "Guardrail", "term_cn": "护栏", "definition": "保护Agent免受恶意输入的机制", "definition_en": "Mechanism protecting agents from malicious inputs"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "输入护栏可以检测提示注入攻击。", "answer": "正确", "explanation": "输入护栏用于检测和阻止各种恶意输入。", "difficulty": 1}
        ]
    },
    "output-guardrail.ipynb": {
        "title": "输出护栏 / Output Guardrails",
        "summary": "Implement output guardrails to ensure safe and appropriate agent responses. / 实现输出护栏确保Agent响应安全适当。",
        "knowledge_points": [
            {
                "title": "输出护栏实现 / Output Guardrail Implementation",
                "description": "实现输出护栏过滤敏感信息、不当内容和潜在有害响应。",
                "description_en": "Implement output guardrails to filter sensitive information, inappropriate content, and potentially harmful responses.",
                "importance": 3,
                "key_concepts": ["Output filtering / 输出过滤", "Content moderation / 内容审核", "PII protection / 个人信息保护", "Response validation / 响应验证"],
                "examples": [{"title": "Output Guardrail", "prompt": "@output_guardrail\ndef check_output(response):\n    if contains_pii(response):\n        return redact_pii(response)\n    return response", "response": "Implement output guardrail for PII protection"}]
            }
        ],
        "terms": [
            {"term": "PII", "term_cn": "个人身份信息", "definition": "需要保护的敏感个人信息", "definition_en": "Sensitive personal information requiring protection"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "输出护栏的主要目的是什么？", "options": ["A. 加快响应速度", "B. 确保响应安全和适当", "C. 减少响应长度", "D. 增加响应多样性"], "answer": "B", "explanation": "输出护栏确保Agent响应安全适当。", "difficulty": 1}
        ]
    },
    "tools-security.ipynb": {
        "title": "工具安全 / Tools Security",
        "summary": "Secure agent tools and prevent unauthorized access. / 保护Agent工具并防止未授权访问。",
        "knowledge_points": [
            {
                "title": "工具安全配置 / Tool Security Configuration",
                "description": "配置工具访问权限、参数验证和执行限制，防止工具滥用。",
                "description_en": "Configure tool access permissions, parameter validation, and execution limits to prevent tool abuse.",
                "importance": 3,
                "key_concepts": ["Access control / 访问控制", "Parameter validation / 参数验证", "Execution limits / 执行限制", "Tool permissions / 工具权限"],
                "examples": [{"title": "Tool Security", "prompt": "@secure_tool(permissions=['read'], rate_limit=10)\ndef safe_query(query: str) -> str:\n    return database.query(query)", "response": "Configure secure tool with permissions"}]
            }
        ],
        "terms": [
            {"term": "Tool Security", "term_cn": "工具安全", "definition": "保护Agent工具免受滥用的措施", "definition_en": "Measures protecting agent tools from abuse"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "工具安全配置可以防止工具滥用。", "answer": "正确", "explanation": "工具安全配置包括访问控制和执行限制。", "difficulty": 1}
        ]
    },
    "agent-observability-with-qualifire.ipynb": {
        "title": "Qualifire 可观测性 / Qualifire Observability",
        "summary": "Implement observability for AI agents using Qualifire platform. / 使用Qualifire平台实现AI Agent可观测性。",
        "knowledge_points": [
            {
                "title": "Agent 可观测性 / Agent Observability",
                "description": "使用Qualifire监控Agent行为、性能指标和异常检测。",
                "description_en": "Use Qualifire to monitor agent behavior, performance metrics, and anomaly detection.",
                "importance": 2,
                "key_concepts": ["Observability / 可观测性", "Metrics / 指标", "Anomaly detection / 异常检测", "Monitoring / 监控"],
                "examples": [{"title": "Qualifire Setup", "prompt": "from qualifire import Qualifire\nqf = Qualifire(api_key='your_key')\nqf.monitor(agent)", "response": "Setup Qualifire monitoring for agent"}]
            }
        ],
        "terms": [
            {"term": "Observability", "term_cn": "可观测性", "definition": "系统内部状态的可观察能力", "definition_en": "Ability to observe internal system state"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "可观测性的主要目的是什么？", "options": ["A. 加快执行速度", "B. 监控和诊断系统行为", "C. 减少内存使用", "D. 简化代码"], "answer": "B", "explanation": "可观测性用于监控和诊断系统行为。", "difficulty": 1}
        ]
    },
    "hybrid-agent-tutorial.ipynb": {
        "title": "混合 Agent 教程 / Hybrid Agent Tutorial",
        "summary": "Build hybrid agents combining local and cloud capabilities. / 构建结合本地和云端能力的混合Agent。",
        "knowledge_points": [
            {
                "title": "混合 Agent 架构 / Hybrid Agent Architecture",
                "description": "结合本地LLM和云端API的优势，实现成本和性能的平衡。",
                "description_en": "Combine advantages of local LLMs and cloud APIs to balance cost and performance.",
                "importance": 2,
                "key_concepts": ["Hybrid architecture / 混合架构", "Local LLM / 本地LLM", "Cloud API / 云端API", "Cost optimization / 成本优化"],
                "examples": [{"title": "Hybrid Agent", "prompt": "class HybridAgent:\n    def __init__(self):\n        self.local_llm = OllamaLLM(model='llama3')\n        self.cloud_llm = ChatOpenAI(model='gpt-4o')", "response": "Create hybrid agent with local and cloud LLMs"}]
            }
        ],
        "terms": [
            {"term": "Hybrid Agent", "term_cn": "混合Agent", "definition": "结合本地和云端能力的Agent", "definition_en": "Agent combining local and cloud capabilities"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "混合Agent可以平衡成本和性能。", "answer": "正确", "explanation": "混合Agent结合本地和云端优势，优化成本和性能。", "difficulty": 1}
        ]
    },
    "search-extract-crawl.ipynb": {
        "title": "搜索提取爬取 / Search Extract Crawl",
        "summary": "Build agents that can search, extract, and crawl web content. / 构建能够搜索、提取和爬取网页内容的Agent。",
        "knowledge_points": [
            {
                "title": "Web 内容提取 / Web Content Extraction",
                "description": "实现网页搜索、内容提取和爬虫功能，获取结构化数据。",
                "description_en": "Implement web search, content extraction, and crawling to obtain structured data.",
                "importance": 2,
                "key_concepts": ["Web crawling / 网页爬取", "Content extraction / 内容提取", "Data scraping / 数据抓取", "Structured data / 结构化数据"],
                "examples": [{"title": "Web Extraction", "prompt": "from tavily import TavilyClient\nclient = TavilyClient()\nresults = client.extract('https://example.com')", "response": "Extract content from web page"}]
            }
        ],
        "terms": [
            {"term": "Web Crawling", "term_cn": "网页爬取", "definition": "自动浏览和提取网页内容", "definition_en": "Automatically browsing and extracting web content"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "Web内容提取的主要目的是什么？", "options": ["A. 加快网页加载", "B. 获取结构化数据", "C. 提高SEO排名", "D. 减少带宽使用"], "answer": "B", "explanation": "Web内容提取用于从网页获取结构化数据。", "difficulty": 1}
        ]
    },
    "vectorize_tutorial.ipynb": {
        "title": "向量化教程 / Vectorize Tutorial",
        "summary": "Learn vectorization techniques for AI agent applications. / 学习AI Agent应用的向量化技术。",
        "knowledge_points": [
            {
                "title": "向量化处理 / Vectorization Processing",
                "description": "将文本和数据进行向量化处理，支持语义搜索和相似性匹配。",
                "description_en": "Vectorize text and data to support semantic search and similarity matching.",
                "importance": 2,
                "key_concepts": ["Embedding / 嵌入", "Vector storage / 向量存储", "Semantic search / 语义搜索", "Similarity matching / 相似性匹配"],
                "examples": [{"title": "Vectorization", "prompt": "from openai import OpenAI\nclient = OpenAI()\nembedding = client.embeddings.create(input=text, model='text-embedding-ada-002')", "response": "Create text embedding for vectorization"}]
            }
        ],
        "terms": [
            {"term": "Embedding", "term_cn": "嵌入", "definition": "将文本转换为向量表示", "definition_en": "Converting text to vector representation"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "向量化支持语义搜索功能。", "answer": "正确", "explanation": "向量化将文本转换为向量，支持语义搜索。", "difficulty": 1}
        ]
    },
    "basic_usage.ipynb": {
        "title": "Ollama 基础用法 / Ollama Basic Usage",
        "summary": "Learn basic usage of Ollama for local LLM inference. / 学习Ollama本地LLM推理的基础用法。",
        "knowledge_points": [
            {
                "title": "Ollama 基础操作 / Ollama Basic Operations",
                "description": "学习Ollama的模型拉取、运行和管理基础操作。",
                "description_en": "Learn basic operations for pulling, running, and managing models with Ollama.",
                "importance": 2,
                "key_concepts": ["Model pulling / 模型拉取", "Model running / 模型运行", "Model management / 模型管理", "Local inference / 本地推理"],
                "examples": [{"title": "Ollama Basic", "prompt": "# Pull model\nollama pull llama3.2\n# Run model\nollama run llama3.2", "response": "Basic Ollama model operations"}]
            }
        ],
        "terms": [
            {"term": "Model Pulling", "term_cn": "模型拉取", "definition": "下载模型到本地", "definition_en": "Downloading model to local machine"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "Ollama模型拉取命令是什么？", "options": ["A. ollama download", "B. ollama pull", "C. ollama get", "D. ollama fetch"], "answer": "B", "explanation": "使用ollama pull命令下载模型。", "difficulty": 1}
        ]
    },
    "langchain_agent.ipynb": {
        "title": "LangChain + Ollama Agent / LangChain + Ollama Agent",
        "summary": "Build agents using LangChain with Ollama for local inference. / 使用LangChain和Ollama构建本地推理Agent。",
        "knowledge_points": [
            {
                "title": "LangChain Ollama 集成 / LangChain Ollama Integration",
                "description": "集成LangChain和Ollama，构建使用本地LLM的Agent。",
                "description_en": "Integrate LangChain with Ollama to build agents using local LLMs.",
                "importance": 3,
                "key_concepts": ["LangChain integration / LangChain集成", "Local LLM / 本地LLM", "Agent creation / Agent创建", "Tool binding / 工具绑定"],
                "examples": [{"title": "LangChain Ollama", "prompt": "from langchain_ollama import ChatOllama\nfrom langchain.agents import create_react_agent\nllm = ChatOllama(model='llama3.2')\nagent = create_react_agent(llm, tools, prompt)", "response": "Create LangChain agent with Ollama"}]
            }
        ],
        "terms": [
            {"term": "ChatOllama", "term_cn": "ChatOllama类", "definition": "LangChain的Ollama集成类", "definition_en": "LangChain's Ollama integration class"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "LangChain可以与Ollama集成使用本地LLM。", "answer": "正确", "explanation": "LangChain通过ChatOllama类支持Ollama集成。", "difficulty": 1}
        ]
    },
    "creating_multi_step_ai_agents_with_xpander_tutorial.ipynb": {
        "title": "多步骤 Agent 教程 / Multi-Step Agent Tutorial",
        "summary": "Build multi-step AI agents using xpander.ai platform. / 使用xpander.ai平台构建多步骤AI Agent。",
        "knowledge_points": [
            {
                "title": "多步骤 Agent 设计 / Multi-Step Agent Design",
                "description": "设计能够执行复杂多步骤任务的Agent工作流。",
                "description_en": "Design agent workflows capable of executing complex multi-step tasks.",
                "importance": 2,
                "key_concepts": ["Multi-step workflow / 多步骤工作流", "Task decomposition / 任务分解", "State management / 状态管理", "Sequential execution / 顺序执行"],
                "examples": [{"title": "Multi-Step Agent", "prompt": "class MultiStepAgent:\n    def execute(self, task):\n        steps = self.decompose(task)\n        for step in steps:\n            result = self.execute_step(step)\n            self.update_state(result)", "response": "Design multi-step agent workflow"}]
            }
        ],
        "terms": [
            {"term": "Task Decomposition", "term_cn": "任务分解", "definition": "将复杂任务分解为多个子任务", "definition_en": "Breaking complex tasks into subtasks"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "多步骤Agent的主要特点是什么？", "options": ["A. 更快的执行", "B. 执行复杂多步骤任务", "C. 更少的内存使用", "D. 更简单的代码"], "answer": "B", "explanation": "多步骤Agent能够执行复杂的多步骤任务。", "difficulty": 1}
        ]
    }
}

def create_course_material(notebook_name: str, course_data: dict) -> str:
    content = f"""# {course_data['title']}

## Overview / 概述

{course_data['summary']}

## Key Knowledge Points / 核心知识点

"""
    for i, kp in enumerate(course_data['knowledge_points'], 1):
        content += f"""### {i}. {kp['title']}

**English:** {kp['description_en']}

**中文:** {kp['description']}

**Key Concepts / 核心概念:**
"""
        for concept in kp['key_concepts']:
            content += f"- {concept}\n"
        
        if kp.get('examples'):
            content += "\n**Example / 示例:**\n```python\n"
            for ex in kp['examples']:
                content += f"{ex['prompt']}\n# → {ex['response']}\n\n"
            content += "```\n"
        content += "\n---\n\n"
    
    content += """## Summary / 总结

This lesson covered key production deployment concepts. Practice these techniques to build robust production systems.

本课程涵盖了关键的生产部署技术。练习这些技术以构建健壮的生产系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own production agents / 构建自己的生产Agent
3. Explore advanced patterns / 探索高级模式
"""
    return content

def batch_update_production_courses():
    print("Starting batch update of Production courses...")
    db = SessionLocal()
    
    try:
        prod_module = db.query(Module).filter(Module.name.like('%PROD%')).first()
        if not prod_module:
            prod_module = Module(
                name="PROD 生产落地",
                description="Production deployment and operations for AI agents. / AI Agent的生产部署和运维。"
            )
            db.add(prod_module)
            db.commit()
            print(f"Created module: {prod_module.name}")
        else:
            print(f"Using existing module: {prod_module.name}")
        
        total_lessons = 0
        total_kps = 0
        total_terms = 0
        total_questions = 0
        
        for notebook_name, course_data in PRODUCTION_COURSES_DATA.items():
            print(f"\nProcessing: {notebook_name}")
            
            existing_lesson = db.query(Lesson).filter(Lesson.title == course_data['title']).first()
            if existing_lesson:
                lesson = existing_lesson
                db.query(KnowledgePoint).filter(KnowledgePoint.lesson_id == lesson.id).delete()
                db.query(LessonTerm).filter(LessonTerm.lesson_id == lesson.id).delete()
                print(f"  Updating existing lesson: {lesson.title}")
            else:
                lesson = Lesson(
                    module_id=prod_module.id,
                    title=course_data['title'],
                    date="2024-01-01",
                    topics=[kp['title'].split('/')[0].strip() for kp in course_data['knowledge_points']],
                    difficulty="intermediate",
                    time_estimate=45,
                    summary=course_data['summary'],
                    materials=[]
                )
                db.add(lesson)
                db.flush()
                print(f"  Created new lesson: {lesson.title}")
            
            material_content = create_course_material(notebook_name, course_data)
            material_filename = f"production_{notebook_name.replace('.ipynb', '')}.md"
            material_path = os.path.join(backend_dir, 'course_content', material_filename)
            
            os.makedirs(os.path.dirname(material_path), exist_ok=True)
            with open(material_path, 'w', encoding='utf-8') as f:
                f.write(material_content)
            
            lesson.materials = [{
                'title': course_data['title'],
                'path': material_path.replace('\\', '/'),
                'type': 'markdown'
            }]
            
            kp_map = {}
            for kp_data in course_data['knowledge_points']:
                kp = KnowledgePoint(
                    lesson_id=lesson.id,
                    title=kp_data['title'],
                    description=kp_data['description'],
                    category='production',
                    importance=kp_data.get('importance', 2),
                    key_concepts=kp_data.get('key_concepts', []),
                    examples=kp_data.get('examples', []),
                    common_mistakes=kp_data.get('common_mistakes', []),
                    best_practices=kp_data.get('best_practices', [])
                )
                db.add(kp)
                db.flush()
                kp_map[kp_data['title']] = kp
                total_kps += 1
            print(f"  Added {len(course_data['knowledge_points'])} knowledge points")
            
            for term_data in course_data.get('terms', []):
                existing_term = db.query(Term).filter(Term.term == term_data['term']).first()
                if not existing_term:
                    term = Term(
                        term=term_data['term'],
                        definition=term_data['definition'],
                        category='production',
                        related_terms=[],
                        detailed_definition=term_data.get('definition_en', ''),
                        is_predefined=True
                    )
                    db.add(term)
                    db.flush()
                else:
                    term = existing_term
                
                lesson_term = LessonTerm(
                    lesson_id=lesson.id,
                    term_id=term.id
                )
                db.add(lesson_term)
                total_terms += 1
            print(f"  Added {len(course_data.get('terms', []))} terms")
            
            for q_data in course_data.get('questions', []):
                kp_index = q_data['kp_index']
                if kp_index < len(course_data['knowledge_points']):
                    kp = kp_map[course_data['knowledge_points'][kp_index]['title']]
                    question = PracticeQuestion(
                        knowledge_point_id=kp.id,
                        question_type=q_data['type'],
                        question_text=q_data['question'],
                        options=q_data.get('options', []),
                        correct_answer=q_data['answer'],
                        explanation=q_data.get('explanation', ''),
                        difficulty=q_data.get('difficulty', 1),
                        order_index=total_questions
                    )
                    db.add(question)
                    total_questions += 1
            print(f"  Added {len(course_data.get('questions', []))} questions")
            
            total_lessons += 1
        
        db.commit()
        
        print(f"\n{'='*50}")
        print("Batch update completed!")
        print(f"Total lessons: {total_lessons}")
        print(f"Total knowledge points: {total_kps}")
        print(f"Total terms: {total_terms}")
        print(f"Total practice questions: {total_questions}")
        print(f"{'='*50}")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    batch_update_production_courses()
