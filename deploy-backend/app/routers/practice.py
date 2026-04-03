from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from pydantic import BaseModel
from typing import List, Optional
from app.utils.database import get_db
from app.models.models import PracticeQuestion, UserAnswer, KnowledgePoint
from app.routers.auth import get_current_user

router = APIRouter(prefix="/api/practice", tags=["practice"])

class QuestionOption(BaseModel):
    label: str
    text: str

class PracticeQuestionResponse(BaseModel):
    id: str
    knowledge_point_id: str
    question_type: str
    question_text: str
    options: List[str]
    correct_answer: Optional[str] = None
    explanation: Optional[str] = None
    difficulty: int
    order_index: int
    
    class Config:
        from_attributes = True

class SubmitAnswerRequest(BaseModel):
    question_id: str
    user_answer: str

class SubmitAnswerResponse(BaseModel):
    is_correct: bool
    correct_answer: str
    explanation: str

class ProgressResponse(BaseModel):
    total_questions: int
    answered_questions: int
    correct_answers: int
    progress_percentage: float

@router.get("/knowledge-point/{kp_id}", response_model=List[PracticeQuestionResponse])
def get_practice_questions(
    kp_id: str,
    db: Session = Depends(get_db)
):
    questions = db.query(PracticeQuestion).filter(
        PracticeQuestion.knowledge_point_id == kp_id
    ).order_by(PracticeQuestion.order_index).all()
    
    return [
        PracticeQuestionResponse(
            id=q.id,
            knowledge_point_id=q.knowledge_point_id,
            question_type=q.question_type,
            question_text=q.question_text,
            options=q.options or [],
            correct_answer=None,
            explanation=None,
            difficulty=q.difficulty,
            order_index=q.order_index
        )
        for q in questions
    ]

@router.post("/submit", response_model=SubmitAnswerResponse)
def submit_answer(
    request: SubmitAnswerRequest,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    question = db.query(PracticeQuestion).filter(
        PracticeQuestion.id == request.question_id
    ).first()
    
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    is_correct = False
    correct_answer = question.correct_answer
    
    if question.question_type == "single_choice":
        is_correct = request.user_answer.strip().upper() == correct_answer.strip().upper()
    elif question.question_type == "multiple_choice":
        user_set = set(request.user_answer.strip().upper().split(","))
        correct_set = set(correct_answer.strip().upper().split(","))
        is_correct = user_set == correct_set
    elif question.question_type == "true_false":
        is_correct = request.user_answer.strip().lower() == correct_answer.strip().lower()
    elif question.question_type == "fill_blank":
        correct_answers = [a.strip().lower() for a in correct_answer.split("|")]
        is_correct = request.user_answer.strip().lower() in correct_answers
    elif question.question_type == "short_answer":
        keywords = [k.strip().lower() for k in correct_answer.split(",")]
        user_answer_lower = request.user_answer.strip().lower()
        is_correct = any(kw in user_answer_lower for kw in keywords)
    
    existing_answer = db.query(UserAnswer).filter(
        UserAnswer.user_id == current_user.id,
        UserAnswer.question_id == request.question_id
    ).first()
    
    if existing_answer:
        existing_answer.user_answer = request.user_answer
        existing_answer.is_correct = is_correct
    else:
        user_answer = UserAnswer(
            user_id=current_user.id,
            question_id=request.question_id,
            user_answer=request.user_answer,
            is_correct=is_correct
        )
        db.add(user_answer)
    
    db.commit()
    
    return SubmitAnswerResponse(
        is_correct=is_correct,
        correct_answer=correct_answer,
        explanation=question.explanation or ""
    )

@router.get("/progress/{kp_id}", response_model=ProgressResponse)
def get_progress(
    kp_id: str,
    db: Session = Depends(get_db),
    current_user = Depends(get_current_user)
):
    total_questions = db.query(PracticeQuestion).filter(
        PracticeQuestion.knowledge_point_id == kp_id
    ).count()
    
    question_ids = [q.id for q in db.query(PracticeQuestion.id).filter(
        PracticeQuestion.knowledge_point_id == kp_id
    ).all()]
    
    answered = db.query(UserAnswer).filter(
        UserAnswer.user_id == current_user.id,
        UserAnswer.question_id.in_(question_ids)
    ).all()
    
    answered_questions = len(answered)
    correct_answers = sum(1 for a in answered if a.is_correct)
    
    progress_percentage = (answered_questions / total_questions * 100) if total_questions > 0 else 0
    
    return ProgressResponse(
        total_questions=total_questions,
        answered_questions=answered_questions,
        correct_answers=correct_answers,
        progress_percentage=round(progress_percentage, 1)
    )

@router.get("/question/{question_id}", response_model=PracticeQuestionResponse)
def get_question_detail(
    question_id: str,
    db: Session = Depends(get_db)
):
    question = db.query(PracticeQuestion).filter(
        PracticeQuestion.id == question_id
    ).first()
    
    if not question:
        raise HTTPException(status_code=404, detail="Question not found")
    
    return PracticeQuestionResponse(
        id=question.id,
        knowledge_point_id=question.knowledge_point_id,
        question_type=question.question_type,
        question_text=question.question_text,
        options=question.options or [],
        correct_answer=question.correct_answer,
        explanation=question.explanation,
        difficulty=question.difficulty,
        order_index=question.order_index
    )
