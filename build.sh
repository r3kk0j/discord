#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
pip install Pillow dj-database-url whitenoise # upewnij się, że są zainstalowane

python manage.py collectstatic --no-input
python manage.py makemigrations chat
python manage.py migrate