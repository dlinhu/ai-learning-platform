import os
import sys

backend_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, backend_dir)

from app.utils.database import SessionLocal
from app.models.models import Module, Lesson, KnowledgePoint, Term, LessonTerm, PracticeQuestion

RAG_COURSES_DATA = {
    "simple_rag.ipynb": {
        "title": "Simple RAG / 基础RAG系统",
        "summary": "Learn the fundamentals of Retrieval-Augmented Generation systems including document processing, chunking, vector storage, and retrieval. / 学习检索增强生成系统的基础知识，包括文档处理、分块、向量存储和检索。",
        "knowledge_points": [
            {
                "title": "RAG System Components / RAG系统组件",
                "description": "RAG系统由文档加载器、文本分割器、嵌入模型、向量存储和检索器组成，实现从文档到检索的完整流程。",
                "description_en": "RAG systems consist of document loaders, text splitters, embedding models, vector stores, and retrievers, implementing the complete flow from documents to retrieval.",
                "importance": 3,
                "key_concepts": ["Document Loading / 文档加载", "Text Chunking / 文本分块", "Vector Store / 向量存储", "Retriever / 检索器"],
                "examples": [{"title": "Basic RAG Pipeline", "prompt": "loader = PyPDFLoader(path)\ndocuments = loader.load()\ntext_splitter = RecursiveCharacterTextSplitter(chunk_size=1000)\ntexts = text_splitter.split_documents(documents)\nvectorstore = FAISS.from_documents(texts, embeddings)", "response": "Complete RAG pipeline from document to vector store"}]
            },
            {
                "title": "Vector Store Creation / 向量存储创建",
                "description": "使用FAISS和OpenAI嵌入创建高效的向量存储，支持快速相似性搜索。",
                "description_en": "Create efficient vector stores using FAISS and OpenAI embeddings for fast similarity search.",
                "importance": 3,
                "key_concepts": ["FAISS / Facebook AI相似性搜索", "OpenAI Embeddings / OpenAI嵌入", "Similarity Search / 相似性搜索"],
                "examples": [{"title": "FAISS Vector Store", "prompt": "embeddings = OpenAIEmbeddings()\nvectorstore = FAISS.from_documents(texts, embeddings)\nretriever = vectorstore.as_retriever(search_kwargs={'k': 2})", "response": "Create retriever returning top 2 results"}]
            }
        ],
        "terms": [
            {"term": "RAG", "term_cn": "检索增强生成", "definition": "结合检索和生成的AI系统架构", "definition_en": "AI system architecture combining retrieval and generation"},
            {"term": "FAISS", "term_cn": "Facebook AI相似性搜索", "definition": "高效的向量相似性搜索库", "definition_en": "Efficient library for vector similarity search"},
            {"term": "Vector Store", "term_cn": "向量存储", "definition": "存储文档向量表示的数据库", "definition_en": "Database storing vector representations of documents"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "RAG系统的主要组件不包括以下哪个？", "options": ["A. 文档加载器", "B. 文本分割器", "C. 图像处理器", "D. 向量存储"], "answer": "C", "explanation": "RAG系统主要处理文本，核心组件包括文档加载器、文本分割器、嵌入模型、向量存储和检索器。", "difficulty": 1},
            {"kp_index": 1, "type": "single_choice", "question": "FAISS的主要作用是什么？", "options": ["A. 文档加载", "B. 向量相似性搜索", "C. 文本生成", "D. 图像处理"], "answer": "B", "explanation": "FAISS是Facebook开发的向量相似性搜索库，用于高效的向量检索。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "OpenAI Embeddings可以将文本转换为向量表示。", "answer": "正确", "explanation": "OpenAI Embeddings模型可以将文本转换为高维向量，用于相似性计算和检索。", "difficulty": 1}
        ]
    },
    "semantic_chunking.ipynb": {
        "title": "Semantic Chunking / 语义分块",
        "summary": "Learn semantic chunking techniques that create context-aware text segments based on meaning rather than fixed sizes. / 学习语义分块技术，基于语义而非固定大小创建上下文感知的文本片段。",
        "knowledge_points": [
            {
                "title": "Semantic Chunking Concept / 语义分块概念",
                "description": "语义分块根据文本的语义相似性进行分割，保持语义连贯性，避免在句子中间断开。",
                "description_en": "Semantic chunking splits text based on semantic similarity, maintaining semantic coherence and avoiding breaks in the middle of sentences.",
                "importance": 3,
                "key_concepts": ["Semantic coherence / 语义连贯性", "Breakpoint detection / 断点检测", "Context preservation / 上下文保持"],
                "examples": [{"title": "Semantic Chunker", "prompt": "text_splitter = SemanticChunker(\n    OpenAIEmbeddings(),\n    breakpoint_threshold_type='percentile',\n    breakpoint_threshold_amount=90\n)\ndocs = text_splitter.create_documents([content])", "response": "Create semantically coherent chunks"}]
            },
            {
                "title": "Breakpoint Types / 断点类型",
                "description": "三种断点类型：百分位数、标准差、四分位距，用于确定文本分割点。",
                "description_en": "Three breakpoint types: percentile, standard deviation, and interquartile range for determining text split points.",
                "importance": 2,
                "key_concepts": ["Percentile / 百分位数", "Standard Deviation / 标准差", "Interquartile Range / 四分位距"],
                "examples": [{"title": "Breakpoint Options", "prompt": "# Percentile: splits at differences > X percentile\n# Standard deviation: splits at differences > X std\n# Interquartile: uses IQR for split points", "response": "Different methods for semantic boundary detection"}]
            }
        ],
        "terms": [
            {"term": "Semantic Chunking", "term_cn": "语义分块", "definition": "基于语义相似性的文本分割方法", "definition_en": "Text splitting method based on semantic similarity"},
            {"term": "Breakpoint", "term_cn": "断点", "definition": "文本分割的位置点", "definition_en": "Position point for text splitting"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "语义分块相比固定大小分块的主要优势是什么？", "options": ["A. 更快的处理速度", "B. 保持语义连贯性", "C. 更小的存储空间", "D. 更简单的实现"], "answer": "B", "explanation": "语义分块的主要优势是根据语义相似性分割，保持语义连贯性。", "difficulty": 1},
            {"kp_index": 1, "type": "multiple_choice", "question": "语义分块支持哪些断点类型？", "options": ["A. 百分位数", "B. 标准差", "C. 固定长度", "D. 四分位距"], "answer": "A,B,D", "explanation": "语义分块支持百分位数、标准差、四分位距三种断点类型。", "difficulty": 1}
        ]
    },
    "reranking.ipynb": {
        "title": "Reranking / 重排序",
        "summary": "Learn reranking techniques that improve retrieval relevance by reassessing and reordering retrieved documents. / 学习重排序技术，通过重新评估和排序检索文档提高检索相关性。",
        "knowledge_points": [
            {
                "title": "Reranking Concept / 重排序概念",
                "description": "重排序是对初始检索结果进行重新评估和排序，使用更复杂的模型提高相关性判断。",
                "description_en": "Reranking reassesses and reorders initial retrieval results using more sophisticated models for better relevance judgment.",
                "importance": 3,
                "key_concepts": ["Relevance scoring / 相关性评分", "Document reordering / 文档重排序", "Quality improvement / 质量提升"],
                "examples": [{"title": "Reranking Process", "prompt": "1. Initial retrieval with vector search\n2. Score each document with LLM/CrossEncoder\n3. Sort by relevance score\n4. Return top K documents", "response": "Two-stage retrieval with reranking"}]
            },
            {
                "title": "LLM vs Cross-Encoder / LLM与交叉编码器",
                "description": "LLM重排序使用语言模型评分，Cross-Encoder使用专门训练的相关性模型，各有优势。",
                "description_en": "LLM reranking uses language models for scoring, Cross-Encoder uses specially trained relevance models, each with advantages.",
                "importance": 2,
                "key_concepts": ["LLM scoring / LLM评分", "Cross-Encoder / 交叉编码器", "Trade-offs / 权衡取舍"],
                "examples": [{"title": "Cross-Encoder Reranking", "prompt": "cross_encoder = CrossEncoder('cross-encoder/ms-marco-MiniLM-L-6-v2')\nscores = cross_encoder.predict([[query, doc] for doc in docs])", "response": "Fast and accurate relevance scoring"}]
            }
        ],
        "terms": [
            {"term": "Reranking", "term_cn": "重排序", "definition": "对检索结果重新排序的过程", "definition_en": "Process of reordering retrieval results"},
            {"term": "Cross-Encoder", "term_cn": "交叉编码器", "definition": "同时处理查询和文档的相关性模型", "definition_en": "Relevance model processing query and document together"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "重排序的主要目的是什么？", "options": ["A. 加快检索速度", "B. 提高检索相关性", "C. 减少存储空间", "D. 简化代码"], "answer": "B", "explanation": "重排序的主要目的是通过更复杂的模型重新评估文档相关性，提高检索质量。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "Cross-Encoder比LLM重排序更快。", "answer": "正确", "explanation": "Cross-Encoder是专门训练的轻量级模型，通常比调用LLM API更快。", "difficulty": 1}
        ]
    },
    "query_transformations.ipynb": {
        "title": "Query Transformations / 查询转换",
        "summary": "Learn query transformation techniques that improve retrieval by modifying or expanding user queries. / 学习查询转换技术，通过修改或扩展用户查询提高检索效果。",
        "knowledge_points": [
            {
                "title": "Query Expansion / 查询扩展",
                "description": "查询扩展通过生成多个相关查询或添加同义词来增强原始查询，提高召回率。",
                "description_en": "Query expansion enhances original queries by generating multiple related queries or adding synonyms to improve recall.",
                "importance": 3,
                "key_concepts": ["Multi-query generation / 多查询生成", "Synonym expansion / 同义词扩展", "Recall improvement / 召回率提升"],
                "examples": [{"title": "Multi-Query Expansion", "prompt": "original_query = \"climate change effects\"\nexpanded_queries = [\n    \"What are the impacts of climate change?\",\n    \"How does global warming affect the environment?\",\n    \"Consequences of climate change\"\n]", "response": "Generate multiple related queries for better retrieval"}]
            },
            {
                "title": "Query Rewriting / 查询重写",
                "description": "查询重写将模糊或复杂的查询转换为更清晰、更易检索的形式。",
                "description_en": "Query rewriting transforms vague or complex queries into clearer, more retrievable forms.",
                "importance": 2,
                "key_concepts": ["Query clarification / 查询澄清", "Intent understanding / 意图理解", "Optimization / 优化"],
                "examples": [{"title": "Query Rewriting", "prompt": "original = \"it doesn't work\"\nrewritten = \"What are common troubleshooting steps for [specific product] when it fails to start?\"", "response": "Transform vague query to specific one"}]
            }
        ],
        "terms": [
            {"term": "Query Expansion", "term_cn": "查询扩展", "definition": "扩展原始查询以提高检索覆盖范围", "definition_en": "Expanding original query to improve retrieval coverage"},
            {"term": "Query Rewriting", "term_cn": "查询重写", "definition": "重写查询使其更清晰易检索", "definition_en": "Rewriting query to be clearer and more retrievable"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "查询扩展的主要目的是什么？", "options": ["A. 减少查询数量", "B. 提高召回率", "C. 加快检索速度", "D. 减少存储"], "answer": "B", "explanation": "查询扩展通过生成多个相关查询提高召回率，找到更多相关文档。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "查询重写可以将模糊查询转换为更具体的查询。", "answer": "正确", "explanation": "查询重写的目的就是将模糊或复杂的查询转换为更清晰、更易检索的形式。", "difficulty": 1}
        ]
    },
    "contextual_compression.ipynb": {
        "title": "Contextual Compression / 上下文压缩",
        "summary": "Learn contextual compression techniques that extract and compress relevant information from retrieved documents. / 学习上下文压缩技术，从检索文档中提取和压缩相关信息。",
        "knowledge_points": [
            {
                "title": "Compression Concept / 压缩概念",
                "description": "上下文压缩从检索文档中提取与查询相关的部分，减少噪声并提高相关性。",
                "description_en": "Contextual compression extracts query-relevant parts from retrieved documents, reducing noise and improving relevance.",
                "importance": 2,
                "key_concepts": ["Relevant extraction / 相关提取", "Noise reduction / 噪声减少", "Context optimization / 上下文优化"],
                "examples": [{"title": "Contextual Compression", "prompt": "compressor = LLMChainExtractor.from_llm(llm)\ncompression_retriever = ContextualCompressionRetriever(\n    base_compressor=compressor,\n    base_retriever=base_retriever\n)", "response": "Extract only relevant parts from documents"}]
            }
        ],
        "terms": [
            {"term": "Contextual Compression", "term_cn": "上下文压缩", "definition": "从文档中提取相关部分的技术", "definition_en": "Technique for extracting relevant parts from documents"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "上下文压缩的主要作用是什么？", "options": ["A. 增加文档数量", "B. 提取相关部分减少噪声", "C. 加快处理速度", "D. 增加上下文长度"], "answer": "B", "explanation": "上下文压缩从检索文档中提取与查询相关的部分，减少噪声并提高相关性。", "difficulty": 1}
        ]
    },
    "self_rag.ipynb": {
        "title": "Self RAG / 自我RAG",
        "summary": "Learn Self-RAG that enables models to reflect on and improve their own retrieval and generation. / 学习自我RAG，让模型反思并改进自己的检索和生成过程。",
        "knowledge_points": [
            {
                "title": "Self-Reflection / 自我反思",
                "description": "Self-RAG让模型评估检索内容的相关性和生成答案的质量，进行自我改进。",
                "description_en": "Self-RAG enables models to evaluate retrieval relevance and generation quality for self-improvement.",
                "importance": 3,
                "key_concepts": ["Relevance assessment / 相关性评估", "Quality evaluation / 质量评估", "Self-improvement / 自我改进"],
                "examples": [{"title": "Self-RAG Process", "prompt": "1. Retrieve documents\n2. Assess relevance: Is this relevant?\n3. Generate answer\n4. Evaluate: Is this supported by context?\n5. Refine if needed", "response": "Iterative self-improvement loop"}]
            },
            {
                "title": "Adaptive Retrieval / 自适应检索",
                "description": "根据问题复杂度决定是否需要检索，避免不必要的检索操作。",
                "description_en": "Decide whether retrieval is needed based on question complexity, avoiding unnecessary retrieval operations.",
                "importance": 2,
                "key_concepts": ["Need assessment / 需求评估", "Efficiency optimization / 效率优化", "Dynamic decision / 动态决策"],
                "examples": [{"title": "Adaptive Decision", "prompt": "question = \"What is 2+2?\"\ndecision = \"No retrieval needed\"  # Simple question\n\nquestion = \"What are the latest AI trends?\"\ndecision = \"Retrieval needed\"  # Requires current info", "response": "Dynamic retrieval decision based on question type"}]
            }
        ],
        "terms": [
            {"term": "Self-RAG", "term_cn": "自我RAG", "definition": "具备自我反思能力的RAG系统", "definition_en": "RAG system with self-reflection capabilities"},
            {"term": "Self-Reflection", "term_cn": "自我反思", "definition": "模型评估自身输出的能力", "definition_en": "Model's ability to evaluate its own outputs"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "Self-RAG的核心特点是什么？", "options": ["A. 更快的检索", "B. 自我反思和改进", "C. 更大的存储", "D. 更简单的实现"], "answer": "B", "explanation": "Self-RAG的核心特点是让模型评估检索和生成质量，进行自我改进。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "自适应检索可以根据问题复杂度决定是否需要检索。", "answer": "正确", "explanation": "自适应检索会评估问题是否需要检索，避免不必要的检索操作。", "difficulty": 1}
        ]
    },
    "crag.ipynb": {
        "title": "CRAG / 纠正性RAG",
        "summary": "Learn Corrective RAG (CRAG) that corrects retrieval errors through document evaluation and knowledge refinement. / 学习纠正性RAG，通过文档评估和知识精炼纠正检索错误。",
        "knowledge_points": [
            {
                "title": "Document Evaluation / 文档评估",
                "description": "CRAG评估检索文档的相关性，决定是使用、丢弃还是补充知识。",
                "description_en": "CRAG evaluates retrieved document relevance to decide whether to use, discard, or supplement knowledge.",
                "importance": 3,
                "key_concepts": ["Relevance scoring / 相关性评分", "Decision making / 决策制定", "Quality control / 质量控制"],
                "examples": [{"title": "CRAG Flow", "prompt": "1. Retrieve documents\n2. Evaluate: relevant or not?\n3. If relevant → use\n4. If irrelevant → web search\n5. If ambiguous → combine both", "response": "Corrective retrieval with fallback options"}]
            },
            {
                "title": "Knowledge Refinement / 知识精炼",
                "description": "从相关文档中提取关键信息，过滤无关内容，提高答案质量。",
                "description_en": "Extract key information from relevant documents, filter irrelevant content, improve answer quality.",
                "importance": 2,
                "key_concepts": ["Information extraction / 信息提取", "Content filtering / 内容过滤", "Quality enhancement / 质量增强"],
                "examples": [{"title": "Refinement Process", "prompt": "relevant_docs = evaluate_documents(retrieved_docs)\nrefined_knowledge = extract_key_points(relevant_docs)\nanswer = generate_with_context(query, refined_knowledge)", "response": "Extract and refine knowledge for better answers"}]
            }
        ],
        "terms": [
            {"term": "CRAG", "term_cn": "纠正性RAG", "definition": "具备纠正能力的检索增强生成", "definition_en": "Corrective Retrieval-Augmented Generation"},
            {"term": "Knowledge Refinement", "term_cn": "知识精炼", "definition": "从文档中提取和过滤关键信息", "definition_en": "Extracting and filtering key information from documents"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "CRAG对不相关文档的处理方式是什么？", "options": ["A. 直接使用", "B. 丢弃并可能使用网络搜索", "C. 忽略", "D. 重新生成"], "answer": "B", "explanation": "CRAG会评估文档相关性，对不相关文档丢弃并可能使用网络搜索补充知识。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "知识精炼可以提高答案质量。", "answer": "正确", "explanation": "知识精炼从相关文档中提取关键信息，过滤无关内容，提高答案质量。", "difficulty": 1}
        ]
    },
    "graph_rag.ipynb": {
        "title": "Graph RAG / 图RAG",
        "summary": "Learn Graph RAG that uses knowledge graphs to enhance retrieval and reasoning capabilities. / 学习图RAG，使用知识图谱增强检索和推理能力。",
        "knowledge_points": [
            {
                "title": "Knowledge Graph Integration / 知识图谱集成",
                "description": "Graph RAG将知识图谱与向量检索结合，提供结构化知识和语义理解。",
                "description_en": "Graph RAG combines knowledge graphs with vector retrieval, providing structured knowledge and semantic understanding.",
                "importance": 3,
                "key_concepts": ["Entity relationships / 实体关系", "Structured knowledge / 结构化知识", "Graph traversal / 图遍历"],
                "examples": [{"title": "Graph RAG Query", "prompt": "1. Extract entities from query\n2. Find related nodes in graph\n3. Traverse relationships\n4. Combine with vector retrieval\n5. Generate comprehensive answer", "response": "Combine graph and vector retrieval"}]
            },
            {
                "title": "Multi-hop Reasoning / 多跳推理",
                "description": "通过知识图谱的关系链实现多跳推理，回答需要连接多个知识点的问题。",
                "description_en": "Enable multi-hop reasoning through knowledge graph relationship chains for questions requiring connected knowledge.",
                "importance": 2,
                "key_concepts": ["Relationship chains / 关系链", "Reasoning paths / 推理路径", "Knowledge connection / 知识连接"],
                "examples": [{"title": "Multi-hop Query", "prompt": "Query: \"Who is the CEO of the company that acquired Instagram?\"\nHop 1: Instagram → acquired by → Meta\nHop 2: Meta → CEO → Mark Zuckerberg", "response": "Two-hop reasoning through knowledge graph"}]
            }
        ],
        "terms": [
            {"term": "Graph RAG", "term_cn": "图RAG", "definition": "结合知识图谱的检索增强生成", "definition_en": "RAG combined with knowledge graphs"},
            {"term": "Knowledge Graph", "term_cn": "知识图谱", "definition": "结构化的知识表示，包含实体和关系", "definition_en": "Structured knowledge representation with entities and relationships"},
            {"term": "Multi-hop Reasoning", "term_cn": "多跳推理", "definition": "通过多个知识连接进行推理", "definition_en": "Reasoning through multiple knowledge connections"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "Graph RAG的主要优势是什么？", "options": ["A. 更快的检索速度", "B. 提供结构化知识和语义理解", "C. 更小的存储空间", "D. 更简单的实现"], "answer": "B", "explanation": "Graph RAG将知识图谱与向量检索结合，提供结构化知识和语义理解。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "多跳推理可以回答需要连接多个知识点的问题。", "answer": "正确", "explanation": "多跳推理通过知识图谱的关系链连接多个知识点，回答复杂问题。", "difficulty": 1}
        ]
    },
    "HyDe_Hypothetical_Document_Embedding.ipynb": {
        "title": "HyDe / 假设文档嵌入",
        "summary": "Learn Hypothetical Document Embedding (HyDe) that generates hypothetical documents to improve retrieval. / 学习假设文档嵌入技术，通过生成假设文档提高检索效果。",
        "knowledge_points": [
            {
                "title": "Hypothetical Document Generation / 假设文档生成",
                "description": "HyDe让LLM生成一个假设的理想答案文档，然后用这个文档进行检索，提高检索相关性。",
                "description_en": "HyDe has LLM generate a hypothetical ideal answer document, then uses this document for retrieval to improve relevance.",
                "importance": 3,
                "key_concepts": ["Hypothetical answer / 假设答案", "Document generation / 文档生成", "Enhanced retrieval / 增强检索"],
                "examples": [{"title": "HyDe Process", "prompt": "query = \"What causes climate change?\"\nhypothetical_doc = llm.generate(\"Write an answer about climate change causes\")\nembedding = embed(hypothetical_doc)\nresults = vector_store.search(embedding)", "response": "Use hypothetical document for better retrieval"}]
            },
            {
                "title": "Semantic Bridging / 语义桥接",
                "description": "假设文档作为查询和真实文档之间的语义桥梁，弥补词汇不匹配问题。",
                "description_en": "Hypothetical document acts as semantic bridge between query and real documents, addressing vocabulary mismatch.",
                "importance": 2,
                "key_concepts": ["Vocabulary mismatch / 词汇不匹配", "Semantic similarity / 语义相似性", "Bridge mechanism / 桥接机制"],
                "examples": [{"title": "Semantic Bridge", "prompt": "Query: \"How to fix slow computer?\"\nHypothetical: \"To improve computer performance, you can...\"\nThis bridges to documents about \"system optimization\", \"RAM upgrade\", etc.", "response": "Hypothetical document expands semantic coverage"}]
            }
        ],
        "terms": [
            {"term": "HyDe", "term_cn": "假设文档嵌入", "definition": "生成假设文档用于检索的技术", "definition_en": "Hypothetical Document Embedding technique"},
            {"term": "Vocabulary Mismatch", "term_cn": "词汇不匹配", "definition": "查询词与文档词不一致的问题", "definition_en": "Problem where query terms don't match document terms"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "HyDe的核心思想是什么？", "options": ["A. 直接使用查询检索", "B. 生成假设文档用于检索", "C. 增加检索数量", "D. 使用多个嵌入模型"], "answer": "B", "explanation": "HyDe的核心思想是让LLM生成假设的理想答案文档，然后用这个文档进行检索。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "假设文档可以解决词汇不匹配问题。", "answer": "正确", "explanation": "假设文档作为语义桥梁，弥补查询词和文档词不一致的问题。", "difficulty": 1}
        ]
    },
    "raptor.ipynb": {
        "title": "RAPTOR / 递归摘要树",
        "summary": "Learn RAPTOR (Recursive Abstractive Processing for Tree-Organized Retrieval) that builds hierarchical document summaries. / 学习RAPTOR递归摘要树技术，构建层次化文档摘要。",
        "knowledge_points": [
            {
                "title": "Hierarchical Summarization / 层次化摘要",
                "description": "RAPTOR递归地构建文档摘要树，从底层文档到高层摘要，支持多粒度检索。",
                "description_en": "RAPTOR recursively builds document summary trees, from bottom-level documents to top-level summaries, supporting multi-granularity retrieval.",
                "importance": 3,
                "key_concepts": ["Tree structure / 树结构", "Recursive summarization / 递归摘要", "Multi-granularity / 多粒度"],
                "examples": [{"title": "RAPTOR Tree", "prompt": "Level 0: Original documents\nLevel 1: Summaries of document clusters\nLevel 2: Summaries of Level 1 summaries\n...\nQuery: search across all levels", "response": "Hierarchical retrieval from fine to coarse granularity"}]
            },
            {
                "title": "Cluster-based Summarization / 聚类摘要",
                "description": "将相似文档聚类后生成摘要，保留主题连贯性，提高检索效率。",
                "description_en": "Cluster similar documents then generate summaries, preserving topic coherence and improving retrieval efficiency.",
                "importance": 2,
                "key_concepts": ["Document clustering / 文档聚类", "Topic coherence / 主题连贯", "Efficient retrieval / 高效检索"],
                "examples": [{"title": "Clustering Process", "prompt": "1. Embed all documents\n2. Cluster by similarity\n3. Generate summary for each cluster\n4. Recursively cluster summaries\n5. Build tree structure", "response": "Build hierarchical summary tree from documents"}]
            }
        ],
        "terms": [
            {"term": "RAPTOR", "term_cn": "递归摘要树", "definition": "树状组织的递归摘要检索", "definition_en": "Recursive Abstractive Processing for Tree-Organized Retrieval"},
            {"term": "Hierarchical Retrieval", "term_cn": "层次化检索", "definition": "在多个粒度级别进行检索", "definition_en": "Retrieval across multiple granularity levels"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "RAPTOR的主要特点是什么？", "options": ["A. 单层检索", "B. 层次化摘要树", "C. 固定分块", "D. 线性处理"], "answer": "B", "explanation": "RAPTOR的主要特点是递归地构建文档摘要树，支持多粒度检索。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "聚类摘要可以保留主题连贯性。", "answer": "正确", "explanation": "将相似文档聚类后生成摘要，可以保留主题连贯性，提高检索效率。", "difficulty": 1}
        ]
    },
    "fusion_retrieval.ipynb": {
        "title": "Fusion Retrieval / 融合检索",
        "summary": "Learn fusion retrieval techniques that combine multiple retrieval methods for better results. / 学习融合检索技术，结合多种检索方法获得更好结果。",
        "knowledge_points": [
            {
                "title": "Multi-Method Fusion / 多方法融合",
                "description": "融合检索结合向量检索、关键词检索等多种方法，综合排序提高检索质量。",
                "description_en": "Fusion retrieval combines vector retrieval, keyword retrieval, and other methods, ranking comprehensively to improve retrieval quality.",
                "importance": 3,
                "key_concepts": ["Vector retrieval / 向量检索", "Keyword retrieval / 关键词检索", "Result fusion / 结果融合"],
                "examples": [{"title": "Fusion Process", "prompt": "vector_results = vector_store.search(query)\nkeyword_results = bm25_search(query)\nfused_results = reciprocal_rank_fusion(\n    [vector_results, keyword_results]\n)", "response": "Combine multiple retrieval methods"}]
            },
            {
                "title": "Reciprocal Rank Fusion / 倒数排名融合",
                "description": "RRF算法根据各方法的排名倒数计算综合分数，简单有效地融合多种检索结果。",
                "description_en": "RRF algorithm calculates comprehensive scores based on reciprocal ranks from each method, simply and effectively fusing multiple retrieval results.",
                "importance": 2,
                "key_concepts": ["Rank aggregation / 排名聚合", "Score combination / 分数组合", "Simple effective / 简单有效"],
                "examples": [{"title": "RRF Formula", "prompt": "def rrf(rankings, k=60):\n    scores = {}\n    for ranking in rankings:\n        for i, doc in enumerate(ranking):\n            scores[doc] = scores.get(doc, 0) + 1/(k + i + 1)\n    return sorted(scores.items(), key=lambda x: -x[1])", "response": "Simple and effective fusion algorithm"}]
            }
        ],
        "terms": [
            {"term": "Fusion Retrieval", "term_cn": "融合检索", "definition": "结合多种检索方法的检索技术", "definition_en": "Retrieval technique combining multiple retrieval methods"},
            {"term": "Reciprocal Rank Fusion", "term_cn": "倒数排名融合", "definition": "基于排名倒数融合结果的算法", "definition_en": "Algorithm fusing results based on reciprocal ranks"}
        ],
        "questions": [
            {"kp_index": 0, "type": "multiple_choice", "question": "融合检索可以结合哪些方法？", "options": ["A. 向量检索", "B. 关键词检索", "C. 图像检索", "D. 语义检索"], "answer": "A,B,D", "explanation": "融合检索可以结合向量检索、关键词检索、语义检索等多种文本检索方法。", "difficulty": 1},
            {"kp_index": 1, "type": "single_choice", "question": "RRF算法的主要优点是什么？", "options": ["A. 复杂度高", "B. 简单有效", "C. 需要训练", "D. 只支持两种方法"], "answer": "B", "explanation": "RRF算法根据排名倒数计算综合分数，简单有效地融合多种检索结果。", "difficulty": 1}
        ]
    },
    "adaptive_retrieval.ipynb": {
        "title": "Adaptive Retrieval / 自适应检索",
        "summary": "Learn adaptive retrieval techniques that adjust retrieval strategies based on query characteristics. / 学习自适应检索技术，根据查询特征调整检索策略。",
        "knowledge_points": [
            {
                "title": "Query Analysis / 查询分析",
                "description": "自适应检索分析查询的复杂度、类型、领域等特征，选择最适合的检索策略。",
                "description_en": "Adaptive retrieval analyzes query characteristics like complexity, type, and domain to select the most suitable retrieval strategy.",
                "importance": 3,
                "key_concepts": ["Query complexity / 查询复杂度", "Query type / 查询类型", "Strategy selection / 策略选择"],
                "examples": [{"title": "Adaptive Strategy", "prompt": "if is_simple_fact(query):\n    use_keyword_search()\nelif needs_reasoning(query):\n    use_multi_hop_retrieval()\nelse:\n    use_hybrid_search()", "response": "Select retrieval strategy based on query analysis"}]
            }
        ],
        "terms": [
            {"term": "Adaptive Retrieval", "term_cn": "自适应检索", "definition": "根据查询特征调整检索策略", "definition_en": "Adjusting retrieval strategy based on query characteristics"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "自适应检索的核心是什么？", "options": ["A. 固定检索策略", "B. 根据查询特征调整策略", "C. 增加检索数量", "D. 减少检索时间"], "answer": "B", "explanation": "自适应检索的核心是根据查询的复杂度、类型等特征选择最适合的检索策略。", "difficulty": 1}
        ]
    },
    "multi_model_rag_with_captioning.ipynb": {
        "title": "Multi-Modal RAG / 多模态RAG",
        "summary": "Learn multi-modal RAG techniques that handle images, tables, and text in documents. / 学习多模态RAG技术，处理文档中的图像、表格和文本。",
        "knowledge_points": [
            {
                "title": "Image Understanding / 图像理解",
                "description": "多模态RAG使用视觉模型为图像生成描述，使图像内容可被检索。",
                "description_en": "Multi-modal RAG uses vision models to generate descriptions for images, making image content retrievable.",
                "importance": 3,
                "key_concepts": ["Vision models / 视觉模型", "Image captioning / 图像字幕", "Multi-modal embedding / 多模态嵌入"],
                "examples": [{"title": "Image Processing", "prompt": "image = load_image(document)\ncaption = vision_model.generate_caption(image)\nembedding = embed_text(caption)\nstore_in_vector_db(embedding, image_reference)", "response": "Make images searchable through captions"}]
            },
            {
                "title": "Table Extraction / 表格提取",
                "description": "从文档中提取表格数据，转换为结构化格式或文本描述进行检索。",
                "description_en": "Extract table data from documents, convert to structured format or text description for retrieval.",
                "importance": 2,
                "key_concepts": ["Table detection / 表格检测", "Structure extraction / 结构提取", "Text conversion / 文本转换"],
                "examples": [{"title": "Table Processing", "prompt": "tables = extract_tables(pdf)\nfor table in tables:\n    text_representation = table_to_markdown(table)\n    store_for_retrieval(text_representation)", "response": "Convert tables to searchable text"}]
            }
        ],
        "terms": [
            {"term": "Multi-Modal RAG", "term_cn": "多模态RAG", "definition": "处理多种数据类型的RAG系统", "definition_en": "RAG system handling multiple data types"},
            {"term": "Image Captioning", "term_cn": "图像字幕", "definition": "为图像生成文字描述", "definition_en": "Generating text descriptions for images"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "多模态RAG如何处理图像？", "options": ["A. 忽略图像", "B. 生成图像描述用于检索", "C. 只存储图像", "D. 删除图像"], "answer": "B", "explanation": "多模态RAG使用视觉模型为图像生成描述，使图像内容可被检索。", "difficulty": 1},
            {"kp_index": 1, "type": "true_false", "question": "表格可以转换为文本进行检索。", "answer": "正确", "explanation": "从文档中提取的表格可以转换为结构化格式或文本描述进行检索。", "difficulty": 1}
        ]
    },
    "simple_csv_rag.ipynb": {
        "title": "CSV RAG / CSV表格RAG",
        "summary": "Learn RAG techniques specifically designed for CSV and tabular data. / 学习专门为CSV和表格数据设计的RAG技术。",
        "knowledge_points": [
            {
                "title": "Tabular Data Processing / 表格数据处理",
                "description": "CSV RAG将表格数据转换为适合检索的格式，支持结构化查询和自然语言查询。",
                "description_en": "CSV RAG converts tabular data to retrieval-friendly format, supporting structured queries and natural language queries.",
                "importance": 2,
                "key_concepts": ["Data conversion / 数据转换", "Structured queries / 结构化查询", "Natural language interface / 自然语言接口"],
                "examples": [{"title": "CSV Processing", "prompt": "df = pd.read_csv('data.csv')\ndocuments = [\n    Document(page_content=row_to_text(row))\n    for _, row in df.iterrows()\n]\nvectorstore = FAISS.from_documents(documents, embeddings)", "response": "Convert CSV rows to searchable documents"}]
            }
        ],
        "terms": [
            {"term": "CSV RAG", "term_cn": "CSV RAG", "definition": "处理CSV表格数据的RAG系统", "definition_en": "RAG system for CSV tabular data"}
        ],
        "questions": [
            {"kp_index": 0, "type": "single_choice", "question": "CSV RAG如何处理表格数据？", "options": ["A. 直接存储原始文件", "B. 转换为适合检索的格式", "C. 只读取第一行", "D. 忽略表格结构"], "answer": "B", "explanation": "CSV RAG将表格数据转换为适合检索的格式，支持结构化查询和自然语言查询。", "difficulty": 1}
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

This lesson covered key RAG techniques. Practice these concepts to build better retrieval systems.

本课程涵盖了关键RAG技术。练习这些概念以构建更好的检索系统。

## Next Steps / 下一步

1. Implement the techniques / 实现这些技术
2. Compare different approaches / 比较不同方法
3. Optimize for your use case / 针对您的场景优化
"""
    return content

def batch_update_rag_courses():
    print("Starting batch update of RAG courses...")
    db = SessionLocal()
    
    try:
        rag_module = db.query(Module).filter(Module.name.like('%RAG%')).first()
        if not rag_module:
            rag_module = Module(
                name="RAG 检索增强生成",
                description="Comprehensive RAG techniques course covering basic to advanced retrieval methods. / 全面的RAG技术课程，涵盖从基础到高级的检索方法。"
            )
            db.add(rag_module)
            db.commit()
            print(f"Created module: {rag_module.name}")
        else:
            print(f"Using existing module: {rag_module.name}")
        
        total_lessons = 0
        total_kps = 0
        total_terms = 0
        total_questions = 0
        
        for notebook_name, course_data in RAG_COURSES_DATA.items():
            print(f"\nProcessing: {notebook_name}")
            
            existing_lesson = db.query(Lesson).filter(Lesson.title == course_data['title']).first()
            if existing_lesson:
                lesson = existing_lesson
                db.query(KnowledgePoint).filter(KnowledgePoint.lesson_id == lesson.id).delete()
                db.query(LessonTerm).filter(LessonTerm.lesson_id == lesson.id).delete()
                print(f"  Updating existing lesson: {lesson.title}")
            else:
                lesson = Lesson(
                    module_id=rag_module.id,
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
            material_filename = f"rag_{notebook_name.replace('.ipynb', '')}.md"
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
                    category='rag',
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
                        category='rag',
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
    batch_update_rag_courses()
