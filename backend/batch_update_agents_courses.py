import os
import sys

backend_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, backend_dir)

from app.utils.database import SessionLocal
from app.models.models import Module, Lesson, KnowledgePoint, Term, LessonTerm, PracticeQuestion

AGENTS_COURSES_DATA = {
    "langgraph-tutorial.ipynb": {
        "title": "LangGraph 入门教程 / Introduction to LangGraph",
        "summary": "Learn LangGraph fundamentals including StateGraph, nodes, edges, and workflow visualization. / 学习LangGraph基础，包括StateGraph、节点、边和工作流可视化。",
        "knowledge_points": [
            {
                "title": "StateGraph 工作流 / StateGraph Workflow",
                "description": "LangGraph使用StateGraph创建基于图的工作流，每个节点代表一个函数或计算步骤，边定义节点之间的流程。",
                "description_en": "LangGraph uses StateGraph to create graph-based workflows where each node represents a function or computational step, and edges define the flow between nodes.",
                "importance": 3,
                "key_concepts": ["StateGraph / 状态图", "Nodes / 节点", "Edges / 边", "Workflow / 工作流"],
                "examples": [{"title": "StateGraph Example", "prompt": "workflow = StateGraph(State)\nworkflow.add_node('classification_node', classification_node)\nworkflow.add_edge('classification_node', 'entity_extraction')\napp = workflow.compile()", "response": "Create and compile a LangGraph workflow"}]
            },
            {
                "title": "状态管理 / State Management",
                "description": "使用TypedDict定义状态类，在工作流节点之间传递和更新数据。",
                "description_en": "Use TypedDict to define state classes for passing and updating data between workflow nodes.",
                "importance": 3,
                "key_concepts": ["TypedDict / 类型字典", "State / 状态", "Data flow / 数据流"],
                "examples": [{"title": "State Definition", "prompt": "class State(TypedDict):\n    text: str\n    classification: str\n    entities: List[str]\n    summary: str", "response": "Define workflow state with TypedDict"}]
            }
        ],
        "terms": [
            {"term": "LangGraph", "term_cn": "LangGraph框架", "definition": "用于构建基于图的AI工作流的框架", "definition_en": "Framework for building graph-based AI workflows"},
            {"term": "StateGraph", "term_cn": "状态图", "definition": "LangGraph中用于管理工作流状态的核心组件", "definition_en": "Core component in LangGraph for managing workflow state"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "LangGraph中用于定义节点之间流程的是什么？", "options": ["A. 状态", "B. 边", "C. 节点", "D. 变量"], "answer": "B", "explanation": "在LangGraph中，边(Edges)定义节点之间的流程和条件路由。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "TypedDict可以用于定义LangGraph工作流的状态类。", "answer": "正确", "explanation": "TypedDict用于定义状态类，在工作流节点之间传递和更新数据。", "difficulty": 1}
        ]
    },
    "mcp-tutorial.ipynb": {
        "title": "MCP 模型上下文协议 / Model Context Protocol",
        "summary": "Learn MCP (Model Context Protocol) for standardizing AI model integration with external resources and tools. / 学习MCP协议，标准化AI模型与外部资源和工具的集成。",
        "knowledge_points": [
            {
                "title": "MCP 架构 / MCP Architecture",
                "description": "MCP采用客户端-服务器架构，包含Host（AI应用）、Client（连接器）和Server（能力提供者）三个主要组件。",
                "description_en": "MCP follows a client-server architecture with three main components: Host (AI application), Client (connector), and Server (capability provider).",
                "importance": 3,
                "key_concepts": ["Host / 主机", "Client / 客户端", "Server / 服务器", "JSON-RPC 2.0"],
                "examples": [{"title": "MCP Server", "prompt": "@mcp.tool()\nasync def get_crypto_price(crypto_id: str) -> str:\n    return f'Price of {crypto_id}'", "response": "Define MCP tool with decorator"}]
            },
            {
                "title": "工具发现与执行 / Tool Discovery & Execution",
                "description": "MCP支持动态工具发现，AI可以自动发现和使用服务器提供的工具。",
                "description_en": "MCP supports dynamic tool discovery, allowing AI to automatically discover and use tools provided by servers.",
                "importance": 3,
                "key_concepts": ["Tool discovery / 工具发现", "Dynamic execution / 动态执行", "Stdio connection / 标准输入输出连接"],
                "examples": [{"title": "Tool Discovery", "prompt": "tools = await session.list_tools()\nresult = await session.call_tool(tool_name, arguments)", "response": "Discover and execute MCP tools"}]
            }
        ],
        "terms": [
            {"term": "MCP", "term_cn": "模型上下文协议", "definition": "标准化AI模型与外部系统交互的协议", "definition_en": "Protocol for standardizing AI model interaction with external systems"},
            {"term": "MCP Server", "term_cn": "MCP服务器", "definition": "通过MCP协议暴露能力的轻量级程序", "definition_en": "Lightweight program exposing capabilities via MCP protocol"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "MCP架构中的Host指的是什么？", "options": ["A. MCP服务器", "B. AI应用程序", "C. 数据库", "D. API端点"], "answer": "B", "explanation": "Host是AI应用程序（如Claude Desktop），需要访问外部资源。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "MCP支持动态工具发现。", "answer": "正确", "explanation": "MCP支持动态工具发现，AI可以自动发现和使用服务器提供的工具。", "difficulty": 1}
        ]
    },
    "memory-agent-tutorial.ipynb": {
        "title": "记忆增强Agent / Memory-Enhanced Agent",
        "summary": "Build AI agents with three types of memory: semantic, episodic, and procedural using LangGraph and LangMem. / 构建具有三种记忆类型的AI Agent：语义记忆、情景记忆和程序记忆。",
        "knowledge_points": [
            {
                "title": "三种记忆类型 / Three Memory Types",
                "description": "语义记忆存储事实知识，情景记忆记住特定交互，程序记忆学习和改进行为模式。",
                "description_en": "Semantic memory stores facts and knowledge, episodic memory remembers specific interactions, procedural memory learns and improves behavioral patterns.",
                "importance": 3,
                "key_concepts": ["Semantic Memory / 语义记忆", "Episodic Memory / 情景记忆", "Procedural Memory / 程序记忆"],
                "examples": [{"title": "Memory Types", "prompt": "# Semantic: store facts about contacts\n# Episodic: remember past email examples\n# Procedural: improve prompts based on feedback", "response": "Three types of agent memory"}]
            },
            {
                "title": "LangMem 工具 / LangMem Tools",
                "description": "使用create_manage_memory_tool和create_search_memory_tool管理Agent记忆。",
                "description_en": "Use create_manage_memory_tool and create_search_memory_tool to manage agent memory.",
                "importance": 2,
                "key_concepts": ["manage_memory / 管理记忆", "search_memory / 搜索记忆", "InMemoryStore / 内存存储"],
                "examples": [{"title": "LangMem Tools", "prompt": "manage_memory_tool = create_manage_memory_tool(namespace=('assistant', '{user_id}', 'collection'))\nsearch_memory_tool = create_search_memory_tool(namespace=('assistant', '{user_id}', 'collection'))", "response": "Create LangMem memory tools"}]
            }
        ],
        "terms": [
            {"term": "Semantic Memory", "term_cn": "语义记忆", "definition": "存储事实和知识的长期记忆", "definition_en": "Long-term memory storing facts and knowledge"},
            {"term": "Episodic Memory", "term_cn": "情景记忆", "definition": "记住特定事件和交互的记忆", "definition_en": "Memory of specific events and interactions"},
            {"term": "Procedural Memory", "term_cn": "程序记忆", "definition": "学习和改进行为模式的记忆", "definition_en": "Memory for learning and improving behavioral patterns"}
        ],
        "questions": [
            {"kp_index": 0, "type": "multiple_choice", "question": "Agent的三种记忆类型包括哪些？", "options": ["A. 语义记忆", "B. 情景记忆", "C. 程序记忆", "D. 临时记忆"], "answer": "A,B,C", "explanation": "Agent的三种记忆类型是语义记忆、情景记忆和程序记忆。", "difficulty": 1},
            {"kp_index": 1, "type": "single_choice", "question": "哪个LangMem工具用于搜索记忆？", "options": ["A. manage_memory_tool", "B. search_memory_tool", "C. create_memory_tool", "D. delete_memory_tool"], "answer": "B", "explanation": "search_memory_tool用于搜索存储的记忆内容。", "difficulty": 1}
        ]
    },
    "simple_conversational_agent.ipynb": {
        "title": "简单对话Agent / Simple Conversational Agent",
        "summary": "Build a conversational agent that maintains context across multiple interactions using LangChain. / 构建能够在多次交互中保持上下文的对话Agent。",
        "knowledge_points": [
            {
                "title": "对话历史管理 / Conversation History Management",
                "description": "使用RunnableWithMessageHistory管理对话历史，实现上下文感知的对话。",
                "description_en": "Use RunnableWithMessageHistory to manage conversation history for context-aware conversations.",
                "importance": 3,
                "key_concepts": ["RunnableWithMessageHistory / 消息历史包装器", "ChatMessageHistory / 聊天消息历史", "Session management / 会话管理"],
                "examples": [{"title": "History Management", "prompt": "chain_with_history = RunnableWithMessageHistory(\n    chain, get_chat_history,\n    input_messages_key='input',\n    history_messages_key='history'\n)", "response": "Wrap chain with message history"}]
            },
            {
                "title": "提示模板设计 / Prompt Template Design",
                "description": "使用ChatPromptTemplate和MessagesPlaceholder设计包含历史消息的提示模板。",
                "description_en": "Use ChatPromptTemplate and MessagesPlaceholder to design prompts that include historical messages.",
                "importance": 2,
                "key_concepts": ["ChatPromptTemplate / 聊天提示模板", "MessagesPlaceholder / 消息占位符", "System message / 系统消息"],
                "examples": [{"title": "Prompt Template", "prompt": "prompt = ChatPromptTemplate.from_messages([\n    ('system', 'You are a helpful AI assistant.'),\n    MessagesPlaceholder(variable_name='history'),\n    ('human', '{input}')\n])", "response": "Create prompt template with history placeholder"}]
            }
        ],
        "terms": [
            {"term": "RunnableWithMessageHistory", "term_cn": "消息历史包装器", "definition": "LangChain中用于管理对话历史的包装器", "definition_en": "Wrapper in LangChain for managing conversation history"},
            {"term": "Context Awareness", "term_cn": "上下文感知", "definition": "Agent能够记住和引用之前对话内容的能力", "definition_en": "Agent's ability to remember and reference previous conversation content"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "RunnableWithMessageHistory的主要作用是什么？", "options": ["A. 生成回复", "B. 管理对话历史", "C. 调用API", "D. 解析JSON"], "answer": "B", "explanation": "RunnableWithMessageHistory用于管理对话历史，实现上下文感知。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "MessagesPlaceholder用于在提示模板中插入历史消息。", "answer": "正确", "explanation": "MessagesPlaceholder在提示模板中为历史消息预留位置。", "difficulty": 1}
        ]
    },
    "simple_conversational_agent-pydanticai.ipynb": {
        "title": "PydanticAI 对话Agent / PydanticAI Conversational Agent",
        "summary": "Build conversational agents using PydanticAI framework with type safety and validation. / 使用PydanticAI框架构建具有类型安全和验证的对话Agent。",
        "knowledge_points": [
            {
                "title": "PydanticAI Agent / PydanticAI Agent",
                "description": "PydanticAI提供类型安全的Agent框架，结合Pydantic的验证和类型安全原则。",
                "description_en": "PydanticAI provides a type-safe agent framework, combining Pydantic's validation and type-safety principles.",
                "importance": 3,
                "key_concepts": ["Type safety / 类型安全", "Validation / 验证", "Pydantic integration / Pydantic集成"],
                "examples": [{"title": "PydanticAI Agent", "prompt": "agent = Agent(\n    model='openai:gpt-4o-mini',\n    system_prompt='You are a helpful AI assistant.'\n)", "response": "Create PydanticAI agent"}]
            },
            {
                "title": "消息存储与检索 / Message Storage & Retrieval",
                "description": "使用ModelMessagesTypeAdapter进行消息的序列化和反序列化存储。",
                "description_en": "Use ModelMessagesTypeAdapter for message serialization and deserialization storage.",
                "importance": 2,
                "key_concepts": ["ModelMessagesTypeAdapter / 消息类型适配器", "JSON serialization / JSON序列化", "Message history / 消息历史"],
                "examples": [{"title": "Message Storage", "prompt": "messages = ModelMessagesTypeAdapter.validate_json(msg_group)\nstore[session_id].append(run_result.new_messages_json())", "response": "Store and retrieve messages in JSON format"}]
            }
        ],
        "terms": [
            {"term": "PydanticAI", "term_cn": "PydanticAI框架", "definition": "基于Pydantic的类型安全AI Agent框架", "definition_en": "Type-safe AI agent framework based on Pydantic"},
            {"term": "Type Safety", "term_cn": "类型安全", "definition": "确保代码在编译时捕获类型错误", "definition_en": "Ensuring code catches type errors at compile time"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "PydanticAI的主要优势是什么？", "options": ["A. 更快的执行速度", "B. 类型安全和验证", "C. 更小的内存占用", "D. 更简单的API"], "answer": "B", "explanation": "PydanticAI的主要优势是结合Pydantic的类型安全和验证能力。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "ModelMessagesTypeAdapter用于消息的序列化和反序列化。", "answer": "正确", "explanation": "ModelMessagesTypeAdapter用于将消息转换为JSON格式存储和从JSON恢复。", "difficulty": 1}
        ]
    },
    "simple_data_analysis_agent_notebook.ipynb": {
        "title": "数据分析Agent / Data Analysis Agent",
        "summary": "Create an AI-powered data analysis agent that can interpret and answer questions about datasets using natural language. / 创建能够用自然语言解释和回答数据集问题的AI数据分析Agent。",
        "knowledge_points": [
            {
                "title": "Pandas DataFrame Agent / Pandas数据框Agent",
                "description": "使用create_pandas_dataframe_agent创建能够分析数据框的Agent，支持自然语言查询。",
                "description_en": "Use create_pandas_dataframe_agent to create agents that can analyze dataframes with natural language queries.",
                "importance": 3,
                "key_concepts": ["create_pandas_dataframe_agent / Pandas Agent创建", "Natural language queries / 自然语言查询", "Data analysis / 数据分析"],
                "examples": [{"title": "DataFrame Agent", "prompt": "agent = create_pandas_dataframe_agent(\n    ChatOpenAI(model='gpt-4o'),\n    df,\n    verbose=True,\n    allow_dangerous_code=True\n)", "response": "Create Pandas DataFrame agent"}]
            },
            {
                "title": "自然语言数据查询 / Natural Language Data Queries",
                "description": "Agent可以将自然语言问题转换为Python代码执行数据分析。",
                "description_en": "Agent can convert natural language questions into Python code to perform data analysis.",
                "importance": 2,
                "key_concepts": ["Query translation / 查询转换", "Code generation / 代码生成", "Result interpretation / 结果解释"],
                "examples": [{"title": "Natural Language Query", "prompt": "agent.run({'input': 'What is the average price of cars sold?'})\n# Agent generates: df['Price'].mean()", "response": "Natural language to data analysis"}]
            }
        ],
        "terms": [
            {"term": "Pandas Agent", "term_cn": "Pandas Agent", "definition": "能够分析Pandas数据框的AI Agent", "definition_en": "AI agent capable of analyzing Pandas dataframes"},
            {"term": "Natural Language Query", "term_cn": "自然语言查询", "definition": "用自然语言而非代码进行数据查询", "definition_en": "Querying data using natural language instead of code"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "create_pandas_dataframe_agent的主要功能是什么？", "options": ["A. 创建数据可视化", "B. 创建能分析数据框的Agent", "C. 清洗数据", "D. 导出数据"], "answer": "B", "explanation": "create_pandas_dataframe_agent创建能够分析Pandas数据框的Agent。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "Agent可以将自然语言问题转换为Python代码执行数据分析。", "answer": "正确", "explanation": "Agent能够理解自然语言问题并生成相应的Python代码进行分析。", "difficulty": 1}
        ]
    },
    "task_oriented_agent.ipynb": {
        "title": "任务导向Agent / Task-Oriented Agent",
        "summary": "Build agents that can perform specific tasks like summarization and translation using structured tools. / 构建能够使用结构化工具执行特定任务（如摘要和翻译）的Agent。",
        "knowledge_points": [
            {
                "title": "Structured Tools / 结构化工具",
                "description": "使用StructuredTool将自定义函数包装为Agent可用的工具，包含名称、描述和输入模式。",
                "description_en": "Use StructuredTool to wrap custom functions as agent tools with name, description, and input schema.",
                "importance": 3,
                "key_concepts": ["StructuredTool / 结构化工具", "Input schema / 输入模式", "Tool description / 工具描述"],
                "examples": [{"title": "Structured Tool", "prompt": "tools = [\n    StructuredTool.from_function(\n        func=summarize,\n        name='Summarize',\n        description='Useful for summarizing text',\n        args_schema=TextInput\n    )\n]", "response": "Create structured tool from function"}]
            },
            {
                "title": "Agent Executor / Agent执行器",
                "description": "AgentExecutor管理Agent的执行，控制迭代次数和停止条件。",
                "description_en": "AgentExecutor manages agent execution, controlling iteration count and stopping conditions.",
                "importance": 2,
                "key_concepts": ["AgentExecutor / Agent执行器", "max_iterations / 最大迭代次数", "early_stopping_method / 提前停止方法"],
                "examples": [{"title": "Agent Executor", "prompt": "agent_executor = AgentExecutor(\n    agent=agent,\n    tools=tools,\n    verbose=True,\n    max_iterations=3,\n    early_stopping_method='force'\n)", "response": "Configure agent executor with limits"}]
            }
        ],
        "terms": [
            {"term": "StructuredTool", "term_cn": "结构化工具", "definition": "具有定义输入模式的Agent工具", "definition_en": "Agent tool with defined input schema"},
            {"term": "AgentExecutor", "term_cn": "Agent执行器", "definition": "管理Agent执行过程的组件", "definition_en": "Component managing agent execution process"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "StructuredTool需要定义什么？", "options": ["A. 只有名称", "B. 名称、描述和输入模式", "C. 只有函数", "D. 只有描述"], "answer": "B", "explanation": "StructuredTool需要定义名称、描述和输入模式(args_schema)。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "AgentExecutor可以控制Agent的最大迭代次数。", "answer": "正确", "explanation": "AgentExecutor通过max_iterations参数控制最大迭代次数。", "difficulty": 1}
        ]
    },
    "multi_agent_collaboration_system.ipynb": {
        "title": "多Agent协作系统 / Multi-Agent Collaboration System",
        "summary": "Build a multi-agent system where specialized agents collaborate to solve complex problems. / 构建多Agent系统，让专业Agent协作解决复杂问题。",
        "knowledge_points": [
            {
                "title": "Agent协作模式 / Agent Collaboration Pattern",
                "description": "多个专业Agent通过迭代交互共同解决复杂问题，每个Agent负责特定领域。",
                "description_en": "Multiple specialized agents collaborate through iterative interaction to solve complex problems, each responsible for a specific domain.",
                "importance": 3,
                "key_concepts": ["Specialized agents / 专业Agent", "Iterative interaction / 迭代交互", "Context sharing / 上下文共享"],
                "examples": [{"title": "Collaboration System", "prompt": "class CollaborationSystem:\n    def __init__(self):\n        self.history_agent = Agent('Clio', 'History Specialist', [...])\n        self.data_agent = Agent('Data', 'Data Analysis Expert', [...])", "response": "Define multi-agent collaboration system"}]
            },
            {
                "title": "上下文传递 / Context Passing",
                "description": "Agent之间通过共享上下文列表传递信息，实现协作推理。",
                "description_en": "Agents pass information through shared context lists, enabling collaborative reasoning.",
                "importance": 2,
                "key_concepts": ["Context list / 上下文列表", "Message history / 消息历史", "Role-based messages / 基于角色的消息"],
                "examples": [{"title": "Context Passing", "prompt": "context.append({'role': 'ai', 'content': f'History Agent: {result}'})\nnext_result = data_agent.process(task, context)", "response": "Pass context between agents"}]
            }
        ],
        "terms": [
            {"term": "Multi-Agent System", "term_cn": "多Agent系统", "definition": "多个Agent协作完成任务的系统", "definition_en": "System where multiple agents collaborate to complete tasks"},
            {"term": "Agent Collaboration", "term_cn": "Agent协作", "definition": "多个Agent之间的信息交换和任务协调", "definition_en": "Information exchange and task coordination between agents"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "多Agent协作系统的主要优势是什么？", "options": ["A. 更快的执行速度", "B. 结合不同专业知识解决复杂问题", "C. 更少的内存占用", "D. 更简单的代码"], "answer": "B", "explanation": "多Agent协作系统可以结合不同专业领域的知识来解决复杂问题。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "Agent之间通过共享上下文列表传递信息。", "answer": "正确", "explanation": "Agent之间通过共享的上下文列表传递消息和信息。", "difficulty": 1}
        ]
    },
    "self_healing_code.ipynb": {
        "title": "自愈代码Agent / Self-Healing Code Agent",
        "summary": "Build an agent that can detect runtime errors, generate fixes, and maintain a memory of bug patterns using vector databases. / 构建能够检测运行时错误、生成修复并维护bug模式记忆的Agent。",
        "knowledge_points": [
            {
                "title": "错误检测与修复 / Error Detection & Fix",
                "description": "Agent检测运行时错误，使用LLM生成修复代码，并验证修复效果。",
                "description_en": "Agent detects runtime errors, uses LLM to generate fix code, and validates the fix.",
                "importance": 3,
                "key_concepts": ["Error detection / 错误检测", "Code generation / 代码生成", "Patch validation / 补丁验证"],
                "examples": [{"title": "Self-Healing Flow", "prompt": "try:\n    result = function(*arguments)\nexcept Exception as e:\n    error_description = str(e)\n    new_code = llm.invoke(f'Fix this function: {function_string}, Error: {error_description}')", "response": "Detect error and generate fix"}]
            },
            {
                "title": "向量数据库记忆 / Vector Database Memory",
                "description": "使用ChromaDB存储bug报告，通过语义搜索找到相似的历史bug和修复方案。",
                "description_en": "Use ChromaDB to store bug reports and find similar historical bugs and fixes through semantic search.",
                "importance": 3,
                "key_concepts": ["ChromaDB / 向量数据库", "Bug patterns / Bug模式", "Semantic search / 语义搜索"],
                "examples": [{"title": "Bug Memory", "prompt": "collection.add(ids=[id], documents=[bug_report])\nresults = collection.query(query_texts=[new_bug], n_results=10)", "response": "Store and query bug patterns"}]
            }
        ],
        "terms": [
            {"term": "Self-Healing Code", "term_cn": "自愈代码", "definition": "能够自动检测和修复错误的代码系统", "definition_en": "Code system that can automatically detect and fix errors"},
            {"term": "Bug Pattern Memory", "term_cn": "Bug模式记忆", "definition": "存储历史bug和修复方案的知识库", "definition_en": "Knowledge base storing historical bugs and fixes"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "自愈代码Agent如何生成修复？", "options": ["A. 使用预定义规则", "B. 使用LLM生成修复代码", "C. 随机生成", "D. 从互联网搜索"], "answer": "B", "explanation": "自愈代码Agent使用LLM根据错误信息生成修复代码。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "ChromaDB用于存储bug报告并进行语义搜索。", "answer": "正确", "explanation": "ChromaDB存储bug报告，通过语义搜索找到相似的历史bug。", "difficulty": 1}
        ]
    },
    "self_improving_agent.ipynb": {
        "title": "自我改进Agent / Self-Improving Agent",
        "summary": "Build agents that can learn from feedback and improve their behavior over time. / 构建能够从反馈中学习并随时间改进行为的Agent。",
        "knowledge_points": [
            {
                "title": "反馈学习 / Feedback Learning",
                "description": "Agent从用户反馈中学习，调整其行为和响应策略。",
                "description_en": "Agent learns from user feedback and adjusts its behavior and response strategies.",
                "importance": 3,
                "key_concepts": ["User feedback / 用户反馈", "Behavior adjustment / 行为调整", "Learning loop / 学习循环"],
                "examples": [{"title": "Feedback Learning", "prompt": "feedback = 'The response was too verbose'\nimproved_prompt = optimizer.invoke({\n    'trajectories': [(conversation, {'feedback': feedback})],\n    'prompts': current_prompts\n})", "response": "Learn from feedback to improve prompts"}]
            },
            {
                "title": "提示优化 / Prompt Optimization",
                "description": "使用优化器根据反馈自动改进Agent的系统提示。",
                "description_en": "Use optimizer to automatically improve agent's system prompts based on feedback.",
                "importance": 2,
                "key_concepts": ["Prompt optimizer / 提示优化器", "Trajectory analysis / 轨迹分析", "Continuous improvement / 持续改进"],
                "examples": [{"title": "Prompt Optimization", "prompt": "optimizer = create_multi_prompt_optimizer(llm)\nresult = optimizer.invoke({'trajectories': trajectories, 'prompts': prompts})\nimproved_prompt = next(p['prompt'] for p in result if p['name'] == 'response')", "response": "Optimize prompts based on feedback"}]
            }
        ],
        "terms": [
            {"term": "Self-Improvement", "term_cn": "自我改进", "definition": "Agent从反馈中学习并改进的能力", "definition_en": "Agent's ability to learn from feedback and improve"},
            {"term": "Prompt Optimization", "term_cn": "提示优化", "definition": "自动改进Agent系统提示的过程", "definition_en": "Process of automatically improving agent's system prompts"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "自我改进Agent如何学习？", "options": ["A. 从预定义规则", "B. 从用户反馈", "C. 从随机尝试", "D. 从代码分析"], "answer": "B", "explanation": "自我改进Agent从用户反馈中学习并调整行为。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "提示优化器可以自动改进Agent的系统提示。", "answer": "正确", "explanation": "提示优化器根据反馈轨迹自动改进系统提示。", "difficulty": 1}
        ]
    },
    "memory_enhanced_conversational_agent.ipynb": {
        "title": "记忆增强对话Agent / Memory-Enhanced Conversational Agent",
        "summary": "Build conversational agents with enhanced memory capabilities for better context retention. / 构建具有增强记忆能力的对话Agent以更好地保持上下文。",
        "knowledge_points": [
            {
                "title": "长期记忆存储 / Long-term Memory Storage",
                "description": "使用向量存储实现长期记忆，支持语义搜索检索相关历史信息。",
                "description_en": "Use vector storage for long-term memory, supporting semantic search to retrieve relevant historical information.",
                "importance": 3,
                "key_concepts": ["Vector storage / 向量存储", "Long-term memory / 长期记忆", "Semantic retrieval / 语义检索"],
                "examples": [{"title": "Long-term Memory", "prompt": "store.put(('assistant', user_id, 'memories'), memory_id, memory_content)\nrelevant_memories = store.search(('assistant', user_id, 'memories'), query=user_input)", "response": "Store and retrieve long-term memories"}]
            },
            {
                "title": "记忆整合 / Memory Integration",
                "description": "将检索到的记忆整合到当前对话上下文中，提供个性化响应。",
                "description_en": "Integrate retrieved memories into current conversation context for personalized responses.",
                "importance": 2,
                "key_concepts": ["Memory integration / 记忆整合", "Personalization / 个性化", "Context enrichment / 上下文丰富"],
                "examples": [{"title": "Memory Integration", "prompt": "memories = store.search(namespace, query=current_input)\ncontext = f'Relevant memories: {memories}\\nCurrent input: {current_input}'\nresponse = llm.invoke(context)", "response": "Integrate memories into conversation"}]
            }
        ],
        "terms": [
            {"term": "Long-term Memory", "term_cn": "长期记忆", "definition": "Agent持久存储的信息", "definition_en": "Information persistently stored by agent"},
            {"term": "Memory Integration", "term_cn": "记忆整合", "definition": "将历史记忆整合到当前上下文的过程", "definition_en": "Process of integrating historical memories into current context"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "长期记忆存储使用什么技术实现语义搜索？", "options": ["A. 关系数据库", "B. 向量存储", "C. 文件系统", "D. 缓存"], "answer": "B", "explanation": "长期记忆存储使用向量存储实现语义搜索功能。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "记忆整合可以提供个性化的响应。", "answer": "正确", "explanation": "将历史记忆整合到当前上下文可以提供更个性化的响应。", "difficulty": 1}
        ]
    },
    "customer_support_agent_langgraph.ipynb": {
        "title": "客户支持Agent / Customer Support Agent",
        "summary": "Build a customer support agent using LangGraph that can handle inquiries and provide assistance. / 使用LangGraph构建能够处理咨询和提供帮助的客户支持Agent。",
        "knowledge_points": [
            {
                "title": "客户咨询处理 / Customer Inquiry Handling",
                "description": "Agent自动分类客户咨询，提供相应回复或升级处理。",
                "description_en": "Agent automatically classifies customer inquiries and provides appropriate responses or escalates.",
                "importance": 3,
                "key_concepts": ["Inquiry classification / 咨询分类", "Auto-response / 自动回复", "Escalation / 升级处理"],
                "examples": [{"title": "Inquiry Handling", "prompt": "classification = classify_inquiry(customer_message)\nif classification == 'simple':\n    response = auto_respond(customer_message)\nelse:\n    escalate_to_human(customer_message)", "response": "Classify and handle customer inquiry"}]
            }
        ],
        "terms": [
            {"term": "Customer Support Agent", "term_cn": "客户支持Agent", "definition": "处理客户咨询的AI Agent", "definition_en": "AI agent handling customer inquiries"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "客户支持Agent如何处理复杂咨询？", "options": ["A. 忽略", "B. 自动回复", "C. 升级给人工", "D. 删除"], "answer": "C", "explanation": "复杂咨询会被升级给人工客服处理。", "difficulty": 1}
        ]
    },
    "research_team_autogen.ipynb": {
        "title": "AutoGen研究团队 / AutoGen Research Team",
        "summary": "Build a research team using Microsoft AutoGen framework for multi-agent collaboration. / 使用Microsoft AutoGen框架构建研究团队进行多Agent协作。",
        "knowledge_points": [
            {
                "title": "AutoGen框架 / AutoGen Framework",
                "description": "Microsoft AutoGen提供多Agent对话框架，支持Agent之间的自动对话和协作。",
                "description_en": "Microsoft AutoGen provides multi-agent conversation framework, supporting automatic dialogue and collaboration between agents.",
                "importance": 3,
                "key_concepts": ["AutoGen / AutoGen框架", "Multi-agent conversation / 多Agent对话", "Assistant Agent / 助手Agent"],
                "examples": [{"title": "AutoGen Setup", "prompt": "assistant = AssistantAgent('assistant', llm_config=llm_config)\nuser_proxy = UserProxyAgent('user_proxy', code_execution_config=...)\nuser_proxy.initiate_chat(assistant, message='Research topic...')", "response": "Set up AutoGen agents for research"}]
            }
        ],
        "terms": [
            {"term": "AutoGen", "term_cn": "AutoGen框架", "definition": "Microsoft的多Agent对话框架", "definition_en": "Microsoft's multi-agent conversation framework"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "AutoGen是哪个公司开发的？", "options": ["A. Google", "B. Microsoft", "C. OpenAI", "D. Meta"], "answer": "B", "explanation": "AutoGen是Microsoft开发的多Agent对话框架。", "difficulty": 1}
        ]
    },
    "blog_writer_swarm.ipynb": {
        "title": "博客写作Swarm / Blog Writer Swarm",
        "summary": "Build a swarm of agents that collaborate to write blog posts. / 构建协作撰写博客文章的Agent群体。",
        "knowledge_points": [
            {
                "title": "Swarm架构 / Swarm Architecture",
                "description": "多个Agent以群体方式协作，每个Agent负责写作流程的不同阶段。",
                "description_en": "Multiple agents collaborate in a swarm pattern, each responsible for different stages of the writing process.",
                "importance": 2,
                "key_concepts": ["Swarm pattern / 群体模式", "Task distribution / 任务分配", "Collaborative writing / 协作写作"],
                "examples": [{"title": "Swarm Writing", "prompt": "researcher = Agent('researcher', 'Research topics')\nwriter = Agent('writer', 'Write content')\neditor = Agent('editor', 'Edit and polish')\nswarm = [researcher, writer, editor]", "response": "Create swarm of writing agents"}]
            }
        ],
        "terms": [
            {"term": "Swarm", "term_cn": "群体", "definition": "多个Agent协作完成任务的架构", "definition_en": "Architecture where multiple agents collaborate to complete tasks"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "Swarm架构中Agent如何协作？", "options": ["A. 竞争", "B. 各自独立", "C. 协作分工", "D. 随机"], "answer": "C", "explanation": "Swarm架构中Agent协作分工，每个负责不同阶段。", "difficulty": 1}
        ]
    },
    "essay_grading_system_langgraph.ipynb": {
        "title": "论文评分系统 / Essay Grading System",
        "summary": "Build an automated essay grading system using LangGraph. / 使用LangGraph构建自动论文评分系统。",
        "knowledge_points": [
            {
                "title": "自动评分流程 / Automated Grading Process",
                "description": "系统分析论文内容，评估多个维度并给出评分和反馈。",
                "description_en": "System analyzes essay content, evaluates multiple dimensions, and provides scores and feedback.",
                "importance": 2,
                "key_concepts": ["Content analysis / 内容分析", "Multi-dimensional evaluation / 多维评估", "Automated feedback / 自动反馈"],
                "examples": [{"title": "Grading Flow", "prompt": "essay_analysis = analyze_essay(essay)\nscores = evaluate_dimensions(essay_analysis)\nfeedback = generate_feedback(scores)", "response": "Automated essay grading process"}]
            }
        ],
        "terms": [
            {"term": "Automated Grading", "term_cn": "自动评分", "definition": "使用AI自动评估和评分", "definition_en": "Using AI for automatic evaluation and scoring"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "论文评分系统可以评估多个维度。", "answer": "正确", "explanation": "论文评分系统可以评估内容、结构、语法等多个维度。", "difficulty": 1}
        ]
    },
    "scientific_paper_agent_langgraph.ipynb": {
        "title": "科学论文Agent / Scientific Paper Agent",
        "summary": "Build an agent that can analyze and summarize scientific papers. / 构建能够分析和总结科学论文的Agent。",
        "knowledge_points": [
            {
                "title": "论文分析 / Paper Analysis",
                "description": "Agent提取论文关键信息，包括方法、结果和结论。",
                "description_en": "Agent extracts key information from papers including methods, results, and conclusions.",
                "importance": 2,
                "key_concepts": ["Paper parsing / 论文解析", "Key extraction / 关键提取", "Summary generation / 摘要生成"],
                "examples": [{"title": "Paper Analysis", "prompt": "sections = parse_paper(paper_content)\nkey_findings = extract_key_findings(sections)\nsummary = generate_summary(key_findings)", "response": "Analyze scientific paper"}]
            }
        ],
        "terms": [
            {"term": "Scientific Paper Agent", "term_cn": "科学论文Agent", "definition": "分析和总结科学论文的AI Agent", "definition_en": "AI agent for analyzing and summarizing scientific papers"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "科学论文Agent提取哪些关键信息？", "options": ["A. 只有标题", "B. 方法、结果和结论", "C. 只有作者", "D. 只有参考文献"], "answer": "B", "explanation": "科学论文Agent提取方法、结果和结论等关键信息。", "difficulty": 1}
        ]
    },
    "news_tldr_langgraph.ipynb": {
        "title": "新闻摘要Agent / News TLDR Agent",
        "summary": "Build an agent that creates concise summaries of news articles. / 构建能够创建新闻文章简洁摘要的Agent。",
        "knowledge_points": [
            {
                "title": "新闻摘要生成 / News Summary Generation",
                "description": "Agent分析新闻内容，提取关键信息并生成简洁摘要。",
                "description_en": "Agent analyzes news content, extracts key information, and generates concise summaries.",
                "importance": 2,
                "key_concepts": ["News analysis / 新闻分析", "Key point extraction / 关键点提取", "TLDR generation / 摘要生成"],
                "examples": [{"title": "News TLDR", "prompt": "key_points = extract_key_points(news_article)\ntldr = generate_tldr(key_points, max_length=100)", "response": "Generate news TLDR summary"}]
            }
        ],
        "terms": [
            {"term": "TLDR", "term_cn": "太长不看", "definition": "简洁的内容摘要", "definition_en": "Concise content summary"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "新闻摘要Agent可以生成简洁的新闻摘要。", "answer": "正确", "explanation": "新闻摘要Agent分析新闻内容并生成简洁摘要。", "difficulty": 1}
        ]
    },
    "simple_travel_planner_langgraph.ipynb": {
        "title": "旅行规划Agent / Travel Planner Agent",
        "summary": "Build an agent that helps plan travel itineraries. / 构建帮助规划旅行行程的Agent。",
        "knowledge_points": [
            {
                "title": "行程规划 / Itinerary Planning",
                "description": "Agent根据用户偏好和约束条件生成旅行行程建议。",
                "description_en": "Agent generates travel itinerary suggestions based on user preferences and constraints.",
                "importance": 2,
                "key_concepts": ["Preference analysis / 偏好分析", "Itinerary generation / 行程生成", "Constraint satisfaction / 约束满足"],
                "examples": [{"title": "Travel Planning", "prompt": "preferences = analyze_preferences(user_input)\nitinerary = generate_itinerary(preferences, destination, dates)", "response": "Generate travel itinerary"}]
            }
        ],
        "terms": [
            {"term": "Travel Planner Agent", "term_cn": "旅行规划Agent", "definition": "帮助规划旅行行程的AI Agent", "definition_en": "AI agent helping plan travel itineraries"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "旅行规划Agent根据什么生成行程？", "options": ["A. 随机选择", "B. 用户偏好和约束", "C. 固定模板", "D. 价格排序"], "answer": "B", "explanation": "旅行规划Agent根据用户偏好和约束条件生成行程。", "difficulty": 1}
        ]
    },
    "generate_podcast_agent_langgraph.ipynb": {
        "title": "播客生成Agent / Podcast Generator Agent",
        "summary": "Build an agent that generates podcast content and scripts. / 构建能够生成播客内容和脚本的Agent。",
        "knowledge_points": [
            {
                "title": "播客内容生成 / Podcast Content Generation",
                "description": "Agent根据主题生成播客脚本，包括对话和结构。",
                "description_en": "Agent generates podcast scripts based on topics, including dialogue and structure.",
                "importance": 2,
                "key_concepts": ["Script generation / 脚本生成", "Dialogue creation / 对话创建", "Structure planning / 结构规划"],
                "examples": [{"title": "Podcast Script", "prompt": "outline = create_outline(topic, duration)\nscript = generate_script(outline, style='conversational')", "response": "Generate podcast script"}]
            }
        ],
        "terms": [
            {"term": "Podcast Agent", "term_cn": "播客Agent", "definition": "生成播客内容的AI Agent", "definition_en": "AI agent generating podcast content"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "播客生成Agent可以生成对话脚本。", "answer": "正确", "explanation": "播客生成Agent可以生成包含对话的播客脚本。", "difficulty": 1}
        ]
    },
    "music_compositor_agent_langgraph.ipynb": {
        "title": "音乐作曲Agent / Music Compositor Agent",
        "summary": "Build an agent that assists in music composition. / 构建协助音乐创作的Agent。",
        "knowledge_points": [
            {
                "title": "音乐创作辅助 / Music Composition Assistance",
                "description": "Agent根据风格和参数生成音乐创作建议和结构。",
                "description_en": "Agent generates music composition suggestions and structures based on style and parameters.",
                "importance": 2,
                "key_concepts": ["Style analysis / 风格分析", "Composition structure / 作曲结构", "Creative suggestions / 创意建议"],
                "examples": [{"title": "Music Composition", "prompt": "style_params = analyze_style(genre, mood)\ncomposition = generate_composition(style_params, duration)", "response": "Generate music composition suggestions"}]
            }
        ],
        "terms": [
            {"term": "Music Compositor Agent", "term_cn": "音乐作曲Agent", "definition": "协助音乐创作的AI Agent", "definition_en": "AI agent assisting in music composition"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "音乐作曲Agent根据什么生成创作建议？", "options": ["A. 随机生成", "B. 风格和参数", "C. 固定模板", "D. 用户年龄"], "answer": "B", "explanation": "音乐作曲Agent根据风格和参数生成创作建议。", "difficulty": 1}
        ]
    },
    "search_the_internet_and_summarize.ipynb": {
        "title": "网络搜索摘要Agent / Internet Search & Summarize Agent",
        "summary": "Build an agent that searches the internet and summarizes findings. / 构建能够搜索互联网并总结结果的Agent。",
        "knowledge_points": [
            {
                "title": "网络搜索集成 / Internet Search Integration",
                "description": "Agent集成搜索工具，执行搜索并总结结果。",
                "description_en": "Agent integrates search tools, executes searches, and summarizes results.",
                "importance": 3,
                "key_concepts": ["Search tool integration / 搜索工具集成", "Result aggregation / 结果聚合", "Summary synthesis / 摘要综合"],
                "examples": [{"title": "Search & Summarize", "prompt": "search_results = search_tool(query)\naggregated = aggregate_results(search_results)\nsummary = synthesize_summary(aggregated)", "response": "Search internet and summarize findings"}]
            }
        ],
        "terms": [
            {"term": "Search Agent", "term_cn": "搜索Agent", "definition": "执行网络搜索的AI Agent", "definition_en": "AI agent executing internet searches"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "网络搜索摘要Agent可以聚合多个搜索结果。", "answer": "正确", "explanation": "Agent可以聚合多个搜索结果并生成综合摘要。", "difficulty": 1}
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

This lesson covered key AI Agent concepts. Practice these techniques to build better intelligent systems.

本课程涵盖了关键AI Agent技术。练习这些技术以构建更好的智能系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own agents / 构建自己的Agent
3. Explore advanced patterns / 探索高级模式
"""
    return content

def batch_update_agents_courses():
    print("Starting batch update of AI Agents courses...")
    db = SessionLocal()
    
    try:
        agents_module = db.query(Module).filter(Module.name.like('%Agent%')).first()
        if not agents_module:
            agents_module = Module(
                name="Agent 智能体",
                description="Comprehensive AI Agents course covering basic to advanced agent patterns. / 全面的AI Agent课程，涵盖从基础到高级的智能体模式。"
            )
            db.add(agents_module)
            db.commit()
            print(f"Created module: {agents_module.name}")
        else:
            print(f"Using existing module: {agents_module.name}")
        
        total_lessons = 0
        total_kps = 0
        total_terms = 0
        total_questions = 0
        
        for notebook_name, course_data in AGENTS_COURSES_DATA.items():
            print(f"\nProcessing: {notebook_name}")
            
            existing_lesson = db.query(Lesson).filter(Lesson.title == course_data['title']).first()
            if existing_lesson:
                lesson = existing_lesson
                db.query(KnowledgePoint).filter(KnowledgePoint.lesson_id == lesson.id).delete()
                db.query(LessonTerm).filter(LessonTerm.lesson_id == lesson.id).delete()
                print(f"  Updating existing lesson: {lesson.title}")
            else:
                lesson = Lesson(
                    module_id=agents_module.id,
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
            material_filename = f"agents_{notebook_name.replace('.ipynb', '')}.md"
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
                    category='agent',
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
                        category='agent',
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
    batch_update_agents_courses()
