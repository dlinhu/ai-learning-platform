import json
import re
from typing import Optional, List, Dict, Any
from app.services.ai_service import AIProvider, NoneProvider

class AIContentGenerator:
    def __init__(self, ai_provider: AIProvider):
        self.ai_provider = ai_provider
    
    def is_enabled(self) -> bool:
        return not isinstance(self.ai_provider, NoneProvider)
    
    def parse_course_content(self, raw_content: str, filename: str = "") -> Dict[str, Any]:
        if not self.is_enabled():
            return self._fallback_parse(raw_content, filename)
        
        content_preview = raw_content[:3000] if len(raw_content) > 3000 else raw_content
        
        prompt = f"""你是一个专业的课程内容分析师。请分析以下课程内容，提取关键信息。

课程内容：
{content_preview}

请严格按照以下JSON格式返回结果，不要包含任何其他文字：
{{
  "title": "课程标题（简洁明了）",
  "summary": "课程摘要（100-200字，概述课程主要内容）",
  "topics": ["主题1", "主题2", "主题3"],
  "difficulty": "basic",
  "time_estimate": 60,
  "key_concepts": ["核心概念1", "核心概念2"]
}}

注意：
1. difficulty 只能是 basic、intermediate 或 advanced 之一
2. time_estimate 是预计学习时间（分钟），必须是数字
3. topics 数组包含3-5个主要主题
4. key_concepts 数组包含3-5个核心概念"""

        try:
            response = self.ai_provider.generate(prompt)
            result = self._extract_json(response)
            if result:
                return {
                    "title": result.get("title", ""),
                    "summary": result.get("summary", ""),
                    "topics": result.get("topics", []),
                    "difficulty": result.get("difficulty", "basic"),
                    "time_estimate": result.get("time_estimate", 60),
                    "key_concepts": result.get("key_concepts", [])
                }
        except Exception as e:
            print(f"AI parse error: {e}")
        
        return self._fallback_parse(raw_content, filename)
    
    def generate_knowledge_points(self, content: str, count: int = 5) -> List[Dict[str, Any]]:
        if not self.is_enabled():
            return []
        
        content_preview = content[:4000] if len(content) > 4000 else content
        
        prompt = f"""你是一个专业的教育内容专家。请基于以下课程内容，生成{count}个知识点。

课程内容：
{content_preview}

请严格按照以下JSON数组格式返回结果，不要包含任何其他文字：
[
  {{
    "title": "知识点标题",
    "description": "详细描述这个知识点的内容（50-100字）",
    "category": "概念",
    "importance": 3,
    "key_concepts": ["关键概念1", "关键概念2"],
    "examples": ["示例说明1"]
  }}
]

注意：
1. 每个知识点应该独立完整，便于学习
2. category 可以是：概念、原理、方法、应用、工具
3. importance 范围是1-5，5最重要
4. 确保知识点覆盖课程的核心内容"""

        try:
            response = self.ai_provider.generate(prompt)
            result = self._extract_json(response)
            if isinstance(result, list):
                knowledge_points = []
                for i, kp in enumerate(result[:count]):
                    knowledge_points.append({
                        "title": kp.get("title", f"知识点{i+1}"),
                        "description": kp.get("description", ""),
                        "category": kp.get("category", "概念"),
                        "importance": kp.get("importance", 3),
                        "key_concepts": kp.get("key_concepts", []),
                        "examples": kp.get("examples", []),
                        "related_terms": [],
                        "related_knowledge": [],
                        "common_mistakes": [],
                        "best_practices": [],
                        "external_links": []
                    })
                return knowledge_points
        except Exception as e:
            print(f"AI generate knowledge points error: {e}")
        
        return []
    
    def generate_practice_questions(self, knowledge_point: Dict[str, Any], count: int = 3) -> List[Dict[str, Any]]:
        if not self.is_enabled():
            return []
        
        kp_title = knowledge_point.get("title", "")
        kp_description = knowledge_point.get("description", "")
        kp_examples = knowledge_point.get("examples", [])
        
        prompt = f"""你是一个专业的教育测评专家。请基于以下知识点，生成{count}道练习题。

知识点标题：{kp_title}
知识点描述：{kp_description}
示例：{', '.join(kp_examples) if kp_examples else '无'}

请严格按照以下JSON数组格式返回结果，不要包含任何其他文字：
[
  {{
    "question_type": "single_choice",
    "question_text": "题目内容？",
    "options": ["选项A", "选项B", "选项C", "选项D"],
    "correct_answer": "选项A",
    "explanation": "答案解析说明为什么选这个答案",
    "difficulty": 1
  }}
]

要求：
1. question_type 可以是：single_choice（单选）、multiple_choice（多选）、fill_blank（填空）、short_answer（简答）
2. 对于 single_choice 和 multiple_choice，必须提供 options 数组
3. difficulty 范围是1-3，1最简单
4. 题目应该测试对知识点的理解，不要过于简单
5. explanation 要详细说明答案原因"""

        try:
            response = self.ai_provider.generate(prompt)
            result = self._extract_json(response)
            if isinstance(result, list):
                questions = []
                for i, q in enumerate(result[:count]):
                    question = {
                        "question_type": q.get("question_type", "single_choice"),
                        "question_text": q.get("question_text", ""),
                        "options": q.get("options", []),
                        "correct_answer": q.get("correct_answer", ""),
                        "explanation": q.get("explanation", ""),
                        "difficulty": q.get("difficulty", 1),
                        "order_index": i
                    }
                    if question["question_text"]:
                        questions.append(question)
                return questions
        except Exception as e:
            print(f"AI generate practice questions error: {e}")
        
        return []
    
    def generate_lesson_content(self, raw_content: str) -> Dict[str, Any]:
        if not self.is_enabled():
            return self._fallback_lesson_content(raw_content)
        
        content_preview = raw_content[:6000] if len(raw_content) > 6000 else raw_content
        
        prompt = f"""你是一个专业的课程内容编辑。请将以下课程原始内容转换为结构化的课程内容。

原始内容：
{content_preview}

请严格按照以下JSON格式返回，不要包含任何其他文字：
{{
  "sections": [
    {{
      "title": "章节标题",
      "content": "章节内容，使用Markdown格式",
      "type": "text",
      "order": 1
    }}
  ]
}}

要求：
1. 将内容合理分段，每段一个section
2. type可以是：text（文本说明）、code（代码示例）、example（实例演示）、summary（总结）
3. content使用Markdown格式，便于渲染
4. 保持原文的核心内容，适当补充解释说明
5. 章节标题要简洁明了
6. 如果原文有代码，保留代码并用```包裹
7. 生成3-6个章节"""

        try:
            response = self.ai_provider.generate(prompt)
            result = self._extract_json(response)
            if result and isinstance(result.get("sections"), list):
                sections = []
                for i, section in enumerate(result["sections"]):
                    sections.append({
                        "title": section.get("title", f"第{i+1}节"),
                        "content": section.get("content", ""),
                        "type": section.get("type", "text"),
                        "order": section.get("order", i + 1)
                    })
                return {"sections": sections}
        except Exception as e:
            print(f"AI generate lesson content error: {e}")
        
        return self._fallback_lesson_content(raw_content)
    
    def _fallback_lesson_content(self, raw_content: str) -> Dict[str, Any]:
        lines = raw_content.strip().split('\n')
        sections = []
        current_section = None
        current_content = []
        
        for line in lines:
            stripped = line.strip()
            if stripped.startswith('## '):
                if current_section:
                    current_section["content"] = '\n'.join(current_content)
                    sections.append(current_section)
                current_section = {
                    "title": stripped[3:].strip(),
                    "content": "",
                    "type": "text",
                    "order": len(sections) + 1
                }
                current_content = []
            elif stripped.startswith('# '):
                if current_section:
                    current_section["content"] = '\n'.join(current_content)
                    sections.append(current_section)
                current_section = {
                    "title": stripped[2:].strip(),
                    "content": "",
                    "type": "text",
                    "order": len(sections) + 1
                }
                current_content = []
            elif current_section:
                current_content.append(line)
            else:
                if not sections:
                    current_section = {
                        "title": "课程内容",
                        "content": "",
                        "type": "text",
                        "order": 1
                    }
                    current_content = [line]
        
        if current_section:
            current_section["content"] = '\n'.join(current_content)
            sections.append(current_section)
        
        if not sections:
            sections = [{
                "title": "课程内容",
                "content": raw_content,
                "type": "text",
                "order": 1
            }]
        
        return {"sections": sections}
    
    def _fallback_parse(self, raw_content: str, filename: str) -> Dict[str, Any]:
        lines = raw_content.strip().split('\n')
        title = filename
        
        for line in lines[:10]:
            line = line.strip()
            if line.startswith('# '):
                title = line[2:].strip()
                break
        
        summary = raw_content[:300] if len(raw_content) > 300 else raw_content
        if len(raw_content) > 300:
            summary += "..."
        
        return {
            "title": title,
            "summary": summary,
            "topics": [],
            "difficulty": "basic",
            "time_estimate": 60,
            "key_concepts": []
        }
    
    def _extract_json(self, text: str) -> Any:
        json_match = re.search(r'```(?:json)?\s*([\s\S]*?)```', text)
        if json_match:
            text = json_match.group(1)
        
        text = text.strip()
        
        if text.startswith('[') and text.endswith(']'):
            pass
        elif text.startswith('{') and text.endswith('}'):
            pass
        else:
            start_brace = text.find('[')
            if start_brace == -1:
                start_brace = text.find('{')
            
            if start_brace != -1:
                text = text[start_brace:]
                
                if text.startswith('['):
                    end_brace = text.rfind(']')
                else:
                    end_brace = text.rfind('}')
                
                if end_brace != -1:
                    text = text[:end_brace + 1]
        
        try:
            return json.loads(text)
        except json.JSONDecodeError:
            return None
