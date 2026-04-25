#!/usr/bin/env bash
set -o errexit

# Instalacja zależności
pip install -r requirements.txt

# Zbieranie plików statycznych
python manage.py collectstatic --no-input

# KLUCZOWE: Tworzenie migracji dla aplikacji chat i ich aplikowanie
# To naprawia błąd "no such table: chat_profile"
python manage.py makemigrations chat
python manage.py migrate