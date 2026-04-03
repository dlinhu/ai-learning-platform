from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import List, Optional
from pydantic import BaseModel
from datetime import datetime, timedelta
import json
import os

from app.utils.database import get_db
from app.models.models import Progress, Lesson, Module, User
from app.routers.auth import get_current_user
from app.config import settings

router = APIRouter(prefix="/api/dashboard", tags=["dashboard"])

class StatsResponse(BaseModel):
    total_lessons: int
    completed_lessons: int
    total_time_spent: int
    completion_rate: float
    current_streak: int
    longest_streak: int
    weekly_study_days: int
    weekly_time_spent: int
    estimated_total_time: int

class ModuleProgress(BaseModel):
    module_id: str
    module_name: str
    total: int
    completed: int
    percentage: float
    time_spent: int
    estimated_time: int
    last_study_date: Optional[str]

class CalendarDay(BaseModel):
    date: str
    time_spent: int
    lessons_completed: int

class TodayLesson(BaseModel):
    id: str
    title: str
    module_name: str
    status: str

class WeeklyBreakdown(BaseModel):
    day: str
    time: int

class MonthlyTrend(BaseModel):
    week: str
    time: int

class TimeStatsResponse(BaseModel):
    total_time_spent: int
    estimated_total_time: int
    efficiency_rate: float
    daily_average: int
    weekly_breakdown: List[WeeklyBreakdown]
    monthly_trend: List[MonthlyTrend]

@router.get("/stats", response_model=StatsResponse)
def get_stats(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    total_lessons = db.query(Lesson).count()
    
    completed_lessons = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.status == "completed"
    ).count()
    
    total_time = db.query(func.sum(Progress.time_spent)).filter(
        Progress.user_id == current_user.id
    ).scalar() or 0
    
    completion_rate = (completed_lessons / total_lessons * 100) if total_lessons > 0 else 0
    
    completed_dates = db.query(Progress.completed_at).filter(
        Progress.user_id == current_user.id,
        Progress.status == "completed",
        Progress.completed_at.isnot(None)
    ).order_by(Progress.completed_at.desc()).all()
    
    current_streak = 0
    longest_streak = 0
    
    if completed_dates:
        dates = sorted(set([d[0].date() for d in completed_dates if d[0]]), reverse=True)
        
        today = datetime.utcnow().date()
        streak = 0
        for i, date in enumerate(dates):
            expected = today - timedelta(days=i)
            if date == expected:
                streak += 1
            else:
                break
        current_streak = streak
        
        temp_streak = 1
        for i in range(1, len(dates)):
            if (dates[i-1] - dates[i]).days == 1:
                temp_streak += 1
            else:
                longest_streak = max(longest_streak, temp_streak)
                temp_streak = 1
        longest_streak = max(longest_streak, temp_streak)
    
    today_date = datetime.utcnow().date()
    week_start = today_date - timedelta(days=today_date.weekday())
    week_end = week_start + timedelta(days=6)
    
    weekly_progress = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.started_at >= week_start,
        Progress.started_at <= week_end + timedelta(days=1)
    ).all()
    
    weekly_study_days = len(set(
        p.started_at.date() for p in weekly_progress if p.started_at
    ))
    weekly_time_spent = sum(p.time_spent or 0 for p in weekly_progress)
    
    all_lessons = db.query(Lesson).all()
    estimated_total_time = sum(l.time_estimate or 0 for l in all_lessons)
    
    return StatsResponse(
        total_lessons=total_lessons,
        completed_lessons=completed_lessons,
        total_time_spent=total_time,
        completion_rate=round(completion_rate, 1),
        current_streak=current_streak,
        longest_streak=longest_streak,
        weekly_study_days=weekly_study_days,
        weekly_time_spent=weekly_time_spent,
        estimated_total_time=estimated_total_time
    )

@router.get("/modules", response_model=List[ModuleProgress])
def get_module_progress(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    modules = db.query(Module).order_by(Module.order_index).all()
    
    result = []
    for module in modules:
        lessons = db.query(Lesson).filter(Lesson.module_id == module.id).all()
        lesson_ids = [l.id for l in lessons]
        
        completed = db.query(Progress).filter(
            Progress.user_id == current_user.id,
            Progress.status == "completed",
            Progress.lesson_id.in_(lesson_ids)
        ).count()
        
        total = len(lessons)
        percentage = (completed / total * 100) if total > 0 else 0
        
        progress_records = db.query(Progress).filter(
            Progress.user_id == current_user.id,
            Progress.lesson_id.in_(lesson_ids)
        ).all()
        
        time_spent = sum(p.time_spent or 0 for p in progress_records)
        estimated_time = sum(l.time_estimate or 0 for l in lessons)
        
        last_study = None
        if progress_records:
            dates = [p.started_at for p in progress_records if p.started_at]
            if dates:
                last_study = max(dates).isoformat()
        
        result.append(ModuleProgress(
            module_id=module.id,
            module_name=module.name,
            total=total,
            completed=completed,
            percentage=round(percentage, 1),
            time_spent=time_spent,
            estimated_time=estimated_time,
            last_study_date=last_study
        ))
    
    return result

@router.get("/time-stats", response_model=TimeStatsResponse)
def get_time_stats(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    total_time = db.query(func.sum(Progress.time_spent)).filter(
        Progress.user_id == current_user.id
    ).scalar() or 0
    
    all_lessons = db.query(Lesson).all()
    estimated_total_time = sum(l.time_estimate or 0 for l in all_lessons)
    
    efficiency_rate = (total_time / estimated_total_time * 100) if estimated_total_time > 0 else 0
    
    all_progress = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.started_at.isnot(None)
    ).all()
    
    if all_progress:
        first_date = min(p.started_at for p in all_progress if p.started_at)
        days_since_start = max(1, (datetime.utcnow() - first_date).days)
        daily_average = total_time // days_since_start
    else:
        daily_average = 0
    
    today_date = datetime.utcnow().date()
    week_start = today_date - timedelta(days=today_date.weekday())
    
    day_names = ['周一', '周二', '周三', '周四', '周五', '周六', '周日']
    weekly_breakdown = []
    
    for i, day_name in enumerate(day_names):
        day_date = week_start + timedelta(days=i)
        day_progress = db.query(Progress).filter(
            Progress.user_id == current_user.id,
            func.date(Progress.started_at) == day_date
        ).all()
        day_time = sum(p.time_spent or 0 for p in day_progress)
        weekly_breakdown.append(WeeklyBreakdown(day=day_name, time=day_time))
    
    monthly_trend = []
    for week_num in range(4, 0, -1):
        week_end = today_date - timedelta(days=(week_num-1) * 7)
        week_start_calc = week_end - timedelta(days=6)
        
        week_progress = db.query(Progress).filter(
            Progress.user_id == current_user.id,
            Progress.started_at >= week_start_calc,
            Progress.started_at <= week_end + timedelta(days=1)
        ).all()
        
        week_time = sum(p.time_spent or 0 for p in week_progress)
        monthly_trend.append(MonthlyTrend(week=f"W{5-week_num}", time=week_time))
    
    return TimeStatsResponse(
        total_time_spent=total_time,
        estimated_total_time=estimated_total_time,
        efficiency_rate=round(efficiency_rate, 1),
        daily_average=daily_average,
        weekly_breakdown=weekly_breakdown,
        monthly_trend=monthly_trend
    )

@router.get("/calendar", response_model=List[CalendarDay])
def get_calendar(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    end_date = datetime.utcnow().date()
    start_date = end_date - timedelta(days=29)
    
    progress_records = db.query(Progress).filter(
        Progress.user_id == current_user.id,
        Progress.completed_at >= start_date
    ).all()
    
    daily_data = {}
    for record in progress_records:
        if record.completed_at:
            date_str = record.completed_at.date().isoformat()
            if date_str not in daily_data:
                daily_data[date_str] = {"time_spent": 0, "lessons_completed": 0}
            daily_data[date_str]["time_spent"] += record.time_spent or 0
            if record.status == "completed":
                daily_data[date_str]["lessons_completed"] += 1
    
    result = []
    current = start_date
    while current <= end_date:
        date_str = current.isoformat()
        data = daily_data.get(date_str, {"time_spent": 0, "lessons_completed": 0})
        result.append(CalendarDay(
            date=date_str,
            time_spent=data["time_spent"],
            lessons_completed=data["lessons_completed"]
        ))
        current += timedelta(days=1)
    
    return result

@router.get("/today", response_model=List[TodayLesson])
def get_today_lessons(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    today = datetime.utcnow().strftime("%Y-%m-%d")
    
    lessons = db.query(Lesson).filter(Lesson.date == today).all()
    
    result = []
    for lesson in lessons:
        module = db.query(Module).filter(Module.id == lesson.module_id).first()
        progress = db.query(Progress).filter(
            Progress.user_id == current_user.id,
            Progress.lesson_id == lesson.id
        ).first()
        
        result.append(TodayLesson(
            id=lesson.id,
            title=lesson.title,
            module_name=module.name if module else "",
            status=progress.status if progress else "not_started"
        ))
    
    return result

@router.get("/admin/all-progress")
def get_all_progress(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    if current_user.role != "admin":
        return {"error": "Admin access required"}
    
    users = db.query(User).all()
    total_lessons = db.query(Lesson).count()
    
    result = []
    for user in users:
        completed = db.query(Progress).filter(
            Progress.user_id == user.id,
            Progress.status == "completed"
        ).count()
        
        result.append({
            "user_id": user.id,
            "username": user.username,
            "email": user.email,
            "completed_lessons": completed,
            "total_lessons": total_lessons,
            "completion_rate": round(completed / total_lessons * 100, 1) if total_lessons > 0 else 0
        })
    
    return result
