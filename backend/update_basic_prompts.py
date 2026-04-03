import os
import sys

backend_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, backend_dir)

from app.utils.database import SessionLocal
from app.models.models import Lesson, KnowledgePoint, Term, LessonTerm, PracticeQuestion

BASIC_PROMPTS_KNOWLEDGE_POINTS = [
    {
        "title": "Single-turn Prompts / 单轮提示",
        "description": "单轮提示是与语言模型的一次性交互，由单个输入（提示）组成，生成单个输出（响应）。适用于快速、独立的查询，交互之间不维护上下文。",
        "description_en": "Single-turn prompts are one-shot interactions with the language model. They consist of a single input (prompt) and generate a single output (response). Useful for quick, straightforward queries with no context maintained between interactions.",
        "category": "prompt_engineering",
        "importance": 3,
        "related_knowledge": ["Multi-turn Prompts", "Prompt Templates", "Zero-shot Learning"],
        "key_concepts": [
            "One-shot interaction / 一次性交互",
            "No context memory / 无上下文记忆",
            "Isolated queries / 独立查询",
            "Simple input-output / 简单输入输出"
        ],
        "examples": [
            {
                "title": "Basic Single-turn Prompt / 基础单轮提示",
                "prompt": "single_turn_prompt = \"What are the three primary colors?\"\nprint(llm.invoke(single_turn_prompt).content)",
                "response": "The three primary colors are red, blue, and yellow..."
            }
        ],
        "common_mistakes": [
            "Expecting context retention in single-turn prompts / 期望单轮提示保持上下文",
            "Using single-turn for multi-step reasoning / 对多步骤推理使用单轮提示",
            "Not providing complete information in each prompt / 每个提示中未提供完整信息"
        ],
        "best_practices": [
            "Use for isolated, independent queries / 用于独立查询",
            "Provide all necessary context in the prompt / 在提示中提供所有必要上下文",
            "Consider multi-turn for follow-up questions / 对追问考虑使用多轮提示"
        ]
    },
    {
        "title": "Prompt Templates / 提示模板",
        "description": "提示模板是可复用的结构化提示模式，允许使用变量对提示进行参数化，实现一致性提示格式和可重复的提示模式。",
        "description_en": "Prompt Templates are reusable structures for consistent prompting. They allow parameterization of prompts with variables, enabling consistent formatting across multiple calls and repeatable prompt patterns.",
        "category": "prompt_engineering",
        "importance": 3,
        "related_knowledge": ["Single-turn Prompts", "LangChain", "Prompt Engineering"],
        "key_concepts": [
            "Reusability / 可复用性",
            "Variable parameterization / 变量参数化",
            "Consistent formatting / 一致性格式",
            "Template patterns / 模板模式"
        ],
        "examples": [
            {
                "title": "Using PromptTemplate / 使用提示模板",
                "prompt": "structured_prompt = PromptTemplate(\n    input_variables=[\"topic\"],\n    template=\"Provide a brief explanation of {topic} and list its three main components.\"\n)\nchain = structured_prompt | llm\nprint(chain.invoke({\"topic\": \"color theory\"}).content)",
                "response": "Color theory is a framework used to understand how colors interact..."
            }
        ],
        "common_mistakes": [
            "Hardcoding values instead of using variables / 硬编码值而不是使用变量",
            "Not validating input variables / 不验证输入变量",
            "Overly complex templates / 过于复杂的模板"
        ],
        "best_practices": [
            "Use clear variable names / 使用清晰的变量名",
            "Keep templates focused and simple / 保持模板专注和简单",
            "Document expected variables / 记录期望的变量"
        ]
    },
    {
        "title": "Multi-turn Prompts / 多轮提示",
        "description": "多轮提示是维护上下文的一系列交互，允许更复杂、具有上下文感知的对话。每个后续提示都可以引用之前的交流内容，是构建对话式AI应用的基础。",
        "description_en": "Multi-turn prompts involve a series of interactions that maintain context, allowing for more complex, context-aware conversations. Each subsequent prompt can reference previous exchanges, essential for building conversational AI applications.",
        "category": "prompt_engineering",
        "importance": 3,
        "related_knowledge": ["Single-turn Prompts", "Conversation Memory", "ConversationChain"],
        "key_concepts": [
            "Context maintenance / 上下文维护",
            "Conversation history / 对话历史",
            "Follow-up questions / 追问",
            "Context-aware responses / 上下文感知响应"
        ],
        "examples": [
            {
                "title": "Multi-turn Conversation / 多轮对话",
                "prompt": "conversation = ConversationChain(\n    llm=llm,\n    verbose=True,\n    memory=ConversationBufferMemory()\n)\nprint(conversation.predict(input=\"What is the capital of France?\"))\nprint(conversation.predict(input=\"What is its population?\"))",
                "response": "The capital of France is Paris!... As of my last update, the population of Paris is approximately 2.1 million..."
            }
        ],
        "common_mistakes": [
            "Not using memory with ConversationChain / 不在ConversationChain中使用记忆",
            "Overloading conversation history / 过载对话历史",
            "Ignoring token limits / 忽略token限制"
        ],
        "best_practices": [
            "Use appropriate memory type for your use case / 为你的用例使用合适的记忆类型",
            "Consider token limits for long conversations / 考虑长对话的token限制",
            "Clear or summarize history when needed / 需要时清除或总结历史"
        ]
    },
    {
        "title": "Conversation Memory / 对话记忆",
        "description": "ConversationBufferMemory存储整个对话历史，使模型能够引用之前的交流内容，是维护连贯多轮对话的关键组件，允许追问而无需重复上下文。",
        "description_en": "ConversationBufferMemory stores the entire conversation history, enabling the model to reference previous exchanges. It's critical for maintaining coherent multi-turn conversations and allows follow-up questions without repeating context.",
        "category": "prompt_engineering",
        "importance": 2,
        "related_knowledge": ["Multi-turn Prompts", "ConversationChain", "LangChain Memory"],
        "key_concepts": [
            "ConversationBufferMemory / 对话缓冲记忆",
            "History storage / 历史存储",
            "Context reference / 上下文引用",
            "Memory types / 记忆类型"
        ],
        "examples": [
            {
                "title": "Using ConversationBufferMemory / 使用对话缓冲记忆",
                "prompt": "from langchain.memory import ConversationBufferMemory\n\nmemory = ConversationBufferMemory()\nconversation = ConversationChain(llm=llm, memory=memory)",
                "response": "Memory will store all conversation turns for context retrieval."
            }
        ],
        "common_mistakes": [
            "Using ConversationBufferMemory for very long conversations / 对很长对话使用ConversationBufferMemory",
            "Not clearing memory when starting new topic / 开始新话题时不清除记忆",
            "Ignoring memory window limits / 忽略记忆窗口限制"
        ],
        "best_practices": [
            "Choose appropriate memory type / 选择合适的记忆类型",
            "Implement memory management strategies / 实现记忆管理策略",
            "Consider ConversationBufferWindowMemory for long chats / 对长对话考虑使用ConversationBufferWindowMemory"
        ]
    },
    {
        "title": "ConversationChain / 对话链",
        "description": "ConversationChain是LangChain中用于管理多轮对话的组件，自动处理对话历史和上下文传递，简化了对话式应用的开发。",
        "description_en": "ConversationChain is a LangChain component for managing multi-turn conversations. It automatically handles conversation history and context passing, simplifying the development of conversational applications.",
        "category": "prompt_engineering",
        "importance": 2,
        "related_knowledge": ["Multi-turn Prompts", "Conversation Memory", "LangChain Chains"],
        "key_concepts": [
            "Chain abstraction / 链抽象",
            "Automatic context handling / 自动上下文处理",
            "Memory integration / 记忆集成",
            "Verbose mode / 详细模式"
        ],
        "examples": [
            {
                "title": "Creating a ConversationChain / 创建对话链",
                "prompt": "conversation = ConversationChain(\n    llm=llm,\n    verbose=True,  # Shows internal prompt processing\n    memory=ConversationBufferMemory()\n)",
                "response": "Creates a conversation chain with memory and verbose output."
            }
        ],
        "common_mistakes": [
            "Forgetting to add memory / 忘记添加记忆",
            "Not using verbose mode for debugging / 调试时不使用详细模式",
            "Using deprecated ConversationChain / 使用已弃用的ConversationChain"
        ],
        "best_practices": [
            "Always include memory for context retention / 始终包含记忆以保持上下文",
            "Use verbose=True during development / 开发时使用verbose=True",
            "Consider RunnableWithMessageHistory for new projects / 新项目考虑使用RunnableWithMessageHistory"
        ]
    }
]

BASIC_PROMPTS_TERMS = [
    {
        "term": "Single-turn Prompt",
        "term_cn": "单轮提示",
        "definition": "与语言模型的一次性交互，由单个输入生成单个输出，不维护上下文。",
        "definition_en": "A one-shot interaction with a language model consisting of a single input generating a single output, with no context maintenance.",
        "category": "prompt_engineering",
        "examples": [
            "Asking 'What is the capital of France?'",
            "Requesting a simple fact lookup",
            "Getting a quick definition"
        ],
        "related_terms": ["Multi-turn Prompt", "Zero-shot Learning", "Prompt Engineering"],
        "detailed_definition": "单轮提示是最简单的提示形式，每次交互都是独立的。模型不会记住之前的对话内容，每个提示都需要包含所有必要的信息。适用于简单查询、事实检索和一次性任务。",
        "related_concepts": ["Context isolation", "Stateless interaction", "Independent queries"],
        "usage_examples": [
            "llm.invoke('What is 2+2?')",
            "llm.invoke('Translate hello to French')"
        ]
    },
    {
        "term": "Multi-turn Prompt",
        "term_cn": "多轮提示",
        "definition": "维护上下文的一系列交互，允许追问和上下文感知的对话。",
        "definition_en": "A series of interactions that maintain context, allowing for follow-up questions and context-aware conversations.",
        "category": "prompt_engineering",
        "examples": [
            "Customer service chatbot",
            "Interactive tutoring system",
            "Code debugging session"
        ],
        "related_terms": ["Single-turn Prompt", "Conversation Memory", "ConversationChain"],
        "detailed_definition": "多轮提示允许连续的对话，模型会记住之前的交流内容。这对于需要上下文的任务至关重要，如客户服务、教学和复杂问题解决。",
        "related_concepts": ["Context retention", "Conversation history", "Follow-up questions"],
        "usage_examples": [
            "conversation.predict(input='Tell me about Paris')\nconversation.predict(input='What is its population?')",
            "Multi-step reasoning tasks"
        ]
    },
    {
        "term": "PromptTemplate",
        "term_cn": "提示模板",
        "definition": "可复用的结构化提示模式，支持变量参数化以实现一致的提示格式。",
        "definition_en": "A reusable structured prompt pattern that supports variable parameterization for consistent prompt formatting.",
        "category": "langchain",
        "examples": [
            "Template with {topic} variable",
            "Structured format for repeated queries",
            "Parameterized prompts for batch processing"
        ],
        "related_terms": ["Prompt Engineering", "LangChain", "Template Pattern"],
        "detailed_definition": "PromptTemplate是LangChain中的核心组件，允许创建带有变量占位符的提示模板。这使得提示可以复用和参数化，提高代码的可维护性和一致性。",
        "related_concepts": ["Variable interpolation", "Template reuse", "Consistent formatting"],
        "usage_examples": [
            "PromptTemplate(input_variables=['topic'], template='Explain {topic}')",
            "Using | operator: template | llm"
        ]
    },
    {
        "term": "ConversationBufferMemory",
        "term_cn": "对话缓冲记忆",
        "definition": "存储完整对话历史的记忆组件，用于维护多轮对话的上下文。",
        "definition_en": "A memory component that stores the complete conversation history for maintaining context in multi-turn conversations.",
        "category": "langchain",
        "examples": [
            "Storing all conversation turns",
            "Enabling follow-up questions",
            "Maintaining chat context"
        ],
        "related_terms": ["Conversation Memory", "ConversationChain", "Memory Types"],
        "detailed_definition": "ConversationBufferMemory是LangChain中最简单的记忆类型，它存储所有对话历史。虽然简单直接，但对于长对话可能会超出token限制。",
        "related_concepts": ["Memory window", "Token limits", "History management"],
        "usage_examples": [
            "ConversationBufferMemory()",
            "memory = ConversationBufferMemory(return_messages=True)"
        ]
    },
    {
        "term": "ConversationChain",
        "term_cn": "对话链",
        "definition": "LangChain中用于管理多轮对话的链组件，自动处理对话历史和上下文。",
        "definition_en": "A chain component in LangChain for managing multi-turn conversations, automatically handling conversation history and context.",
        "category": "langchain",
        "examples": [
            "Creating conversational AI applications",
            "Building chatbots with memory",
            "Interactive Q&A systems"
        ],
        "related_terms": ["ConversationChain", "LangChain Chains", "Conversation Memory"],
        "detailed_definition": "ConversationChain是LangChain中专门用于对话场景的链。它集成了记忆组件，自动管理对话历史，简化了对话式应用的开发。注意：在LangChain 0.2.7+中已弃用，建议使用RunnableWithMessageHistory。",
        "related_concepts": ["Chain abstraction", "Memory integration", "Deprecation notice"],
        "usage_examples": [
            "ConversationChain(llm=llm, memory=ConversationBufferMemory())",
            "conversation.predict(input='Hello')"
        ]
    }
]

BASIC_PROMPTS_QUESTIONS = [
    {
        "kp_title": "Single-turn Prompts / 单轮提示",
        "questions": [
            {
                "type": "single_choice",
                "question": "单轮提示的主要特点是什么？",
                "options": ["A. 维护对话上下文", "B. 一次性交互，无上下文记忆", "C. 需要ConversationChain", "D. 自动存储历史"],
                "answer": "B",
                "explanation": "单轮提示是一次性交互，每次调用都是独立的，不维护上下文记忆。",
                "difficulty": 1
            },
            {
                "type": "true_false",
                "question": "单轮提示适合用于需要记住之前对话内容的场景。",
                "answer": "错误",
                "explanation": "单轮提示不维护上下文，不适合需要记住之前对话内容的场景。这种场景应该使用多轮提示。",
                "difficulty": 1
            },
            {
                "type": "single_choice",
                "question": "以下哪个是单轮提示的典型应用场景？",
                "options": ["A. 客户服务聊天机器人", "B. 快速事实查询", "C. 多步骤推理", "D. 教学对话系统"],
                "answer": "B",
                "explanation": "单轮提示适合快速、独立的事实查询，不需要上下文的场景。",
                "difficulty": 1
            },
            {
                "type": "fill_blank",
                "question": "单轮提示由单个____和单个____组成。",
                "answer": "输入|输出|input|output",
                "explanation": "单轮提示由单个输入（提示）和单个输出（响应）组成。",
                "difficulty": 1
            },
            {
                "type": "multiple_choice",
                "question": "单轮提示的优点包括哪些？",
                "options": ["A. 简单直接", "B. 无需管理状态", "C. 适合快速查询", "D. 自动维护上下文"],
                "answer": "A,B,C",
                "explanation": "单轮提示简单直接、无需管理状态、适合快速查询。但它不会自动维护上下文。",
                "difficulty": 2
            }
        ]
    },
    {
        "kp_title": "Prompt Templates / 提示模板",
        "questions": [
            {
                "type": "single_choice",
                "question": "PromptTemplate的主要作用是什么？",
                "options": ["A. 存储对话历史", "B. 创建可复用的结构化提示", "C. 自动生成答案", "D. 管理API调用"],
                "answer": "B",
                "explanation": "PromptTemplate用于创建可复用的结构化提示，支持变量参数化。",
                "difficulty": 1
            },
            {
                "type": "single_choice",
                "question": "在PromptTemplate中，input_variables参数的作用是什么？",
                "options": ["A. 指定输出格式", "B. 定义模板中的变量名", "C. 设置模型参数", "D. 配置记忆类型"],
                "answer": "B",
                "explanation": "input_variables定义了模板中可以替换的变量名列表。",
                "difficulty": 2
            },
            {
                "type": "true_false",
                "question": "PromptTemplate可以使用管道操作符(|)与LLM连接。",
                "answer": "正确",
                "explanation": "LangChain支持使用管道操作符将PromptTemplate与LLM连接：template | llm",
                "difficulty": 2
            },
            {
                "type": "fill_blank",
                "question": "PromptTemplate通过____实现提示的参数化。",
                "answer": "变量|variable|input_variables",
                "explanation": "PromptTemplate通过变量(input_variables)实现提示的参数化。",
                "difficulty": 1
            }
        ]
    },
    {
        "kp_title": "Multi-turn Prompts / 多轮提示",
        "questions": [
            {
                "type": "single_choice",
                "question": "多轮提示与单轮提示的主要区别是什么？",
                "options": ["A. 使用不同的模型", "B. 维护对话上下文", "C. 响应速度更快", "D. 不需要API调用"],
                "answer": "B",
                "explanation": "多轮提示的主要特点是维护对话上下文，允许追问和上下文感知的对话。",
                "difficulty": 1
            },
            {
                "type": "multiple_choice",
                "question": "多轮提示适合哪些场景？",
                "options": ["A. 客户服务聊天机器人", "B. 交互式教学系统", "C. 快速事实查询", "D. 多步骤问题解决"],
                "answer": "A,B,D",
                "explanation": "多轮提示适合需要上下文的场景：客户服务、教学系统、多步骤问题。快速事实查询适合单轮提示。",
                "difficulty": 2
            },
            {
                "type": "true_false",
                "question": "在多轮对话中，追问时需要重复之前提到的上下文信息。",
                "answer": "错误",
                "explanation": "多轮对话的优势正是可以追问而无需重复上下文，对话记忆会保存之前的信息。",
                "difficulty": 1
            },
            {
                "type": "short_answer",
                "question": "请简述多轮提示相比单轮提示的优势。",
                "answer": "上下文,追问,对话,记忆,连贯",
                "explanation": "多轮提示可以维护上下文、支持追问、保持对话连贯性、记住之前的信息。",
                "difficulty": 2
            }
        ]
    },
    {
        "kp_title": "Conversation Memory / 对话记忆",
        "questions": [
            {
                "type": "single_choice",
                "question": "ConversationBufferMemory的作用是什么？",
                "options": ["A. 生成对话内容", "B. 存储完整对话历史", "C. 优化模型性能", "D. 管理API密钥"],
                "answer": "B",
                "explanation": "ConversationBufferMemory存储完整的对话历史，用于维护多轮对话的上下文。",
                "difficulty": 1
            },
            {
                "type": "single_choice",
                "question": "ConversationBufferMemory对于很长的对话有什么潜在问题？",
                "options": ["A. 响应变慢", "B. 可能超出token限制", "C. 无法存储历史", "D. 不支持中文"],
                "answer": "B",
                "explanation": "ConversationBufferMemory存储所有历史，对于很长的对话可能超出模型的token限制。",
                "difficulty": 2
            },
            {
                "type": "true_false",
                "question": "ConversationBufferMemory是LangChain中唯一的记忆类型。",
                "answer": "错误",
                "explanation": "LangChain有多种记忆类型，如ConversationBufferWindowMemory、ConversationSummaryMemory等。",
                "difficulty": 1
            },
            {
                "type": "fill_blank",
                "question": "ConversationBufferMemory用于存储____对话历史。",
                "answer": "完整|全部|complete|all",
                "explanation": "ConversationBufferMemory存储完整的对话历史。",
                "difficulty": 1
            }
        ]
    },
    {
        "kp_title": "ConversationChain / 对话链",
        "questions": [
            {
                "type": "single_choice",
                "question": "ConversationChain需要配合什么组件才能维护上下文？",
                "options": ["A. PromptTemplate", "B. Memory组件", "C. Vector Store", "D. Embeddings"],
                "answer": "B",
                "explanation": "ConversationChain需要配合Memory组件（如ConversationBufferMemory）才能维护对话上下文。",
                "difficulty": 1
            },
            {
                "type": "single_choice",
                "question": "ConversationChain的verbose=True参数有什么作用？",
                "options": ["A. 提高响应速度", "B. 显示内部处理过程", "C. 增加token限制", "D. 启用记忆功能"],
                "answer": "B",
                "explanation": "verbose=True会显示ConversationChain内部的提示处理过程，便于调试。",
                "difficulty": 2
            },
            {
                "type": "true_false",
                "question": "ConversationChain在最新版本的LangChain中已被弃用。",
                "answer": "正确",
                "explanation": "ConversationChain在LangChain 0.2.7中已被弃用，建议使用RunnableWithMessageHistory。",
                "difficulty": 2
            },
            {
                "type": "multiple_choice",
                "question": "ConversationChain的常用参数包括哪些？",
                "options": ["A. llm - 语言模型", "B. memory - 记忆组件", "C. verbose - 详细输出", "D. temperature - 温度参数"],
                "answer": "A,B,C",
                "explanation": "ConversationChain常用参数：llm(语言模型)、memory(记忆组件)、verbose(详细输出)。temperature是模型参数。",
                "difficulty": 2
            }
        ]
    }
]

def update_basic_prompts_content():
    print("Updating Basic Prompt Structures content...")
    db = SessionLocal()
    
    try:
        lessons = db.query(Lesson).all()
        target_lesson = None
        for lesson in lessons:
            if "basic" in lesson.title.lower() or "prompt" in lesson.title.lower() or "结构" in lesson.title:
                target_lesson = lesson
                break
        
        if not target_lesson:
            print("Warning: No matching lesson found. Creating a new one...")
            from app.models.models import Module
            modules = db.query(Module).all()
            if modules:
                target_lesson = Lesson(
                    module_id=modules[0].id,
                    title="Basic Prompt Structures / 基础提示结构",
                    date="2024-01-01",
                    topics=["Single-turn Prompts", "Multi-turn Prompts", "Prompt Templates", "Conversation Memory"],
                    difficulty="basic",
                    time_estimate=60,
                    summary="Learn the fundamental prompt structures: single-turn and multi-turn prompts using LangChain and OpenAI."
                )
                db.add(target_lesson)
                db.commit()
                print(f"Created lesson: {target_lesson.title}")
            else:
                print("Error: No modules found in database")
                return
        
        print(f"Using lesson: {target_lesson.title}")
        
        existing_kps = db.query(KnowledgePoint).filter(KnowledgePoint.lesson_id == target_lesson.id).all()
        for kp in existing_kps:
            db.query(PracticeQuestion).filter(PracticeQuestion.knowledge_point_id == kp.id).delete()
        db.query(KnowledgePoint).filter(KnowledgePoint.lesson_id == target_lesson.id).delete()
        db.query(LessonTerm).filter(LessonTerm.lesson_id == target_lesson.id).delete()
        db.commit()
        print("Cleared existing content")
        
        kp_map = {}
        for kp_data in BASIC_PROMPTS_KNOWLEDGE_POINTS:
            kp = KnowledgePoint(
                lesson_id=target_lesson.id,
                title=kp_data["title"],
                description=kp_data["description"],
                category=kp_data["category"],
                importance=kp_data["importance"],
                related_knowledge=kp_data.get("related_knowledge", []),
                key_concepts=kp_data.get("key_concepts", []),
                examples=kp_data.get("examples", []),
                common_mistakes=kp_data.get("common_mistakes", []),
                best_practices=kp_data.get("best_practices", [])
            )
            db.add(kp)
            db.flush()
            kp_map[kp_data["title"]] = kp
            print(f"  Added knowledge point: {kp_data['title']}")
        
        for term_data in BASIC_PROMPTS_TERMS:
            existing_term = db.query(Term).filter(Term.term == term_data["term"]).first()
            if not existing_term:
                term = Term(
                    term=term_data["term"],
                    definition=term_data["definition"],
                    category=term_data["category"],
                    examples=term_data.get("examples", []),
                    related_terms=term_data.get("related_terms", []),
                    detailed_definition=term_data.get("detailed_definition"),
                    related_concepts=term_data.get("related_concepts", []),
                    usage_examples=term_data.get("usage_examples", []),
                    is_predefined=True
                )
                db.add(term)
                db.flush()
            else:
                term = existing_term
            
            lesson_term = LessonTerm(
                lesson_id=target_lesson.id,
                term_id=term.id
            )
            db.add(lesson_term)
            print(f"  Added term: {term_data['term']}")
        
        for qp_data in BASIC_PROMPTS_QUESTIONS:
            kp_title = qp_data["kp_title"]
            if kp_title in kp_map:
                kp = kp_map[kp_title]
                for idx, q_data in enumerate(qp_data["questions"]):
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
                print(f"  Added {len(qp_data['questions'])} questions for: {kp_title}")
        
        db.commit()
        
        total_kps = db.query(KnowledgePoint).filter(KnowledgePoint.lesson_id == target_lesson.id).count()
        total_questions = sum(len(qp["questions"]) for qp in BASIC_PROMPTS_QUESTIONS)
        
        print(f"\nUpdate complete!")
        print(f"  Knowledge points: {total_kps}")
        print(f"  Terms: {len(BASIC_PROMPTS_TERMS)}")
        print(f"  Practice questions: {total_questions}")
        
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    update_basic_prompts_content()
