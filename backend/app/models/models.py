from sqlalchemy import Column, String, DateTime, Boolean, Integer, Text, ForeignKey, JSON, Enum as SQLEnum
from sqlalchemy.orm import relationship
from datetime import datetime
import uuid
import enum
from app.utils.database import Base

class UserRole(str, enum.Enum):
    STUDENT = "student"
    GROUP_ADMIN = "group_admin"
    ADMIN = "admin"

class UserGroup(str, enum.Enum):
    GROUP_1 = "group1"
    GROUP_2 = "group2"
    GROUP_3 = "group3"
    GROUP_4 = "group4"
    GROUP_5 = "group5"
    GROUP_6 = "group6"

class ProgressStatus(str, enum.Enum):
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"

class User(Base):
    __tablename__ = "users"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    username = Column(String, unique=True, nullable=False, index=True)
    email = Column(String, unique=True, nullable=False, index=True)
    password_hash = Column(String, nullable=False)
    role = Column(String, default=UserRole.STUDENT.value)
    group = Column(String, default=UserGroup.GROUP_1.value)
    created_at = Column(DateTime, default=datetime.utcnow)
    settings = Column(JSON, default=dict)
    
    progress = relationship("Progress", back_populates="user")
    notes = relationship("Note", back_populates="user")

class Module(Base):
    __tablename__ = "modules"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, nullable=False)
    description = Column(Text)
    order_index = Column(Integer, default=0)
    
    lessons = relationship("Lesson", back_populates="module")

class Lesson(Base):
    __tablename__ = "lessons"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    module_id = Column(String, ForeignKey("modules.id"), nullable=False)
    date = Column(String)
    title = Column(String, nullable=False)
    topics = Column(JSON, default=list)
    difficulty = Column(String, default="basic")
    time_estimate = Column(Integer, default=60)
    materials = Column(JSON, default=list)
    summary = Column(Text)
    raw_content = Column(Text)
    structured_content = Column(JSON, default=dict)
    
    module = relationship("Module", back_populates="lessons")
    progress = relationship("Progress", back_populates="lesson")
    knowledge_points = relationship("KnowledgePoint", back_populates="lesson")
    lesson_terms = relationship("LessonTerm", back_populates="lesson")

class KnowledgePoint(Base):
    __tablename__ = "knowledge_points"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    lesson_id = Column(String, ForeignKey("lessons.id"), nullable=False)
    title = Column(String, nullable=False)
    description = Column(Text)
    category = Column(String, default="general")
    importance = Column(Integer, default=1)
    related_terms = Column(JSON, default=list)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    related_knowledge = Column(JSON, default=list)
    examples = Column(JSON, default=list)
    key_concepts = Column(JSON, default=list)
    common_mistakes = Column(JSON, default=list)
    best_practices = Column(JSON, default=list)
    external_links = Column(JSON, default=list)
    
    lesson = relationship("Lesson", back_populates="knowledge_points")

class Progress(Base):
    __tablename__ = "progress"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    lesson_id = Column(String, ForeignKey("lessons.id"), nullable=False)
    status = Column(String, default=ProgressStatus.NOT_STARTED.value)
    started_at = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)
    time_spent = Column(Integer, default=0)
    bookmarked = Column(Boolean, default=False)
    
    user = relationship("User", back_populates="progress")
    lesson = relationship("Lesson", back_populates="progress")

class Note(Base):
    __tablename__ = "notes"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    lesson_id = Column(String, ForeignKey("lessons.id"), nullable=False)
    content = Column(Text)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = relationship("User", back_populates="notes")

class Term(Base):
    __tablename__ = "terms"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    term = Column(String, nullable=False, unique=True, index=True)
    definition = Column(Text)
    category = Column(String, default="general")
    examples = Column(JSON, default=list)
    related_terms = Column(JSON, default=list)
    external_links = Column(JSON, default=list)
    is_predefined = Column(Boolean, default=False)
    
    detailed_definition = Column(Text)
    related_concepts = Column(JSON, default=list)
    usage_examples = Column(JSON, default=list)
    common_questions = Column(JSON, default=list)
    
    lesson_terms = relationship("LessonTerm", back_populates="term")

class LessonTerm(Base):
    __tablename__ = "lesson_terms"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    lesson_id = Column(String, ForeignKey("lessons.id"), nullable=False)
    term_id = Column(String, ForeignKey("terms.id"), nullable=False)
    
    lesson = relationship("Lesson", back_populates="lesson_terms")
    term = relationship("Term", back_populates="lesson_terms")

class PracticeQuestion(Base):
    __tablename__ = "practice_questions"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    knowledge_point_id = Column(String, ForeignKey("knowledge_points.id"), nullable=False)
    question_type = Column(String, default="single_choice")
    question_text = Column(Text, nullable=False)
    options = Column(JSON, default=list)
    correct_answer = Column(Text, nullable=False)
    explanation = Column(Text)
    difficulty = Column(Integer, default=1)
    order_index = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    knowledge_point = relationship("KnowledgePoint", backref="practice_questions")

class UserAnswer(Base):
    __tablename__ = "user_answers"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    user_id = Column(String, ForeignKey("users.id"), nullable=False)
    question_id = Column(String, ForeignKey("practice_questions.id"), nullable=False)
    user_answer = Column(Text)
    is_correct = Column(Boolean, default=False)
    answered_at = Column(DateTime, default=datetime.utcnow)
    
    user = relationship("User", backref="answers")
    question = relationship("PracticeQuestion", backref="user_answers")

class AISettings(Base):
    __tablename__ = "ai_settings"

    id = Column(String, primary_key=True, default="default")
    provider = Column(String, default="none")
    openai_api_key = Column(String, nullable=True)
    openai_base_url = Column(String, nullable=True)
    local_model_url = Column(String, nullable=True)
    local_model_name = Column(String, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Article(Base):
    __tablename__ = "articles"
    
    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    title = Column(String, nullable=False)
    content = Column(Text, nullable=False)
    source = Column(String, nullable=False)
    source_url = Column(String, nullable=False)
    category = Column(String, default="general")
    summary = Column(Text)
    author = Column(String, nullable=True)
    published_at = Column(DateTime, nullable=True)
    added_by = Column(String, ForeignKey("users.id"))
    is_published = Column(Boolean, default=True)
    view_count = Column(Integer, default=0)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    user = relationship("User", backref="articles")
