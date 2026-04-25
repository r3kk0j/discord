#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

# Dodanie 'chat' jest kluczowe, żeby stworzyć tabelę chat_profile
python manage.py makemigrations chat
python manage.py migrate