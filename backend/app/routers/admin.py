from fastapi import APIRouter, Depends, Query, UploadFile, File, Form
from sqlalchemy.orm import Session
from sqlalchemy import func, or_
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, timedelta
import math
import os

from app.utils.database import get_db
from app.models.models import Progress, Lesson, Module, User, KnowledgePoint, AISettings, PracticeQuestion
from app.routers.auth import get_current_user

router = APIRouter(prefix="/api/admin", tags=["admin"])

class AdminStatsResponse(BaseModel):
    total_users: int
    active_users_today: int
    active_users_week: int
    total_time_spent: int
    avg_time_per_user: float
    total_completions: int
    avg_completion_rate: float

class UserListItem(BaseModel):
    user_id: str
    username: str
    email: str
    role: str
    group: str = "group1"
    created_at: datetime
    total_time_spent: int
    completed_lessons: int
    in_progress_lessons: int
    completion_rate: float
    last_active: Optional[datetime]
    current_streak: int

class UsersListResponse(BaseModel):
    users: List[UserListItem]
    total: int
    page: int
    per_page: int
    total_pages: int

class ModuleProgressItem(BaseModel):
    module_id: str
    module_name: str
    completed: int
    total: int
    time_spent: int

class RecentActivity(BaseModel):
    lesson_id: str
    lesson_title: str
    module_name: str
    status: str
    time_spent: int
    completed_at: Optional[datetime]

class CalendarDay(BaseModel):
    date: str
    time_spent: int
    lessons: int

class UserDetailResponse(BaseModel):
    user_id: str
    username: str
    email: str
    total_time_spent: int
    completed_lessons: int
    in_progress_lessons: int
    completion_rate: float
    module_progress: List[ModuleProgressItem]
    recent_activities: List[RecentActivity]
    calendar_data: List[CalendarDay]

def require_admin(current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        from fastapi import HTTPException
        raise HTTPException(status_code=403, detail="Admin access required")
    return current_user

def calculate_streak(progress_records: List[Progress]) -> int:
    if not progress_records:
        return 0
    
    dates = sorted(set([
        p.started_at.date() if p.started_at else None
        for p in progress_records
        if p.started_at
    ]), reverse=True)
    
    if not dates:
        return 0
    
    today = datetime.utcnow().date()
    streak = 0
    
    for i, date in enumerate(dates):
        expected = today - timedelta(days=i)
        if date == expected:
            streak += 1
        else:
            break
    
    return streak

@router.get("/stats", response_model=AdminStatsResponse)
def get_admin_stats(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    total_users = db.query(User).count()
    
    today = datetime.utcnow().date()
    today_start = datetime.combine(today, datetime.min.time())
    
    active_today = db.query(Progress).filter(
        Progress.started_at >= today_start
    ).distinct(Progress.user_id).count()
    
    week_start = today - timedelta(days=today.weekday())
    week_start_dt = datetime.combine(week_start, datetime.min.time())
    
    active_week = db.query(Progress).filter(
        Progress.started_at >= week_start_dt
    ).distinct(Progress.user_id).count()
    
    total_time = db.query(func.sum(Progress.time_spent)).scalar() or 0
    
    avg_time = (total_time / total_users) if total_users > 0 else 0
    
    total_completions = db.query(Progress).filter(
        Progress.status == "completed"
    ).count()
    
    total_lessons = db.query(Lesson).count()
    total_possible = total_users * total_lessons
    avg_completion = (total_completions / total_possible * 100) if total_possible > 0 else 0
    
    return AdminStatsResponse(
        total_users=total_users,
        active_users_today=active_today,
        active_users_week=active_week,
        total_time_spent=total_time or 0,
        avg_time_per_user=round(avg_time, 1),
        total_completions=total_completions,
        avg_completion_rate=round(avg_completion, 1)
    )

@router.get("/users", response_model=UsersListResponse)
def get_users_list(
    page: int = Query(1, ge=1),
    per_page: int = Query(20, ge=1, le=100),
    sort_by: str = Query("time_spent", regex="^(time_spent|completion_rate|last_active|username)$"),
    order: str = Query("desc", regex="^(asc|desc)$"),
    search: Optional[str] = Query(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    query = db.query(User)
    
    if search:
        search_pattern = f"%{search}%"
        query = query.filter(
            or_(
                User.username.ilike(search_pattern),
                User.email.ilike(search_pattern)
            )
        )
    
    total = query.count()
    
    users = query.all()
    total_lessons = db.query(Lesson).count()
    
    user_data = []
    for user in users:
        progress_records = db.query(Progress).filter(
            Progress.user_id == user.id
        ).all()
        
        total_time = sum(p.time_spent or 0 for p in progress_records)
        completed = len([p for p in progress_records if p.status == "completed"])
        in_progress = len([p for p in progress_records if p.status == "in_progress"])
        completion_rate = (completed / total_lessons * 100) if total_lessons > 0 else 0
        
        last_active = None
        dates = [p.started_at for p in progress_records if p.started_at]
        if dates:
            last_active = max(dates)
        
        streak = calculate_streak(progress_records)
        
        user_data.append({
            "user": user,
            "total_time": total_time,
            "completed": completed,
            "in_progress": in_progress,
            "completion_rate": completion_rate,
            "last_active": last_active,
            "streak": streak
        })
    
    sort_keys = {
        "time_spent": lambda x: x["total_time"],
        "completion_rate": lambda x: x["completion_rate"],
        "last_active": lambda x: x["last_active"] or datetime.min,
        "username": lambda x: x["user"].username.lower()
    }
    
    user_data.sort(
        key=sort_keys[sort_by],
        reverse=(order == "desc")
    )
    
    total_pages = math.ceil(total / per_page)
    start_idx = (page - 1) * per_page
    end_idx = start_idx + per_page
    paginated_data = user_data[start_idx:end_idx]
    
    users_list = [
        UserListItem(
            user_id=data["user"].id,
            username=data["user"].username,
            email=data["user"].email,
            role=data["user"].role,
            group=getattr(data["user"], 'group', 'group1'),
            created_at=data["user"].created_at,
            total_time_spent=data["total_time"],
            completed_lessons=data["completed"],
            in_progress_lessons=data["in_progress"],
            completion_rate=round(data["completion_rate"], 1),
            last_active=data["last_active"],
            current_streak=data["streak"]
        )
        for data in paginated_data
    ]
    
    return UsersListResponse(
        users=users_list,
        total=total,
        page=page,
        per_page=per_page,
        total_pages=total_pages
    )

@router.put("/users/{user_id}/group")
def update_user_group(
    user_id: str,
    group: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    from fastapi import HTTPException
    
    valid_groups = ["group1", "group2", "group3", "group4", "group5", "group6"]
    if group not in valid_groups:
        raise HTTPException(status_code=400, detail="Invalid group")
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    user.group = group
    db.commit()
    return {"message": "Group updated", "group": group}

@router.put("/users/{user_id}/role")
def update_user_role(
    user_id: str,
    role: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    from fastapi import HTTPException
    
    valid_roles = ["student", "admin"]
    if role not in valid_roles:
        raise HTTPException(status_code=400, detail="Invalid role. Must be 'student' or 'admin'")
    
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    if user.id == current_user.id:
        raise HTTPException(status_code=400, detail="Cannot change your own role")
    
    user.role = role
    db.commit()
    return {"message": "Role updated", "role": role, "username": user.username}

class GroupMemberProgress(BaseModel):
    user_id: str
    username: str
    email: str
    role: str
    group: str
    total_time_spent: int
    completed_lessons: int
    in_progress_lessons: int
    completion_rate: float
    last_active: Optional[datetime]
    current_streak: int

class GroupProgressResponse(BaseModel):
    group_name: str
    total_members: int
    members: List[GroupMemberProgress]

@router.get("/groups/{group_name}/progress", response_model=GroupProgressResponse)
def get_group_progress(
    group_name: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    from fastapi import HTTPException
    
    valid_groups = ["group1", "group2", "group3", "group4", "group5", "group6"]
    if group_name not in valid_groups:
        raise HTTPException(status_code=400, detail="Invalid group name")
    
    users = db.query(User).filter(User.group == group_name).all()
    total_lessons = db.query(Lesson).count()
    
    members_progress = []
    for user in users:
        progress_records = db.query(Progress).filter(
            Progress.user_id == user.id
        ).all()
        
        total_time = sum(p.time_spent or 0 for p in progress_records)
        completed = len([p for p in progress_records if p.status == "completed"])
        in_progress = len([p for p in progress_records if p.status == "in_progress"])
        completion_rate = (completed / total_lessons * 100) if total_lessons > 0 else 0
        
        last_active = None
        dates = [p.started_at for p in progress_records if p.started_at]
        if dates:
            last_active = max(dates)
        
        streak = calculate_streak(progress_records)
        
        members_progress.append(GroupMemberProgress(
            user_id=user.id,
            username=user.username,
            email=user.email,
            role=user.role,
            group=user.group,
            total_time_spent=total_time,
            completed_lessons=completed,
            in_progress_lessons=in_progress,
            completion_rate=round(completion_rate, 1),
            last_active=last_active,
            current_streak=streak
        ))
    
    members_progress.sort(key=lambda x: x.completion_rate, reverse=True)
    
    return GroupProgressResponse(
        group_name=group_name,
        total_members=len(users),
        members=members_progress
    )

@router.get("/groups/summary")
def get_groups_summary(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    groups_summary = []
    valid_groups = ["group1", "group2", "group3", "group4", "group5", "group6"]
    
    for group_name in valid_groups:
        users = db.query(User).filter(User.group == group_name).all()
        
        total_time = 0
        total_completed = 0
        total_in_progress = 0
        
        for user in users:
            progress_records = db.query(Progress).filter(
                Progress.user_id == user.id
            ).all()
            total_time += sum(p.time_spent or 0 for p in progress_records)
            total_completed += len([p for p in progress_records if p.status == "completed"])
            total_in_progress += len([p for p in progress_records if p.status == "in_progress"])
        
        groups_summary.append({
            "group_name": group_name,
            "member_count": len(users),
            "total_time_spent": total_time,
            "total_completed": total_completed,
            "total_in_progress": total_in_progress,
            "admins": len([u for u in users if u.role == "admin"])
        })
    
    return {"groups": groups_summary}

@router.get("/users/{user_id}/detail", response_model=UserDetailResponse)
def get_user_detail(
    user_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="User not found")
    
    progress_records = db.query(Progress).filter(
        Progress.user_id == user_id
    ).all()
    
    total_time = sum(p.time_spent or 0 for p in progress_records)
    completed = len([p for p in progress_records if p.status == "completed"])
    in_progress = len([p for p in progress_records if p.status == "in_progress"])
    total_lessons = db.query(Lesson).count()
    completion_rate = (completed / total_lessons * 100) if total_lessons > 0 else 0
    
    modules = db.query(Module).order_by(Module.order_index).all()
    module_progress = []
    
    for module in modules:
        lessons = db.query(Lesson).filter(Lesson.module_id == module.id).all()
        lesson_ids = [l.id for l in lessons]
        
        module_progress_records = [
            p for p in progress_records
            if p.lesson_id in lesson_ids
        ]
        
        module_completed = len([
            p for p in module_progress_records
            if p.status == "completed"
        ])
        module_time = sum(p.time_spent or 0 for p in module_progress_records)
        
        module_progress.append(ModuleProgressItem(
            module_id=module.id,
            module_name=module.name,
            completed=module_completed,
            total=len(lessons),
            time_spent=module_time
        ))
    
    recent_progress = sorted(
        [p for p in progress_records if p.started_at],
        key=lambda x: x.started_at,
        reverse=True
    )[:10]
    
    recent_activities = []
    for p in recent_progress:
        lesson = db.query(Lesson).filter(Lesson.id == p.lesson_id).first()
        if lesson:
            module = db.query(Module).filter(Module.id == lesson.module_id).first()
            recent_activities.append(RecentActivity(
                lesson_id=lesson.id,
                lesson_title=lesson.title,
                module_name=module.name if module else "",
                status=p.status,
                time_spent=p.time_spent or 0,
                completed_at=p.completed_at
            ))
    
    end_date = datetime.utcnow().date()
    start_date = end_date - timedelta(days=29)
    
    calendar_data = []
    current_date = start_date
    while current_date <= end_date:
        date_str = current_date.isoformat()
        day_progress = [
            p for p in progress_records
            if p.started_at and p.started_at.date() == current_date
        ]
        
        day_time = sum(p.time_spent or 0 for p in day_progress)
        day_lessons = len(set(p.lesson_id for p in day_progress))
        
        calendar_data.append(CalendarDay(
            date=date_str,
            time_spent=day_time,
            lessons=day_lessons
        ))
        
        current_date += timedelta(days=1)
    
    return UserDetailResponse(
        user_id=user.id,
        username=user.username,
        email=user.email,
        total_time_spent=total_time,
        completed_lessons=completed,
        in_progress_lessons=in_progress,
        completion_rate=round(completion_rate, 1),
        module_progress=module_progress,
        recent_activities=recent_activities,
        calendar_data=calendar_data
    )

class LessonUpdateRequest(BaseModel):
    title: Optional[str] = None
    topics: Optional[List[str]] = None
    difficulty: Optional[str] = None
    time_estimate: Optional[int] = None
    summary: Optional[str] = None
    date: Optional[str] = None

class ModuleUpdateRequest(BaseModel):
    name: Optional[str] = None
    description: Optional[str] = None
    order_index: Optional[int] = None

class ModuleCreateRequest(BaseModel):
    name: str
    description: Optional[str] = None

class LessonCreateRequest(BaseModel):
    module_id: str
    title: str
    date: Optional[str] = None
    topics: Optional[List[str]] = None
    difficulty: Optional[str] = "basic"
    time_estimate: Optional[int] = 60
    summary: Optional[str] = None
    materials: Optional[List[dict]] = None
    raw_content: Optional[str] = None

@router.get("/modules")
def get_all_modules(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    modules = db.query(Module).order_by(Module.order_index).all()
    result = []
    for module in modules:
        lessons = db.query(Lesson).filter(Lesson.module_id == module.id).all()
        result.append({
            "id": module.id,
            "name": module.name,
            "description": module.description or "",
            "order_index": module.order_index,
            "lesson_count": len(lessons)
        })
    return result

@router.post("/modules")
def create_module(
    data: ModuleCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    max_order = db.query(func.max(Module.order_index)).scalar() or 0
    module = Module(
        name=data.name,
        description=data.description,
        order_index=max_order + 1
    )
    db.add(module)
    db.commit()
    db.refresh(module)
    return {"id": module.id, "name": module.name, "message": "Module created"}

@router.put("/modules/{module_id}")
def update_module(
    module_id: str,
    data: ModuleUpdateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    module = db.query(Module).filter(Module.id == module_id).first()
    if not module:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Module not found")
    
    if data.name is not None:
        module.name = data.name
    if data.description is not None:
        module.description = data.description
    if data.order_index is not None:
        module.order_index = data.order_index
    
    db.commit()
    return {"message": "Module updated"}

@router.delete("/modules/{module_id}")
def delete_module(
    module_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    module = db.query(Module).filter(Module.id == module_id).first()
    if not module:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Module not found")
    
    lessons = db.query(Lesson).filter(Lesson.module_id == module_id).all()
    if lessons:
        from fastapi import HTTPException
        raise HTTPException(status_code=400, detail="Cannot delete module with lessons")
    
    db.delete(module)
    db.commit()
    return {"message": "Module deleted"}

@router.put("/lessons/{lesson_id}")
def update_lesson(
    lesson_id: str,
    data: LessonUpdateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Lesson not found")
    
    if data.title is not None:
        lesson.title = data.title
    if data.topics is not None:
        lesson.topics = data.topics
    if data.difficulty is not None:
        lesson.difficulty = data.difficulty
    if data.time_estimate is not None:
        lesson.time_estimate = data.time_estimate
    if data.summary is not None:
        lesson.summary = data.summary
    if data.date is not None:
        lesson.date = data.date
    
    db.commit()
    return {"message": "Lesson updated"}

@router.delete("/lessons/{lesson_id}")
def delete_lesson(
    lesson_id: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    lesson = db.query(Lesson).filter(Lesson.id == lesson_id).first()
    if not lesson:
        from fastapi import HTTPException
        raise HTTPException(status_code=404, detail="Lesson not found")
    
    db.query(Progress).filter(Progress.lesson_id == lesson_id).delete()
    db.delete(lesson)
    db.commit()
    return {"message": "Lesson deleted"}

@router.post("/lessons")
def create_lesson(
    data: LessonCreateRequest,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    import uuid
    lesson = Lesson(
        id=str(uuid.uuid4()),
        module_id=data.module_id,
        title=data.title,
        date=data.date or "",
        topics=data.topics or [],
        difficulty=data.difficulty or "basic",
        time_estimate=data.time_estimate or 60,
        summary=data.summary,
        materials=data.materials or [],
        raw_content=data.raw_content
    )
    db.add(lesson)
    db.commit()
    db.refresh(lesson)
    return {"id": lesson.id, "title": lesson.title, "message": "Lesson created"}

@router.post("/lessons/upload")
async def upload_lesson(
    module_id: str,
    file: UploadFile = File(...),
    title: Optional[str] = Form(None),
    date: Optional[str] = Form(None),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    from fastapi import HTTPException
    from app.services.content_parser import ContentParser
    from app.services.ai_service import get_ai_provider
    from app.services.ai_content_generator import AIContentGenerator
    from app.config import settings
    import uuid
    import tempfile
    
    allowed_types = ['.md', '.ipynb', '.txt']
    file_ext = os.path.splitext(file.filename)[1].lower()
    if file_ext not in allowed_types:
        raise HTTPException(status_code=400, detail=f"File type not supported. Allowed: {allowed_types}")
    
    content = await file.read()
    try:
        text_content = content.decode('utf-8')
    except UnicodeDecodeError:
        text_content = content.decode('gbk', errors='ignore')
    
    with tempfile.NamedTemporaryFile(mode='w', suffix=file_ext, delete=False, encoding='utf-8') as tmp:
        tmp.write(text_content)
        tmp_path = tmp.name
    
    try:
        parser = ContentParser(os.path.dirname(tmp_path))
        parsed = parser.parse_file(os.path.basename(tmp_path))
        
        raw_content = text_content
        if parsed and parsed.raw_content:
            raw_content = parsed.raw_content
        
        ai_settings = db.query(AISettings).filter(AISettings.id == "default").first()
        ai_provider = get_ai_provider(ai_settings)
        ai_generator = AIContentGenerator(ai_provider)
        
        filename = os.path.splitext(file.filename)[0]
        ai_result = ai_generator.parse_course_content(raw_content, filename)
        
        lesson_title = title or ai_result.get("title") or filename
        summary = ai_result.get("summary", "")
        topics = ai_result.get("topics", [])
        difficulty = ai_result.get("difficulty", "basic")
        time_estimate = ai_result.get("time_estimate", 60)
        
        if not summary:
            summary = raw_content[:500] if len(raw_content) > 500 else raw_content
        
        structured_content = {}
        if ai_generator.is_enabled():
            structured_content = ai_generator.generate_lesson_content(raw_content)
        
        lesson = Lesson(
            id=str(uuid.uuid4()),
            module_id=module_id,
            title=lesson_title,
            date=date or "",
            topics=topics,
            difficulty=difficulty,
            time_estimate=time_estimate,
            summary=summary,
            materials=[],
            raw_content=raw_content,
            structured_content=structured_content
        )
        db.add(lesson)
        db.commit()
        db.refresh(lesson)
        
        knowledge_points_data = []
        questions_count = 0
        
        if ai_generator.is_enabled():
            knowledge_points_data = ai_generator.generate_knowledge_points(raw_content, count=5)
            
            for i, kp_data in enumerate(knowledge_points_data):
                kp = KnowledgePoint(
                    id=str(uuid.uuid4()),
                    lesson_id=lesson.id,
                    title=kp_data.get("title", f"知识点{i+1}"),
                    description=kp_data.get("description", ""),
                    category=kp_data.get("category", "概念"),
                    importance=kp_data.get("importance", 3),
                    related_terms=kp_data.get("related_terms", []),
                    related_knowledge=kp_data.get("related_knowledge", []),
                    examples=kp_data.get("examples", []),
                    key_concepts=kp_data.get("key_concepts", []),
                    common_mistakes=kp_data.get("common_mistakes", []),
                    best_practices=kp_data.get("best_practices", []),
                    external_links=kp_data.get("external_links", [])
                )
                db.add(kp)
                db.commit()
                db.refresh(kp)
                
                questions_data = ai_generator.generate_practice_questions(kp_data, count=3)
                for j, q_data in enumerate(questions_data):
                    question = PracticeQuestion(
                        id=str(uuid.uuid4()),
                        knowledge_point_id=kp.id,
                        question_type=q_data.get("question_type", "single_choice"),
                        question_text=q_data.get("question_text", ""),
                        options=q_data.get("options", []),
                        correct_answer=q_data.get("correct_answer", ""),
                        explanation=q_data.get("explanation", ""),
                        difficulty=q_data.get("difficulty", 1),
                        order_index=j
                    )
                    db.add(question)
                    questions_count += 1
                
                db.commit()
        
        kp_list = []
        for kp in db.query(KnowledgePoint).filter(KnowledgePoint.lesson_id == lesson.id).all():
            q_count = db.query(PracticeQuestion).filter(PracticeQuestion.knowledge_point_id == kp.id).count()
            kp_list.append({
                "id": kp.id,
                "title": kp.title,
                "description": kp.description[:100] + "..." if len(kp.description or "") > 100 else kp.description,
                "category": kp.category,
                "importance": kp.importance,
                "questions_count": q_count
            })
        
        ai_status = "AI已启用" if ai_generator.is_enabled() else "AI未配置，使用基础解析"
        message = f"课程创建成功"
        if knowledge_points_data:
            message += f"，已生成{len(knowledge_points_data)}个知识点和{questions_count}道练习题"
        
        return {
            "id": lesson.id,
            "title": lesson.title,
            "summary": lesson.summary,
            "topics": lesson.topics,
            "difficulty": lesson.difficulty,
            "time_estimate": lesson.time_estimate,
            "knowledge_points": kp_list,
            "questions_count": questions_count,
            "ai_enabled": ai_generator.is_enabled(),
            "message": message
        }
    finally:
        os.unlink(tmp_path)

class AISettingsResponse(BaseModel):
    provider: str = "none"
    openai_api_key: Optional[str] = None
    openai_base_url: Optional[str] = None
    local_model_url: Optional[str] = None
    local_model_name: Optional[str] = None

class AISettingsUpdate(BaseModel):
    provider: str = "none"
    openai_api_key: Optional[str] = None
    openai_base_url: Optional[str] = None
    local_model_url: Optional[str] = None
    local_model_name: Optional[str] = None

@router.get("/ai-settings", response_model=AISettingsResponse)
def get_ai_settings(
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    settings = db.query(AISettings).filter(AISettings.id == "default").first()
    if not settings:
        return AISettingsResponse()
    
    masked_key = None
    if settings.openai_api_key:
        key = settings.openai_api_key
        if len(key) > 8:
            masked_key = key[:4] + "****" + key[-4:]
        else:
            masked_key = "****"
    
    return AISettingsResponse(
        provider=settings.provider or "none",
        openai_api_key=masked_key,
        openai_base_url=settings.openai_base_url,
        local_model_url=settings.local_model_url,
        local_model_name=settings.local_model_name
    )

@router.put("/ai-settings")
def update_ai_settings(
    data: AISettingsUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    settings = db.query(AISettings).filter(AISettings.id == "default").first()
    
    if not settings:
        settings = AISettings(
            id="default",
            provider=data.provider,
            openai_base_url=data.openai_base_url,
            local_model_url=data.local_model_url,
            local_model_name=data.local_model_name
        )
        if data.openai_api_key and not data.openai_api_key.startswith("sk-****"):
            settings.openai_api_key = data.openai_api_key
        db.add(settings)
    else:
        settings.provider = data.provider
        settings.openai_base_url = data.openai_base_url
        settings.local_model_url = data.local_model_url
        settings.local_model_name = data.local_model_name
        if data.openai_api_key and not data.openai_api_key.startswith("sk-****"):
            settings.openai_api_key = data.openai_api_key
    
    db.commit()
    return {"message": "AI设置已更新"}

@router.post("/ai-settings/test")
def test_ai_settings(
    data: AISettingsUpdate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_admin)
):
    from app.services.ai_service import OpenAIProvider, LocalModelProvider
    
    if data.provider == "none":
        return {"success": True, "message": "AI功能已禁用"}
    
    if data.provider == "openai":
        api_key = data.openai_api_key
        if not api_key or api_key.startswith("sk-****"):
            settings = db.query(AISettings).filter(AISettings.id == "default").first()
            if settings and settings.openai_api_key:
                api_key = settings.openai_api_key
            else:
                return {"success": False, "message": "请提供OpenAI API Key"}
        
        provider = OpenAIProvider(api_key, data.openai_base_url)
        success, message = provider.test_connection()
        return {"success": success, "message": message}
    
    if data.provider == "local":
        if not data.local_model_url or not data.local_model_name:
            return {"success": False, "message": "请提供本地模型地址和名称"}
        
        provider = LocalModelProvider(data.local_model_url, data.local_model_name)
        success, message = provider.test_connection()
        return {"success": success, "message": message}
    
    return {"success": False, "message": "未知的AI提供商"}
