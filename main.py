import argparse
from database import get_session
from seed import seed_data
from models import Student, Teacher, Group, Subject, Grade

def main():
    parser = argparse.ArgumentParser(description="CLI для роботи з базою даних студентів")
    parser.add_argument("-a", "--action", required=True)
    parser.add_argument("-m", "--model")
    parser.add_argument("-n", "--name")
    parser.add_argument("--id", type=int)
    parser.add_argument("--teacher_id", type=int)
    parser.add_argument("--student_id", type=int)
    parser.add_argument("--subject_id", type=int)
    parser.add_argument("--group_id", type=int)
    parser.add_argument("--grade", type=int)
    args = parser.parse_args()
    session = get_session()

    if args.action == "seed":
        seed_data(session)
        return

    if not args.model:
        return

    model_mapping = {
        "Student": Student,
        "Teacher": Teacher,
        "Group": Group,
        "Subject": Subject,
        "Grade": Grade
    }

    model_class = model_mapping.get(args.model)
    if not model_class:
        return

    if args.action == "create":
        if args.model == "Student":
            session.add(Student(fullname=args.name, group_id=args.group_id))
        elif args.model == "Teacher":
            session.add(Teacher(fullname=args.name))
        elif args.model == "Group":
            session.add(Group(name=args.name))
        elif args.model == "Subject":
            session.add(Subject(name=args.name, teacher_id=args.teacher_id))
        elif args.model == "Grade":
            session.add(Grade(grade=args.grade, student_id=args.student_id, subject_id=args.subject_id))
        session.commit()

    elif args.action == "list":
        items = session.query(model_class).all()
        for item in items:
            print(item)

    elif args.action == "update":
        if not args.id:
            return
        obj = session.get(model_class, args.id)
        if not obj:
            return
        if args.name:
            if args.model in ["Student", "Teacher"]:
                obj.fullname = args.name
            elif args.model in ["Group", "Subject"]:
                obj.name = args.name
        if args.grade and args.model == "Grade":
            obj.grade = args.grade
        session.commit()

    elif args.action == "remove":
        if not args.id:
            return
        obj = session.get(model_class, args.id)
        if not obj:
            return
        session.delete(obj)
        session.commit()

if __name__ == "__main__":
    main()
