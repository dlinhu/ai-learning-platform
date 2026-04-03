from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime

import json

from app.utils.database import get_db
from app.models.models import Module, Lesson, Progress, User, KnowledgePoint, Term, LessonTerm
from app.routers.auth import get_current_user
from app.services.course_parser import parse_course_schedule, ModuleData
from app.services.content_renderer import ContentRenderer
from app.config import settings

router = APIRouter(prefix="/api/courses", tags=["courses"])

class MaterialResponse(BaseModel):
    title: str
    path: str
    type: str = "markdown"

class KnowledgePointResponse(BaseModel):
    id: str
    title: str
    description: str
    category: str
    importance: int
    related_terms: List[str]
    related_knowledge: List[str] = []
    examples: List[dict] = []
    key_concepts: List[str] = []
    common_mistakes: List[str] = []
    best_practices: List[str] = []
    external_links: List[str] = []
    
    class Config:
        from_attributes = True

class TermResponse(BaseModel):
    id: str
    term: str
    definition: str
    category: str
    examples: List[str]
    related_terms: List[str]
    detailed_definition: str = ""
    related_concepts: List[str] = []
    usage_examples: List[str] = []
    external_links: List[str] = []
    
    class Config:
        from_attributes = True

class LessonResponse(BaseModel):
    id: str
    module_id: str
    date: str
    title: str
    topics: List[str]
    difficulty: str
    time_estimate: int
    materials: List[MaterialResponse]
    materials_count: int = 0
    material_titles: List[str] = []
    summary: Optional[str] = None
    progress_status: str = "not_started"
    knowledge_points: List[KnowledgePointResponse] = []
    terms: List[TermResponse] = []
    structured_content: Optional[dict] = None
    
    class Config:
        from_attributes = True

class ModuleResponse(BaseModel):
    id: str
    name: str
    description: str
    order_index: int
    lesson_count: int
    completed_count: int = 0
    
    class Config:
        from_attributes = True

class ContentResponse(BaseModel):
    type: str
    html: str
    raw: str = ""
    error: str = ""

content_renderer = ContentRenderer(settings.CONTENT_PATH)

def load_or_create_modules(db: Session) -> List[Module]:
    modules = db.query(Module).order_by(Module.order_index).all()
    return modules

@router.get("/modules", response_model=List[ModuleResponse])
def get_modules(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    modules = load_or_create_modules(db)
    
    result = []
    for module in modules:
        lessons = db.query(Lesson).filter(Lesson.module_id == module.id).all()
        completed = db.query(Progress).filter(
            Progress.user_id == current_user.id,
            Progress.status == "completed",
            Progress.lesson_id.in_([l.id for l in lessons])
        ).count()
        
        result.append(ModuleResponse(
            id=module.id,
            name=module.name,
            description=module.description or "",
            order_index=module.order_index,
            lesson_count=len(lessons),
            completed_count=completed
        ))
    
    return result
@router.get("/modules/{module_id}", response_model=ModuleResponse)
def get_module(module_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    module = db.query(Module).filter(Module.id == module_id).first()
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    
    lessons = db.query(Lesson).filter(Lesson.module_id == module.id).all()
    completed = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.status == "completed",
        Progress.lesson_id.in_([l.id for l in lessons])
    ).count()
    
    return ModuleResponse(
        id=module.id,
        name=module.name,
        description=module.description or "",
        order_index=module.order_index,
        lesson_count=len(lessons),
        completed_count=completed
    )
@router.get("/modules/{module_id}/lessons", response_model=List[LessonResponse])
def get_module_lessons(module_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    module = db.query(Module).filter(Module.id == module_id).first()
    if not module:
        raise HTTPException(status_code=404, detail="Module not found")
    
    lessons = db.query(Lesson).filter(Lesson.module_id == module_id).order_by(Lesson.date).all()
    
    result = []
    for lesson in lessons:
        progress = db.query(Progress).filter(
            Progress.user_id == current_user.id,
            Progress.lesson_id == lesson.id
        ).first()
        
        result.append(LessonResponse(
            id=lesson.id,
            module_id=lesson.module_id,
            date=lesson.date,
            title=lesson.title,
            topics=lesson.topics or [],
            difficulty=lesson.difficulty,
            time_estimate=lesson.time_estimate,
            materials=[MaterialResponse(**m) for m in (lesson.materials or [])],
            materials_count=len(lesson.materials or []),
            material_titles=[m.get('title') for m in (lesson.materials or [])],
            summary=lesson.summary,
            progress_status=progress.status if progress else "not_started",
            knowledge_points=[],
            terms=[],
            structured_content=lesson.structured_content
        ))
    
    return result
@router.get("/lessons/{lesson_id}", response_model=LessonResponse)
def get_lesson(lesson_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    
    progress = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.lesson_id == lesson_id
    ).first()
    
    knowledge_points = db.query(KnowledgePoint).filter(
        KnowledgePoint.lesson_id == lesson_id
    ).order_by(KnowledgePoint.importance.desc()).all()
    
    lesson_terms = db.query(LessonTerm).filter(LessonTerm.lesson_id == lesson_id).all()
    term_ids = [lt.term_id for lt in lesson_terms]
    terms = db.query(Term).filter(Term.id.in_(term_ids)).all() if term_ids else []
    
    return LessonResponse(
        id=lesson.id,
        module_id=lesson.module_id,
        date=lesson.date,
        title=lesson.title,
        topics=lesson.topics or [],
        difficulty=lesson.difficulty,
        time_estimate=lesson.time_estimate,
        materials=[MaterialResponse(**m) for m in (lesson.materials or [])],
        materials_count=len(lesson.materials or []),
        material_titles=[m.get('title') for m in (lesson.materials or [])],
        summary=lesson.summary,
        progress_status=progress.status if progress else "not_started",
        knowledge_points=[KnowledgePointResponse(
            id=kp.id,
            title=kp.title,
            description=kp.description or "",
            category=kp.category,
            importance=kp.importance,
            related_terms=kp.related_terms or [],
            related_knowledge=kp.related_knowledge or [],
            examples=kp.examples or [],
            key_concepts=kp.key_concepts or [],
            common_mistakes=kp.common_mistakes or [],
            best_practices=kp.best_practices or [],
            external_links=kp.external_links or []
        ) for kp in knowledge_points],
        terms=[TermResponse(
            id=t.id,
            term=t.term,
            definition=t.definition or "",
            category=t.category,
            examples=t.examples or [],
            related_terms=t.related_terms or [],
            detailed_definition=t.detailed_definition or "",
            related_concepts=t.related_concepts or [],
            usage_examples=t.usage_examples or [],
            external_links=t.external_links or []
        ) for t in terms],
        structured_content=lesson.structured_content
    )
@router.get("/content/{path:path}", response_model=ContentResponse)
def get_content(path: str, current_user: User = Depends(get_current_user)):
    result = content_renderer.render_content(path)
    return ContentResponse(**result)
@router.get("/timeline")
def get_timeline(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    modules = load_or_create_modules(db)
    
    lessons = db.query(Lesson).order_by(Lesson.date).all()
    
    result = []
    for lesson in lessons:
        progress = db.query(Progress).filter(
            Progress.user_id == current_user.id,
            Progress.lesson_id == lesson.id
        ).first()
        
        result.append({
            "id": lesson.id,
            "date": lesson.date,
            "title": lesson.title,
            "module_id": lesson.module_id,
            "status": progress.status if progress else "not_started"
        })
    
    return result
@router.get("/terms", response_model=List[TermResponse])
def get_all_terms(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    terms = db.query(Term).order_by(Term.term).all()
    return [TermResponse(
        id=t.id,
        term=t.term,
        definition=t.definition or "",
        category=t.category,
        examples=t.examples or [],
        related_terms=t.related_terms or [],
        detailed_definition=t.detailed_definition or "",
        related_concepts=t.related_concepts or [],
        usage_examples=t.usage_examples or [],
        external_links=t.external_links or []
    ) for t in terms]
@router.get("/terms/{term_id}", response_model=TermResponse)
def get_term(term_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    term = db.query(Term).filter(Term.id == term_id).first()
    if not term:
        raise HTTPException(status_code=404, detail="Term not found")
    
    return TermResponse(
        id=term.id,
        term=term.term,
        definition=term.definition or "",
        category=term.category,
        examples=term.examples or [],
        related_terms=term.related_terms or [],
        detailed_definition=term.detailed_definition or "",
        related_concepts=term.related_concepts or [],
        usage_examples=term.usage_examples or [],
        external_links=term.external_links or []
    )
