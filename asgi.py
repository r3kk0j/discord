import os
import django
from django.core.asgi import get_asgi_application

# 1. Ustawienie modułu ustawień
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')

# 2. Inicjalizacja Django (Kluczowy krok!)
django.setup()

# 3. Importy po inicjalizacji
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import chat.routing

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            chat.routing.websocket_urlpatterns
        )
    ),
})