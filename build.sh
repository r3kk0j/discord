#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input

# CAŁKOWITY RESET MIGRACJI - usuwamy historię, żeby nie było konfliktów
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
find . -path "*/migrations/*.pyc" -delete

# Tworzymy wszystko od zera
python manage.py makemigrations chat
python manage.py makemigrations
python manage.py migrate --run-syncdb