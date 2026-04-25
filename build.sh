#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
python manage.py collectstatic --no-input

# To rozwiązanie "na chama" – tworzy tabele pomijając system migracji, jeśli ten zawiedzie
python manage.py makemigrations chat
python manage.py migrate --run-syncdb