import os
import sys
from datetime import datetime

backend_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, backend_dir)

from app.utils.database import engine, SessionLocal, Base
from app.models.models import Module, Lesson, KnowledgePoint, Term, LessonTerm, PracticeQuestion

PRACTICE_QUESTIONS = {
    "原子提示 (Atomic Prompting)": [
        {
            "type": "single_choice",
            "question": "原子提示的三个核心要素是什么？",
            "options": ["A. 输入、处理、输出", "B. TASK、CONSTRAINTS、OUTPUT", "C. 问题、分析、答案", "D. 数据、模型、结果"],
            "answer": "B",
            "explanation": "原子提示包含三个核心要素：TASK(任务描述)、CONSTRAINTS(约束条件)、OUTPUT(输出格式)。这三个要素缺一不可，共同构成完整的提示指令。",
            "difficulty": 1
        },
        {
            "type": "single_choice",
            "question": "在原子提示中，TASK要素的作用是什么？",
            "options": ["A. 限制模型行为边界", "B. 明确告诉模型要做什么", "C. 指定输出结果格式", "D. 提供示例参考"],
            "answer": "B",
            "explanation": "TASK(任务描述)的作用是明确告诉模型要做什么，让模型清楚理解任务目标。",
            "difficulty": 1
        },
        {
            "type": "true_false",
            "question": "原子提示中，约束条件是可选的，不是必须的。",
            "options": ["正确", "错误"],
            "answer": "错误",
            "explanation": "原子提示的三个要素(TASK、CONSTRAINTS、OUTPUT)都是必须的，约束条件用于限制模型的行为边界，确保输出符合预期。",
            "difficulty": 1
        },
        {
            "type": "fill_blank",
            "question": "原子提示的三要素是：____、____、____。",
            "options": [],
            "answer": "TASK|CONSTRAINTS|OUTPUT|任务|约束|输出",
            "explanation": "原子提示包含TASK(任务描述)、CONSTRAINTS(约束条件)、OUTPUT(输出格式)三个核心要素。",
            "difficulty": 1
        },
        {
            "type": "single_choice",
            "question": "以下哪个是好的原子提示示例？",
            "options": ["A. 帮我写点东西", "B. 写一篇文章", "C. 任务：写一篇关于AI的短文；约束：100字以内，包含3个要点；输出：带编号的要点列表", "D. 写一篇AI文章，字数不限"],
            "answer": "C",
            "explanation": "选项C包含了完整的三个要素：任务(写短文)、约束(100字、3要点)、输出格式(编号列表)，是一个标准的原子提示。",
            "difficulty": 2
        },
        {
            "type": "multiple_choice",
            "question": "原子提示的优点包括哪些？",
            "options": ["A. 结构清晰", "B. 易于验证", "C. 可复用", "D. 自动执行"],
            "answer": "A,B,C",
            "explanation": "原子提示具有结构清晰、易于验证结果、可复用等优点。但它本身不能自动执行，需要模型来处理。",
            "difficulty": 2
        },
        {
            "type": "short_answer",
            "question": "请解释为什么原子提示需要包含约束条件？",
            "options": [],
            "answer": "限制,边界,范围,控制,符合预期",
            "explanation": "约束条件用于限制模型的行为边界，防止输出偏离预期，确保结果符合特定要求(如格式、长度、风格等)。",
            "difficulty": 2
        },
        {
            "type": "single_choice",
            "question": "OUTPUT要素主要解决什么问题？",
            "options": ["A. 告诉模型做什么", "B. 限制模型行为", "C. 指定期望的结果格式", "D. 提供背景信息"],
            "answer": "C",
            "explanation": "OUTPUT(输出格式)要素用于指定期望的结果格式，让模型知道应该以什么样的形式输出答案。",
            "difficulty": 1
        }
    ],
    "零样本学习 (Zero-shot Learning)": [
        {
            "type": "single_choice",
            "question": "零样本学习的主要特点是什么？",
            "options": ["A. 需要大量训练数据", "B. 不需要示例就能完成任务", "C. 必须提供多个示例", "D. 只能处理简单任务"],
            "answer": "B",
            "explanation": "零样本学习的核心特点是不需要示例，模型仅通过任务描述就能完成任务，依赖预训练知识和泛化能力。",
            "difficulty": 1
        },
        {
            "type": "true_false",
            "question": "零样本学习比少样本学习效果一定更好。",
            "options": ["正确", "错误"],
            "answer": "错误",
            "explanation": "零样本学习不一定比少样本学习效果好。对于复杂任务，少样本学习通常效果更好，因为示例能帮助模型更好地理解任务。",
            "difficulty": 1
        },
        {
            "type": "single_choice",
            "question": "零样本学习最适合什么类型的任务？",
            "options": ["A. 复杂推理任务", "B. 简单分类任务", "C. 需要特定格式的任务", "D. 多步骤任务"],
            "answer": "B",
            "explanation": "零样本学习最适合简单、直接的任务，如简单分类。复杂任务通常需要示例或思维链来提高效果。",
            "difficulty": 1
        },
        {
            "type": "fill_blank",
            "question": "零样本学习依赖模型的____能力和____知识。",
            "options": [],
            "answer": "泛化|预训练|generalization|pre-training",
            "explanation": "零样本学习依赖模型的泛化能力和预训练知识，这是模型在没有示例情况下完成任务的基础。",
            "difficulty": 2
        },
        {
            "type": "multiple_choice",
            "question": "零样本学习的优点有哪些？",
            "options": ["A. 简单直接", "B. 节省token", "C. 适合快速测试", "D. 效果一定最好"],
            "answer": "A,B,C",
            "explanation": "零样本学习的优点包括简单直接、节省token(不需要示例)、适合快速测试。但效果不一定最好，复杂任务可能需要示例。",
            "difficulty": 2
        },
        {
            "type": "short_answer",
            "question": "什么情况下应该选择零样本学习而不是少样本学习？",
            "options": [],
            "answer": "简单,快速,测试,token,基础",
            "explanation": "当任务简单直接、需要快速测试、或想节省token时，可以选择零样本学习。如果效果不佳再考虑添加示例。",
            "difficulty": 2
        }
    ],
    "少样本学习 (Few-shot Learning)": [
        {
            "type": "single_choice",
            "question": "少样本学习中，通常建议使用多少个示例？",
            "options": ["A. 1个", "B. 2-5个", "C. 10个以上", "D. 越多越好"],
            "answer": "B",
            "explanation": "少样本学习通常建议使用2-5个示例。示例太少可能不够，太多会占用上下文且可能干扰模型。",
            "difficulty": 1
        },
        {
            "type": "true_false",
            "question": "少样本学习中的示例越多，效果一定越好。",
            "options": ["正确", "错误"],
            "answer": "错误",
            "explanation": "示例不是越多越好。过多示例会占用上下文空间，增加成本，且可能干扰模型理解。通常2-5个效果最佳。",
            "difficulty": 1
        },
        {
            "type": "single_choice",
            "question": "少样本学习示例应该具备什么特点？",
            "options": ["A. 越复杂越好", "B. 代表性强、格式一致", "C. 随机选择即可", "D. 数量最重要"],
            "answer": "B",
            "explanation": "少样本学习的示例应该具有代表性，能覆盖不同情况，且格式保持一致，帮助模型建立正确的任务理解。",
            "difficulty": 2
        },
        {
            "type": "multiple_choice",
            "question": "设计少样本学习示例时应该注意什么？",
            "options": ["A. 示例格式一致", "B. 示例内容正确", "C. 覆盖不同情况", "D. 示例越难越好"],
            "answer": "A,B,C",
            "explanation": "设计示例时应注意：格式一致、内容正确、覆盖不同情况。示例难度应与实际任务匹配，不是越难越好。",
            "difficulty": 2
        },
        {
            "type": "fill_blank",
            "question": "少样本学习通过提供____帮助模型理解任务要求。",
            "options": [],
            "answer": "示例|例子|example|样本",
            "explanation": "少样本学习通过提供少量示例，帮助模型理解任务的输入输出模式和要求。",
            "difficulty": 1
        },
        {
            "type": "short_answer",
            "question": "为什么少样本学习比零样本学习在某些任务上效果更好？",
            "options": [],
            "answer": "示例,理解,模式,学习,参考",
            "explanation": "少样本学习通过示例让模型更清楚地理解任务要求和期望的输出模式，特别是对于复杂或特定格式的任务。",
            "difficulty": 2
        }
    ],
    "思维链 (Chain of Thought, CoT)": [
        {
            "type": "single_choice",
            "question": "思维链(CoT)技术最早由谁提出？",
            "options": ["A. OpenAI", "B. Google", "C. Anthropic", "D. Meta"],
            "answer": "B",
            "explanation": "思维链(Chain of Thought)技术由Google在2022年提出，是一种让模型逐步展示推理过程的技术。",
            "difficulty": 1
        },
        {
            "type": "single_choice",
            "question": "以下哪个是激活思维链的常用触发语？",
            "options": ["A. 请快速回答", "B. 让我们一步一步思考", "C. 简短回答", "D. 只给答案"],
            "answer": "B",
            "explanation": "'让我们一步一步思考'是激活思维链的常用触发语，让模型在给出最终答案前先输出中间推理步骤。",
            "difficulty": 1
        },
        {
            "type": "true_false",
            "question": "思维链技术对所有类型的任务都有帮助。",
            "options": ["正确", "错误"],
            "answer": "错误",
            "explanation": "思维链主要对需要推理的复杂任务有帮助，如数学问题、逻辑推理。对于简单任务，使用CoT反而会增加不必要的复杂度。",
            "difficulty": 2
        },
        {
            "type": "multiple_choice",
            "question": "思维链技术适合哪些类型的任务？",
            "options": ["A. 数学计算", "B. 逻辑推理", "C. 简单分类", "D. 多步骤问题"],
            "answer": "A,B,D",
            "explanation": "思维链适合需要推理的任务：数学计算、逻辑推理、多步骤问题。简单分类任务通常不需要CoT。",
            "difficulty": 2
        },
        {
            "type": "fill_blank",
            "question": "思维链的核心思想是让模型在给出最终答案前先输出____步骤。",
            "options": [],
            "answer": "推理|中间|思考|reasoning|intermediate",
            "explanation": "思维链的核心思想是让模型在给出最终答案前先输出中间推理步骤，使推理过程可见。",
            "difficulty": 1
        },
        {
            "type": "short_answer",
            "question": "请简述思维链技术的主要优势。",
            "options": [],
            "answer": "推理,可见,准确,复杂,验证",
            "explanation": "思维链的主要优势包括：使推理过程可见、提高复杂问题的准确性、便于验证和调试、帮助发现推理错误。",
            "difficulty": 2
        },
        {
            "type": "single_choice",
            "question": "Zero-shot CoT和Few-shot CoT的主要区别是什么？",
            "options": ["A. 使用不同的模型", "B. 是否提供推理示例", "C. 输出格式不同", "D. 任务类型不同"],
            "answer": "B",
            "explanation": "Zero-shot CoT只使用触发语激活推理，Few-shot CoT则提供推理示例来引导模型的推理方式。",
            "difficulty": 2
        }
    ],
    "RAG基本原理": [
        {
            "type": "single_choice",
            "question": "RAG的全称是什么？",
            "options": ["A. Retrieval-Augmented Generation", "B. Reading and Generation", "C. Random Access Generation", "D. Rule-based AI Generation"],
            "answer": "A",
            "explanation": "RAG全称是Retrieval-Augmented Generation（检索增强生成），是一种结合信息检索和文本生成的技术。",
            "difficulty": 1
        },
        {
            "type": "single_choice",
            "question": "RAG的主要作用是什么？",
            "options": ["A. 训练新模型", "B. 减少幻觉，提高准确性", "C. 加快推理速度", "D. 减少存储空间"],
            "answer": "B",
            "explanation": "RAG通过检索相关文档作为上下文，可以有效减少模型幻觉，提高答案的准确性和可追溯性。",
            "difficulty": 1
        },
        {
            "type": "true_false",
            "question": "RAG需要重新训练语言模型才能使用新知识。",
            "options": ["正确", "错误"],
            "answer": "错误",
            "explanation": "RAG的优势之一就是不需要重新训练模型，只需更新知识库文档即可使用新知识。",
            "difficulty": 1
        },
        {
            "type": "multiple_choice",
            "question": "RAG系统的核心组件包括哪些？",
            "options": ["A. 向量数据库", "B. Embedding模型", "C. 大语言模型", "D. 图形处理器"],
            "answer": "A,B,C",
            "explanation": "RAG系统核心组件包括：向量数据库(存储向量)、Embedding模型(文本向量化)、大语言模型(生成答案)。",
            "difficulty": 2
        },
        {
            "type": "fill_blank",
            "question": "RAG的工作流程是：先____相关文档，再____答案。",
            "options": [],
            "answer": "检索|生成|retrieve|generate|搜索",
            "explanation": "RAG的工作流程是：先从知识库检索相关文档，再将检索结果作为上下文输入LLM生成答案。",
            "difficulty": 1
        },
        {
            "type": "short_answer",
            "question": "RAG相比传统微调方法有什么优势？",
            "options": [],
            "answer": "更新,成本,追溯,幻觉,知识",
            "explanation": "RAG的优势包括：知识可更新(无需重新训练)、成本更低、答案可追溯到来源、减少幻觉、可快速适应新领域。",
            "difficulty": 2
        }
    ],
    "AI Agent定义": [
        {
            "type": "single_choice",
            "question": "AI Agent与普通LLM的主要区别是什么？",
            "options": ["A. 参数量更大", "B. 能够自主决策和执行行动", "C. 响应速度更快", "D. 只能回答问题"],
            "answer": "B",
            "explanation": "AI Agent的核心特点是能够自主决策、感知环境、执行行动，而普通LLM只能被动回答问题。",
            "difficulty": 1
        },
        {
            "type": "multiple_choice",
            "question": "AI Agent具有哪些核心特性？",
            "options": ["A. 自主性", "B. 反应性", "C. 主动性", "D. 社交性"],
            "answer": "A,B,C,D",
            "explanation": "AI Agent具有四大核心特性：自主性(独立决策)、反应性(响应环境)、主动性(追求目标)、社交性(与其他Agent协作)。",
            "difficulty": 2
        },
        {
            "type": "true_false",
            "question": "Agent只能单独工作，不能与其他Agent协作。",
            "options": ["正确", "错误"],
            "answer": "错误",
            "explanation": "Agent具有社交性，可以与其他Agent协作完成复杂任务，这是多Agent系统的基础。",
            "difficulty": 1
        },
        {
            "type": "single_choice",
            "question": "以下哪个不是Agent的典型组件？",
            "options": ["A. 感知模块", "B. 决策模块", "C. 执行模块", "D. 训练模块"],
            "answer": "D",
            "explanation": "Agent的典型组件包括感知、决策、执行、记忆等模块。训练模块不是Agent运行时的组件。",
            "difficulty": 2
        },
        {
            "type": "fill_blank",
            "question": "Agent能够调用____来与外部世界交互。",
            "options": [],
            "answer": "工具|Tool|API|函数",
            "explanation": "Agent通过调用工具(Tool/API/函数)来与外部世界交互，执行各种任务。",
            "difficulty": 1
        },
        {
            "type": "short_answer",
            "question": "请简述Agent的自主性是什么意思。",
            "options": [],
            "answer": "独立,决策,人工,自动,目标",
            "explanation": "Agent的自主性指能够独立做出决策和行动，不需要人工干预就能完成目标。",
            "difficulty": 2
        }
    ],
    "ReAct模式": [
        {
            "type": "single_choice",
            "question": "ReAct模式中的'ReAct'代表什么？",
            "options": ["A. Read and Act", "B. Reasoning and Acting", "C. Request and Action", "D. Response and Activity"],
            "answer": "B",
            "explanation": "ReAct代表Reasoning and Acting（推理与行动），是一种结合推理和行动的Agent模式。",
            "difficulty": 1
        },
        {
            "type": "multiple_choice",
            "question": "ReAct模式的三个核心步骤是什么？",
            "options": ["A. Thought(思考)", "B. Action(行动)", "C. Observation(观察)", "D. Training(训练)"],
            "answer": "A,B,C",
            "explanation": "ReAct模式包含三个核心步骤：Thought(思考当前状态)、Action(执行行动)、Observation(获取结果)，形成TAO循环。",
            "difficulty": 2
        },
        {
            "type": "true_false",
            "question": "ReAct模式中，Agent可以跳过思考步骤直接行动。",
            "options": ["正确", "错误"],
            "answer": "错误",
            "explanation": "ReAct模式强调每次行动前都要思考，跳过思考可能导致错误的行动选择。",
            "difficulty": 1
        },
        {
            "type": "single_choice",
            "question": "ReAct模式的主要优势是什么？",
            "options": ["A. 执行速度最快", "B. 推理过程可解释", "C. 不需要工具", "D. 只能处理简单任务"],
            "answer": "B",
            "explanation": "ReAct模式的主要优势是推理过程清晰可见，每一步思考都有记录，便于理解和调试。",
            "difficulty": 2
        },
        {
            "type": "fill_blank",
            "question": "ReAct模式通过____循环持续执行直到任务完成。",
            "options": [],
            "answer": "TAO|Thought-Action-Observation|思考-行动-观察",
            "explanation": "ReAct模式通过Thought-Action-Observation(TAO)循环持续执行，直到任务完成。",
            "difficulty": 2
        },
        {
            "type": "short_answer",
            "question": "为什么ReAct模式需要设置最大迭代次数？",
            "options": [],
            "answer": "循环,终止,无限,限制,安全",
            "explanation": "设置最大迭代次数是为了防止Agent陷入无限循环，确保任务能在合理时间内终止。",
            "difficulty": 2
        }
    ],
    "MCP协议概述": [
        {
            "type": "single_choice",
            "question": "MCP协议是由哪家公司提出的？",
            "options": ["A. OpenAI", "B. Google", "C. Anthropic", "D. Microsoft"],
            "answer": "C",
            "explanation": "MCP(Model Context Protocol)是由Anthropic在2024年11月提出的开放协议。",
            "difficulty": 1
        },
        {
            "type": "single_choice",
            "question": "MCP协议的主要目的是什么？",
            "options": ["A. 训练新模型", "B. 标准化LLM与工具的交互", "C. 加快推理速度", "D. 减少存储需求"],
            "answer": "B",
            "explanation": "MCP协议的目的是标准化LLM与外部数据源、工具的交互方式，被称为AI模型的'万能插座'。",
            "difficulty": 1
        },
        {
            "type": "multiple_choice",
            "question": "MCP Server可以提供哪些类型的资源？",
            "options": ["A. Tools(工具)", "B. Resources(资源)", "C. Prompts(提示模板)", "D. Models(模型)"],
            "answer": "A,B,C",
            "explanation": "MCP Server可以提供Tools(可调用的函数)、Resources(可访问的数据)、Prompts(预定义的提示模板)。",
            "difficulty": 2
        },
        {
            "type": "true_false",
            "question": "MCP协议是闭源的，只能由Anthropic使用。",
            "options": ["正确", "错误"],
            "answer": "错误",
            "explanation": "MCP是一个开放协议，任何人都可以开发兼容的Server和Client，促进工具生态发展。",
            "difficulty": 1
        },
        {
            "type": "fill_blank",
            "question": "MCP采用____架构，Client连接Server获取能力。",
            "options": [],
            "answer": "Client-Server|客户端-服务器|CS",
            "explanation": "MCP采用Client-Server架构，MCP Client(如Claude Desktop)连接MCP Server获取工具和资源。",
            "difficulty": 1
        },
        {
            "type": "short_answer",
            "question": "MCP协议相比传统工具集成方式有什么优势？",
            "options": [],
            "answer": "标准,复用,一次,兼容,生态",
            "explanation": "MCP的优势是标准化接口，一次开发的工具可以在所有兼容Client使用，降低集成成本，促进生态发展。",
            "difficulty": 2
        }
    ],
    "LangGraph概述": [
        {
            "type": "single_choice",
            "question": "LangGraph是由哪个团队开发的？",
            "options": ["A. OpenAI", "B. LangChain", "C. Anthropic", "D. Google"],
            "answer": "B",
            "explanation": "LangGraph是由LangChain团队开发的Agent编排框架，基于图状态机构建。",
            "difficulty": 1
        },
        {
            "type": "single_choice",
            "question": "LangGraph的核心概念是什么？",
            "options": ["A. 链式结构", "B. StateGraph(状态图)", "C. 线性流程", "D. 单一节点"],
            "answer": "B",
            "explanation": "LangGraph的核心概念是StateGraph(状态图)，图由节点和边组成，状态在节点间传递和更新。",
            "difficulty": 1
        },
        {
            "type": "multiple_choice",
            "question": "LangGraph支持哪些控制流？",
            "options": ["A. 循环", "B. 分支", "C. 并行", "D. 只支持线性"],
            "answer": "A,B,C",
            "explanation": "LangGraph支持循环、分支、并行等复杂控制流，这是相比传统链式结构的优势。",
            "difficulty": 2
        },
        {
            "type": "true_false",
            "question": "LangGraph中的状态是不可变的，不能被修改。",
            "options": ["正确", "错误"],
            "answer": "错误",
            "explanation": "LangGraph中的状态可以被节点修改，但应该通过reducer函数进行增量更新，而不是直接修改。",
            "difficulty": 2
        },
        {
            "type": "fill_blank",
            "question": "LangGraph中的边分为普通边和____边。",
            "options": [],
            "answer": "条件|conditional",
            "explanation": "LangGraph中的边分为普通边(固定转换)和条件边(根据状态选择路径)。",
            "difficulty": 2
        },
        {
            "type": "short_answer",
            "question": "LangGraph的持久化功能有什么作用？",
            "options": [],
            "answer": "保存,恢复,暂停,人机,检查点",
            "explanation": "持久化功能可以保存执行状态、支持暂停和恢复执行、实现人机协作，对长时间运行的Agent很重要。",
            "difficulty": 2
        }
    ]
}

def init_db():
    print("Recreating database tables...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

def load_practice_questions():
    print("Loading practice questions...")
    db = SessionLocal()
    
    try:
        knowledge_points = db.query(KnowledgePoint).all()
        kp_dict = {kp.title: kp for kp in knowledge_points}
        
        total_questions = 0
        
        for kp_title, questions in PRACTICE_QUESTIONS.items():
            if kp_title in kp_dict:
                kp = kp_dict[kp_title]
                
                for idx, q_data in enumerate(questions):
                    question = PracticeQuestion(
                        knowledge_point_id=kp.id,
                        question_type=q_data["type"],
                        question_text=q_data["question"],
                        options=q_data.get("options", []),
                        correct_answer=q_data["answer"],
                        explanation=q_data.get("explanation", ""),
                        difficulty=q_data.get("difficulty", 1),
                        order_index=idx
                    )
                    db.add(question)
                    total_questions += 1
                
                print(f"  {kp_title}: {len(questions)} questions")
            else:
                print(f"  Warning: Knowledge point '{kp_title}' not found")
        
        db.commit()
        print(f"\nTotal practice questions loaded: {total_questions}")
        
    except Exception as e:
        print(f"Error loading practice questions: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
    
    from expand_knowledge_points import expand_knowledge_points
    expand_knowledge_points()
    
    load_practice_questions()
