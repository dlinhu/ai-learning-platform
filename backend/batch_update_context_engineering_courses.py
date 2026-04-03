import os
import sys

backend_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, backend_dir)

from app.utils.database import SessionLocal
from app.models.models import Module, Lesson, KnowledgePoint, Term, LessonTerm, PracticeQuestion

CONTEXT_ENGINEERING_COURSES_DATA = {
    "00_mathematical_foundations": {
        "title": "数学基础 / Mathematical Foundations",
        "summary": "Learn the mathematical foundations of context engineering including formalization, optimization, and information theory. / 学习上下文工程的数学基础，包括形式化、优化和信息论。",
        "knowledge_points": [
            {
                "title": "上下文组装方程 / Context Assembly Equation",
                "description": "上下文组装的核心方程 C = A(c₁, c₂, ..., cₙ)，定义了如何将多个上下文组件组合成完整上下文。",
                "description_en": "The core context assembly equation C = A(c₁, c₂, ..., cₙ) defines how to combine multiple context components into a complete context.",
                "importance": 3,
                "key_concepts": ["Context Assembly / 上下文组装", "Context Components / 上下文组件", "Assembly Function / 组装函数", "Complete Context / 完整上下文"],
                "examples": [{"title": "Context Assembly", "prompt": "C = A(system_prompt, user_query, retrieved_docs, conversation_history)", "response": "Assemble context from multiple components"}]
            },
            {
                "title": "四大支柱 / Four Pillars",
                "description": "上下文工程的四大数学支柱：形式化、优化、信息论和贝叶斯推断。",
                "description_en": "Four mathematical pillars of context engineering: Formalization, Optimization, Information Theory, and Bayesian Inference.",
                "importance": 3,
                "key_concepts": ["Formalization / 形式化", "Optimization / 优化", "Information Theory / 信息论", "Bayesian Inference / 贝叶斯推断"],
                "examples": [{"title": "Four Pillars", "prompt": "pillars = ['formalization', 'optimization', 'information_theory', 'bayesian_inference']", "response": "Define the four mathematical pillars"}]
            },
            {
                "title": "Software 3.0 范式 / Software 3.0 Paradigm",
                "description": "Software 3.0的三大范式：Prompts（模板）、Programming（算法）、Protocols（编排）。",
                "description_en": "Three paradigms of Software 3.0: Prompts (templates), Programming (algorithms), Protocols (orchestration).",
                "importance": 3,
                "key_concepts": ["Prompts / 提示模板", "Programming / 编程算法", "Protocols / 协议编排", "Paradigm Shift / 范式转变"],
                "examples": [{"title": "Software 3.0", "prompt": "paradigm = {\n    'prompts': 'Natural language templates',\n    'programming': 'Algorithmic processing',\n    'protocols': 'Agent orchestration'\n}", "response": "Define Software 3.0 paradigm components"}]
            }
        ],
        "terms": [
            {"term": "Context Assembly", "term_cn": "上下文组装", "definition": "将多个上下文组件组合成完整上下文的过程", "definition_en": "Process of combining multiple context components into complete context"},
            {"term": "Formalization", "term_cn": "形式化", "definition": "将上下文工程概念转化为数学模型", "definition_en": "Converting context engineering concepts to mathematical models"},
            {"term": "Bayesian Inference", "term_cn": "贝叶斯推断", "definition": "基于先验知识和观测数据更新概率分布", "definition_en": "Updating probability distributions based on prior knowledge and observed data"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "上下文组装方程 C = A(c₁, c₂, ..., cₙ) 中的 A 代表什么？", "options": ["A. 算法", "B. 组装函数", "C. 上下文", "D. 参数"], "answer": "B", "explanation": "A代表Assembly Function（组装函数），用于组合上下文组件。", "difficulty": 1},
            {"kp_index": 1, "type": "multiple_choice", "question": "上下文工程的四大支柱包括哪些？", "options": ["A. 形式化", "B. 优化", "C. 信息论", "D. 深度学习"], "answer": "A,B,C", "explanation": "四大支柱是形式化、优化、信息论和贝叶斯推断。", "difficulty": 1},
            {"kp_index": 2, "type": "true_false", "question": "Software 3.0范式包括Prompts、Programming和Protocols三个层次。", "answer": "正确", "explanation": "Software 3.0的三大范式是Prompts（模板）、Programming（算法）、Protocols（编排）。", "difficulty": 1}
        ]
    },
    "01_context_retrieval_generation": {
        "title": "上下文检索与生成 / Context Retrieval & Generation",
        "summary": "Learn semantic retrieval engines and dynamic context assembly algorithms. / 学习语义检索引擎和动态上下文组装算法。",
        "knowledge_points": [
            {
                "title": "语义检索引擎 / Semantic Retrieval Engine",
                "description": "基于语义相似度的检索系统，使用向量嵌入和近似最近邻搜索。",
                "description_en": "Retrieval system based on semantic similarity using vector embeddings and approximate nearest neighbor search.",
                "importance": 3,
                "key_concepts": ["Vector Embeddings / 向量嵌入", "Semantic Similarity / 语义相似度", "ANN Search / 近似最近邻搜索", "Dense Retrieval / 稠密检索"],
                "examples": [{"title": "Semantic Retrieval", "prompt": "def semantic_retrieve(query, corpus, k=5):\n    query_emb = embed(query)\n    scores = cosine_similarity(query_emb, corpus_embeddings)\n    return top_k(corpus, scores, k)", "response": "Implement semantic retrieval function"}]
            },
            {
                "title": "动态上下文组装 / Dynamic Context Assembly",
                "description": "根据查询动态组装上下文，优化信息密度和相关性。",
                "description_en": "Dynamically assemble context based on query, optimizing information density and relevance.",
                "importance": 3,
                "key_concepts": ["Dynamic Assembly / 动态组装", "Information Density / 信息密度", "Relevance Optimization / 相关性优化", "Context Window / 上下文窗口"],
                "examples": [{"title": "Dynamic Assembly", "prompt": "def assemble_context(query, docs, max_tokens):\n    selected = []\n    for doc in rank_by_relevance(query, docs):\n        if token_count(selected + doc) <= max_tokens:\n            selected.append(doc)\n    return selected", "response": "Implement dynamic context assembly"}]
            }
        ],
        "terms": [
            {"term": "Semantic Retrieval", "term_cn": "语义检索", "definition": "基于语义相似度的信息检索方法", "definition_en": "Information retrieval based on semantic similarity"},
            {"term": "Dense Retrieval", "term_cn": "稠密检索", "definition": "使用稠密向量表示进行检索", "definition_en": "Retrieval using dense vector representations"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "语义检索引擎主要使用什么技术？", "options": ["A. 关键词匹配", "B. 向量嵌入和相似度", "C. 正则表达式", "D. 数据库索引"], "answer": "B", "explanation": "语义检索使用向量嵌入和语义相似度进行检索。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "动态上下文组装需要考虑上下文窗口限制。", "answer": "正确", "explanation": "动态组装需要优化信息密度并遵守上下文窗口限制。", "difficulty": 1}
        ]
    },
    "02_context_processing": {
        "title": "上下文处理 / Context Processing",
        "summary": "Learn context compression, transformation, and optimization techniques. / 学习上下文压缩、转换和优化技术。",
        "knowledge_points": [
            {
                "title": "上下文压缩 / Context Compression",
                "description": "减少上下文长度同时保留关键信息的技术，包括摘要和提取。",
                "description_en": "Techniques to reduce context length while preserving key information, including summarization and extraction.",
                "importance": 3,
                "key_concepts": ["Summarization / 摘要", "Information Extraction / 信息提取", "Token Reduction / Token减少", "Key Information / 关键信息"],
                "examples": [{"title": "Context Compression", "prompt": "def compress_context(context, target_length):\n    summary = llm.summarize(context, max_tokens=target_length)\n    return summary", "response": "Compress context using summarization"}]
            },
            {
                "title": "上下文转换 / Context Transformation",
                "description": "将上下文转换为不同格式或表示，以优化模型理解。",
                "description_en": "Transform context to different formats or representations to optimize model understanding.",
                "importance": 2,
                "key_concepts": ["Format Conversion / 格式转换", "Representation Learning / 表示学习", "Schema Mapping / 模式映射", "Normalization / 标准化"],
                "examples": [{"title": "Context Transform", "prompt": "def transform_context(raw_context):\n    structured = extract_entities(raw_context)\n    normalized = normalize_format(structured)\n    return normalized", "response": "Transform context to structured format"}]
            }
        ],
        "terms": [
            {"term": "Context Compression", "term_cn": "上下文压缩", "definition": "减少上下文长度同时保留关键信息", "definition_en": "Reducing context length while preserving key information"},
            {"term": "Context Transformation", "term_cn": "上下文转换", "definition": "将上下文转换为优化格式", "definition_en": "Converting context to optimized formats"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "上下文压缩的主要目的是什么？", "options": ["A. 增加信息量", "B. 减少长度保留关键信息", "C. 加快处理速度", "D. 提高准确性"], "answer": "B", "explanation": "上下文压缩旨在减少长度同时保留关键信息。", "difficulty": 1}
        ]
    },
    "03_context_management": {
        "title": "上下文管理 / Context Management",
        "summary": "Learn context lifecycle management, versioning, and state tracking. / 学习上下文生命周期管理、版本控制和状态跟踪。",
        "knowledge_points": [
            {
                "title": "上下文生命周期 / Context Lifecycle",
                "description": "管理上下文从创建到销毁的完整生命周期，包括初始化、更新和清理。",
                "description_en": "Manage the complete lifecycle of context from creation to destruction, including initialization, updates, and cleanup.",
                "importance": 3,
                "key_concepts": ["Lifecycle States / 生命周期状态", "State Transitions / 状态转换", "Resource Management / 资源管理", "Cleanup Strategies / 清理策略"],
                "examples": [{"title": "Context Lifecycle", "prompt": "class ContextManager:\n    def __init__(self):\n        self.contexts = {}\n    def create(self, id): self.contexts[id] = Context()\n    def update(self, id, data): self.contexts[id].update(data)\n    def cleanup(self, id): del self.contexts[id]", "response": "Implement context lifecycle manager"}]
            },
            {
                "title": "上下文版本控制 / Context Versioning",
                "description": "跟踪上下文变更历史，支持回滚和审计。",
                "description_en": "Track context change history, supporting rollback and auditing.",
                "importance": 2,
                "key_concepts": ["Version History / 版本历史", "Change Tracking / 变更跟踪", "Rollback / 回滚", "Audit Trail / 审计跟踪"],
                "examples": [{"title": "Version Control", "prompt": "class VersionedContext:\n    def __init__(self):\n        self.versions = []\n    def commit(self, context):\n        self.versions.append({'context': context, 'timestamp': now()})\n    def rollback(self, version): return self.versions[version]", "response": "Implement versioned context"}]
            }
        ],
        "terms": [
            {"term": "Context Lifecycle", "term_cn": "上下文生命周期", "definition": "上下文从创建到销毁的完整过程", "definition_en": "Complete process of context from creation to destruction"},
            {"term": "Version Control", "term_cn": "版本控制", "definition": "跟踪和管理上下文变更历史", "definition_en": "Tracking and managing context change history"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "上下文生命周期管理包括初始化、更新和清理。", "answer": "正确", "explanation": "生命周期管理覆盖上下文的完整生命周期。", "difficulty": 1}
        ]
    },
    "04_retrieval_augmented_generation": {
        "title": "检索增强生成 / Retrieval Augmented Generation",
        "summary": "Learn RAG fundamentals, architectures, and optimization strategies. / 学习RAG基础、架构和优化策略。",
        "knowledge_points": [
            {
                "title": "RAG 基础架构 / RAG Fundamentals",
                "description": "RAG系统的核心架构：检索器、重排序器和生成器的协同工作。",
                "description_en": "Core architecture of RAG systems: collaboration between retriever, reranker, and generator.",
                "importance": 3,
                "key_concepts": ["Retriever / 检索器", "Reranker / 重排序器", "Generator / 生成器", "Pipeline / 流水线"],
                "examples": [{"title": "RAG Architecture", "prompt": "class RAGSystem:\n    def __init__(self):\n        self.retriever = DenseRetriever()\n        self.reranker = CrossEncoderReranker()\n        self.generator = LLMGenerator()\n    def query(self, q):\n        docs = self.retriever.retrieve(q)\n        ranked = self.reranker.rerank(q, docs)\n        return self.generator.generate(q, ranked)", "response": "Implement RAG system architecture"}]
            },
            {
                "title": "稠密段落检索 / Dense Passage Retrieval",
                "description": "使用双编码器架构进行高效的段落检索。",
                "description_en": "Efficient passage retrieval using dual-encoder architecture.",
                "importance": 3,
                "key_concepts": ["Dual Encoder / 双编码器", "Passage Embedding / 段落嵌入", "Query Encoding / 查询编码", "FAISS Index / FAISS索引"],
                "examples": [{"title": "DPR Implementation", "prompt": "class DualEncoder:\n    def encode_query(self, query): return self.query_encoder(query)\n    def encode_passage(self, passage): return self.passage_encoder(passage)\n    def retrieve(self, query, index, k=10):\n        q_emb = self.encode_query(query)\n        return index.search(q_emb, k)", "response": "Implement dual encoder for DPR"}]
            },
            {
                "title": "混合检索策略 / Hybrid Retrieval Strategies",
                "description": "结合稀疏检索（BM25）和稠密检索的优势。",
                "description_en": "Combining advantages of sparse retrieval (BM25) and dense retrieval.",
                "importance": 2,
                "key_concepts": ["BM25 / BM25算法", "Dense Retrieval / 稠密检索", "Score Fusion / 分数融合", "Reciprocal Rank / 倒数排名"],
                "examples": [{"title": "Hybrid Retrieval", "prompt": "def hybrid_retrieve(query, sparse_idx, dense_idx, alpha=0.5):\n    sparse_results = bm25_search(query, sparse_idx)\n    dense_results = dense_search(query, dense_idx)\n    return reciprocal_rank_fusion(sparse_results, dense_results, alpha)", "response": "Implement hybrid retrieval"}]
            }
        ],
        "terms": [
            {"term": "RAG", "term_cn": "检索增强生成", "definition": "结合检索和生成的AI系统架构", "definition_en": "AI system architecture combining retrieval and generation"},
            {"term": "Dense Passage Retrieval", "term_cn": "稠密段落检索", "definition": "使用稠密向量进行段落检索", "definition_en": "Passage retrieval using dense vectors"},
            {"term": "Dual Encoder", "term_cn": "双编码器", "definition": "分别编码查询和文档的模型架构", "definition_en": "Model architecture encoding queries and documents separately"}
        ],
        "questions": [
            {"kp_index": 0, "type": "multiple_choice", "question": "RAG系统的核心组件包括哪些？", "options": ["A. 检索器", "B. 重排序器", "C. 生成器", "D. 分类器"], "answer": "A,B,C", "explanation": "RAG系统由检索器、重排序器和生成器组成。", "difficulty": 1},
            {"kp_index": 1, "type": "single_choice", "question": "稠密段落检索使用什么架构？", "options": ["A. 单编码器", "B. 双编码器", "C. 三编码器", "D. 无编码器"], "answer": "B", "explanation": "DPR使用双编码器分别编码查询和段落。", "difficulty": 1},
            {"kp_index": 2, "type": "true_false", "question": "混合检索结合了稀疏检索和稠密检索的优势。", "answer": "正确", "explanation": "混合检索融合BM25和稠密检索的结果。", "difficulty": 1}
        ]
    },
    "05_memory_systems": {
        "title": "记忆系统 / Memory Systems",
        "summary": "Learn short-term and long-term memory architectures for AI agents. / 学习AI Agent的短期和长期记忆架构。",
        "knowledge_points": [
            {
                "title": "短期记忆 / Short-Term Memory",
                "description": "管理当前对话上下文，包括滑动窗口和优先级队列策略。",
                "description_en": "Manage current conversation context with sliding window and priority queue strategies.",
                "importance": 3,
                "key_concepts": ["Sliding Window / 滑动窗口", "Token Budget / Token预算", "Priority Queue / 优先级队列", "Context Overflow / 上下文溢出"],
                "examples": [{"title": "Short-Term Memory", "prompt": "class ShortTermMemory:\n    def __init__(self, max_tokens=4000):\n        self.messages = []\n        self.max_tokens = max_tokens\n    def add(self, msg):\n        self.messages.append(msg)\n        self._trim_if_needed()", "response": "Implement short-term memory with token limit"}]
            },
            {
                "title": "长期记忆 / Long-Term Memory",
                "description": "使用向量存储持久化记忆，支持语义搜索和记忆检索。",
                "description_en": "Persist memories using vector storage, supporting semantic search and memory retrieval.",
                "importance": 3,
                "key_concepts": ["Vector Store / 向量存储", "Memory Persistence / 记忆持久化", "Semantic Search / 语义搜索", "Memory Consolidation / 记忆巩固"],
                "examples": [{"title": "Long-Term Memory", "prompt": "class LongTermMemory:\n    def __init__(self, vector_store):\n        self.store = vector_store\n    def store_memory(self, memory):\n        embedding = embed(memory)\n        self.store.add(embedding, metadata=memory)\n    def recall(self, query, k=5):\n        return self.store.search(embed(query), k)", "response": "Implement long-term memory with vector store"}]
            },
            {
                "title": "记忆类型 / Memory Types",
                "description": "情景记忆（用户经历）、语义记忆（通用知识）、程序记忆（技能）。",
                "description_en": "Episodic memory (user experiences), semantic memory (general knowledge), procedural memory (skills).",
                "importance": 2,
                "key_concepts": ["Episodic Memory / 情景记忆", "Semantic Memory / 语义记忆", "Procedural Memory / 程序记忆", "Memory Classification / 记忆分类"],
                "examples": [{"title": "Memory Types", "prompt": "class MemoryType(Enum):\n    EPISODIC = 'episodic'    # User experiences\n    SEMANTIC = 'semantic'     # General knowledge\n    PROCEDURAL = 'procedural' # Skills and procedures", "response": "Define memory type classification"}]
            }
        ],
        "terms": [
            {"term": "Short-Term Memory", "term_cn": "短期记忆", "definition": "管理当前对话上下文的临时记忆", "definition_en": "Temporary memory managing current conversation context"},
            {"term": "Long-Term Memory", "term_cn": "长期记忆", "definition": "持久化存储的记忆，支持检索", "definition_en": "Persistently stored memory supporting retrieval"},
            {"term": "Episodic Memory", "term_cn": "情景记忆", "definition": "存储用户特定经历和事件的记忆", "definition_en": "Memory storing user-specific experiences and events"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "短期记忆管理的主要策略是什么？", "options": ["A. 数据库存储", "B. 滑动窗口和Token预算", "C. 文件系统", "D. 网络传输"], "answer": "B", "explanation": "短期记忆使用滑动窗口和Token预算策略管理上下文。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "长期记忆使用向量存储支持语义搜索。", "answer": "正确", "explanation": "长期记忆通过向量嵌入支持语义搜索和检索。", "difficulty": 1},
            {"kp_index": 2, "type": "multiple_choice", "question": "记忆类型包括哪些？", "options": ["A. 情景记忆", "B. 语义记忆", "C. 程序记忆", "D. 临时记忆"], "answer": "A,B,C", "explanation": "三种主要记忆类型是情景、语义和程序记忆。", "difficulty": 1}
        ]
    },
    "06_tool_integration": {
        "title": "工具集成 / Tool Integration",
        "summary": "Learn tool discovery, binding, and execution for AI agents. / 学习AI Agent的工具发现、绑定和执行。",
        "knowledge_points": [
            {
                "title": "工具发现 / Tool Discovery",
                "description": "动态发现可用工具，包括API端点、函数和外部服务。",
                "description_en": "Dynamically discover available tools including API endpoints, functions, and external services.",
                "importance": 3,
                "key_concepts": ["Dynamic Discovery / 动态发现", "Tool Registry / 工具注册表", "API Introspection / API内省", "Service Discovery / 服务发现"],
                "examples": [{"title": "Tool Discovery", "prompt": "class ToolRegistry:\n    def __init__(self):\n        self.tools = {}\n    def register(self, name, func, schema):\n        self.tools[name] = {'func': func, 'schema': schema}\n    def discover(self, query):\n        return [t for t in self.tools if matches(query, t)]", "response": "Implement tool discovery registry"}]
            },
            {
                "title": "工具绑定 / Tool Binding",
                "description": "将工具绑定到LLM，支持函数调用和参数验证。",
                "description_en": "Bind tools to LLM supporting function calling and parameter validation.",
                "importance": 3,
                "key_concepts": ["Function Calling / 函数调用", "Parameter Validation / 参数验证", "Schema Binding / 模式绑定", "Type Coercion / 类型转换"],
                "examples": [{"title": "Tool Binding", "prompt": "def bind_tool(llm, tool_schema):\n    return llm.bind_tools([tool_schema])\n\ntool_schema = {\n    'name': 'search',\n    'parameters': {'query': {'type': 'string'}}\n}", "response": "Bind tool to LLM with schema"}]
            },
            {
                "title": "工具执行 / Tool Execution",
                "description": "安全执行工具调用，包括错误处理和结果解析。",
                "description_en": "Safely execute tool calls including error handling and result parsing.",
                "importance": 3,
                "key_concepts": ["Safe Execution / 安全执行", "Error Handling / 错误处理", "Result Parsing / 结果解析", "Timeout Management / 超时管理"],
                "examples": [{"title": "Tool Execution", "prompt": "async def execute_tool(tool, params, timeout=30):\n    try:\n        result = await asyncio.wait_for(\n            tool(**params), timeout=timeout\n        )\n        return {'success': True, 'result': result}\n    except Exception as e:\n        return {'success': False, 'error': str(e)}", "response": "Implement safe tool execution"}]
            }
        ],
        "terms": [
            {"term": "Tool Discovery", "term_cn": "工具发现", "definition": "动态发现可用工具的过程", "definition_en": "Process of dynamically discovering available tools"},
            {"term": "Function Calling", "term_cn": "函数调用", "definition": "LLM调用外部函数的能力", "definition_en": "LLM capability to call external functions"},
            {"term": "Tool Schema", "term_cn": "工具模式", "definition": "定义工具参数和返回值的JSON Schema", "definition_en": "JSON Schema defining tool parameters and return values"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "工具发现可以动态发现可用的API端点和函数。", "answer": "正确", "explanation": "工具发现支持动态发现各种可用工具。", "difficulty": 1},
            {"kp_index": 1, "type": "single_choice", "question": "工具绑定的主要作用是什么？", "options": ["A. 加快执行速度", "B. 支持函数调用和参数验证", "C. 减少内存使用", "D. 简化代码"], "answer": "B", "explanation": "工具绑定支持函数调用和参数验证。", "difficulty": 1}
        ]
    },
    "07_multi_agent_systems": {
        "title": "多Agent系统 / Multi-Agent Systems",
        "summary": "Learn multi-agent coordination, communication, and collaboration patterns. / 学习多Agent协调、通信和协作模式。",
        "knowledge_points": [
            {
                "title": "Agent 协调模式 / Agent Coordination Patterns",
                "description": "多Agent协调模式：层级式、对等式、混合式协调。",
                "description_en": "Multi-agent coordination patterns: hierarchical, peer-to-peer, and hybrid coordination.",
                "importance": 3,
                "key_concepts": ["Hierarchical / 层级式", "Peer-to-Peer / 对等式", "Hybrid / 混合式", "Orchestration / 编排"],
                "examples": [{"title": "Coordination Patterns", "prompt": "class Coordinator:\n    def __init__(self, agents):\n        self.agents = agents\n    def hierarchical_execute(self, task):\n        subtasks = self.decompose(task)\n        return [agent.execute(st) for agent, st in zip(self.agents, subtasks)]", "response": "Implement hierarchical coordination"}]
            },
            {
                "title": "Agent 通信协议 / Agent Communication Protocols",
                "description": "Agent间通信协议：消息传递、共享记忆、黑板模式。",
                "description_en": "Inter-agent communication protocols: message passing, shared memory, blackboard pattern.",
                "importance": 3,
                "key_concepts": ["Message Passing / 消息传递", "Shared Memory / 共享记忆", "Blackboard / 黑板模式", "Protocol Standards / 协议标准"],
                "examples": [{"title": "Communication Protocol", "prompt": "class AgentMessage:\n    sender: str\n    receiver: str\n    content: dict\n    timestamp: datetime\n\nclass MessageBus:\n    def send(self, msg: AgentMessage): self.queue.put(msg)\n    def receive(self, agent_id): return self.queue.get(agent_id)", "response": "Implement agent message passing"}]
            },
            {
                "title": "协作工作流 / Collaborative Workflows",
                "description": "设计Agent协作工作流，包括任务分解、结果聚合和冲突解决。",
                "description_en": "Design agent collaboration workflows including task decomposition, result aggregation, and conflict resolution.",
                "importance": 2,
                "key_concepts": ["Task Decomposition / 任务分解", "Result Aggregation / 结果聚合", "Conflict Resolution / 冲突解决", "Workflow Design / 工作流设计"],
                "examples": [{"title": "Collaborative Workflow", "prompt": "async def collaborative_workflow(task, agents):\n    subtasks = decompose(task)\n    results = await gather(*[a.execute(s) for a, s in zip(agents, subtasks)])\n    return aggregate(results)", "response": "Implement collaborative workflow"}]
            }
        ],
        "terms": [
            {"term": "Multi-Agent System", "term_cn": "多Agent系统", "definition": "多个Agent协作完成任务的系统", "definition_en": "System where multiple agents collaborate to complete tasks"},
            {"term": "Coordination Pattern", "term_cn": "协调模式", "definition": "Agent之间协调工作的模式", "definition_en": "Pattern for coordinating work between agents"},
            {"term": "Message Passing", "term_cn": "消息传递", "definition": "Agent之间通过消息通信", "definition_en": "Agents communicate through messages"}
        ],
        "questions": [
            {"kp_index": 0, "type": "multiple_choice", "question": "Agent协调模式包括哪些？", "options": ["A. 层级式", "B. 对等式", "C. 混合式", "D. 独立式"], "answer": "A,B,C", "explanation": "协调模式包括层级式、对等式和混合式。", "difficulty": 1},
            {"kp_index": 1, "type": "single_choice", "question": "Agent通信协议不包括以下哪种？", "options": ["A. 消息传递", "B. 共享记忆", "C. 直接调用", "D. 黑板模式"], "answer": "C", "explanation": "Agent通信通过消息传递、共享记忆或黑板模式。", "difficulty": 1}
        ]
    },
    "08_field_theory_integration": {
        "title": "场论整合 / Field Theory Integration",
        "summary": "Learn neural field theory and attractor dynamics for context engineering. / 学习上下文工程的神经场论和吸引子动力学。",
        "knowledge_points": [
            {
                "title": "神经场基础 / Neural Field Foundations",
                "description": "将上下文视为连续语义场，使用场论方法分析上下文动态。",
                "description_en": "View context as continuous semantic fields, using field theory methods to analyze context dynamics.",
                "importance": 3,
                "key_concepts": ["Semantic Field / 语义场", "Field Dynamics / 场动力学", "Continuous Representation / 连续表示", "Field Operators / 场算子"],
                "examples": [{"title": "Context Field", "prompt": "class ContextField:\n    def __init__(self, dimension=768):\n        self.field = np.zeros(dimension)\n    def inject(self, content, position):\n        self.field[position] += embed(content)\n    def read(self, position):\n        return self.field[position]", "response": "Implement context field representation"}]
            },
            {
                "title": "吸引子动力学 / Attractor Dynamics",
                "description": "上下文场中的吸引子形成稳定状态，影响信息检索和生成。",
                "description_en": "Attractors in context fields form stable states, affecting information retrieval and generation.",
                "importance": 3,
                "key_concepts": ["Attractor / 吸引子", "Stable States / 稳定状态", "Basin of Attraction / 吸引域", "Convergence / 收敛"],
                "examples": [{"title": "Attractor Dynamics", "prompt": "def find_attractor(field, initial_state, learning_rate=0.1):\n    state = initial_state\n    for _ in range(max_iterations):\n        gradient = compute_gradient(field, state)\n        state = state - learning_rate * gradient\n        if converged(state): break\n    return state", "response": "Implement attractor finding algorithm"}]
            },
            {
                "title": "场共振优化 / Field Resonance Optimization",
                "description": "优化上下文场的共振特性，增强语义连贯性。",
                "description_en": "Optimize resonance properties of context fields to enhance semantic coherence.",
                "importance": 2,
                "key_concepts": ["Resonance / 共振", "Semantic Coherence / 语义连贯性", "Field Harmonics / 场谐波", "Optimization / 优化"],
                "examples": [{"title": "Resonance Optimization", "prompt": "def optimize_resonance(field, target_coherence):\n    harmonics = compute_harmonics(field)\n    adjusted = adjust_amplitude(harmonics, target_coherence)\n    return reconstruct_field(adjusted)", "response": "Implement field resonance optimization"}]
            }
        ],
        "terms": [
            {"term": "Neural Field", "term_cn": "神经场", "definition": "将上下文表示为连续语义场", "definition_en": "Representing context as continuous semantic fields"},
            {"term": "Attractor", "term_cn": "吸引子", "definition": "场中形成稳定状态的区域", "definition_en": "Regions in field forming stable states"},
            {"term": "Field Resonance", "term_cn": "场共振", "definition": "场中语义成分的协调共振", "definition_en": "Coordinated resonance of semantic components in field"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "神经场论将上下文视为连续语义场。", "answer": "正确", "explanation": "神经场论使用连续场表示上下文。", "difficulty": 1},
            {"kp_index": 1, "type": "single_choice", "question": "吸引子动力学中的吸引子代表什么？", "options": ["A. 数据点", "B. 稳定状态", "C. 随机噪声", "D. 错误状态"], "answer": "B", "explanation": "吸引子代表场中的稳定状态。", "difficulty": 1}
        ]
    },
    "09_evaluation_methodologies": {
        "title": "评估方法论 / Evaluation Methodologies",
        "summary": "Learn evaluation metrics and methodologies for context engineering systems. / 学习上下文工程系统的评估指标和方法论。",
        "knowledge_points": [
            {
                "title": "评估指标 / Evaluation Metrics",
                "description": "上下文系统的评估指标：准确性、相关性、连贯性、效率。",
                "description_en": "Evaluation metrics for context systems: accuracy, relevance, coherence, efficiency.",
                "importance": 3,
                "key_concepts": ["Accuracy / 准确性", "Relevance / 相关性", "Coherence / 连贯性", "Efficiency / 效率"],
                "examples": [{"title": "Evaluation Metrics", "prompt": "def evaluate_context(context, query, response):\n    return {\n        'accuracy': compute_accuracy(response, ground_truth),\n        'relevance': compute_relevance(context, query),\n        'coherence': compute_coherence(context),\n        'efficiency': tokens_used / max_tokens\n    }", "response": "Implement context evaluation metrics"}]
            },
            {
                "title": "基准测试 / Benchmarking",
                "description": "使用标准基准测试评估上下文系统性能。",
                "description_en": "Evaluate context system performance using standard benchmarks.",
                "importance": 2,
                "key_concepts": ["Benchmark Datasets / 基准数据集", "Performance Baselines / 性能基线", "Comparative Analysis / 比较分析", "Metric Aggregation / 指标聚合"],
                "examples": [{"title": "Benchmarking", "prompt": "def run_benchmark(system, dataset):\n    results = []\n    for sample in dataset:\n        output = system.process(sample.input)\n        results.append(evaluate(output, sample.expected))\n    return aggregate_results(results)", "response": "Implement benchmark evaluation"}]
            }
        ],
        "terms": [
            {"term": "Evaluation Metric", "term_cn": "评估指标", "definition": "衡量系统性能的量化标准", "definition_en": "Quantitative standard measuring system performance"},
            {"term": "Benchmark", "term_cn": "基准测试", "definition": "用于评估系统性能的标准测试集", "definition_en": "Standard test set for evaluating system performance"}
        ],
        "questions": [
            {"kp_index": 0, "type": "multiple_choice", "question": "上下文系统评估指标包括哪些？", "options": ["A. 准确性", "B. 相关性", "C. 连贯性", "D. 代码行数"], "answer": "A,B,C", "explanation": "评估指标包括准确性、相关性和连贯性。", "difficulty": 1}
        ]
    },
    "10_meta_recursive_systems": {
        "title": "元递归系统 / Meta-Recursive Systems",
        "summary": "Learn self-improving and meta-learning systems for context engineering. / 学习上下文工程的自改进和元学习系统。",
        "knowledge_points": [
            {
                "title": "元学习 / Meta-Learning",
                "description": "系统学习如何学习，优化学习过程本身。",
                "description_en": "System learns how to learn, optimizing the learning process itself.",
                "importance": 3,
                "key_concepts": ["Learning to Learn / 学习如何学习", "Meta-Optimization / 元优化", "Few-Shot Adaptation / 少样本适应", "Transfer Learning / 迁移学习"],
                "examples": [{"title": "Meta-Learning", "prompt": "class MetaLearner:\n    def meta_train(self, tasks):\n        for task in tasks:\n            self.inner_loop(task)\n        self.meta_update()\n    def adapt(self, new_task, steps=5):\n        return self.fine_tune(new_task, steps)", "response": "Implement meta-learning system"}]
            },
            {
                "title": "自改进循环 / Self-Improvement Loops",
                "description": "系统通过反馈循环持续改进自身性能。",
                "description_en": "System continuously improves its own performance through feedback loops.",
                "importance": 3,
                "key_concepts": ["Feedback Loop / 反馈循环", "Self-Modification / 自修改", "Performance Tracking / 性能跟踪", "Improvement Rate / 改进率"],
                "examples": [{"title": "Self-Improvement", "prompt": "class SelfImproving:\n    def improve(self):\n        performance = self.evaluate()\n        feedback = self.analyze(performance)\n        self.modify(feedback)\n        return self.evaluate()", "response": "Implement self-improvement loop"}]
            }
        ],
        "terms": [
            {"term": "Meta-Learning", "term_cn": "元学习", "definition": "学习如何学习的学习方法", "definition_en": "Learning approach that learns how to learn"},
            {"term": "Self-Improvement", "term_cn": "自改进", "definition": "系统通过反馈持续改进自身", "definition_en": "System continuously improves itself through feedback"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "元学习的主要特点是什么？", "options": ["A. 学习更多数据", "B. 学习如何学习", "C. 学习更快", "D. 学习更少"], "answer": "B", "explanation": "元学习是学习如何学习的过程。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "自改进循环通过反馈持续改进系统性能。", "answer": "正确", "explanation": "自改进循环利用反馈持续优化系统。", "difficulty": 1}
        ]
    },
    "11_quantum_semantics": {
        "title": "量子语义 / Quantum Semantics",
        "summary": "Explore quantum-inspired approaches to semantic representation. / 探索量子启发的语义表示方法。",
        "knowledge_points": [
            {
                "title": "量子语义基础 / Quantum Semantics Foundations",
                "description": "使用量子力学概念建模语义歧义和上下文依赖。",
                "description_en": "Use quantum mechanics concepts to model semantic ambiguity and context dependency.",
                "importance": 2,
                "key_concepts": ["Superposition / 叠加态", "Entanglement / 纠缠", "Measurement / 测量", "Context Dependency / 上下文依赖"],
                "examples": [{"title": "Quantum Semantics", "prompt": "class QuantumSemantic:\n    def __init__(self):\n        self.state = superposition([meaning1, meaning2])\n    def measure(self, context):\n        return collapse(self.state, context)", "response": "Implement quantum semantic representation"}]
            },
            {
                "title": "语义叠加 / Semantic Superposition",
                "description": "语义状态在测量前处于多种含义的叠加态。",
                "description_en": "Semantic states exist in superposition of multiple meanings before measurement.",
                "importance": 2,
                "key_concepts": ["Meaning Superposition / 含义叠加", "Probability Amplitude / 概率幅", "Context Collapse / 上下文坍缩", "Ambiguity Resolution / 歧义消解"],
                "examples": [{"title": "Semantic Superposition", "prompt": "def semantic_superposition(word):\n    meanings = get_possible_meanings(word)\n    amplitudes = compute_probabilities(meanings)\n    return QuantumState(meanings, amplitudes)", "response": "Create semantic superposition state"}]
            }
        ],
        "terms": [
            {"term": "Quantum Semantics", "term_cn": "量子语义", "definition": "使用量子概念建模语义", "definition_en": "Modeling semantics using quantum concepts"},
            {"term": "Superposition", "term_cn": "叠加态", "definition": "多种状态同时存在的量子态", "definition_en": "Quantum state where multiple states exist simultaneously"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "量子语义使用量子概念建模语义歧义。", "answer": "正确", "explanation": "量子语义利用量子力学概念处理语义问题。", "difficulty": 1}
        ]
    },
    "12_interpretability": {
        "title": "可解释性 / Interpretability",
        "summary": "Learn interpretability methods for context engineering systems. / 学习上下文工程系统的可解释性方法。",
        "knowledge_points": [
            {
                "title": "可解释性方法 / Interpretability Methods",
                "description": "解释上下文系统决策的方法：注意力可视化、特征归因、反事实分析。",
                "description_en": "Methods to explain context system decisions: attention visualization, feature attribution, counterfactual analysis.",
                "importance": 3,
                "key_concepts": ["Attention Visualization / 注意力可视化", "Feature Attribution / 特征归因", "Counterfactual Analysis / 反事实分析", "Explanation Generation / 解释生成"],
                "examples": [{"title": "Interpretability", "prompt": "def explain_decision(context, decision):\n    attention_weights = get_attention(context)\n    important_tokens = get_top_tokens(attention_weights)\n    return generate_explanation(important_tokens, decision)", "response": "Implement decision explanation"}]
            },
            {
                "title": "透明度设计 / Transparency Design",
                "description": "设计透明的上下文系统，支持可审计和可解释的决策。",
                "description_en": "Design transparent context systems supporting auditable and explainable decisions.",
                "importance": 2,
                "key_concepts": ["Audit Trail / 审计跟踪", "Decision Logging / 决策日志", "Transparency Report / 透明度报告", "Human-in-the-Loop / 人在环中"],
                "examples": [{"title": "Transparency", "prompt": "class TransparentContext:\n    def __init__(self):\n        self.decision_log = []\n    def decide(self, context):\n        decision = self.model(context)\n        self.log_decision(context, decision)\n        return decision", "response": "Implement transparent context system"}]
            }
        ],
        "terms": [
            {"term": "Interpretability", "term_cn": "可解释性", "definition": "理解和解释系统决策的能力", "definition_en": "Ability to understand and explain system decisions"},
            {"term": "Feature Attribution", "term_cn": "特征归因", "definition": "确定哪些特征影响决策", "definition_en": "Determining which features influence decisions"}
        ],
        "questions": [
            {"kp_index": 0, "type": "multiple_choice", "question": "可解释性方法包括哪些？", "options": ["A. 注意力可视化", "B. 特征归因", "C. 反事实分析", "D. 数据加密"], "answer": "A,B,C", "explanation": "可解释性方法包括注意力可视化、特征归因和反事实分析。", "difficulty": 1}
        ]
    },
    "13_collaborative_evolution": {
        "title": "协作演化 / Collaborative Evolution",
        "summary": "Learn collaborative evolution patterns for multi-agent systems. / 学习多Agent系统的协作演化模式。",
        "knowledge_points": [
            {
                "title": "协作演化模式 / Collaborative Evolution Patterns",
                "description": "Agent群体通过协作演化提升整体能力。",
                "description_en": "Agent populations improve overall capabilities through collaborative evolution.",
                "importance": 2,
                "key_concepts": ["Population Evolution / 群体演化", "Collaborative Learning / 协作学习", "Emergent Behavior / 涌现行为", "Fitness Landscape / 适应度景观"],
                "examples": [{"title": "Collaborative Evolution", "prompt": "class CollaborativeEvolution:\n    def evolve(self, population, generations):\n        for gen in range(generations):\n            fitness = self.evaluate(population)\n            selected = self.select(population, fitness)\n            population = self.reproduce(selected)\n        return population", "response": "Implement collaborative evolution"}]
            },
            {
                "title": "涌现行为 / Emergent Behavior",
                "description": "从简单Agent交互中涌现出复杂智能行为。",
                "description_en": "Complex intelligent behaviors emerge from simple agent interactions.",
                "importance": 2,
                "key_concepts": ["Emergence / 涌现", "Complex Systems / 复杂系统", "Self-Organization / 自组织", "Collective Intelligence / 集体智能"],
                "examples": [{"title": "Emergence", "prompt": "def simulate_emergence(agents, interactions):\n    for _ in range(interactions):\n        pairs = random_pairs(agents)\n        for a1, a2 in pairs:\n            a1.interact(a2)\n    return measure_collective_behavior(agents)", "response": "Simulate emergent behavior"}]
            }
        ],
        "terms": [
            {"term": "Collaborative Evolution", "term_cn": "协作演化", "definition": "Agent群体通过协作提升能力", "definition_en": "Agent populations improve through collaboration"},
            {"term": "Emergent Behavior", "term_cn": "涌现行为", "definition": "从简单交互中涌现的复杂行为", "definition_en": "Complex behaviors emerging from simple interactions"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "协作演化通过群体协作提升整体能力。", "answer": "正确", "explanation": "协作演化使Agent群体通过协作提升能力。", "difficulty": 1}
        ]
    },
    "14_cross_modal_integration": {
        "title": "跨模态整合 / Cross-Modal Integration",
        "summary": "Learn cross-modal context integration for multimodal AI systems. / 学习多模态AI系统的跨模态上下文整合。",
        "knowledge_points": [
            {
                "title": "跨模态上下文 / Cross-Modal Context",
                "description": "整合文本、图像、音频等多模态信息到统一上下文表示。",
                "description_en": "Integrate text, image, audio and other modalities into unified context representation.",
                "importance": 3,
                "key_concepts": ["Multimodal Fusion / 多模态融合", "Cross-Modal Alignment / 跨模态对齐", "Unified Representation / 统一表示", "Modality Encoding / 模态编码"],
                "examples": [{"title": "Cross-Modal", "prompt": "class CrossModalContext:\n    def __init__(self):\n        self.text_encoder = TextEncoder()\n        self.image_encoder = ImageEncoder()\n    def integrate(self, text, image):\n        text_emb = self.text_encoder(text)\n        image_emb = self.image_encoder(image)\n        return self.fuse(text_emb, image_emb)", "response": "Implement cross-modal context integration"}]
            },
            {
                "title": "模态对齐 / Modality Alignment",
                "description": "对齐不同模态的语义空间，支持跨模态检索和生成。",
                "description_en": "Align semantic spaces of different modalities for cross-modal retrieval and generation.",
                "importance": 2,
                "key_concepts": ["Semantic Alignment / 语义对齐", "Shared Embedding Space / 共享嵌入空间", "Contrastive Learning / 对比学习", "Cross-Modal Retrieval / 跨模态检索"],
                "examples": [{"title": "Modality Alignment", "prompt": "def align_modalities(text_emb, image_emb):\n    aligned = contrastive_loss(text_emb, image_emb)\n    return aligned\n\ndef cross_modal_retrieve(query, modality, index):\n    return index.search(encode(query, modality))", "response": "Implement modality alignment"}]
            }
        ],
        "terms": [
            {"term": "Cross-Modal Integration", "term_cn": "跨模态整合", "definition": "整合多种模态信息到统一表示", "definition_en": "Integrating multiple modalities into unified representation"},
            {"term": "Multimodal Fusion", "term_cn": "多模态融合", "definition": "融合多种模态特征的方法", "definition_en": "Methods for fusing features from multiple modalities"}
        ],
        "questions": [
            {"kp_index": 0, "type": "multiple_choice", "question": "跨模态上下文整合涉及哪些模态？", "options": ["A. 文本", "B. 图像", "C. 音频", "D. 代码"], "answer": "A,B,C", "explanation": "跨模态整合包括文本、图像、音频等多种模态。", "difficulty": 1}
        ]
    },
    "15_future_directions": {
        "title": "未来方向 / Future Directions",
        "summary": "Explore future research directions in context engineering. / 探索上下文工程的未来研究方向。",
        "knowledge_points": [
            {
                "title": "前沿研究方向 / Frontier Research Directions",
                "description": "上下文工程的前沿研究方向：自适应上下文、神经符号整合、认知架构。",
                "description_en": "Frontier research directions in context engineering: adaptive context, neuro-symbolic integration, cognitive architectures.",
                "importance": 2,
                "key_concepts": ["Adaptive Context / 自适应上下文", "Neuro-Symbolic / 神经符号", "Cognitive Architecture / 认知架构", "Emergent Capabilities / 涌现能力"],
                "examples": [{"title": "Future Directions", "prompt": "future_directions = [\n    'adaptive_context_assembly',\n    'neuro_symbolic_integration',\n    'cognitive_architecture_design',\n    'emergent_capability_research'\n]", "response": "Define future research directions"}]
            },
            {
                "title": "开放挑战 / Open Challenges",
                "description": "上下文工程面临的开放挑战：可扩展性、鲁棒性、安全性。",
                "description_en": "Open challenges in context engineering: scalability, robustness, security.",
                "importance": 2,
                "key_concepts": ["Scalability / 可扩展性", "Robustness / 鲁棒性", "Security / 安全性", "Ethical Considerations / 伦理考量"],
                "examples": [{"title": "Open Challenges", "prompt": "challenges = {\n    'scalability': 'Context window expansion',\n    'robustness': 'Adversarial context attacks',\n    'security': 'Context injection prevention',\n    'ethics': 'Bias in context assembly'\n}", "response": "Define open challenges in context engineering"}]
            }
        ],
        "terms": [
            {"term": "Adaptive Context", "term_cn": "自适应上下文", "definition": "根据任务动态调整的上下文", "definition_en": "Context that dynamically adjusts based on tasks"},
            {"term": "Neuro-Symbolic", "term_cn": "神经符号", "definition": "结合神经网络和符号推理的方法", "definition_en": "Approach combining neural networks and symbolic reasoning"}
        ],
        "questions": [
            {"kp_index": 0, "type": "true_false", "question": "上下文工程的未来方向包括自适应上下文和神经符号整合。", "answer": "正确", "explanation": "这些是上下文工程的前沿研究方向。", "difficulty": 1}
        ]
    }
}

def create_course_material(module_name: str, course_data: dict) -> str:
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

This lesson covered key context engineering concepts. Practice these techniques to build robust context systems.

本课程涵盖了关键的上下文工程技术。练习这些技术以构建健壮的上下文系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Build your own context systems / 构建自己的上下文系统
3. Explore advanced patterns / 探索高级模式
"""
    return content

def batch_update_context_engineering_courses():
    print("Starting batch update of Context Engineering courses...")
    db = SessionLocal()
    
    try:
        ce_module = db.query(Module).filter(Module.name.like('%Context%')).first()
        if not ce_module:
            ce_module = Module(
                name="Context Engineering 上下文工程",
                description="Comprehensive context engineering course covering mathematical foundations to frontier research. / 全面覆盖数学基础到前沿研究的上下文工程课程。"
            )
            db.add(ce_module)
            db.commit()
            print(f"Created module: {ce_module.name}")
        else:
            print(f"Using existing module: {ce_module.name}")
        
        total_lessons = 0
        total_kps = 0
        total_terms = 0
        total_questions = 0
        
        for module_name, course_data in CONTEXT_ENGINEERING_COURSES_DATA.items():
            print(f"\nProcessing: {module_name}")
            
            existing_lesson = db.query(Lesson).filter(Lesson.title == course_data['title']).first()
            if existing_lesson:
                lesson = existing_lesson
                db.query(KnowledgePoint).filter(KnowledgePoint.lesson_id == lesson.id).delete()
                db.query(LessonTerm).filter(LessonTerm.lesson_id == lesson.id).delete()
                print(f"  Updating existing lesson: {lesson.title}")
            else:
                lesson = Lesson(
                    module_id=ce_module.id,
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
            
            material_content = create_course_material(module_name, course_data)
            material_filename = f"context_engineering_{module_name}.md"
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
                    category='context_engineering',
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
                        category='context_engineering',
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
    batch_update_context_engineering_courses()
