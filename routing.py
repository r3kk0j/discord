from django.urls import re_path
import consumers

websocket_urlpatterns = [
    # Poprawiono z as_async_view() na as_asgi()
    re_path(r'ws/chat/(?P<room_name>\w+)/$', consumers.ChatConsumer.as_asgi()),
]