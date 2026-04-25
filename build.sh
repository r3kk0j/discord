#!/usr/bin/env bash
# exit on error
set -o errexit

# Instalacja zależności
python -m pip install --upgrade pip
pip install -r requirements.txt

# Przygotowanie statyków i bazy
python manage.py collectstatic --no-input
python manage.py makemigrations chat
python manage.py migrate