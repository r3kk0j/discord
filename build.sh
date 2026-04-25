#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt
pip install Pillow

python manage.py collectstatic --no-input
python manage.py makemigrations chat
python manage.py migrate