import sys
import os
import json

backend_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, backend_dir)

from app.utils.database import engine, SessionLocal
from app.models.models import Base, Module, Lesson, KnowledgePoint, Term, LessonTerm
from app.services.course_parser import parse_course_schedule, ModuleData
from app.services.content_parser import ContentParser
from app.config import settings

def init_db():
    print("Creating database tables...")
    Base.metadata.drop_all(bind=engine)
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")

def load_course_content():
    print("Loading course content...")
    db = SessionLocal()
    
    try:
        schedule_path = settings.COURSE_SCHEDULE_PATH
        if not os.path.exists(schedule_path):
            print(f"Schedule file not found: {schedule_path}")
            return
        
        parsed_modules = parse_course_schedule(schedule_path)
        content_parser = ContentParser(settings.CONTENT_PATH)
        
        for mod_data in parsed_modules:
            module = Module(
                name=mod_data.name,
                description=mod_data.description,
                order_index=mod_data.order
            )
            db.add(module)
            db.flush()
            
            print(f"\nModule {mod_data.order}: {mod_data.name}")
            
            for lesson_data in mod_data.lessons:
                lesson = Lesson(
                    module_id=module.id,
                    date=lesson_data.date,
                    title=lesson_data.title,
                    topics=lesson_data.topics,
                    difficulty=lesson_data.difficulty,
                    time_estimate=lesson_data.time_estimate,
                    materials=[{"title": m.title, "text": m.text, "path": m.path} for m in lesson_data.materials]
                )
                
                all_content = []
                all_knowledge_points = []
                all_terms = []
                
                for material in lesson_data.materials:
                    parsed = content_parser.parse_file(material.path)
                    if parsed:
                        all_content.append(f"## {material.title}\n\n{parsed.summary}")
                        all_knowledge_points.extend(parsed.knowledge_points)
                        all_terms.extend(parsed.terms)
                
                if all_content:
                    lesson.summary = "\n\n".join(all_content[:3])
                    lesson.raw_content = "\n\n---\n\n".join(all_content)
                
                db.add(lesson)
                db.flush()
                
                for kp in all_knowledge_points[:10]:
                    knowledge_point = KnowledgePoint(
                        lesson_id=lesson.id,
                        title=kp.title,
                        description=kp.description,
                        category=kp.category,
                        importance=kp.importance,
                        related_terms=kp.related_terms
                    )
                    db.add(knowledge_point)
                
                seen_terms = set()
                for term_data in all_terms:
                    if term_data.term in seen_terms:
                        continue
                    seen_terms.add(term_data.term)
                    
                    existing_term = db.query(Term).filter(Term.term == term_data.term).first()
                    
                    if not existing_term:
                        existing_term = Term(
                            term=term_data.term,
                            definition=term_data.definition,
                            category=term_data.category,
                            examples=term_data.examples,
                            related_terms=term_data.related_terms,
                            is_predefined=True
                        )
                        db.add(existing_term)
                        db.flush()
                    
                    lesson_term = LessonTerm(
                        lesson_id=lesson.id,
                        term_id=existing_term.id
                    )
                    db.add(lesson_term)
                
                print(f"  - Lesson: {lesson.title} ({len(all_knowledge_points)} knowledge points, {len(seen_terms)} terms)")
        
        db.commit()
        print("\nCourse content loaded successfully!")
        
        modules_count = db.query(Module).count()
        lessons_count = db.query(Lesson).count()
        kp_count = db.query(KnowledgePoint).count()
        terms_count = db.query(Term).count()
        
        print(f"\nStatistics:")
        print(f"  Modules: {modules_count}")
        print(f"  Lessons: {lessons_count}")
        print(f"  Knowledge Points: {kp_count}")
        print(f"  Terms: {terms_count}")
        
    except Exception as e:
        print(f"Error loading course content: {e}")
        import traceback
        traceback.print_exc()
        db.rollback()
    finally:
        db.close()

if __name__ == "__main__":
    init_db()
    load_course_content()
