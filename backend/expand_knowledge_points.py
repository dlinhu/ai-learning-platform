import os
import sys
import json
from datetime import datetime

backend_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, backend_dir)

from app.utils.database import engine, SessionLocal, Base
from app.models.models import Module, Lesson, KnowledgePoint, Term, LessonTerm

from app.config import settings

EXPANDED_KNOWLEDGE_POINTS = {
    "原子提示 (Atomic Prompting)": {
        "related_knowledge": [
            "任务描述设计 (Task Description Design)",
            "约束条件定义 (Constraint Definition)",
            "输出格式规范 (Output Format Specification)",
            "提示词模板 (Prompt Templates)",
            "变量替换 (Variable Substitution)",
            "提示词组合 (Prompt Composition)",
            "提示词继承 (Prompt Inheritance)",
            "提示词验证 (Prompt Validation)",
            "提示词优化 (Prompt Optimization)",
            "提示词测试 (Prompt Testing)"
        ],
        "examples": [
            {
                "title": "简单任务提示",
                "prompt": "任务: 将以下文本翻译成英文\\n约束: 保持原意，使用正式语气\\n输出: 仅输出翻译结果\\n\\n文本: 你好，世界",
                "response": "Hello, world."
            },
            {
                "title": "带约束的生成任务",
                "prompt": "任务: 生成一篇关于AI的短文\\n约束: 100字以内，包含3个要点\\n输出: 带编号的要点列表",
                "response": "1. AI可以自动化重复任务\\n2. AI能够处理大量数据\\n3. AI提供智能决策支持"
            }
        ],
        "key_concepts": [
            "TASK - 明确告诉模型要做什么",
            "CONSTRAINTS - 限制模型的行为边界",
            "OUTPUT - 指定期望的结果格式",
            "清晰性 - 每个要素都要清晰无歧义",
            "完整性 - 三要素缺一不可"
        ],
        "common_mistakes": [
            "任务描述模糊 - 模型不知道具体要做什么",
            "约束条件缺失 - 输出可能不符合预期",
            "输出格式未指定 - 结果格式混乱",
            "三要素顺序混乱 - 影响模型理解",
            "过度复杂化 - 简单任务不需要复杂提示"
        ],
        "best_practices": [
            "使用模板确保三要素完整",
            "为每个要素设置明确的标记",
            "先写任务，再写约束，最后写输出",
            "使用示例验证提示效果",
            "迭代优化提示词"
        ]
    },
    "零样本学习 (Zero-shot Learning)": {
        "related_knowledge": [
            "少样本学习 (Few-shot Learning)",
            "上下文学习 (In-context Learning)",
            "提示词工程 (Prompt Engineering)",
            "模型泛化能力 (Model Generalization)",
            "预训练知识 (Pre-training Knowledge)",
            "迁移学习 (Transfer Learning)",
            "零样本分类 (Zero-shot Classification)",
            "零样本推理 (Zero-shot Reasoning)",
            "提示词设计 (Prompt Design)",
            "任务理解 (Task Understanding)"
        ],
        "examples": [
            {
                "title": "情感分析",
                "prompt": "分析以下句子的情感倾向(积极/消极/中性): '这个产品真是太棒了!'",
                "response": "积极"
            },
            {
                "title": "文本分类",
                "prompt": "将以下文本分类为新闻/广告/评论: '今日股市大涨5%'",
                "response": "新闻"
            }
        ],
        "key_concepts": [
            "无需示例 - 模型依靠预训练知识",
            "简单直接 - 提示词简洁明了",
            "依赖泛化 - 需要模型有良好的泛化能力",
            "快速迭代 - 可以快速测试不同提示",
            "基线方法 - 作为其他方法的对照"
        ],
        "common_mistakes": [
            "任务过于复杂 - 零样本可能效果不佳",
            "期望过高 - 复杂任务需要示例",
            "忽略模型能力 - 不同模型零样本能力不同",
            "提示词歧义 - 可能导致错误理解",
            "缺乏验证 - 不验证结果是否正确"
        ],
        "best_practices": [
            "从简单任务开始尝试零样本",
            "与Few-shot对比效果",
            "使用清晰的任务描述",
            "验证输出是否符合预期",
            "根据结果决定是否需要示例"
        ]
    },
    "少样本学习 (Few-shot Learning)": {
        "related_knowledge": [
            "零样本学习 (Zero-shot Learning)",
            "上下文学习 (In-context Learning)",
            "示例选择 (Example Selection)",
            "提示词工程 (Prompt Engineering)",
            "模式学习 (Pattern Learning)",
            "示例数量优化 (Example Count Optimization)",
            "示例多样性 (Example Diversity)",
            "示例格式设计 (Example Format Design)",
            "提示词长度 (Prompt Length)",
            "示例排序 (Example Ordering)"
        ],
        "examples": [
            {
                "title": "情感分析示例",
                "prompt": "分析情感倾向:\\n文本: '太棒了!' -> 积极\\n文本: '太差了!' -> 消极\\n文本: '还行吧' -> 中性\\n文本: '这个服务很好!' -> ?",
                "response": "积极"
            },
            {
                "title": "翻译示例",
                "prompt": "翻译成英文:\\n中文: '你好' -> Hello\\n中文: '谢谢' -> Thank you\\n中文: '再见' -> ?",
                "response": "Goodbye"
            }
        ],
        "key_concepts": [
            "示例数量 - 通常2-5个最佳",
            "示例多样性 - 覆盖不同情况",
            "示例格式 - 输入输出格式一致",
            "示例顺序 - 可能影响模型行为",
            "示例相关性 - 与任务直接相关"
        ],
        "common_mistakes": [
            "示例过多 - 占用上下文且可能干扰",
            "示例单一 - 无法覆盖不同情况",
            "示例无关 - 与任务不匹配",
            "格式混乱 - 示例格式不一致",
            "示例错误 - 包含错误的示例"
        ],
        "best_practices": [
            "选择代表性示例",
            "保持示例格式一致",
            "控制示例数量在2-5个",
            "确保示例正确性",
            "测试不同示例组合的效果"
        ]
    },
    "思维链 (Chain of Thought, CoT)": {
        "related_knowledge": [
            "零样本思维链 (Zero-shot CoT)",
            "少样本思维链 (Few-shot CoT)",
            "自洽性推理 (Self-Consistency)",
            "思维树 (Tree of Thoughts)",
            "思维图 (Graph of Thoughts)",
            "逐步推理 (Step-by-step Reasoning)",
            "分解推理 (Decomposition)",
            "验证推理 (Verification)",
            "回溯推理 (Backtracking)",
            "元推理 (Meta-Reasoning)"
        ],
        "examples": [
            {
                "title": "数学问题求解",
                "prompt": "问题: 小明有5个苹果,给了小红3个,又买了2个,请问小明现在有几个苹果?\\n让我们一步一步思考:",
                "response": "第一步: 小明原来有5个苹果\\n第二步: 给了小红3个,剩下 5-3=2 个\\n第三步: 又买了2个,现在有 2+2=4 个\\n答案: 小明现在有4个苹果"
            },
            {
                "title": "逻辑推理",
                "prompt": "所有猫都是动物。所有动物都需要水.因此,所有猫都需要水.\\n请验证这个推理:",
                "response": "让我们一步一步验证:\\n1. 前提1: 所有猫都是动物 ✓\\n2. 前提2: 所有动物都需要水 ✓\\n3. 结论: 所有猫都需要水 ✓\\n推理有效,因为结论是从前提中逻辑推导出来的."
            }
        ],
        "key_concepts": [
            "推理过程可视化 - 让模型的思考过程可见",
            "中间步骤生成 - 产生连接问题和答案的桥梁",
            "问题分解能力 - 将复杂问题拆解为简单步骤",
            "触发语敏感性 - 对特定短语如'一步一步'敏感",
            "上下文依赖性 - 推理质量依赖于上下文设置"
        ],
        "common_mistakes": [
            "过度依赖触发语 - 不是所有问题都需要CoT",
            "推理步骤冗余 - 添加不必要的步骤增加成本",
            "忽略问题类型 - 简单问题使用CoT反而复杂化",
            "缺乏验证机制 - 不检查推理步骤的正确性",
            "上下文过长 - 推理过程占用过多上下文空间"
        ],
        "best_practices": [
            "根据问题复杂度决定是否使用CoT",
            "结合Few-shot提供推理示例",
            "使用Self-Consistency验证重要推理",
            "设计清晰的步骤分隔符",
            "在关键步骤添加验证点"
        ]
    },
    "RAG基本原理": {
        "related_knowledge": [
            "向量数据库 (Vector Database)",
            "文本嵌入 (Text Embedding)",
            "语义检索 (Semantic Search)",
            "文档分块 (Document Chunking)",
            "上下文注入 (Context Injection)",
            "检索增强 (Retrieval Augmentation)",
            "知识库构建 (Knowledge Base Construction)",
            "检索优化 (Retrieval Optimization)",
            "生成增强 (Generation Enhancement)",
            "端到端RAG (End-to-End RAG)"
        ],
        "examples": [
            {
                "title": "简单RAG流程",
                "prompt": "用户问题: '什么是机器学习?'\\n检索相关文档...\\n构建增强提示...",
                "response": "1. 将问题转换为向量\\n2. 在向量数据库中检索相似文档\\n3. 将检索结果注入提示\\n4. LLM生成答案"
            }
        ],
        "key_concepts": [
            "检索-生成结合 - 先检索后生成",
            "知识可更新 - 不需要重新训练模型",
            "来源可追溯 - 答案可以追溯到文档",
            "减少幻觉 - 基于真实文档生成",
            "领域适应 - 可以快速适应新领域"
        ],
        "common_mistakes": [
            "检索质量差 - 找不到相关文档",
            "分块不合理 - 信息被切断",
            "上下文过长 - 超过模型窗口限制",
            "忽略查询理解 - 直接检索可能不准确",
            "缺乏重排序 - 检索结果顺序不佳"
        ],
        "best_practices": [
            "优化文档分块策略",
            "使用重排序提高相关性",
            "控制注入上下文长度",
            "验证检索结果相关性",
            "持续更新知识库"
        ]
    },
    "Agent定义": {
        "related_knowledge": [
            "自主决策 (Autonomous Decision)",
            "环境感知 (Environment Perception)",
            "目标导向 (Goal-oriented)",
            "工具使用 (Tool Usage)",
            "记忆系统 (Memory System)",
            "规划能力 (Planning Ability)",
            "执行能力 (Execution Ability)",
            "反思能力 (Reflection Ability)",
            "协作能力 (Collaboration)",
            "学习能力 (Learning Ability)"
        ],
        "examples": [
            {
                "title": "简单Agent示例",
                "prompt": "任务: 查找今天的天气并给出穿衣建议\\nAgent思考: 我需要先搜索天气信息...",
                "response": "1. 调用天气API获取信息\\n2. 分析温度和天气状况\\n3. 基于分析给出穿衣建议"
            }
        ],
        "key_concepts": [
            "自主性 - 能够独立做出决策",
            "反应性 - 能够感知和响应环境",
            "主动性 - 能够主动追求目标",
            "社交性 - 能够与其他Agent协作",
            "持续性 - 能够长期运行"
        ],
        "common_mistakes": [
            "过度自主 - Agent做出超出范围的决策",
            "缺乏约束 - 没有限制Agent的行为边界",
            "工具滥用 - 不必要地调用工具",
            "记忆丢失 - 忘记之前的交互",
            "目标漂移 - 偏离原始目标"
        ],
        "best_practices": [
            "设置清晰的目标和边界",
            "实现完善的记忆系统",
            "添加人工审核点",
            "监控Agent行为",
            "定期评估和优化"
        ]
    },
    "ReAct模式": {
        "related_knowledge": [
            "TAO循环 (Thought-Action-Observation)",
            "推理-行动结合 (Reasoning-Acting)",
            "工具调用 (Tool Calling)",
            "观察处理 (Observation Processing)",
            "迭代推理 (Iterative Reasoning)",
            "状态跟踪 (State Tracking)",
            "错误恢复 (Error Recovery)",
            "任务分解 (Task Decomposition)",
            "结果验证 (Result Verification)",
            "循环控制 (Loop Control)"
        ],
        "examples": [
            {
                "title": "搜索任务",
                "prompt": "任务: 查找Python最新版本\\nThought: 我需要搜索Python官网",
                "response": "Action: search('Python latest version')\\nObservation: 找到Python 3.12是最新版本\\nThought: 我已经得到答案\\nAction: finish('Python 3.12')"
            }
        ],
        "key_concepts": [
            "Thought - 思考当前状态和下一步",
            "Action - 执行工具或给出答案",
            "Observation - 获取执行结果",
            "循环 - 持续直到任务完成",
            "可解释性 - 推理过程清晰可见"
        ],
        "common_mistakes": [
            "无限循环 - 没有设置终止条件",
            "跳过思考 - 直接行动可能导致错误",
            "忽略观察 - 不处理工具返回结果",
            "过度推理 - 思考太多行动太少",
            "工具选择错误 - 调用不合适的工具"
        ],
        "best_practices": [
            "设置最大迭代次数",
            "每次迭代都进行思考",
            "仔细处理观察结果",
            "设计清晰的终止条件",
            "记录完整的推理链"
        ]
    },
    "MCP协议": {
        "related_knowledge": [
            "模型上下文 (Model Context)",
            "Server/Client架构",
            "工具标准化 (Tool Standardization)",
            "资源访问 (Resource Access)",
            "提示模板 (Prompt Templates)",
            "协议实现 (Protocol Implementation)",
            "Claude集成 (Claude Integration)",
            "工具发现 (Tool Discovery)",
            "能力协商 (Capability Negotiation)",
            "开放标准 (Open Standard)"
        ],
        "examples": [
            {
                "title": "MCP Server示例",
                "prompt": "创建一个提供文件读取能力的MCP Server",
                "response": "Server定义:\\n- Tool: read_file(path) -> content\\n- Resource: file://path -> content\\n- Prompt: '读取文件{path}'"
            }
        ],
        "key_concepts": [
            "标准化 - 统一的工具接口",
            "可插拔 - 一次开发多处使用",
            "资源抽象 - 统一的资源访问方式",
            "提示复用 - 预定义的提示模板",
            "开放生态 - 社区驱动的工具库"
        ],
        "common_mistakes": [
            "忽略协议版本 - 使用过时的API",
            "工具定义不清 - 描述不够详细",
            "资源路径错误 - 无法正确访问",
            "缺少错误处理 - 异常情况未处理",
            "性能问题 - 工具响应太慢"
        ],
        "best_practices": [
            "遵循最新协议规范",
            "提供详细的工具描述",
            "实现完善的错误处理",
            "优化工具响应速度",
            "添加使用示例"
        ]
    },
    "LangGraph": {
        "related_knowledge": [
            "状态图 (State Graph)",
            "节点设计 (Node Design)",
            "边定义 (Edge Definition)",
            "状态管理 (State Management)",
            "条件分支 (Conditional Branching)",
            "循环控制 (Loop Control)",
            "持久化 (Persistence)",
            "检查点 (Checkpointing)",
            "人机协作 (Human-in-the-loop)",
            "并行执行 (Parallel Execution)"
        ],
        "examples": [
            {
                "title": "简单工作流",
                "prompt": "创建一个简单的问答工作流",
                "response": "Graph定义:\\n- Node: understand_question\\n- Node: search_knowledge\\n- Node: generate_answer\\n- Edge: understand -> search\\n- Edge: search -> generate"
            }
        ],
        "key_concepts": [
            "状态传递 - 数据在节点间流动",
            "图结构 - 定义执行流程",
            "节点处理 - 每个节点的逻辑",
            "边条件 - 决定下一步走向",
            "状态更新 - 增量修改状态"
        ],
        "common_mistakes": [
            "状态设计不合理 - 太复杂或太简单",
            "节点粒度不当 - 过大或过小",
            "缺少终止条件 - 图无法结束",
            "边条件遗漏 - 某些情况无法处理",
            "状态不可变错误 - 直接修改状态"
        ],
        "best_practices": [
            "使用TypedDict定义状态",
            "设计合理的节点粒度",
            "设置明确的终止条件",
            "使用reducer更新状态",
            "添加检查点支持恢复"
        ]
    }
}

EXPANDED_TERMS = {
    "Prompt": {
        "detailed_definition": "提示词（Prompt）是用户输入给AI模型的指令或问题，用于引导模型生成期望的输出。它是人机交互的核心媒介，决定了模型理解任务和生成结果的方式。好的提示词应该清晰、具体、可执行。",
        "examples": [
            "\"翻译以下文本成英文：你好\"",
            "\"用简单的语言解释量子计算\"",
            "\"写一首关于春天的诗，四行，押韵\""
        ],
        "related_concepts": ["Prompt Engineering", "System Prompt", "User Prompt", "Prompt Template"],
        "usage_examples": [
            "设计清晰的提示词可以提高模型输出质量",
            "提示词应该包含任务、约束和输出格式",
            "避免模糊和多义的提示词"
        ]
    },
    "CoT": {
        "detailed_definition": "Chain of Thought（思维链）是一种提示工程技术，由Google在2022年提出。它通过让大语言模型在给出最终答案之前，先输出中间推理步骤，从而提高复杂问题的解决能力。这种方法特别适合数学推理、逻辑推理等需要多步思考的任务。",
        "examples": [
            "使用「让我们一步一步思考」触发CoT",
            "在数学问题中展示计算过程",
            "在逻辑推理中展示推理链条"
        ],
        "related_concepts": ["Zero-shot CoT", "Few-shot CoT", "Self-Consistency", "Tree of Thoughts"],
        "usage_examples": [
            "添加「让我们一步一步思考」激活思维链",
            "为复杂推理任务提供推理示例",
            "结合自洽性验证推理结果"
        ]
    },
    "RAG": {
        "detailed_definition": "Retrieval-Augmented Generation（检索增强生成）是一种结合信息检索和文本生成的AI技术。它首先从知识库中检索相关文档，然后将检索结果作为上下文输入LLM生成答案。这种方法可以有效减少幻觉，提高答案的准确性和可追溯性。",
        "examples": [
            "企业知识库问答系统",
            "基于文档的客服机器人",
            "法律条文检索和解释"
        ],
        "related_concepts": ["Vector Store", "Embedding", "Semantic Search", "Chunking"],
        "usage_examples": [
            "构建企业知识库问答系统",
            "实现基于文档的智能客服",
            "开发可追溯来源的AI助手"
        ]
    },
    "Agent": {
        "detailed_definition": "智能体（Agent）是能够感知环境、做出决策、执行行动的AI系统。与普通LLM不同，Agent具有自主性、反应性、主动性和社交性。它可以调用工具、维护记忆、进行规划，并在复杂环境中实现目标。",
        "examples": [
            "自动编程助手 - 分析需求、编写代码、测试",
            "研究助手 - 搜索、总结、报告",
            "个人助理 - 安排日程、回复邮件、预订"
        ],
        "related_concepts": ["ReAct", "Tool", "Memory", "Planning", "Multi-agent"],
        "usage_examples": [
            "构建能自主完成复杂任务的AI系统",
            "实现能调用外部工具的智能助手",
            "开发多Agent协作系统"
        ]
    },
    "MCP": {
        "detailed_definition": "Model Context Protocol（模型上下文协议）是Anthropic在2024年发布的开放协议，旨在标准化LLM与外部数据源、工具的交互方式。它被称为AI模型的「万能插座」，解决了不同工具集成的碎片化问题，让一次开发的工具可以在所有兼容客户端使用。",
        "examples": [
            "Claude Desktop连接文件系统MCP Server",
            "开发自定义MCP Server提供API访问",
            "使用社区MCP Server访问数据库"
        ],
        "related_concepts": ["Tool", "Function Calling", "Server/Client", "Protocol"],
        "usage_examples": [
            "为Claude开发自定义工具",
            "构建标准化的AI工具接口",
            "实现工具的可插拔和复用"
        ]
    }
}

def init_db():
    print("Recreating database tables...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

def expand_knowledge_points():
    print("Expanding knowledge points...")
    db = SessionLocal()
    
    try:
        modules_data = [
            {"name": "Prompts 提示词工程", "order": 1, "lessons": [
                {"title": "原子 + 零/少样本", "topics": ["TASK+CONSTRAINTS+OUTPUT", "Zero-shot vs Few-shot", "分子提示"], "summary": "本课程介绍提示词工程的基础概念，包括原子提示的三大要素（任务、约束、输出格式），以及零样本学习和少样本学习的区别与应用场景。"},
                {"title": "CoT + 角色 + 约束 + 自洽", "topics": ["思维链", "Role/Persona", "约束生成", "Self-Consistency"], "summary": "本课程深入探讨高级提示技术，包括思维链推理、角色扮演、约束生成和自洽性方法,帮助学员掌握复杂任务的提示设计技巧。"},
                {"title": "指令 + 任务分解 + 提示链", "topics": ["清晰指令", "复杂任务拆解", "多步串联"], "summary": "本课程介绍如何设计清晰的指令、将复杂任务分解为子任务，以及通过提示链串联多个步骤完成复杂工作流程。"},
                {"title": "记忆 + 控制循环 + 认知", "topics": ["Cells of Context", "多步控制", "认知模板"], "summary": "本课程探讨上下文记忆单元、控制循环机制和认知模板的设计,帮助学员理解如何构建具有记忆和控制能力的复杂提示系统。"},
                {"title": "提示编程 + 优化 + Schema + 小结", "topics": ["类代码推理", "Prompt 优化", "Schema 设计", "评估"], "summary": "本课程总结提示工程的高级技术,包括类代码推理、提示优化方法、Schema设计和评估技术,帮助学员掌握系统化的提示工程方法论。"}
            ]},
            {"name": "RAG 检索增强生成", "order": 2, "lessons": [
                {"title": "RAG 原理 + Simple RAG", "topics": ["检索-生成流程", "RAG基础理论", "动手实践"], "summary": "本课程介绍RAG（检索增强生成）的基本原理,包括检索-生成的完整流程,以及如何实现一个简单的RAG系统。"},
                {"title": "分块 + Reliable RAG", "topics": ["Chunk size", "语义分块", "相关性验证"], "summary": "本课程深入探讨文档分块策略和如何构建可靠的RAG系统,包括分块大小选择、语义分块技术和相关性验证方法。"},
                {"title": "查询变换 + HyDE", "topics": ["Query Rewriting", "Step-back", "假设文档生成"], "summary": "本课程介绍查询优化技术,包括查询重写、后退提示和假设文档嵌入（HyDE）,帮助提高检索的准确性和召回率。"},
                {"title": "Reranking + Fusion + 上下文压缩", "topics": ["重排序", "向量+关键词融合", "Token 优化"], "summary": "本课程介绍高级检索优化技术,包括重排序、多路融合检索和上下文压缩,帮助提高检索质量和效率。"},
                {"title": "长上下文 + 压缩策略", "topics": ["长文档处理", "128K/200K 窗口", "压缩策略"], "summary": "本课程探讨如何处理长文档和利用大上下文窗口,以及各种上下文压缩策略。"},
                {"title": "RAG 评估 + 小结", "topics": ["评估清单", "Token 预算", "端到端设计"], "summary": "本课程总结RAG模块内容,介绍RAG系统评估方法和端到端设计最佳实践。"}
            ]},
            {"name": "Agent 智能体", "order": 3, "lessons": [
                {"title": "Agent 概念 + Organs + Function Calling", "topics": ["多 AI 协作", "Orchestrator", "工具调用基础"], "summary": "本课程介绍AI Agent的基本概念,包括Agent架构、多AI协作模式和Function Calling机制。"},
                {"title": "简单对话 + ReAct Agent", "topics": ["对话 Agent", "ReAct 模式", "工具调用"], "summary": "本课程介绍如何构建对话Agent和ReAct模式的Agent,这是Agent开发的基础模式。"},
                {"title": "Tools 详解", "topics": ["自定义 Tool", "Web 工具"], "summary": "本课程深入探讨工具的设计和实现,包括自定义工具开发和Web工具集成。"},
                {"title": "MCP 模型上下文协议", "topics": ["Server/Client", "工具与资源标准化"], "summary": "本课程介绍Anthropic提出的MCP协议,这是AI模型与外部系统交互的标准化方案。"},
                {"title": "LangGraph", "topics": ["StateGraph", "工作流编排"], "summary": "本课程介绍LangGraph框架,这是构建复杂Agent工作流的强大工具。"},
                {"title": "Memory", "topics": ["短期/长期记忆", "记忆架构"], "summary": "本课程探讨Agent的记忆系统,包括短期记忆、长期记忆和各种记忆架构设计。"},
                {"title": "多 Agent 系统", "topics": ["通信协议", "编排机制", "Supervisor/Subagent"], "summary": "本课程介绍多Agent系统的设计和实现,包括Agent间通信、编排机制和Supervisor模式。"}
            ]},
            {"name": "PROD 生产落地", "order": 4, "lessons": [
                {"title": "安全 + 可观测", "topics": ["Guardrails", "LangSmith Tracing"], "summary": "本课程介绍AI系统生产环境中的安全防护和可观测性建设。"},
                {"title": "生产级 Memory + API", "topics": ["Redis", "FastAPI", "Docker"], "summary": "本课程介绍生产环境的Memory存储、API开发和容器化部署。"},
                {"title": "评估 + UI + 流式输出", "topics": ["IntellAgent评估", "Streamlit", "Streaming/SSE"], "summary": "本课程介绍Agent评估方法、UI开发和流式输出技术。"},
                {"title": "生产安全评估 + GPU 部署", "topics": ["安全测试", "云端GPU部署"], "summary": "本课程介绍生产环境的安全评估和GPU部署策略。"}
            ]},
            {"name": "收尾与弹性", "order": 5, "lessons": [
                {"title": "Neural Fields", "topics": ["神经场理论", "连续场建模", "语义空间"], "summary": "本课程介绍神经场理论,探讨如何用连续场模型来理解语义空间。"},
                {"title": "Field Theory Integration", "topics": ["场论整合", "吸引子动力学", "场共振"], "summary": "本课程整合场论概念,探讨Context、Memory、Agent的统一框架。"},
                {"title": "Quantum Semantics", "topics": ["量子语义", "不确定性", "叠加态"], "summary": "本课程探讨量子力学概念在语义理解中的应用。"},
                {"title": "Unified Field", "topics": ["统一场理论", "演化与动力学"], "summary": "本课程总结场论模块,提出Context/Memory/Agent的统一框架。"}
            ]}
        ]
        
        for mod_data in modules_data:
            module = Module(
                name=mod_data["name"],
                description=f"{mod_data['name']} - AI培训课程",
                order_index=mod_data["order"]
            )
            db.add(module)
            db.flush()
            
            print(f"\nModule {mod_data['order']}: {mod_data['name']}")
            
            for idx, lesson_data in enumerate(mod_data["lessons"]):
                date = f"2026-03-{16 + idx:02d}" if mod_data["order"] == 1 else f"2026-0{mod_data['order'] + 2}-{idx + 1:02d}"
                
                lesson = Lesson(
                    module_id=module.id,
                    date=date,
                    title=lesson_data["title"],
                    topics=lesson_data["topics"],
                    difficulty="basic",
                    time_estimate=60,
                    materials=[],
                    summary=lesson_data["summary"],
                    raw_content=lesson_data["summary"]
                )
                db.add(lesson)
                db.flush()
                
                kp_data_list = get_knowledge_points_for_lesson(lesson_data["title"])
                term_data_list = get_terms_for_lesson(lesson_data["title"])
                
                for kp_data in kp_data_list:
                    expanded = EXPANDED_KNOWLEDGE_POINTS.get(kp_data["title"], {})
                    kp = KnowledgePoint(
                        lesson_id=lesson.id,
                        title=kp_data["title"],
                        description=kp_data["description"],
                        category=kp_data["category"],
                        importance=kp_data["importance"],
                        related_terms=kp_data.get("related_terms", []),
                        related_knowledge=expanded.get("related_knowledge", []),
                        examples=expanded.get("examples", []),
                        key_concepts=expanded.get("key_concepts", []),
                        common_mistakes=expanded.get("common_mistakes", []),
                        best_practices=expanded.get("best_practices", []),
                        external_links=expanded.get("external_links", [])
                    )
                    db.add(kp)
                
                for term_data in term_data_list:
                    expanded = EXPANDED_TERMS.get(term_data["term"], {})
                    existing_term = db.query(Term).filter(Term.term == term_data["term"]).first()
                    
                    if not existing_term:
                        existing_term = Term(
                            term=term_data["term"],
                            definition=term_data["definition"],
                            category=term_data["category"],
                            examples=expanded.get("examples", []),
                            related_terms=term_data.get("related_terms", []),
                            external_links=expanded.get("external_links", []),
                            is_predefined=True,
                            detailed_definition=expanded.get("detailed_definition", term_data["definition"]),
                            related_concepts=expanded.get("related_concepts", []),
                            usage_examples=expanded.get("usage_examples", [])
                        )
                        db.add(existing_term)
                        db.flush()
                    
                    lesson_term = LessonTerm(
                        lesson_id=lesson.id,
                        term_id=existing_term.id
                    )
                    db.add(lesson_term)
                
                print(f"  - {lesson_data['title']}: {len(kp_data_list)} knowledge points, {len(term_data_list)} terms")
        
        db.commit()
        print("\nKnowledge points expanded successfully!")
        
        modules_count = db.query(Module).count()
        lessons_count = db.query(Lesson).count()
        kp_count = db.query(KnowledgePoint).count()
        terms_count = db.query(Term).count()
        
        print(f"\nStatistics:")
        print(f"  Modules: {modules_count}")
        print(f"  Lessons: {lessons_count}")
        print(f"  Knowledge Points: {kp_count}")
        print(f"  Terms: {terms_count}")
        
    except Exception as e:
        print(f"Error expanding knowledge points: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

def get_knowledge_points_for_lesson(lesson_title):
    kp_map = {
        "原子 + 零/少样本": [
            {"title": "原子提示 (Atomic Prompting)", "description": "原子提示是提示词的最小组成单元,包含三个核心要素:TASK(任务描述)、CONSTRAINTS(约束条件)、OUTPUT(输出格式)。好的原子提示应该清晰、具体、可执行。", "category": "prompt_engineering", "importance": 3},
            {"title": "零样本学习 (Zero-shot Learning)", "description": "零样本学习是指模型在没有示例的情况下,仅通过任务描述就能完成任务。这种方式依赖模型的预训练知识和泛化能力。优点是简单直接,缺点是对于复杂任务可能效果不佳。", "category": "prompt_engineering", "importance": 3},
            {"title": "少样本学习 (Few-shot Learning)", "description": "少样本学习通过提供少量示例帮助模型理解任务要求。通常2-5个示例效果最佳。示例应该覆盖不同的输入输出模式,帮助模型建立正确的任务理解。", "category": "prompt_engineering", "importance": 3},
            {"title": "分子提示 (Molecular Prompting)", "description": "分子提示是由多个原子提示组合而成的复杂提示结构。通过组合不同的原子,可以构建处理复杂任务的提示链。分子提示体现了提示的组合性和层次性。", "category": "prompt_engineering", "importance": 2},
            {"title": "提示词设计原则", "description": "好的提示词应该遵循:清晰性(任务描述明确)、具体性(避免模糊表达)、可验证性(输出可检验)、简洁性(避免冗余)。这些原则是提示工程的基础。", "category": "prompt_engineering", "importance": 2}
        ],
        "CoT + 角色 + 约束 + 自洽": [
            {"title": "思维链 (Chain of Thought, CoT)", "description": "思维链是一种让模型逐步展示推理过程的技术。2022年Google提出,通过让模型在给出最终答案前先输出中间推理步骤,大幅提高了复杂问题的解决能力。常用触发语:「让我们一步一步思考」。", "category": "prompt_engineering", "importance": 3},
            {"title": "角色提示 (Role Prompting)", "description": "通过指定模型扮演特定角色来引导其输出风格和内容。例如「你是一位经验丰富的软件架构师」。角色设定可以影响模型的语气、专业程度和回答角度。", "category": "prompt_engineering", "importance": 2},
            {"title": "约束生成 (Constrained Generation)", "description": "通过明确的约束条件限制模型的输出范围和格式。约束可以是格式约束(如JSON输出)、内容约束(如字数限制)、风格约束(如正式语气)等。", "category": "prompt_engineering", "importance": 2},
            {"title": "自洽性 (Self-Consistency)", "description": "通过多次采样取一致性结果的方法。对同一问题生成多个推理路径,然后选择最一致的答案。这种方法可以显著提高推理任务的准确性。", "category": "prompt_engineering", "importance": 2},
            {"title": "Zero-shot CoT", "description": "零样本思维链,不需要示例,只需添加「让我们一步一步思考」等触发语即可激活模型的推理能力。这是一种简单但强大的技术。", "category": "prompt_engineering", "importance": 2}
        ],
        "RAG 原理 + Simple RAG": [
            {"title": "RAG基本原理", "description": "RAG(Retrieval-Augmented Generation)是一种结合信息检索和文本生成的技术。它首先从知识库检索相关文档,然后将检索结果作为上下文输入LLM生成答案。这种方法可以有效减少幻觉,提高答案的准确性和可追溯性。", "category": "rag", "importance": 3},
            {"title": "向量数据库", "description": "向量数据库专门用于存储和检索向量。常用的有Pinecone、Weaviate、Chroma、FAISS等。选择时需考虑性能、扩展性、易用性等因素。", "category": "rag", "importance": 2},
            {"title": "Embedding模型", "description": "Embedding模型将文本转换为向量表示。常用的有OpenAI的text-embedding-ada-002、Sentence Transformers等。好的Embedding是RAG效果的基础。", "category": "rag", "importance": 2},
            {"title": "语义检索", "description": "语义检索基于向量相似度而非关键词匹配。可以找到语义相关但词汇不同的内容,是RAG的核心检索方式。", "category": "rag", "importance": 2},
            {"title": "Simple RAG架构", "description": "最简单的RAG实现包括:文档切分、向量化存储、相似度检索、上下文注入、答案生成。适合快速原型开发和学习理解。", "category": "rag", "importance": 2}
        ],
        "Agent 概念 + Organs + Function Calling": [
            {"title": "AI Agent定义", "description": "AI Agent是能够感知环境、做出决策、执行行动的智能系统。与普通LLM不同,Agent具有:自主性(独立决策)、反应性(响应环境变化)、主动性(主动追求目标)、社交性(与其他Agent协作)。", "category": "agent", "importance": 3},
            {"title": "Function Calling", "description": "Function Calling是LLM调用外部函数的能力。模型输出结构化的函数调用请求,由系统执行后返回结果。这是Agent与外部世界交互的核心机制。OpenAI、Anthropic等都支持此功能。", "category": "agent", "importance": 3},
            {"title": "Organs架构", "description": "Organs是Agent的组织架构模型,将Agent比作生物器官:感知器官(接收输入)、大脑(推理决策)、手脚(执行工具)、记忆(存储信息)。这种类比帮助理解Agent的组件和协作方式。", "category": "agent", "importance": 2},
            {"title": "工具定义", "description": "定义工具需要指定:名称、描述、参数Schema。好的工具定义应该清晰描述功能、参数含义和返回格式。工具粒度要适中,过细增加复杂度,过粗降低灵活性。", "category": "agent", "importance": 2},
            {"title": "Orchestrator编排器", "description": "Orchestrator是协调多个Agent或工具的中心组件。负责:任务分解、分配、执行监控、结果整合。好的编排器是构建复杂Agent系统的关键。", "category": "agent", "importance": 2}
        ],
        "MCP 模型上下文协议": [
            {"title": "MCP协议概述", "description": "MCP(Model Context Protocol)是Anthropic在2024年11月发布的开放协议,旨在标准化LLM与外部数据源、工具的交互方式。被称为AI模型的「万能插座」,解决了不同工具集成的碎片化问题。", "category": "agent", "importance": 3},
            {"title": "MCP架构", "description": "MCP采用Client-Server架构:MCP Client(如Claude Desktop)连接MCP Server(提供工具和资源)。Server可以提供:Tools(可调用的函数)、Resources(可访问的数据)、Prompts(预定义的提示模板)。", "category": "agent", "importance": 3},
            {"title": "MCP Server开发", "description": "开发MCP Server需要:定义工具和资源、实现处理逻辑、遵循MCP协议规范。可以使用Python、TypeScript等语言的SDK快速开发。Server可以是本地服务或远程服务。", "category": "agent", "importance": 2},
            {"title": "MCP vs 传统工具集成", "description": "传统方式:每个应用需要单独集成每个工具。MCP方式:一次开发,所有兼容Client可用。这大大降低了集成成本,促进了工具生态的发展。", "category": "agent", "importance": 2},
            {"title": "MCP生态系统", "description": "MCP正在快速发展:官方提供了文件系统、数据库、GitHub等Server;社区贡献了更多工具。未来可能成为AI工具集成的标准协议。", "category": "agent", "importance": 2}
        ],
        "LangGraph": [
            {"title": "LangGraph概述", "description": "LangGraph是LangChain团队开发的Agent编排框架,基于图状态机构建。与传统的链式结构不同,LangGraph支持循环、分支、并行等复杂控制流,适合构建生产级Agent系统。", "category": "agent", "importance": 3},
            {"title": "StateGraph概念", "description": "StateGraph是LangGraph的核心概念:图由节点(处理函数)和边(转换条件)组成,状态在节点间传递和更新。每个节点可以访问和修改状态,决定下一步走向。", "category": "agent", "importance": 3},
            {"title": "节点和边", "description": "节点是处理逻辑的单元,接收状态、处理数据、返回更新。边定义节点间的转换:条件边(根据状态选择路径)、普通边(固定转换)。图的定义决定了Agent的行为。", "category": "agent", "importance": 2},
            {"title": "状态管理", "description": "状态是图执行过程中传递的数据结构。LangGraph使用TypedDict定义状态Schema,支持增量更新(reducer)。状态设计是Agent架构的关键。", "category": "agent", "importance": 2},
            {"title": "持久化和恢复", "description": "LangGraph支持检查点和持久化:可以保存执行状态、暂停和恢复执行、实现人机协作。这对于长时间运行的Agent非常重要。", "category": "agent", "importance": 2}
        ],
        "简单对话 + ReAct Agent": [
            {"title": "ReAct模式", "description": "ReAct(Reasoning and Acting)是一种结合推理和行动的Agent模式。它通过Thought-Action-Observation循环,让Agent能够边思考边行动,实现复杂任务的自动化执行。", "category": "agent", "importance": 3},
            {"title": "对话Agent", "description": "对话Agent是能够进行多轮对话的智能体。它需要维护对话历史、理解用户意图、生成合适的回复,是Agent应用的基础形式。", "category": "agent", "importance": 2},
            {"title": "TAO循环", "description": "TAO循环是ReAct模式的核心:Thought(思考当前状态)、Action(执行行动)、Observation(获取结果)。通过这个循环,Agent可以持续执行直到任务完成。", "category": "agent", "importance": 3},
            {"title": "工具调用流程", "description": "工具调用流程包括:识别需要调用的工具、准备调用参数、执行工具、处理返回结果。这是Agent与外部世界交互的关键机制。", "category": "agent", "importance": 2},
            {"title": "循环终止条件", "description": "ReAct Agent需要设置循环终止条件,包括:任务完成、达到最大迭代次数、遇到错误。合理的终止条件可以防止无限循环。", "category": "agent", "importance": 2}
        ]
    }
    return kp_map.get(lesson_title, [
        {"title": "知识点1", "description": "描述1", "category": "general", "importance": 1},
        {"title": "知识点2", "description": "描述2", "category": "general", "importance": 1}
    ])

def get_terms_for_lesson(lesson_title):
    term_map = {
        "原子 + 零/少样本": [
            {"term": "Prompt", "definition": "提示词,用户输入给AI模型的指令或问题,用于引导模型生成期望的输出。", "category": "prompt_engineering"},
            {"term": "Zero-shot", "definition": "零样本学习,模型在没有示例的情况下完成任务的能力。", "category": "prompt_engineering"},
            {"term": "Few-shot", "definition": "少样本学习,通过少量示例帮助模型理解任务要求的技术。", "category": "prompt_engineering"},
            {"term": "In-context Learning", "definition": "上下文学习,模型从提示词中的上下文信息学习任务模式的能力。", "category": "prompt_engineering"},
            {"term": "Task Description", "definition": "任务描述,提示词中明确说明需要模型完成什么任务的部分。", "category": "prompt_engineering"}
        ],
        "CoT + 角色 + 约束 + 自洽": [
            {"term": "CoT", "definition": "Chain of Thought,思维链,一种让模型逐步展示推理过程的技术。", "category": "prompt_engineering"},
            {"term": "Role Prompting", "definition": "角色提示,通过指定模型扮演特定角色来引导输出。", "category": "prompt_engineering"},
            {"term": "Self-consistency", "definition": "自洽性,通过多次采样取一致性结果的方法。", "category": "prompt_engineering"},
            {"term": "Persona", "definition": "人格设定,为AI模型设定的特定身份和特征。", "category": "prompt_engineering"},
            {"term": "Reasoning", "definition": "推理,模型进行逻辑思考和得出结论的过程。", "category": "prompt_engineering"}
        ],
        "RAG 原理 + Simple RAG": [
            {"term": "RAG", "definition": "Retrieval-Augmented Generation,检索增强生成,结合检索和生成的AI技术。", "category": "rag"},
            {"term": "Embedding", "definition": "嵌入,将文本转换为向量表示的过程。", "category": "rag"},
            {"term": "Vector Store", "definition": "向量存储,专门存储和检索向量的数据库系统。", "category": "rag"},
            {"term": "Semantic Search", "definition": "语义搜索,基于语义相似度而非关键词匹配的搜索方式。", "category": "rag"},
            {"term": "Retrieval", "definition": "检索,从知识库中查找相关信息的过程。", "category": "rag"}
        ],
        "Agent 概念 + Organs + Function Calling": [
            {"term": "Agent", "definition": "智能体,能够自主执行任务的AI系统。", "category": "agent"},
            {"term": "Function Calling", "definition": "函数调用,LLM调用外部函数的能力。", "category": "agent"},
            {"term": "Tool", "definition": "工具,Agent可以调用的外部功能。", "category": "agent"},
            {"term": "Orchestrator", "definition": "编排器,协调多个Agent的中心组件。", "category": "agent"},
            {"term": "Autonomous", "definition": "自主的,能够独立决策和行动的能力。", "category": "agent"}
        ],
        "MCP 模型上下文协议": [
            {"term": "MCP", "definition": "Model Context Protocol,模型上下文协议,AI工具集成标准。", "category": "agent"},
            {"term": "Protocol", "definition": "协议,通信和数据交换的规范。", "category": "agent"},
            {"term": "Server", "definition": "服务器,提供服务的程序。", "category": "agent"},
            {"term": "Client", "definition": "客户端,请求服务的程序。", "category": "agent"},
            {"term": "Standardization", "definition": "标准化,制定统一规范的过程。", "category": "agent"}
        ],
        "LangGraph": [
            {"term": "LangGraph", "definition": "LangChain的图状态机框架,用于构建复杂Agent。", "category": "agent"},
            {"term": "StateGraph", "definition": "状态图,基于状态的图结构。", "category": "agent"},
            {"term": "Node", "definition": "节点,图中的处理单元。", "category": "agent"},
            {"term": "Edge", "definition": "边,节点间的连接和转换。", "category": "agent"},
            {"term": "Workflow", "definition": "工作流,任务执行的定义和编排。", "category": "agent"}
        ]
    }
    return term_map.get(lesson_title, [
        {"term": "Term1", "definition": "定义1", "category": "general"},
        {"term": "Term2", "definition": "定义2", "category": "general"}
    ])

if __name__ == "__main__":
    init_db()
    expand_knowledge_points()
