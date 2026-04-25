#!/usr/bin/env bash
# exit on error
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input
# Te dwie linie są kluczowe, żeby stworzyć tabele w bazie:
python manage.py makemigrations chat
python manage.py migrate