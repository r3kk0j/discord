from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'views.custom_404'