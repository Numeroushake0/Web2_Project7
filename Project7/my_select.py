from sqlalchemy import func, desc
from config import Session
from models import Student, Grade, Subject, Teacher, Group

def select_1():
    session = Session()
    r = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')).select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    session.close()
    return r

def select_2(subject_name):
    session = Session()
    r = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Student.id).order_by(desc('avg_grade')).first()
    session.close()
    return r

def select_3(subject_name):
    session = Session()
    r = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')).join(Student).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Group.id).all()
    session.close()
    return r

def select_4():
    session = Session()
    r = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).all()
    session.close()
    return r

def select_5(teacher_name):
    session = Session()
    r = session.query(Subject.name).join(Teacher).filter(Teacher.fullname == teacher_name).all()
    session.close()
    return r

def select_6(group_name):
    session = Session()
    r = session.query(Student.fullname).join(Group).filter(Group.name == group_name).all()
    session.close()
    return r

def select_7(group_name, subject_name):
    session = Session()
    r = session.query(Student.fullname, Grade.grade).join(Group).join(Grade).join(Subject).filter(Group.name == group_name, Subject.name == subject_name).all()
    session.close()
    return r

def select_8(teacher_name):
    session = Session()
    r = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).join(Subject).join(Teacher).filter(Teacher.fullname == teacher_name).all()
    session.close()
    return r

def select_9(student_name):
    session = Session()
    r = session.query(Subject.name).join(Grade).join(Student).filter(Student.fullname == student_name).distinct().all()
    session.close()
    return r

def select_10(student_name, teacher_name):
    session = Session()
    r = session.query(Subject.name).join(Teacher).join(Grade).join(Student).filter(Student.fullname == student_name, Teacher.fullname == teacher_name).distinct().all()
    session.close()
    return r
from sqlalchemy import func, desc
from config import Session
from models import Student, Grade, Subject, Teacher, Group

def select_1():
    session = Session()
    r = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')).select_from(Grade).join(Student).group_by(Student.id).order_by(desc('avg_grade')).limit(5).all()
    session.close()
    return r

def select_2(subject_name):
    session = Session()
    r = session.query(Student.fullname, func.round(func.avg(Grade.grade), 2).label('avg_grade')).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Student.id).order_by(desc('avg_grade')).first()
    session.close()
    return r

def select_3(subject_name):
    session = Session()
    r = session.query(Group.name, func.round(func.avg(Grade.grade), 2).label('avg_grade')).join(Student).join(Grade).join(Subject).filter(Subject.name == subject_name).group_by(Group.id).all()
    session.close()
    return r

def select_4():
    session = Session()
    r = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).all()
    session.close()
    return r

def select_5(teacher_name):
    session = Session()
    r = session.query(Subject.name).join(Teacher).filter(Teacher.fullname == teacher_name).all()
    session.close()
    return r

def select_6(group_name):
    session = Session()
    r = session.query(Student.fullname).join(Group).filter(Group.name == group_name).all()
    session.close()
    return r

def select_7(group_name, subject_name):
    session = Session()
    r = session.query(Student.fullname, Grade.grade).join(Group).join(Grade).join(Subject).filter(Group.name == group_name, Subject.name == subject_name).all()
    session.close()
    return r

def select_8(teacher_name):
    session = Session()
    r = session.query(func.round(func.avg(Grade.grade), 2).label('avg_grade')).join(Subject).join(Teacher).filter(Teacher.fullname == teacher_name).all()
    session.close()
    return r

def select_9(student_name):
    session = Session()
    r = session.query(Subject.name).join(Grade).join(Student).filter(Student.fullname == student_name).distinct().all()
    session.close()
    return r

def select_10(student_name, teacher_name):
    session = Session()
    r = session.query(Subject.name).join(Teacher).join(Grade).join(Student).filter(Student.fullname == student_name, Teacher.fullname == teacher_name).distinct().all()
    session.close()
    return r
