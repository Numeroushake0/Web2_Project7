cd Project7
alembic upgrade head > /dev/null
python3 seed.py > /dev/null

echo "Список студентів:"
python3 main.py -a list -m Student