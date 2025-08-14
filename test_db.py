from database import get_session
from models import Student, Teacher, Group, Subject, Grade

session = get_session()

print("✅ Перевірка бази даних:")

print("Кількість студентів:", session.query(Student).count())
print("Кількість викладачів:", session.query(Teacher).count())
print("Кількість груп:", session.query(Group).count())
print("Кількість предметів:", session.query(Subject).count())
print("Кількість оцінок:", session.query(Grade).count())
