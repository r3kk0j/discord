from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from chat import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('chat/<str:room_name>/', views.chat_room, name='chat_room'),
]