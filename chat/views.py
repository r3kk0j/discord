from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.decorators import login_required
from .models import Channel

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
    # Proste pobranie kanałów, jeśli baza pusta - stwórz jeden
    channels = Channel.objects.all()
    if not channels.exists():
        Channel.objects.create(name="ogolny")
    return render(request, 'index.html', {'channels': channels, 'type': 'home'})

@login_required
def chat_room(request, room_name):
    return render(request, 'chat.html', {'room_name': room_name})


from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from .models import Channel, DatabaseTest


@login_required
def index(request):
    # TEST BAZY: Spróbuj stworzyć wpis
    db_status = "Oczekiwanie..."
    try:
        DatabaseTest.objects.create(status="Baza działa i zapisuje!")
        db_status = "SUKCES: Baza danych się uaktualniła!"
    except Exception as e:
        db_status = f"BŁĄD: Tabela nie istnieje lub brak uprawnień: {str(e)}"

    channels = Channel.objects.all()
    if not channels.exists():
        Channel.objects.create(name="ogolny")

    return render(request, 'index.html', {
        'channels': channels,
        'type': 'home',
        'db_test': db_status
    })

# Pozostałe widoki (register_view, login_view) zostaw bez zmian (tylko usuń odwołania do Profile)