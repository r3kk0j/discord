#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input

# Usuwamy stare śmieci w migracjach
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete

# Inicjalizacja bazy w RAM
python manage.py makemigrations chat
python manage.py migrate