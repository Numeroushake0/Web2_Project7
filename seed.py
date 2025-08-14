from faker import Faker
from random import randint, choice
from datetime import date
from models import Group, Student, Teacher, Subject, Grade

fake = Faker()

def seed_data(session):
    groups = [Group(name=f"Group {i}") for i in range(1, 4)]
    session.add_all(groups)

    teachers = [Teacher(fullname=fake.name()) for _ in range(4)]
    session.add_all(teachers)

    subjects = [Subject(name=fake.word().capitalize(), teacher=choice(teachers)) for _ in range(6)]
    session.add_all(subjects)

    students = [Student(fullname=fake.name(), group=choice(groups)) for _ in range(40)]
    session.add_all(students)

    session.commit()

    for student in students:
        for subject in subjects:
            for _ in range(randint(10, 20)):
                session.add(Grade(
                    grade=randint(1, 12),
                    date_received=fake.date_this_year(),
                    student=student,
                    subject=subject
                ))

    session.commit()
    print("✅ Database seeded successfully.")

if __name__ == "__main__":
    from database import get_session
    session = get_session()
    seed_data(session)
