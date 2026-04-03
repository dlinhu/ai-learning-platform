import os
import sys
import json
from datetime import datetime

backend_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, backend_dir)

from app.utils.database import engine, SessionLocal, Base
from app.models.models import Module, Lesson, KnowledgePoint, Term, LessonTerm, User, Progress, Note

COURSE_SUPPLEMENTS = {
    "第一模块": {
        "name": "Prompts 提示词工程",
        "lessons": [
            {
                "title": "原子 + 零/少样本",
                "topics": ["TASK+CONSTRAINTS+OUTPUT", "Zero-shot vs Few-shot", "分子提示"],
                "summary": "本课程介绍提示词工程的基础概念，包括原子提示的三大要素（任务、约束、输出格式），以及零样本学习和少样本学习的区别与应用场景。",
                "knowledge_points": [
                    {"title": "原子提示 (Atomic Prompting)", "description": "原子提示是提示词的最小组成单元，包含三个核心要素：TASK（任务描述）、CONSTRAINTS（约束条件）、OUTPUT（输出格式）。好的原子提示应该清晰、具体、可执行。", "category": "prompt_engineering", "importance": 3},
                    {"title": "零样本学习 (Zero-shot Learning)", "description": "零样本学习是指模型在没有示例的情况下，仅通过任务描述就能完成任务。这种方式依赖模型的预训练知识和泛化能力。优点是简单直接，缺点是对于复杂任务可能效果不佳。", "category": "prompt_engineering", "importance": 3},
                    {"title": "少样本学习 (Few-shot Learning)", "description": "少样本学习通过提供少量示例帮助模型理解任务要求。通常2-5个示例效果最佳。示例应该覆盖不同的输入输出模式，帮助模型建立正确的任务理解。", "category": "prompt_engineering", "importance": 3},
                    {"title": "分子提示 (Molecular Prompting)", "description": "分子提示是由多个原子提示组合而成的复杂提示结构。通过组合不同的原子，可以构建处理复杂任务的提示链。分子提示体现了提示的组合性和层次性。", "category": "prompt_engineering", "importance": 2},
                    {"title": "提示词设计原则", "description": "好的提示词应该遵循：清晰性（任务描述明确）、具体性（避免模糊表达）、可验证性（输出可检验）、简洁性（避免冗余）。这些原则是提示工程的基础。", "category": "prompt_engineering", "importance": 2}
                ],
                "terms": [
                    {"term": "Prompt", "definition": "提示词，用户输入给AI模型的指令或问题，用于引导模型生成期望的输出。", "category": "prompt_engineering"},
                    {"term": "Zero-shot", "definition": "零样本学习，模型在没有示例的情况下完成任务的能力。", "category": "prompt_engineering"},
                    {"term": "Few-shot", "definition": "少样本学习，通过少量示例帮助模型理解任务要求的技术。", "category": "prompt_engineering"},
                    {"term": "In-context Learning", "definition": "上下文学习，模型从提示词中的上下文信息学习任务模式的能力。", "category": "prompt_engineering"},
                    {"term": "Task Description", "definition": "任务描述，提示词中明确说明需要模型完成什么任务的部分。", "category": "prompt_engineering"}
                ]
            },
            {
                "title": "CoT + 角色 + 约束 + 自洽",
                "topics": ["思维链", "Role/Persona", "约束生成", "Self-Consistency"],
                "summary": "本课程深入探讨高级提示技术，包括思维链推理、角色扮演、约束生成和自洽性方法，帮助学员掌握复杂任务的提示设计技巧。",
                "knowledge_points": [
                    {"title": "思维链 (Chain of Thought, CoT)", "description": "思维链是一种让模型逐步展示推理过程的技术。2022年Google提出，通过让模型在给出最终答案前先输出中间推理步骤，大幅提高了复杂问题的解决能力。常用触发语：「让我们一步一步思考」。", "category": "prompt_engineering", "importance": 3},
                    {"title": "角色提示 (Role Prompting)", "description": "通过指定模型扮演特定角色来引导其输出风格和内容。例如「你是一位经验丰富的软件架构师」。角色设定可以影响模型的语气、专业程度和回答角度。", "category": "prompt_engineering", "importance": 2},
                    {"title": "约束生成 (Constrained Generation)", "description": "通过明确的约束条件限制模型的输出范围和格式。约束可以是格式约束（如JSON输出）、内容约束（如字数限制）、风格约束（如正式语气）等。", "category": "prompt_engineering", "importance": 2},
                    {"title": "自洽性 (Self-Consistency)", "description": "通过多次采样取一致性结果的方法。对同一问题生成多个推理路径，然后选择最一致的答案。这种方法可以显著提高推理任务的准确性。", "category": "prompt_engineering", "importance": 2},
                    {"title": "Zero-shot CoT", "description": "零样本思维链，不需要示例，只需添加「让我们一步一步思考」等触发语即可激活模型的推理能力。这是一种简单但强大的技术。", "category": "prompt_engineering", "importance": 2}
                ],
                "terms": [
                    {"term": "CoT", "definition": "Chain of Thought，思维链，一种让模型逐步展示推理过程的技术。", "category": "prompt_engineering"},
                    {"term": "Role Prompting", "definition": "角色提示，通过指定模型扮演特定角色来引导输出。", "category": "prompt_engineering"},
                    {"term": "Self-consistency", "definition": "自洽性，通过多次采样取一致性结果的方法。", "category": "prompt_engineering"},
                    {"term": "Persona", "definition": "人格设定，为AI模型设定的特定身份和特征。", "category": "prompt_engineering"},
                    {"term": "Reasoning", "definition": "推理，模型进行逻辑思考和得出结论的过程。", "category": "prompt_engineering"}
                ]
            },
            {
                "title": "指令 + 任务分解 + 提示链",
                "topics": ["清晰指令", "复杂任务拆解", "多步串联"],
                "summary": "本课程介绍如何设计清晰的指令、将复杂任务分解为子任务，以及通过提示链串联多个步骤完成复杂工作流程。",
                "knowledge_points": [
                    {"title": "指令工程 (Instruction Engineering)", "description": "设计清晰、有效的指令是提示工程的核心。好的指令应该：明确任务目标、提供必要上下文、指定输出格式、设定边界条件。避免模糊和多义性。", "category": "prompt_engineering", "importance": 3},
                    {"title": "任务分解 (Task Decomposition)", "description": "将复杂任务拆分为多个简单子任务的方法。每个子任务应该有明确的输入输出，可以独立执行。分解粒度要适中，过细增加复杂度，过粗难以管理。", "category": "prompt_engineering", "importance": 3},
                    {"title": "提示链 (Prompt Chaining)", "description": "将多个提示按顺序串联，前一个提示的输出作为后一个提示的输入。适用于需要多步处理的复杂任务。关键在于设计好各步骤之间的接口。", "category": "prompt_engineering", "importance": 3},
                    {"title": "步骤化提示", "description": "在单个提示中明确列出处理步骤，引导模型按步骤执行。例如：「第一步：分析问题；第二步：列出要点；第三步：给出结论」。", "category": "prompt_engineering", "importance": 2},
                    {"title": "中间结果传递", "description": "在提示链中，如何有效地传递中间结果是关键。可以使用变量、JSON格式或结构化文本来确保信息不丢失。", "category": "prompt_engineering", "importance": 2}
                ],
                "terms": [
                    {"term": "Task Decomposition", "definition": "任务分解，将复杂任务拆分为多个简单子任务的方法。", "category": "prompt_engineering"},
                    {"term": "Prompt Chaining", "definition": "提示链，将多个提示按顺序串联执行的技术。", "category": "prompt_engineering"},
                    {"term": "Instruction", "definition": "指令，告诉模型需要执行什么任务的具体说明。", "category": "prompt_engineering"},
                    {"term": "Multi-step Reasoning", "definition": "多步推理，需要多个步骤才能完成的推理过程。", "category": "prompt_engineering"},
                    {"term": "Pipeline", "definition": "管道，一系列按顺序执行的处理步骤。", "category": "prompt_engineering"}
                ]
            },
            {
                "title": "记忆 + 控制循环 + 认知",
                "topics": ["Cells of Context", "多步控制", "认知模板"],
                "summary": "本课程探讨上下文记忆单元、控制循环机制和认知模板的设计，帮助学员理解如何构建具有记忆和控制能力的复杂提示系统。",
                "knowledge_points": [
                    {"title": "上下文记忆单元 (Cells of Context)", "description": "上下文记忆是模型在对话或任务执行过程中保留和检索信息的能力。包括短期记忆（当前对话）和长期记忆（持久化存储）。记忆管理是构建智能系统的关键。", "category": "context_management", "importance": 3},
                    {"title": "控制循环 (Control Loops)", "description": "控制循环是实现迭代处理和条件分支的机制。常见的模式包括：while循环（持续执行直到条件满足）、for循环（遍历处理）、条件分支（if-else逻辑）。", "category": "prompt_engineering", "importance": 2},
                    {"title": "认知模板 (Cognitive Templates)", "description": "认知模板是预定义的思维框架，用于引导模型按照特定模式思考。例如：问题分析模板、决策模板、创意生成模板等。模板可以提高输出的结构性和一致性。", "category": "prompt_engineering", "importance": 2},
                    {"title": "状态管理", "description": "在多轮对话或复杂任务中，需要管理状态信息。状态包括：当前进度、已完成的步骤、待处理的项目等。良好的状态管理是构建可靠系统的基础。", "category": "context_management", "importance": 2},
                    {"title": "认知工具 (Cognitive Tools)", "description": "认知工具是辅助模型思考和决策的框架和方法。包括：思维导图、决策矩阵、问题分解树等。这些工具可以帮助模型更系统地处理复杂问题。", "category": "prompt_engineering", "importance": 2}
                ],
                "terms": [
                    {"term": "Memory", "definition": "记忆，AI系统存储和检索信息的能力。", "category": "context_management"},
                    {"term": "Context Window", "definition": "上下文窗口，模型能处理的最大文本长度。", "category": "context_management"},
                    {"term": "Control Flow", "definition": "控制流，程序执行的顺序和分支逻辑。", "category": "prompt_engineering"},
                    {"term": "State", "definition": "状态，系统在某一时刻的完整信息描述。", "category": "context_management"},
                    {"term": "Cognitive Architecture", "definition": "认知架构，模拟人类认知过程的系统结构。", "category": "prompt_engineering"}
                ]
            },
            {
                "title": "提示编程 + 优化 + Schema + 小结",
                "topics": ["类代码推理", "Prompt 优化", "Schema 设计", "评估"],
                "summary": "本课程总结提示工程的高级技术，包括类代码推理、提示优化方法、Schema设计和评估技术，帮助学员掌握系统化的提示工程方法论。",
                "knowledge_points": [
                    {"title": "提示编程 (Prompt Programming)", "description": "将提示设计视为编程活动，使用变量、函数、条件语句等编程概念来构建提示。这种方法可以提高提示的可复用性和可维护性。", "category": "prompt_engineering", "importance": 3},
                    {"title": "提示优化技术", "description": "优化提示的方法包括：A/B测试比较不同版本、迭代改进基于反馈、自动优化使用工具辅助。好的提示需要反复打磨和测试。", "category": "prompt_engineering", "importance": 2},
                    {"title": "Schema设计", "description": "Schema定义了数据的结构和约束。在提示工程中，Schema用于指定输入输出的格式，确保模型生成符合预期的结构化数据。", "category": "prompt_engineering", "importance": 2},
                    {"title": "提示评估", "description": "评估提示效果的方法包括：准确性评估（输出是否正确）、一致性评估（多次输出是否稳定）、效率评估（Token消耗是否合理）。", "category": "prompt_engineering", "importance": 2},
                    {"title": "模块化提示设计", "description": "将提示分解为可复用的模块，每个模块负责特定功能。模块化设计可以提高开发效率，便于维护和升级。", "category": "prompt_engineering", "importance": 2}
                ],
                "terms": [
                    {"term": "Schema", "definition": "模式，定义数据结构和约束的规范。", "category": "prompt_engineering"},
                    {"term": "Prompt Optimization", "definition": "提示优化，改进提示效果的过程和方法。", "category": "prompt_engineering"},
                    {"term": "Evaluation", "definition": "评估，测量和判断系统性能的过程。", "category": "prompt_engineering"},
                    {"term": "Modular Design", "definition": "模块化设计，将系统分解为独立可复用组件的方法。", "category": "prompt_engineering"},
                    {"term": "A/B Testing", "definition": "A/B测试，比较两个版本效果的实验方法。", "category": "prompt_engineering"}
                ]
            }
        ]
    },
    "第二模块": {
        "name": "RAG 检索增强生成",
        "lessons": [
            {
                "title": "RAG 原理 + Simple RAG",
                "topics": ["检索-生成流程", "RAG基础理论", "动手实践"],
                "summary": "本课程介绍RAG（检索增强生成）的基本原理，包括检索-生成的完整流程，以及如何实现一个简单的RAG系统。",
                "knowledge_points": [
                    {"title": "RAG基本原理", "description": "RAG（Retrieval-Augmented Generation）是一种结合信息检索和文本生成的技术。它首先从知识库检索相关文档，然后将检索结果作为上下文输入LLM生成答案。这种方法可以有效减少幻觉，提高答案的准确性和可追溯性。", "category": "rag", "importance": 3},
                    {"title": "RAG工作流程", "description": "标准RAG流程包括：1) 用户提问 2) 问题向量化 3) 向量检索相似文档 4) 构建增强提示 5) LLM生成答案。每个环节都有优化空间。", "category": "rag", "importance": 3},
                    {"title": "Simple RAG架构", "description": "最简单的RAG实现包括：文档切分、向量化存储、相似度检索、上下文注入、答案生成。适合快速原型开发和学习理解。", "category": "rag", "importance": 2},
                    {"title": "向量数据库", "description": "向量数据库专门用于存储和检索向量。常用的有Pinecone、Weaviate、Chroma、FAISS等。选择时需考虑性能、扩展性、易用性等因素。", "category": "rag", "importance": 2},
                    {"title": "Embedding模型", "description": "Embedding模型将文本转换为向量表示。常用的有OpenAI的text-embedding-ada-002、Sentence Transformers等。好的Embedding是RAG效果的基础。", "category": "rag", "importance": 2}
                ],
                "terms": [
                    {"term": "RAG", "definition": "Retrieval-Augmented Generation，检索增强生成，结合检索和生成的AI技术。", "category": "rag"},
                    {"term": "Embedding", "definition": "嵌入，将文本转换为向量表示的过程。", "category": "rag"},
                    {"term": "Vector Store", "definition": "向量存储，专门存储和检索向量的数据库系统。", "category": "rag"},
                    {"term": "Semantic Search", "definition": "语义搜索，基于语义相似度而非关键词匹配的搜索方式。", "category": "rag"},
                    {"term": "Retrieval", "definition": "检索，从知识库中查找相关信息的过程。", "category": "rag"}
                ]
            },
            {
                "title": "分块 + Reliable RAG",
                "topics": ["Chunk size", "语义分块", "相关性验证"],
                "summary": "本课程深入探讨文档分块策略和如何构建可靠的RAG系统，包括分块大小选择、语义分块技术和相关性验证方法。",
                "knowledge_points": [
                    {"title": "文档分块策略", "description": "分块是RAG的关键步骤。常见的分块方法包括：固定大小分块（简单但可能切断语义）、句子分块（保持语义完整性）、段落分块（适合结构化文档）、语义分块（基于内容相似度）。", "category": "rag", "importance": 3},
                    {"title": "Chunk Size选择", "description": "分块大小的选择需要平衡：太小会丢失上下文，太大则包含太多无关信息。通常建议256-1024个Token，具体取决于文档类型和应用场景。需要通过实验确定最佳值。", "category": "rag", "importance": 2},
                    {"title": "语义分块", "description": "语义分块根据内容的语义相似度来决定分块边界。当相邻内容的语义差异超过阈值时，创建新的分块。这种方法可以更好地保持语义完整性。", "category": "rag", "importance": 2},
                    {"title": "Reliable RAG", "description": "Reliable RAG通过添加验证步骤提高系统可靠性：1) 检索后验证相关性 2) 生成时引用来源 3) 答案后验证事实一致性。这些步骤可以减少错误和幻觉。", "category": "rag", "importance": 3},
                    {"title": "重叠分块", "description": "在相邻分块之间添加重叠区域，确保上下文不会在分块边界处完全丢失。通常设置10-20%的重叠比例。", "category": "rag", "importance": 2}
                ],
                "terms": [
                    {"term": "Chunk", "definition": "分块，将长文档分割成较小的片段。", "category": "rag"},
                    {"term": "Chunk Size", "definition": "分块大小，每个分块包含的Token数量。", "category": "rag"},
                    {"term": "Semantic Chunking", "definition": "语义分块，基于内容语义相似度的分块方法。", "category": "rag"},
                    {"term": "Overlap", "definition": "重叠，相邻分块之间共享的内容区域。", "category": "rag"},
                    {"term": "Relevance", "definition": "相关性，检索结果与查询的匹配程度。", "category": "rag"}
                ]
            },
            {
                "title": "查询变换 + HyDE",
                "topics": ["Query Rewriting", "Step-back", "假设文档生成"],
                "summary": "本课程介绍查询优化技术，包括查询重写、后退提示和假设文档嵌入（HyDE），帮助提高检索的准确性和召回率。",
                "knowledge_points": [
                    {"title": "查询变换", "description": "查询变换是将用户原始查询转换为更适合检索的形式。常见方法包括：查询扩展（添加相关词）、查询重写（改写为更清晰的形式）、查询分解（将复杂查询拆分为多个子查询）。", "category": "rag", "importance": 3},
                    {"title": "HyDE (Hypothetical Document Embedding)", "description": "HyDE是一种创新的检索方法：首先让LLM生成一个假设的理想文档来回答用户问题，然后用这个假设文档的向量来检索真实文档。这种方法可以找到语义相关但词汇不同的内容。", "category": "rag", "importance": 3},
                    {"title": "Step-back Prompting", "description": "后退提示是一种推理技术：先让模型思考更高层次的抽象概念或原理，再回到具体问题。在RAG中，可以先用抽象问题检索背景知识，再用具体问题检索细节。", "category": "rag", "importance": 2},
                    {"title": "多查询检索", "description": "将用户查询扩展为多个相关查询，分别检索后合并结果。可以提高召回率，找到更多相关文档。需要注意去重和排序。", "category": "rag", "importance": 2},
                    {"title": "查询理解", "description": "在检索前先理解用户意图：识别查询类型（事实问答、比较、解释等）、提取关键实体、判断时间范围等。这些信息可以指导检索策略。", "category": "rag", "importance": 2}
                ],
                "terms": [
                    {"term": "Query Transformation", "definition": "查询变换，将原始查询转换为更适合检索的形式。", "category": "rag"},
                    {"term": "HyDE", "definition": "Hypothetical Document Embedding，假设文档嵌入，用假设文档检索真实文档的方法。", "category": "rag"},
                    {"term": "Query Rewriting", "definition": "查询重写，改写查询以提高检索效果的技术。", "category": "rag"},
                    {"term": "Query Expansion", "definition": "查询扩展，添加相关词汇到查询中。", "category": "rag"},
                    {"term": "Recall", "definition": "召回率，检索系统找到所有相关文档的能力。", "category": "rag"}
                ]
            },
            {
                "title": "Reranking + Fusion + 上下文压缩",
                "topics": ["重排序", "向量+关键词融合", "Token 优化"],
                "summary": "本课程介绍高级检索优化技术，包括重排序、多路融合检索和上下文压缩，帮助提高检索质量和效率。",
                "knowledge_points": [
                    {"title": "Reranking重排序", "description": "重排序是在初步检索后对结果进行精细排序。使用更精确但更慢的模型（如Cross-Encoder）计算查询与文档的相关性分数，重新排列结果。可以显著提高Top-K结果的准确性。", "category": "rag", "importance": 3},
                    {"title": "Fusion Retrieval融合检索", "description": "融合检索结合多种检索方法的结果：向量检索（语义相似）、关键词检索（精确匹配）、混合检索（两者结合）。通过RRF（Reciprocal Rank Fusion）等算法合并排序。", "category": "rag", "importance": 3},
                    {"title": "上下文压缩", "description": "上下文压缩减少注入LLM的上下文长度：提取文档中与查询相关的片段、去除冗余信息、压缩相似内容。可以节省Token并提高相关性。", "category": "rag", "importance": 2},
                    {"title": "Cross-Encoder vs Bi-Encoder", "description": "Bi-Encoder（双塔模型）分别编码查询和文档，速度快但精度较低；Cross-Encoder（交叉编码器）同时处理查询和文档，精度高但速度慢。通常先用Bi-Encoder粗筛，再用Cross-Encoder精排。", "category": "rag", "importance": 2},
                    {"title": "RRF算法", "description": "Reciprocal Rank Fusion是一种简单的排名融合算法：对每个文档，计算其在各检索结果中排名的倒数之和，作为最终分数。简单有效，广泛使用。", "category": "rag", "importance": 2}
                ],
                "terms": [
                    {"term": "Reranking", "definition": "重排序，对检索结果进行精细排序的过程。", "category": "rag"},
                    {"term": "Fusion", "definition": "融合，结合多种检索方法结果的技术。", "category": "rag"},
                    {"term": "Cross-Encoder", "definition": "交叉编码器，同时处理查询和文档的模型。", "category": "rag"},
                    {"term": "RRF", "definition": "Reciprocal Rank Fusion，倒数排名融合算法。", "category": "rag"},
                    {"term": "Compression", "definition": "压缩，减少上下文长度的技术。", "category": "rag"}
                ]
            },
            {
                "title": "长上下文 + 压缩策略",
                "topics": ["长文档处理", "128K/200K 窗口", "压缩策略"],
                "summary": "本课程探讨如何处理长文档和利用大上下文窗口，以及各种上下文压缩策略。",
                "knowledge_points": [
                    {"title": "长上下文处理", "description": "现代LLM支持128K甚至200K+的上下文窗口。长上下文处理策略包括：分段处理、层次化摘要、关键信息提取、滑动窗口等。需要平衡完整性和效率。", "category": "rag", "importance": 3},
                    {"title": "上下文压缩策略", "description": "压缩策略包括：提取式压缩（保留原文关键句）、生成式压缩（LLM生成摘要）、语义压缩（合并相似内容）、结构化压缩（提取实体关系）。选择取决于任务需求。", "category": "rag", "importance": 2},
                    {"title": "Lost in the Middle问题", "description": "研究表明，放在上下文中间的信息容易被模型忽略。解决方案：将重要信息放在开头或结尾，或使用多轮对话逐步引入信息。", "category": "rag", "importance": 2},
                    {"title": "上下文预算管理", "description": "合理分配上下文预算：系统提示、检索文档、对话历史、用户查询各占多少Token。需要根据任务特点动态调整。", "category": "rag", "importance": 2},
                    {"title": "分层检索", "description": "对于超长文档，可以先检索相关章节，再在章节内检索具体段落。分层检索可以提高效率和准确性。", "category": "rag", "importance": 2}
                ],
                "terms": [
                    {"term": "Long Context", "definition": "长上下文，模型能处理的大量文本。", "category": "rag"},
                    {"term": "Context Window", "definition": "上下文窗口，模型能处理的最大文本长度。", "category": "rag"},
                    {"term": "Token Budget", "definition": "Token预算，分配给各部分的Token数量。", "category": "rag"},
                    {"term": "Hierarchical Retrieval", "definition": "分层检索，多层次的检索策略。", "category": "rag"},
                    {"term": "Summarization", "definition": "摘要，将长文本压缩为简短描述。", "category": "rag"}
                ]
            },
            {
                "title": "RAG 评估 + 小结",
                "topics": ["评估清单", "Token 预算", "端到端设计"],
                "summary": "本课程总结RAG模块内容，介绍RAG系统评估方法和端到端设计最佳实践。",
                "knowledge_points": [
                    {"title": "RAG评估指标", "description": "RAG系统评估包括：检索质量（召回率、精确率、MRR）、生成质量（准确性、相关性、流畅性）、端到端效果（用户满意度、任务完成率）。需要建立完整的评估体系。", "category": "rag", "importance": 3},
                    {"title": "RAGAS评估框架", "description": "RAGAS是一个流行的RAG评估框架，提供自动化评估指标：Faithfulness（忠实度）、Answer Relevance（答案相关性）、Context Precision（上下文精确度）、Context Recall（上下文召回率）。", "category": "rag", "importance": 2},
                    {"title": "端到端RAG设计", "description": "设计RAG系统需要考虑：数据预处理、索引策略、检索方法、重排序、上下文构建、提示设计、答案生成、后处理等环节。每个环节都可能成为瓶颈。", "category": "rag", "importance": 2},
                    {"title": "常见问题与解决", "description": "RAG常见问题：检索不到相关文档（优化查询、扩展知识库）、答案不准确（改进提示、添加验证）、响应太慢（缓存、异步处理）、成本太高（压缩、模型选择）。", "category": "rag", "importance": 2},
                    {"title": "RAG vs 微调", "description": "RAG适合需要实时更新知识、可追溯来源的场景；微调适合需要特定风格、领域深度的场景。两者可以结合使用：微调模型+RAG增强。", "category": "rag", "importance": 2}
                ],
                "terms": [
                    {"term": "Evaluation", "definition": "评估，测量系统性能的过程。", "category": "rag"},
                    {"term": "RAGAS", "definition": "RAG评估框架，自动化评估RAG系统的工具。", "category": "rag"},
                    {"term": "Faithfulness", "definition": "忠实度，答案与上下文的一致程度。", "category": "rag"},
                    {"term": "MRR", "definition": "Mean Reciprocal Rank，平均倒数排名，检索评估指标。", "category": "rag"},
                    {"term": "Fine-tuning", "definition": "微调，在特定数据上训练模型的过程。", "category": "rag"}
                ]
            }
        ]
    },
    "第三模块": {
        "name": "Agent 智能体",
        "lessons": [
            {
                "title": "Agent 概念 + Organs + Function Calling",
                "topics": ["多 AI 协作", "Orchestrator", "工具调用基础"],
                "summary": "本课程介绍AI Agent的基本概念，包括Agent架构、多AI协作模式和Function Calling机制。",
                "knowledge_points": [
                    {"title": "AI Agent定义", "description": "AI Agent是能够感知环境、做出决策、执行行动的智能系统。与普通LLM不同，Agent具有：自主性（独立决策）、反应性（响应环境变化）、主动性（主动追求目标）、社交性（与其他Agent协作）。", "category": "agent", "importance": 3},
                    {"title": "Organs架构", "description": "Organs是Agent的组织架构模型，将Agent比作生物器官：感知器官（接收输入）、大脑（推理决策）、手脚（执行工具）、记忆（存储信息）。这种类比帮助理解Agent的组件和协作方式。", "category": "agent", "importance": 2},
                    {"title": "Function Calling", "description": "Function Calling是LLM调用外部函数的能力。模型输出结构化的函数调用请求，由系统执行后返回结果。这是Agent与外部世界交互的核心机制。OpenAI、Anthropic等都支持此功能。", "category": "agent", "importance": 3},
                    {"title": "工具定义", "description": "定义工具需要指定：名称、描述、参数Schema。好的工具定义应该清晰描述功能、参数含义和返回格式。工具粒度要适中，过细增加复杂度，过粗降低灵活性。", "category": "agent", "importance": 2},
                    {"title": "Orchestrator编排器", "description": "Orchestrator是协调多个Agent或工具的中心组件。负责：任务分解、分配、执行监控、结果整合。好的编排器是构建复杂Agent系统的关键。", "category": "agent", "importance": 2}
                ],
                "terms": [
                    {"term": "Agent", "definition": "智能体，能够自主执行任务的AI系统。", "category": "agent"},
                    {"term": "Function Calling", "definition": "函数调用，LLM调用外部函数的能力。", "category": "agent"},
                    {"term": "Tool", "definition": "工具，Agent可以调用的外部功能。", "category": "agent"},
                    {"term": "Orchestrator", "definition": "编排器，协调多个Agent的中心组件。", "category": "agent"},
                    {"term": "Autonomous", "definition": "自主的，能够独立决策和行动的能力。", "category": "agent"}
                ]
            },
            {
                "title": "简单对话 + ReAct Agent",
                "topics": ["对话 Agent", "ReAct 模式", "工具调用"],
                "summary": "本课程介绍如何构建对话Agent和ReAct模式的Agent，这是Agent开发的基础模式。",
                "knowledge_points": [
                    {"title": "ReAct模式", "description": "ReAct（Reasoning + Acting）是Google在2022年提出的Agent框架。核心思想是让模型交替进行推理和行动：Thought（思考下一步）→ Action（执行工具）→ Observation（观察结果）→ 循环。这种模式显著提高了复杂任务的解决能力。", "category": "agent", "importance": 3},
                    {"title": "TAO循环", "description": "TAO是ReAct的核心循环：Thought（思考当前状态和下一步行动）、Action（调用工具或给出答案）、Observation（获取执行结果）。循环直到任务完成。这种显式的推理过程使Agent行为可解释。", "category": "agent", "importance": 3},
                    {"title": "对话Agent设计", "description": "设计对话Agent需要考虑：对话状态管理、上下文维护、意图识别、槽位填充、回复生成。可以使用状态机或更灵活的LLM驱动方式。", "category": "agent", "importance": 2},
                    {"title": "工具选择策略", "description": "Agent需要决定何时调用工具、调用哪个工具。策略包括：基于描述匹配、基于历史成功率、基于任务分解。好的工具选择是Agent效率的关键。", "category": "agent", "importance": 2},
                    {"title": "错误处理", "description": "Agent执行过程中可能遇到：工具调用失败、结果不符合预期、陷入循环等。需要设计重试机制、回退策略、终止条件来处理这些情况。", "category": "agent", "importance": 2}
                ],
                "terms": [
                    {"term": "ReAct", "definition": "Reasoning + Acting，推理与行动结合的Agent模式。", "category": "agent"},
                    {"term": "TAO", "definition": "Thought-Action-Observation，ReAct的核心循环。", "category": "agent"},
                    {"term": "Reasoning", "definition": "推理，模型进行逻辑思考的过程。", "category": "agent"},
                    {"term": "Observation", "definition": "观察，获取工具执行结果的过程。", "category": "agent"},
                    {"term": "Loop", "definition": "循环，重复执行直到条件满足。", "category": "agent"}
                ]
            },
            {
                "title": "Tools 详解",
                "topics": ["自定义 Tool", "Web 工具"],
                "summary": "本课程深入探讨工具的设计和实现，包括自定义工具开发和Web工具集成。",
                "knowledge_points": [
                    {"title": "工具设计原则", "description": "好的工具应该：单一职责（一个工具做一件事）、清晰接口（参数和返回值明确）、容错处理（优雅处理异常）、可组合性（与其他工具配合使用）。工具是Agent能力的延伸。", "category": "agent", "importance": 3},
                    {"title": "自定义工具开发", "description": "开发自定义工具需要：定义工具Schema、实现执行逻辑、处理异常情况、添加使用示例。工具可以是API调用、数据库查询、文件操作等任何可编程功能。", "category": "agent", "importance": 2},
                    {"title": "Web工具集成", "description": "Web工具让Agent能够访问互联网：搜索（Google/Bing API）、网页抓取、API调用。需要注意速率限制、认证安全、结果解析等问题。", "category": "agent", "importance": 2},
                    {"title": "工具链组合", "description": "多个工具可以组合成工具链：前一个工具的输出作为后一个工具的输入。例如：搜索→抓取→摘要→存储。工具链可以完成复杂任务。", "category": "agent", "importance": 2},
                    {"title": "工具安全", "description": "工具调用需要考虑安全：输入验证（防止注入攻击）、权限控制（最小权限原则）、输出过滤（敏感信息保护）、审计日志（记录所有调用）。", "category": "agent", "importance": 2}
                ],
                "terms": [
                    {"term": "Tool", "definition": "工具，Agent可以调用的外部功能。", "category": "agent"},
                    {"term": "API", "definition": "Application Programming Interface，应用程序编程接口。", "category": "agent"},
                    {"term": "Web Scraping", "definition": "网页抓取，从网页提取数据的技术。", "category": "agent"},
                    {"term": "Tool Chain", "definition": "工具链，多个工具按顺序组合。", "category": "agent"},
                    {"term": "Security", "definition": "安全，保护系统免受攻击的措施。", "category": "agent"}
                ]
            },
            {
                "title": "MCP 模型上下文协议",
                "topics": ["Server/Client", "工具与资源标准化"],
                "summary": "本课程介绍Anthropic提出的MCP协议，这是AI模型与外部系统交互的标准化方案。",
                "knowledge_points": [
                    {"title": "MCP协议概述", "description": "MCP（Model Context Protocol）是Anthropic在2024年11月发布的开放协议，旨在标准化LLM与外部数据源、工具的交互方式。被称为AI模型的「万能插座」，解决了不同工具集成的碎片化问题。", "category": "agent", "importance": 3},
                    {"title": "MCP架构", "description": "MCP采用Client-Server架构：MCP Client（如Claude Desktop）连接MCP Server（提供工具和资源）。Server可以提供：Tools（可调用的函数）、Resources（可访问的数据）、Prompts（预定义的提示模板）。", "category": "agent", "importance": 3},
                    {"title": "MCP Server开发", "description": "开发MCP Server需要：定义工具和资源、实现处理逻辑、遵循MCP协议规范。可以使用Python、TypeScript等语言的SDK快速开发。Server可以是本地服务或远程服务。", "category": "agent", "importance": 2},
                    {"title": "MCP vs 传统工具集成", "description": "传统方式：每个应用需要单独集成每个工具。MCP方式：一次开发，所有兼容Client可用。这大大降低了集成成本，促进了工具生态的发展。", "category": "agent", "importance": 2},
                    {"title": "MCP生态系统", "description": "MCP正在快速发展：官方提供了文件系统、数据库、GitHub等Server；社区贡献了更多工具。未来可能成为AI工具集成的标准协议。", "category": "agent", "importance": 2}
                ],
                "terms": [
                    {"term": "MCP", "definition": "Model Context Protocol，模型上下文协议，AI工具集成标准。", "category": "agent"},
                    {"term": "Protocol", "definition": "协议，通信和数据交换的规范。", "category": "agent"},
                    {"term": "Server", "definition": "服务器，提供服务的程序。", "category": "agent"},
                    {"term": "Client", "definition": "客户端，请求服务的程序。", "category": "agent"},
                    {"term": "Standardization", "definition": "标准化，制定统一规范的过程。", "category": "agent"}
                ]
            },
            {
                "title": "LangGraph",
                "topics": ["StateGraph", "工作流编排"],
                "summary": "本课程介绍LangGraph框架，这是构建复杂Agent工作流的强大工具。",
                "knowledge_points": [
                    {"title": "LangGraph概述", "description": "LangGraph是LangChain团队开发的Agent编排框架，基于图状态机构建。与传统的链式结构不同，LangGraph支持循环、分支、并行等复杂控制流，适合构建生产级Agent系统。", "category": "agent", "importance": 3},
                    {"title": "StateGraph概念", "description": "StateGraph是LangGraph的核心概念：图由节点（处理函数）和边（转换条件）组成，状态在节点间传递和更新。每个节点可以访问和修改状态，决定下一步走向。", "category": "agent", "importance": 3},
                    {"title": "节点和边", "description": "节点是处理逻辑的单元，接收状态、处理数据、返回更新。边定义节点间的转换：条件边（根据状态选择路径）、普通边（固定转换）。图的定义决定了Agent的行为。", "category": "agent", "importance": 2},
                    {"title": "状态管理", "description": "状态是图执行过程中传递的数据结构。LangGraph使用TypedDict定义状态Schema，支持增量更新（reducer）。状态设计是Agent架构的关键。", "category": "agent", "importance": 2},
                    {"title": "持久化和恢复", "description": "LangGraph支持检查点和持久化：可以保存执行状态、暂停和恢复执行、实现人机协作。这对于长时间运行的Agent非常重要。", "category": "agent", "importance": 2}
                ],
                "terms": [
                    {"term": "LangGraph", "definition": "LangChain的图状态机框架，用于构建复杂Agent。", "category": "agent"},
                    {"term": "StateGraph", "definition": "状态图，基于状态的图结构。", "category": "agent"},
                    {"term": "Node", "definition": "节点，图中的处理单元。", "category": "agent"},
                    {"term": "Edge", "definition": "边，节点间的连接和转换。", "category": "agent"},
                    {"term": "Workflow", "definition": "工作流，任务执行的定义和编排。", "category": "agent"}
                ]
            },
            {
                "title": "Memory",
                "topics": ["短期/长期记忆", "记忆架构"],
                "summary": "本课程探讨Agent的记忆系统，包括短期记忆、长期记忆和各种记忆架构设计。",
                "knowledge_points": [
                    {"title": "Agent记忆类型", "description": "Agent记忆分为：短期记忆（当前对话上下文）、工作记忆（当前任务相关）、长期记忆（持久化知识）、情景记忆（历史交互记录）。不同类型服务于不同需求。", "category": "agent", "importance": 3},
                    {"title": "记忆架构设计", "description": "记忆架构需要考虑：存储方式（向量数据库、关系数据库、文件系统）、检索策略（相似度、时间、重要性）、更新机制（添加、修改、遗忘）、容量管理（淘汰策略）。", "category": "agent", "importance": 3},
                    {"title": "对话记忆", "description": "对话记忆保存交互历史：消息列表、摘要、关键实体。需要处理上下文窗口限制：滑动窗口、摘要压缩、关键信息提取。", "category": "agent", "importance": 2},
                    {"title": "长期记忆存储", "description": "长期记忆通常使用向量数据库存储：将记忆编码为向量，支持语义检索。存储时需要考虑：索引策略、元数据管理、更新频率。", "category": "agent", "importance": 2},
                    {"title": "记忆增强生成", "description": "记忆增强生成（Memory-augmented Generation）将检索到的记忆注入提示：检索相关记忆→排序和过滤→构建增强提示→生成回答。记忆质量直接影响生成效果。", "category": "agent", "importance": 2}
                ],
                "terms": [
                    {"term": "Memory", "definition": "记忆，Agent存储和检索信息的能力。", "category": "agent"},
                    {"term": "Short-term Memory", "definition": "短期记忆，当前对话的上下文信息。", "category": "agent"},
                    {"term": "Long-term Memory", "definition": "长期记忆，持久化存储的知识和经验。", "category": "agent"},
                    {"term": "Episodic Memory", "definition": "情景记忆，历史交互事件的记录。", "category": "agent"},
                    {"term": "Retrieval", "definition": "检索，从记忆中查找相关信息的过程。", "category": "agent"}
                ]
            },
            {
                "title": "多 Agent 系统",
                "topics": ["通信协议", "编排机制", "Supervisor/Subagent"],
                "summary": "本课程介绍多Agent系统的设计和实现，包括Agent间通信、编排机制和Supervisor模式。",
                "knowledge_points": [
                    {"title": "多Agent系统概述", "description": "多Agent系统由多个协作的Agent组成，每个Agent可以专注于特定领域。优势：专业化分工、并行处理、可扩展性、容错性。挑战：协调复杂、通信开销、一致性维护。", "category": "agent", "importance": 3},
                    {"title": "Supervisor模式", "description": "Supervisor模式是一种常见的多Agent架构：一个中心Supervisor Agent负责任务分解、分配和结果整合；多个Sub-agent负责具体执行。Supervisor是无状态的协调者。", "category": "agent", "importance": 3},
                    {"title": "Agent通信协议", "description": "Agent间通信需要定义：消息格式（JSON、自然语言）、通信模式（同步、异步、发布订阅）、协议规范（A2A协议）。标准化通信是协作的基础。", "category": "agent", "importance": 2},
                    {"title": "编排机制", "description": "编排机制决定Agent如何协作：顺序执行（流水线）、并行执行（同时处理）、条件分支（根据结果选择）、循环迭代（反复优化）。LangGraph、CrewAI等框架提供编排能力。", "category": "agent", "importance": 2},
                    {"title": "A2A协议", "description": "A2A（Agent-to-Agent）是Google提出的Agent间通信协议，标准化了Agent发现、能力描述、消息传递。有助于构建开放的Agent生态系统。", "category": "agent", "importance": 2}
                ],
                "terms": [
                    {"term": "Multi-agent", "definition": "多智能体，多个Agent协作的系统。", "category": "agent"},
                    {"term": "Supervisor", "definition": "监督者，协调多个Agent的中心组件。", "category": "agent"},
                    {"term": "Sub-agent", "definition": "子智能体，执行具体任务的Agent。", "category": "agent"},
                    {"term": "A2A", "definition": "Agent-to-Agent，Agent间通信协议。", "category": "agent"},
                    {"term": "Coordination", "definition": "协调，管理多个Agent协作的过程。", "category": "agent"}
                ]
            }
        ]
    },
    "第四模块": {
        "name": "PROD 生产落地",
        "lessons": [
            {
                "title": "安全 + 可观测",
                "topics": ["Guardrails", "LangSmith Tracing"],
                "summary": "本课程介绍AI系统生产环境中的安全防护和可观测性建设。",
                "knowledge_points": [
                    {"title": "AI安全护栏", "description": "安全护栏是保护AI系统的机制：输入护栏（过滤恶意输入）、输出护栏（检查敏感信息）、工具护栏（限制危险操作）。多层防护确保系统安全。", "category": "production", "importance": 3},
                    {"title": "Prompt Injection防护", "description": "Prompt Injection是AI系统的主要安全威胁：攻击者通过精心构造的输入覆盖系统指令。防护方法：输入过滤、指令隔离、输出验证、权限最小化。", "category": "production", "importance": 3},
                    {"title": "可观测性", "description": "可观测性是了解系统内部状态的能力：追踪（Tracing，请求链路）、指标（Metrics，性能数据）、日志（Logging，事件记录）。完整的可观测性是运维的基础。", "category": "production", "importance": 3},
                    {"title": "LangSmith", "description": "LangSmith是LangChain的监控调试平台：追踪LLM调用链、查看提示和响应、分析Token消耗、评估效果。是开发和运维LangChain应用的利器。", "category": "production", "importance": 2},
                    {"title": "审计日志", "description": "审计日志记录所有重要操作：用户请求、模型响应、工具调用、异常事件。日志是安全审计、问题排查、合规要求的基础。", "category": "production", "importance": 2}
                ],
                "terms": [
                    {"term": "Guardrails", "definition": "护栏，限制和保护AI系统的机制。", "category": "production"},
                    {"term": "Observability", "definition": "可观测性，了解系统内部状态的能力。", "category": "production"},
                    {"term": "Tracing", "definition": "追踪，跟踪请求处理链路的技术。", "category": "production"},
                    {"term": "LangSmith", "definition": "LangChain的监控和调试平台。", "category": "production"},
                    {"term": "Audit Log", "definition": "审计日志，记录系统操作的日志。", "category": "production"}
                ]
            },
            {
                "title": "生产级 Memory + API",
                "topics": ["Redis", "FastAPI", "Docker"],
                "summary": "本课程介绍生产环境的Memory存储、API开发和容器化部署。",
                "knowledge_points": [
                    {"title": "Redis记忆存储", "description": "Redis是生产环境常用的记忆存储：高性能、支持过期时间、支持发布订阅。可以存储会话状态、对话历史、缓存结果。是构建可扩展Agent的关键组件。", "category": "production", "importance": 3},
                    {"title": "FastAPI开发", "description": "FastAPI是构建AI API的优秀框架：高性能异步、自动文档、类型验证。可以快速构建RESTful API、WebSocket服务、SSE流式输出。", "category": "production", "importance": 3},
                    {"title": "Docker容器化", "description": "Docker简化了AI应用的部署：环境一致性、快速启动、资源隔离。可以容器化模型服务、API服务、前端应用。是云原生部署的基础。", "category": "production", "importance": 2},
                    {"title": "API设计最佳实践", "description": "AI API设计需要考虑：认证授权、速率限制、错误处理、版本管理、文档完善。良好的API设计提高可用性和可维护性。", "category": "production", "importance": 2},
                    {"title": "会话管理", "description": "生产环境会话管理：会话ID生成、状态存储、超时处理、并发控制。需要考虑分布式场景下的一致性问题。", "category": "production", "importance": 2}
                ],
                "terms": [
                    {"term": "Redis", "definition": "高性能内存数据库，常用于缓存和会话存储。", "category": "production"},
                    {"term": "FastAPI", "definition": "高性能Python Web框架，适合构建AI API。", "category": "production"},
                    {"term": "Docker", "definition": "容器化平台，简化应用部署和管理。", "category": "production"},
                    {"term": "API", "definition": "Application Programming Interface，应用程序接口。", "category": "production"},
                    {"term": "Session", "definition": "会话，用户与系统的交互状态。", "category": "production"}
                ]
            },
            {
                "title": "评估 + UI + 流式输出",
                "topics": ["IntellAgent评估", "Streamlit", "Streaming/SSE"],
                "summary": "本课程介绍Agent评估方法、UI开发和流式输出技术。",
                "knowledge_points": [
                    {"title": "Agent评估方法", "description": "评估Agent需要多维度指标：任务完成率（是否达成目标）、效率（步数、时间）、成本（Token消耗）、安全性（是否有危险行为）。需要设计评估数据集和自动化测试。", "category": "production", "importance": 3},
                    {"title": "Streamlit UI开发", "description": "Streamlit是快速构建AI应用UI的工具：Python原生、组件丰富、支持聊天界面。可以快速构建原型和内部工具，适合数据科学和AI应用。", "category": "production", "importance": 2},
                    {"title": "流式输出", "description": "流式输出让用户更快看到响应：SSE（Server-Sent Events）是常用协议，LangChain和OpenAI都支持stream模式。需要处理连接管理、错误恢复、中断处理。", "category": "production", "importance": 3},
                    {"title": "用户体验设计", "description": "AI应用UX设计要点：加载状态、错误提示、进度展示、中断恢复。好的UX让AI能力更容易被用户接受和使用。", "category": "production", "importance": 2},
                    {"title": "性能优化", "description": "AI应用性能优化：模型选择（速度vs质量）、缓存策略、并行处理、预加载。需要在用户体验和成本之间找到平衡。", "category": "production", "importance": 2}
                ],
                "terms": [
                    {"term": "Evaluation", "definition": "评估，测量系统性能的过程。", "category": "production"},
                    {"term": "Streamlit", "definition": "Python快速UI开发框架。", "category": "production"},
                    {"term": "Streaming", "definition": "流式输出，逐步返回结果的技术。", "category": "production"},
                    {"term": "SSE", "definition": "Server-Sent Events，服务器推送事件。", "category": "production"},
                    {"term": "UX", "definition": "User Experience，用户体验。", "category": "production"}
                ]
            },
            {
                "title": "生产安全评估 + GPU 部署",
                "topics": ["安全测试", "云端GPU部署"],
                "summary": "本课程介绍生产环境的安全评估和GPU部署策略。",
                "knowledge_points": [
                    {"title": "安全评估框架", "description": "AI系统安全评估包括：渗透测试（模拟攻击）、红队测试（对抗性评估）、合规审计（GDPR、SOC2）。需要建立持续的安全评估流程。", "category": "production", "importance": 3},
                    {"title": "GPU部署策略", "description": "GPU部署选择：云服务（AWS、GCP、Azure）、专业平台（RunPod、Lambda Labs）、本地部署（成本高但可控）。需要根据负载、预算、延迟要求选择。", "category": "production", "importance": 3},
                    {"title": "模型服务化", "description": "将模型部署为服务：vLLM（高吞吐推理）、TGI（HuggingFace方案）、TensorRT-LLM（NVIDIA优化）。选择取决于模型类型和性能需求。", "category": "production", "importance": 2},
                    {"title": "成本优化", "description": "AI系统成本优化：模型选择（小模型够用就不用大模型）、缓存策略（减少重复调用）、批处理（提高吞吐）、Spot实例（降低云成本）。", "category": "production", "importance": 2},
                    {"title": "高可用设计", "description": "生产环境高可用：负载均衡、自动扩缩容、故障转移、多区域部署。AI服务需要考虑模型加载时间、GPU资源调度等特殊因素。", "category": "production", "importance": 2}
                ],
                "terms": [
                    {"term": "GPU", "definition": "Graphics Processing Unit，图形处理器，AI计算核心。", "category": "production"},
                    {"term": "Deployment", "definition": "部署，将应用发布到生产环境的过程。", "category": "production"},
                    {"term": "High Availability", "definition": "高可用，系统持续可用的能力。", "category": "production"},
                    {"term": "Scaling", "definition": "扩缩容，调整资源以适应负载变化。", "category": "production"},
                    {"term": "Cost Optimization", "definition": "成本优化，降低系统运行成本的方法。", "category": "production"}
                ]
            }
        ]
    },
    "第五模块": {
        "name": "收尾与弹性",
        "lessons": [
            {
                "title": "Neural Fields",
                "topics": ["神经场理论", "连续场建模", "语义空间"],
                "summary": "本课程介绍神经场理论，探讨如何用连续场模型来理解语义空间。",
                "knowledge_points": [
                    {"title": "神经场概念", "description": "神经场是将语义空间建模为连续向量场的理论框架。在这个视角下，语言不再是离散的符号，而是连续场中的点。场论提供了理解语言现象的新视角。", "category": "advanced_theory", "importance": 2},
                    {"title": "语义场", "description": "语义场是概念在向量空间中的分布。相似的概念在场中距离近，相关的概念形成场中的结构。场的拓扑结构反映了语言的深层规律。", "category": "advanced_theory", "importance": 2},
                    {"title": "吸引子动力学", "description": "吸引子是系统趋向的稳定状态。在语言场中，吸引子对应稳定的概念或表达。理解吸引子有助于理解语言的稳定性和变化。", "category": "advanced_theory", "importance": 2}
                ],
                "terms": [
                    {"term": "Neural Field", "definition": "神经场，连续的语义空间表示。", "category": "advanced_theory"},
                    {"term": "Attractor", "definition": "吸引子，系统趋向的稳定状态。", "category": "advanced_theory"},
                    {"term": "Topology", "definition": "拓扑，空间结构的数学描述。", "category": "advanced_theory"}
                ]
            },
            {
                "title": "Field Theory Integration",
                "topics": ["场论整合", "吸引子动力学", "场共振"],
                "summary": "本课程整合场论概念，探讨Context、Memory、Agent的统一框架。",
                "knowledge_points": [
                    {"title": "统一场理论", "description": "统一场理论试图将Context、Memory、Agent统一在一个框架下。在这个视角下，它们都是场的不同表现形式，遵循相同的动力学规律。", "category": "advanced_theory", "importance": 2},
                    {"title": "场共振", "description": "场共振描述不同场之间的相互作用和能量传递。在AI系统中，不同组件的「共振」可以产生涌现行为，这是理解复杂系统行为的关键。", "category": "advanced_theory", "importance": 2},
                    {"title": "边界管理", "description": "边界管理处理不同场之间的边界：信息如何跨边界流动、边界如何影响系统行为。这对于设计模块化系统有指导意义。", "category": "advanced_theory", "importance": 2}
                ],
                "terms": [
                    {"term": "Field Theory", "definition": "场论，研究场的物理理论。", "category": "advanced_theory"},
                    {"term": "Resonance", "definition": "共振，系统的周期性增强现象。", "category": "advanced_theory"},
                    {"term": "Emergence", "definition": "涌现，系统整体表现出的新特性。", "category": "advanced_theory"}
                ]
            },
            {
                "title": "Quantum Semantics",
                "topics": ["量子语义", "不确定性", "叠加态"],
                "summary": "本课程探讨量子力学概念在语义理解中的应用。",
                "knowledge_points": [
                    {"title": "量子语义概念", "description": "量子语义将量子力学的概念应用于语言理解：语义的不确定性（类似量子叠加）、语境的影响（类似测量坍缩）、概念的纠缠（类似量子纠缠）。", "category": "advanced_theory", "importance": 2},
                    {"title": "语义不确定性", "description": "语义在测量（理解）之前处于叠加态，包含多种可能含义。语境的作用类似于测量，使语义坍缩到特定解释。这解释了语言的歧义性和语境依赖性。", "category": "advanced_theory", "importance": 2},
                    {"title": "概念纠缠", "description": "概念纠缠描述概念之间的深层关联：理解一个概念会影响相关概念的状态。这对于理解语言的整体性和上下文效应有启发。", "category": "advanced_theory", "importance": 2}
                ],
                "terms": [
                    {"term": "Quantum Semantics", "definition": "量子语义，用量子概念理解语言的理论。", "category": "advanced_theory"},
                    {"term": "Superposition", "definition": "叠加态，同时处于多种状态的状态。", "category": "advanced_theory"},
                    {"term": "Entanglement", "definition": "纠缠，量子系统间的深层关联。", "category": "advanced_theory"}
                ]
            },
            {
                "title": "Unified Field",
                "topics": ["统一场理论", "演化与动力学"],
                "summary": "本课程总结场论模块，提出Context/Memory/Agent的统一框架。",
                "knowledge_points": [
                    {"title": "统一框架", "description": "统一场框架将AI系统的核心组件统一理解：Context是场的当前状态，Memory是场的历史轨迹，Agent是场的演化动力。这种视角有助于理解系统的整体行为。", "category": "advanced_theory", "importance": 2},
                    {"title": "场的演化", "description": "场的演化遵循动力学方程：输入改变场状态、场状态决定输出、历史影响当前状态。理解演化规律有助于预测和控制AI系统行为。", "category": "advanced_theory", "importance": 2},
                    {"title": "工程启示", "description": "场论视角对工程的启示：关注系统整体而非局部、理解组件间的相互作用、考虑历史和上下文的影响。这有助于设计更优雅、更强大的AI系统。", "category": "advanced_theory", "importance": 2}
                ],
                "terms": [
                    {"term": "Unified Field", "definition": "统一场，整合多种场的理论框架。", "category": "advanced_theory"},
                    {"term": "Evolution", "definition": "演化，系统状态随时间变化的过程。", "category": "advanced_theory"},
                    {"term": "Dynamics", "definition": "动力学，研究系统演化的学科。", "category": "advanced_theory"}
                ]
            }
        ]
    }
}

def init_db():
    print("Recreating database tables...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

def load_supplements():
    print("Loading course supplements...")
    db = SessionLocal()
    
    chinese_num_map = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10}
    
    try:
        for module_key, module_data in COURSE_SUPPLEMENTS.items():
            chinese_num = module_key.replace("第", "").replace("模块", "")
            order = chinese_num_map.get(chinese_num, 1)
            
            module = Module(
                name=module_data["name"],
                description=f"{module_data['name']} - AI培训课程",
                order_index=order
            )
            db.add(module)
            db.flush()
            
            print(f"\nModule {order}: {module_data['name']}")
            
            for idx, lesson_data in enumerate(module_data["lessons"]):
                date = f"2026-03-{16 + idx:02d}" if order == 1 else f"2026-0{order + 2}-{idx + 1:02d}"
                
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
                
                for kp_data in lesson_data["knowledge_points"]:
                    kp = KnowledgePoint(
                        lesson_id=lesson.id,
                        title=kp_data["title"],
                        description=kp_data["description"],
                        category=kp_data["category"],
                        importance=kp_data["importance"],
                        related_terms=[]
                    )
                    db.add(kp)
                
                for term_data in lesson_data["terms"]:
                    existing_term = db.query(Term).filter(Term.term == term_data["term"]).first()
                    if not existing_term:
                        existing_term = Term(
                            term=term_data["term"],
                            definition=term_data["definition"],
                            category=term_data["category"],
                            examples=[],
                            related_terms=[],
                            is_predefined=True
                        )
                        db.add(existing_term)
                        db.flush()
                    
                    lesson_term = LessonTerm(
                        lesson_id=lesson.id,
                        term_id=existing_term.id
                    )
                    db.add(lesson_term)
                
                print(f"  - {lesson_data['title']}: {len(lesson_data['knowledge_points'])} knowledge points, {len(lesson_data['terms'])} terms")
        
        db.commit()
        print("\nCourse supplements loaded successfully!")
        
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
        print(f"Error loading supplements: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
    load_supplements()
