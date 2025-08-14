from sqlalchemy import func, desc
from models import Student, Teacher, Grade, Group, Subject
from database import session

def select_11(teacher_id: int, student_id: int):
    return session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade'))\
        .join(Subject, Grade.subject_id == Subject.id)\
        .filter(Subject.teacher_id == teacher_id, Grade.student_id == student_id)\
        .scalar()

def select_12(group_id: int, subject_id: int):
    subquery = session.query(func.max(Grade.date).label('last_date'))\
        .filter(Grade.subject_id == subject_id).subquery()
    
    return session.query(Student.fullname, Grade.grade, Grade.date)\
        .join(Grade, Grade.student_id == Student.id)\
        .filter(Student.group_id == group_id, Grade.subject_id == subject_id, Grade.date == subquery.c.last_date)\
        .all()
