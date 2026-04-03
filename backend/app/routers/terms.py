from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List, Optional
from pydantic import BaseModel
import json
import os

from app.utils.database import get_db
from app.models.models import Term, LessonTerm, Lesson, User
from app.routers.auth import get_current_user
from app.config import settings

router = APIRouter(prefix="/api/terms", tags=["terms"])

class ExternalLink(BaseModel):
    title: str
    url: str
    type: str = "article"

class TermResponse(BaseModel):
    id: str
    term: str
    definition: str
    examples: List[str]
    related_terms: List[str]
    external_links: List[ExternalLink]
    is_predefined: bool
    
    class Config:
        from_attributes = True

def load_predefined_terms(db: Session):
    terms_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "data", "terms.json")
    
    if os.path.exists(terms_path):
        with open(terms_path, 'r', encoding='utf-8') as f:
            terms_data = json.load(f)
        
        for term_key, term_info in terms_data.items():
            existing = db.query(Term).filter(Term.term == term_key).first()
            if not existing:
                term = Term(
                    term=term_key,
                    definition=term_info.get("definition", ""),
                    examples=term_info.get("examples", []),
                    related_terms=term_info.get("related_terms", []),
                    external_links=term_info.get("external_links", []),
                    is_predefined=True
                )
                db.add(term)
        
        db.commit()

@router.get("/{term_name}", response_model=TermResponse)
def get_term(term_name: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    load_predefined_terms(db)
    
    term = db.query(Term).filter(Term.term == term_name).first()
    
    if not term:
        return TermResponse(
            id="",
            term=term_name,
            definition="",
            examples=[],
            related_terms=[],
            external_links=[],
            is_predefined=False
        )
    
    return TermResponse(
        id=term.id,
        term=term.term,
        definition=term.definition or "",
        examples=term.examples or [],
        related_terms=term.related_terms or [],
        external_links=[ExternalLink(**l) for l in (term.external_links or [])],
        is_predefined=term.is_predefined
    )

@router.get("/lesson/{lesson_id}", response_model=List[TermResponse])
def get_lesson_terms(lesson_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    load_predefined_terms(db)
    
    lesson_terms = db.query(LessonTerm).filter(LessonTerm.lesson_id == lesson_id).all()
    
    if not lesson_terms:
        lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
        if lesson:
            predefined_terms = db.query(Term).filter(Term.is_predefined == True).all()
            
            for term in predefined_terms:
                lesson_term = LessonTerm(lesson_id=lesson_id, term_id=term.id)
                db.add(lesson_term)
            
            db.commit()
            lesson_terms = db.query(LessonTerm).filter(LessonTerm.lesson_id == lesson_id).all()
    
    result = []
    for lt in lesson_terms:
        term = db.query(Term).filter(Term.id == lt.term_id).first()
        if term:
            result.append(TermResponse(
                id=term.id,
                term=term.term,
                definition=term.definition or "",
                examples=term.examples or [],
                related_terms=term.related_terms or [],
                external_links=[ExternalLink(**l) for l in (term.external_links or [])],
                is_predefined=term.is_predefined
            ))
    
    return result

@router.get("/search/{query}")
def search_terms(query: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    load_predefined_terms(db)
    
    terms = db.query(Term).filter(Term.term.contains(query)).limit(10).all()
    
    return [{
        "term": t.term,
        "definition": t.definition[:100] + "..." if t.definition and len(t.definition) > 100 else t.definition
    } for t in terms]
