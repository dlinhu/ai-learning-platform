import re
import json
from datetime import datetime
from typing import List, Dict, Optional
from dataclasses import dataclass, field, asdict

@dataclass
class Material:
    title: str
    text: str
    path: str

@dataclass
class LessonData:
    date: str
    title: str
    topics: List[str] = field(default_factory=list)
    difficulty: str = "basic"
    time_estimate: int = 60
    materials: List[Material] = field(default_factory=list)

@dataclass
class ModuleData:
    order: int
    name: str
    description: str = ""
    lessons: List[LessonData] = field(default_factory=list)

class CourseScheduleParser:
    def __init__(self, md_content: str):
        self.content = md_content
        self.modules: List[ModuleData] = []
    
    def parse(self) -> List[ModuleData]:
        lines = self.content.split('\n')
        current_module: Optional[ModuleData] = None
        current_week_lessons: List[LessonData] = []
        
        chinese_num_map = {'一': 1, '二': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10}
        
        i = 0
        while i < len(lines):
            line = lines[i]
            
            module_match = re.match(r'## 第([一二三四五六七八九十]+)模块[：:](.+)', line)
            if module_match:
                if current_module:
                    current_module.lessons.extend(current_week_lessons)
                    self.modules.append(current_module)
                    current_week_lessons = []
                
                chinese_num = module_match.group(1)
                order = chinese_num_map.get(chinese_num, len(self.modules) + 1)
                name = module_match.group(2).strip()
                name = re.sub(r'[（(].+[）)]', '', name).strip()
                
                current_module = ModuleData(
                    order=order,
                    name=name
                )
                i += 1
                continue
            
            break_match = re.match(r'### Break \d+[：:](.+)', line)
            if break_match and current_module:
                current_module.lessons.extend(current_week_lessons)
                current_week_lessons = []
                i += 1
                continue
            
            break_match2 = re.match(r'### Break[：:](.+)', line)
            if break_match2 and current_module:
                current_module.lessons.extend(current_week_lessons)
                current_week_lessons = []
                i += 1
                continue
            
            lesson_match = re.match(r'\|\s*(\d+月\d+日)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|\s*(.+?)\s*\|', line)
            if lesson_match and current_module:
                lesson = LessonData(
                    date=self._parse_date(lesson_match.group(1)),
                    title=lesson_match.group(2).strip(),
                    topics=self._parse_topics(lesson_match.group(3)),
                    materials=self._parse_materials(lesson_match.group(4))
                )
                
                if '🔥' in lesson.title:
                    lesson.difficulty = "advanced"
                if '⏰' in lesson.title:
                    lesson.time_estimate = 90
                
                lesson.title = re.sub(r'[🔥⏰]\s*', '', lesson.title).strip()
                current_week_lessons.append(lesson)
            
            i += 1
        
        if current_module:
            current_module.lessons.extend(current_week_lessons)
            self.modules.append(current_module)
        
        return self.modules
    
    def _parse_date(self, date_str: str) -> str:
        match = re.match(r'(\d+)月(\d+)日', date_str)
        if match:
            return f"2026-{int(match.group(1)):02d}-{int(match.group(2)):02d}"
        return date_str
    
    def _parse_topics(self, topics_str: str) -> List[str]:
        topics = [t.strip() for t in topics_str.split('；') if t.strip()]
        if not topics:
            topics = [t.strip() for t in topics_str.split('+') if t.strip()]
        return topics
    
    def _parse_materials(self, materials_str: str) -> List[Material]:
        materials = []
        pattern = r'\*\*(.+?)\*\*\s*\[(.+?)\]\((.+?)\)'
        for match in re.finditer(pattern, materials_str):
            materials.append(Material(
                title=match.group(1),
                text=match.group(2),
                path=match.group(3)
            ))
        return materials
    
    def to_dict(self) -> List[Dict]:
        return [asdict(m) for m in self.modules]

def parse_course_schedule(file_path: str) -> List[ModuleData]:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    parser = CourseScheduleParser(content)
    return parser.parse()

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        modules = parse_course_schedule(sys.argv[1])
        print(json.dumps([asdict(m) for m in modules], ensure_ascii=False, indent=2))
