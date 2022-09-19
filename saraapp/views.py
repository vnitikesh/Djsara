from django.shortcuts import render
# from .models import UserActivity

# Create your views here.

def landing(request):
    return render(request, 'saraap/landing.html')

def index(request):
    return render(request, 'saraapp/index.html')

def room(request, room_name):
    return render(request, 'saraapp/room.html', {
        'room_name': room_name
    })


