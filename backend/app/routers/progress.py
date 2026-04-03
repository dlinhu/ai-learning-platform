from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, timedelta

from app.utils.database import get_db
from app.models.models import Progress, Lesson, Module, Note, User
from app.routers.auth import get_current_user

router = APIRouter(prefix="/api/progress", tags=["progress"])

class ProgressUpdate(BaseModel):
    status: Optional[str] = None
    time_spent: Optional[int] = None

class TimeUpdateRequest(BaseModel):
    lesson_id: str
    time_spent: int
    action: str = "study"

class NoteCreate(BaseModel):
    lesson_id: str
    content: str

class NoteResponse(BaseModel):
    id: str
    lesson_id: str
    content: str
    created_at: datetime
    updated_at: datetime
    
    class Config:
        from_attributes = True

class ProgressResponse(BaseModel):
    lesson_id: str
    status: str
    started_at: Optional[datetime]
    completed_at: Optional[datetime]
    time_spent: int
    bookmarked: bool
    
    class Config:
        from_attributes = True

@router.get("", response_model=List[ProgressResponse])
def get_progress(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    progress_list = db.query(Progress).filter(Progress.user_id == current_user.id).all()
    return progress_list

@router.post("/{lesson_id}/start")
def start_lesson(lesson_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        raise HTTPException(status_code=404, detail="Lesson not found")
    
    progress = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.lesson_id == lesson_id
    ).first()
    
    if not progress:
        progress = Progress(
            user_id=current_user.id,
            lesson_id=lesson_id,
            status="in_progress",
            started_at=datetime.utcnow()
        )
        db.add(progress)
    elif progress.status == "not_started":
        progress.status = "in_progress"
        progress.started_at = datetime.utcnow()
    
    db.commit()
    return {"message": "Lesson started", "status": progress.status}

@router.post("/{lesson_id}/complete")
def complete_lesson(lesson_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    progress = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.lesson_id == lesson_id
    ).first()
    
    if not progress:
        progress = Progress(
            user_id=current_user.id,
            lesson_id=lesson_id,
            status="completed",
            started_at=datetime.utcnow(),
            completed_at=datetime.utcnow()
        )
        db.add(progress)
    else:
        progress.status = "completed"
        progress.completed_at = datetime.utcnow()
    
    db.commit()
    return {"message": "Lesson completed", "status": "completed"}

@router.put("/{lesson_id}/time")
def update_time(lesson_id: str, time_spent: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    progress = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.lesson_id == lesson_id
    ).first()
    
    if not progress:
        progress = Progress(
            user_id=current_user.id,
            lesson_id=lesson_id,
            time_spent=time_spent
        )
        db.add(progress)
    else:
        progress.time_spent = time_spent
    
    db.commit()
    return {"message": "Time updated", "time_spent": time_spent}

@router.post("/update-time")
def update_time_v2(data: TimeUpdateRequest, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    progress = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.lesson_id == data.lesson_id
    ).first()
    
    if not progress:
        progress = Progress(
            user_id=current_user.id,
            lesson_id=data.lesson_id,
            time_spent=data.time_spent,
            started_at=datetime.utcnow()
        )
        db.add(progress)
    else:
        if progress.time_spent is None:
            progress.time_spent = data.time_spent
        else:
            progress.time_spent += data.time_spent
        
        if not progress.started_at:
            progress.started_at = datetime.utcnow()
    
    db.commit()
    return {
        "message": "Time updated successfully",
        "lesson_id": data.lesson_id,
        "total_time": progress.time_spent
    }

@router.post("/{lesson_id}/bookmark")
def toggle_bookmark(lesson_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    progress = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.lesson_id == lesson_id
    ).first()
    
    if not progress:
        progress = Progress(
            user_id=current_user.id,
            lesson_id=lesson_id,
            bookmarked=True
        )
        db.add(progress)
    else:
        progress.bookmarked = not progress.bookmarked
    
    db.commit()
    return {"message": "Bookmark toggled", "bookmarked": progress.bookmarked if progress else True}

@router.get("/bookmarks")
def get_bookmarks(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    bookmarks = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.bookmarked == True
    ).all()
    
    lesson_ids = [p.lesson_id for p in bookmarks]
    lessons = db.query(Lesson).filter(Lesson.id.in_(lesson_ids)).all()
    lesson_map = {l.id: l for l in lessons}
    
    return [{
        "lesson_id": p.lesson_id,
        "title": lesson_map.get(p.lesson_id, {}).title if p.lesson_id in lesson_map else "",
        "date": lesson_map.get(p.lesson_id, {}).date if p.lesson_id in lesson_map else ""
    } for p in bookmarks]

@router.post("/notes", response_model=NoteResponse)
def create_note(note_data: NoteCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note = Note(
        user_id=current_user.id,
        lesson_id=note_data.lesson_id,
        content=note_data.content
    )
    db.add(note)
    db.commit()
    db.refresh(note)
    return note

@router.get("/notes/{lesson_id}", response_model=Optional[NoteResponse])
def get_note(lesson_id: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note = db.query(Note).filter(
        Note.user_id == current_user.id,
        Note.lesson_id == lesson_id
    ).first()
    return note

@router.put("/notes/{lesson_id}", response_model=NoteResponse)
def update_note(lesson_id: str, content: str, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    note = db.query(Note).filter(
        Note.user_id == current_user.id,
        Note.lesson_id == lesson_id
    ).first()
    
    if not note:
        note = Note(
            user_id=current_user.id,
            lesson_id=lesson_id,
            content=content
        )
        db.add(note)
    else:
        note.content = content
        note.updated_at = datetime.utcnow()
    
    db.commit()
    db.refresh(note)
    return note
