import argparse
from config import Session
from models import Group, Student, Teacher, Subject

parser = argparse.ArgumentParser()
parser.add_argument("-a", "--action", choices=["create", "list", "update", "remove"])
parser.add_argument("-m", "--model", choices=["Group", "Student", "Teacher", "Subject"])
parser.add_argument("-n", "--name")
parser.add_argument("--id", type=int)

args = parser.parse_args()
if not args.action or not args.model:
    print("Вкажи --action та --model")
    exit(1)

session = Session()
Model = globals()[args.model]

if args.action == "create":
    obj = Model(name=args.name) if hasattr(Model, "name") else Model(fullname=args.name)
    session.add(obj)
    session.commit()
    print(f"{args.model} created.")

elif args.action == "list":
    for obj in session.query(Model).all():
        print(obj.id, getattr(obj, "name", getattr(obj, "fullname", "")))

elif args.action == "update":
    obj = session.query(Model).get(args.id)
    if obj:
        if hasattr(obj, "name"):
            obj.name = args.name
        else:
            obj.fullname = args.name
        session.commit()
        print(f"{args.model} updated.")

elif args.action == "remove":
    obj = session.query(Model).get(args.id)
    if obj:
        session.delete(obj)
        session.commit()
        print(f"{args.model} removed.")

session.close()
