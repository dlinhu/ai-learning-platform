import os
import re
import json
import nbformat
from typing import List, Dict, Optional, Tuple
from dataclasses import dataclass, field, asdict
from pathlib import Path

@dataclass
class KnowledgePoint:
    title: str
    description: str
    category: str = "general"
    importance: int = 1
    related_terms: List[str] = field(default_factory=list)

@dataclass
class Term:
    term: str
    definition: str
    category: str = "general"
    examples: List[str] = field(default_factory=list)
    related_terms: List[str] = field(default_factory=list)

@dataclass
class ParsedContent:
    title: str
    summary: str
    sections: List[Dict]
    knowledge_points: List[KnowledgePoint]
    terms: List[Term]
    code_examples: List[Dict]
    raw_content: str

class ContentParser:
    def __init__(self, content_path: str):
        self.content_path = Path(content_path)
        self.ai_terms = self._load_ai_terms()
    
    def _load_ai_terms(self) -> Dict:
        return {
            "Prompt": "提示词，用户输入给AI模型的指令或问题",
            "Zero-shot": "零样本学习，模型在没有示例的情况下完成任务",
            "Few-shot": "少样本学习，模型通过少量示例学习完成任务",
            "CoT": "Chain of Thought，思维链，通过逐步推理解决复杂问题",
            "RAG": "Retrieval-Augmented Generation，检索增强生成",
            "Agent": "智能体，能够自主执行任务的AI系统",
            "ReAct": "Reasoning + Acting，推理与行动结合的Agent模式",
            "Tool": "工具，Agent可以调用的外部功能",
            "Memory": "记忆，Agent存储和检索信息的能力",
            "Context": "上下文，模型处理时的背景信息",
            "Token": "词元，文本的最小处理单位",
            "Embedding": "嵌入，将文本转换为向量表示",
            "Vector Store": "向量存储，存储和检索嵌入向量的数据库",
            "Chunk": "分块，将长文本分割成较小的片段",
            "Reranking": "重排序，对检索结果进行重新排序",
            "HyDE": "Hypothetical Document Embedding，假设文档嵌入",
            "LangGraph": "LangChain的工作流编排框架",
            "MCP": "Model Context Protocol，模型上下文协议",
            "Schema": "模式，定义数据结构的规范",
            "Prompt Engineering": "提示词工程，设计和优化提示词的技术",
            "Temperature": "温度，控制模型输出随机性的参数",
            "Top-p": "核采样参数，控制模型输出的多样性",
            "Max Tokens": "最大词元数，限制模型输出的长度",
            "System Prompt": "系统提示，定义模型行为和角色的指令",
            "User Prompt": "用户提示，用户的具体问题或指令",
            "Assistant": "助手，AI模型的回复角色",
            "Function Calling": "函数调用，模型调用外部函数的能力",
            "Streaming": "流式输出，逐步返回模型生成的内容",
            "Hallucination": "幻觉，模型生成不准确或虚假信息",
            "Fine-tuning": "微调，在特定数据上训练模型",
            "In-context Learning": "上下文学习，模型从上下文中学习",
            "Self-consistency": "自洽性，多次采样取一致结果",
            "Role Prompting": "角色提示，让模型扮演特定角色",
            "Task Decomposition": "任务分解，将复杂任务拆分为子任务",
            "Prompt Chaining": "提示链，多个提示词串联执行",
            "Long Context": "长上下文，处理大量文本的能力",
            "Context Window": "上下文窗口，模型能处理的最大文本长度",
            "Semantic Search": "语义搜索，基于语义相似度的搜索",
            "Knowledge Graph": "知识图谱，结构化的知识表示",
            "Multi-agent": "多智能体，多个Agent协作的系统",
            "Orchestrator": "编排器，协调多个Agent的组件",
            "Guardrails": "护栏，限制模型行为的机制",
            "Observability": "可观测性，监控系统状态的能力",
            "LangSmith": "LangChain的监控和调试平台",
            "Ollama": "本地运行大语言模型的工具",
            "Docker": "容器化部署平台",
            "FastAPI": "高性能Python Web框架",
            "Redis": "内存数据库，常用于缓存和会话存储",
            "SSE": "Server-Sent Events，服务器推送事件",
            "Neural Field": "神经场，连续的语义空间表示",
            "Attractor": "吸引子，系统趋向的稳定状态",
            "Emergence": "涌现，系统整体表现出的新特性",
        }
    
    def parse_file(self, file_path: str) -> Optional[ParsedContent]:
        full_path = self.content_path / file_path
        
        if not full_path.exists():
            return None
        
        ext = full_path.suffix.lower()
        
        if ext == '.md':
            return self._parse_markdown(full_path)
        elif ext == '.ipynb':
            return self._parse_notebook(full_path)
        elif ext == '.py':
            return self._parse_python(full_path)
        
        return None
    
    def _parse_markdown(self, file_path: Path) -> ParsedContent:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.split('\n')
        title = ""
        sections = []
        current_section = {"title": "", "content": [], "level": 1}
        code_examples = []
        in_code_block = False
        code_block = {"language": "", "code": ""}
        
        for line in lines:
            if line.startswith('# '):
                if current_section["content"]:
                    sections.append(current_section)
                title = line[2:].strip()
                current_section = {"title": title, "content": [], "level": 1}
            elif line.startswith('## '):
                if current_section["content"]:
                    sections.append(current_section)
                current_section = {"title": line[3:].strip(), "content": [], "level": 2}
            elif line.startswith('### '):
                if current_section["content"]:
                    sections.append(current_section)
                current_section = {"title": line[4:].strip(), "content": [], "level": 3}
            elif line.startswith('```'):
                if in_code_block:
                    if code_block["code"]:
                        code_examples.append(code_block)
                    code_block = {"language": "", "code": ""}
                    in_code_block = False
                else:
                    in_code_block = True
                    code_block = {"language": line[3:].strip(), "code": ""}
            elif in_code_block:
                code_block["code"] += line + '\n'
            else:
                current_section["content"].append(line)
        
        if current_section["content"]:
            sections.append(current_section)
        
        summary = self._generate_summary(content, sections)
        knowledge_points = self._extract_knowledge_points(content, sections)
        terms = self._extract_terms(content)
        
        return ParsedContent(
            title=title or file_path.stem,
            summary=summary,
            sections=sections,
            knowledge_points=knowledge_points,
            terms=terms,
            code_examples=code_examples,
            raw_content=content
        )
    
    def _parse_notebook(self, file_path: Path) -> ParsedContent:
        with open(file_path, 'r', encoding='utf-8') as f:
            nb = nbformat.read(f, as_version=4)
        
        title = file_path.stem
        sections = []
        code_examples = []
        markdown_content = []
        
        for cell in nb.cells:
            if cell.cell_type == 'markdown':
                lines = cell.source.split('\n')
                for line in lines:
                    if line.startswith('# '):
                        title = line[2:].strip()
                    elif line.startswith('## '):
                        if markdown_content:
                            sections.append({
                                "title": line[3:].strip(),
                                "content": markdown_content,
                                "level": 2
                            })
                            markdown_content = []
                    else:
                        markdown_content.append(line)
            elif cell.cell_type == 'code':
                code_examples.append({
                    "language": "python",
                    "code": cell.source
                })
        
        content = '\n'.join([s.get('content', '') if isinstance(s.get('content'), str) else '\n'.join(s.get('content', [])) for s in sections])
        summary = self._generate_summary(content, sections)
        knowledge_points = self._extract_knowledge_points(content, sections)
        terms = self._extract_terms(content)
        
        return ParsedContent(
            title=title,
            summary=summary,
            sections=sections,
            knowledge_points=knowledge_points,
            terms=terms,
            code_examples=code_examples,
            raw_content=content
        )
    
    def _parse_python(self, file_path: Path) -> ParsedContent:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        docstring = ""
        match = re.search(r'"""(.+?)"""', content, re.DOTALL)
        if match:
            docstring = match.group(1).strip()
        
        functions = re.findall(r'def\s+(\w+)\s*\([^)]*\):\s*"""([^"]*)"""?', content, re.DOTALL)
        classes = re.findall(r'class\s+(\w+)[^:]*:\s*"""([^"]*)"""?', content, re.DOTALL)
        
        sections = []
        for func_name, func_doc in functions:
            sections.append({
                "title": f"Function: {func_name}",
                "content": [func_doc.strip()],
                "level": 2
            })
        
        for class_name, class_doc in classes:
            sections.append({
                "title": f"Class: {class_name}",
                "content": [class_doc.strip()],
                "level": 2
            })
        
        knowledge_points = self._extract_knowledge_points(content, sections)
        terms = self._extract_terms(content)
        
        return ParsedContent(
            title=file_path.stem,
            summary=docstring[:500] if docstring else f"Python file: {file_path.name}",
            sections=sections,
            knowledge_points=knowledge_points,
            terms=terms,
            code_examples=[{"language": "python", "code": content}],
            raw_content=content
        )
    
    def _generate_summary(self, content: str, sections: List[Dict]) -> str:
        paragraphs = []
        for section in sections:
            text = ' '.join(section.get('content', []))
            text = re.sub(r'[#*`_\[\]]', '', text)
            text = re.sub(r'\s+', ' ', text).strip()
            if text:
                paragraphs.append(text)
        
        summary = ' '.join(paragraphs[:3])
        if len(summary) > 500:
            summary = summary[:500] + '...'
        
        return summary
    
    def _extract_knowledge_points(self, content: str, sections: List[Dict]) -> List[KnowledgePoint]:
        knowledge_points = []
        
        patterns = [
            (r'##\s+(.+?)(?:\n|$)', 2),
            (r'###\s+(.+?)(?:\n|$)', 3),
            (r'\*\*(.+?)\*\*[：:]\s*(.+?)(?:\n|$)', 1),
            (r'^[-*]\s+\*\*(.+?)\*\*[：:]?\s*(.+?)$', 1),
        ]
        
        seen_titles = set()
        
        for section in sections:
            title = section.get('title', '')
            if title and title not in seen_titles:
                content_text = ' '.join(section.get('content', []))
                importance = 1 if section.get('level', 1) == 2 else 2
                
                related = []
                for term in self.ai_terms:
                    if term.lower() in content_text.lower() or term.lower() in title.lower():
                        related.append(term)
                
                kp = KnowledgePoint(
                    title=title,
                    description=content_text[:200] if content_text else f"关于{title}的内容",
                    category=self._categorize(title, content_text),
                    importance=importance,
                    related_terms=related[:5]
                )
                knowledge_points.append(kp)
                seen_titles.add(title)
        
        return knowledge_points[:20]
    
    def _extract_terms(self, content: str) -> List[Term]:
        terms = []
        found_terms = set()
        
        for term, definition in self.ai_terms.items():
            if term.lower() in content.lower() and term not in found_terms:
                context = self._find_context(content, term)
                terms.append(Term(
                    term=term,
                    definition=definition,
                    category=self._categorize(term, definition),
                    examples=[context] if context else [],
                    related_terms=self._find_related_terms(term)
                ))
                found_terms.add(term)
        
        return terms
    
    def _find_context(self, content: str, term: str) -> str:
        pattern = rf'.{{0,100}}{re.escape(term)}.{{0,100}}'
        match = re.search(pattern, content, re.IGNORECASE | re.DOTALL)
        if match:
            context = match.group(0).strip()
            context = re.sub(r'\s+', ' ', context)
            return context[:200]
        return ""
    
    def _find_related_terms(self, term: str) -> List[str]:
        related_map = {
            "Prompt": ["Prompt Engineering", "System Prompt", "User Prompt"],
            "Zero-shot": ["Few-shot", "In-context Learning"],
            "Few-shot": ["Zero-shot", "In-context Learning"],
            "CoT": ["Self-consistency", "Task Decomposition"],
            "RAG": ["Vector Store", "Embedding", "Chunk", "Semantic Search"],
            "Agent": ["ReAct", "Tool", "Memory", "Multi-agent"],
            "ReAct": ["Agent", "Tool", "Reasoning"],
            "LangGraph": ["Agent", "Orchestrator", "Multi-agent"],
            "MCP": ["Tool", "Function Calling", "Agent"],
            "Context": ["Context Window", "Long Context", "Token"],
            "Embedding": ["Vector Store", "Semantic Search", "RAG"],
        }
        return related_map.get(term, [])
    
    def _categorize(self, title: str, content: str) -> str:
        text = (title + ' ' + content).lower()
        
        if any(kw in text for kw in ['prompt', '提示', '指令']):
            return "prompt_engineering"
        elif any(kw in text for kw in ['rag', 'retrieval', '检索', 'embedding', 'vector']):
            return "rag"
        elif any(kw in text for kw in ['agent', '智能体', 'tool', 'react']):
            return "agent"
        elif any(kw in text for kw in ['memory', '记忆', 'context', '上下文']):
            return "context_management"
        elif any(kw in text for kw in ['deploy', '生产', 'docker', 'api']):
            return "production"
        elif any(kw in text for kw in ['neural field', 'attractor', 'emergence']):
            return "advanced_theory"
        
        return "general"
