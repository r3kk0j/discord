#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py collectstatic --no-input

# To przygotuje instrukcje stworzenia tabel dla wszystkich modeli (Profile, Channel itd.)
python manage.py makemigrations chat
python manage.py makemigrations

# To fizycznie stworzy brakujące tabele w db.sqlite3
python manage.py migrate --run-syncdb