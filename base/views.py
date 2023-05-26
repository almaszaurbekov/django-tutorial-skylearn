from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Room, Topic

def home(request):
    rooms = Room.objects.all()
    context = { 'rooms': rooms }
    return render(request, "base/home.html", context)

def room(request, id):
    room = Room.objects.get(id=id)
    context = {'room': room}
    return render(request, "base/room.html", context)

def create_topic(request):
    if request.method == 'GET':
        return render(request, "base/create_topic.html")
    elif request.method == 'POST':
        try:
            created_topic = request.POST.get('name')
            Topic.objects.create(name=created_topic)
            return redirect('home')
        except Exception as ex:
            context = {'error': ex}
            return render(request, 'base/error.html', context)

def create_room(request):
    room = Room.objects.create(name="", description="", topic="")
    context = {'room': room}
    return render(request, "base/room.html", context)

def error(request):
    context = {'error': ''}
    return render(request, 'base/error.html', context)