from app.utils.database import SessionLocal
from app.models.models import Module, Lesson, KnowledgePoint, PracticeQuestion, LessonTerm

db = SessionLocal()

# 删除重复的模块 '基础提示结构'
duplicate_module = db.query(Module).filter(Module.name == '基础提示结构').first()
if duplicate_module:
    # 先删除该模块下的课程
    lessons = db.query(Lesson).filter(Lesson.module_id == duplicate_module.id).all()
    for lesson in lessons:
        db.query(KnowledgePoint).filter(KnowledgePoint.lesson_id == lesson.id).delete()
        db.query(LessonTerm).filter(LessonTerm.lesson_id == lesson.id).delete()
        db.query(Lesson).filter(Lesson.id == lesson.id).delete()
    db.delete(duplicate_module)
    print('Deleted duplicate module: 基础提示结构')

db.commit()
db.close()
print('Database cleaned up')
