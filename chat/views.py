from django.shortcuts import render, redirect
from chat.models import Message, Room


def home(request):
    return render(request, 'home.html')


def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.create(name=room)
    
    return render(request, 'room.html', {
                  'username': username,
                  'room': room,
                  'room_details': room_details,
                  })


def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']
    
    if Room.objects.filter(name=room).exists():
        return redirect(f"/{room}/?username={username}")
    else:
      new_room = Room.objects.create(name=room)
      new_room.save()
      
      return redirect(f"/{room}/?username={username}")
