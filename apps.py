from django.apps import AppConfig

class ChatConfig(AppConfig):
    name = 'chat'
    path = '.'  # Wskazuje na bieżący katalog
    label = 'chat'