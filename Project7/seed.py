from faker import Faker
import random
from config import Session, engine, Base
from models import Group, Student, Teacher, Subject, Grade

fake = Faker()

def seed_data():
    Base.metadata.create_all(engine)
    session = Session()
    groups = [Group(name=f"Group {i}") for i in range(1, 4)]
    session.add_all(groups)
    teachers = [Teacher(fullname=fake.name()) for _ in range(5)]
    session.add_all(teachers)
    subjects = [Subject(name=fake.word(), teacher=random.choice(teachers)) for _ in range(8)]
    session.add_all(subjects)
    students = [Student(fullname=fake.name(), group=random.choice(groups)) for _ in range(50)]
    session.add_all(students)
    for student in students:
        for subject in subjects:
            for _ in range(random.randint(10, 20)):
                grade = Grade(
                    grade=random.randint(1, 12),
                    student=student,
                    subject=subject
                )
                session.add(grade)
    session.commit()
    session.close()

if __name__ == "__main__":
    seed_data()
