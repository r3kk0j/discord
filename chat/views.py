from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Channel, Message

def register_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'index.html', {'form': form, 'type': 'register'})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('index')
    else:
        form = AuthenticationForm()
    return render(request, 'index.html', {'form': form, 'type': 'login'})

@login_required
def index(request):
    channels = Channel.objects.all()
    if not channels.exists():
        Channel.objects.get_or_create(name="ogolny")
    return render(request, 'index.html', {'channels': channels, 'type': 'home'})

@login_required
def chat_room(request, room_name):
    channel, created = Channel.objects.get_or_create(name=room_name)
    chat_messages = Message.objects.filter(channel=channel)
    channels = Channel.objects.all()
    return render(request, 'chat.html', {
        'room_name': room_name,
        'chat_messages': chat_messages,
        'channels': channels
    })