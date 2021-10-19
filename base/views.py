from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm, TopicForm

# Create your views here.
def loginPage(request):
  context = {}
  return render(request, 'base/auth/login.html', context)

def home(request):
  Rooms = Room.objects.all()
  topics = Topic.objects.all()

  context = {'rooms': Rooms, 'topics': topics}
  return render(request, 'base/home.html', context)

def topics(request):
  topics = Topic.objects.all()
  searchedValue = None
  if request.method == 'POST':
    form = request.POST
    searchedValue = form.get("topic_name")
    topics = Topic.objects.filter(name__icontains=searchedValue)

  topicContext = {'topics': topics, 'searchedValue': searchedValue}

  return render(request, 'base/topic/topics.html', topicContext)

def topic(request, id):
  rooms = Room.objects.filter(topic=id)
  topic = Topic.objects.get(id=id)
  topicContext = {'topic': topic, 'rooms': rooms}

  return render(request, 'base/topic/topic.html', topicContext)

def rooms(request):
    rooms = Room.objects.all()
    searchedValue = None

    if request.method == 'POST':
      form = request.POST
      searchedValue = form.get("room_name")
      rooms = Room.objects.filter(name__icontains=searchedValue)
    
    context = {'rooms': rooms, 'searchedValue': searchedValue}
    return render(request, 'base/room/rooms.html', context)

def room(request, id):
  room = Room.objects.get(id=id)
  context = {'room': room}

  return render(request, 'base/room/room.html', context)

def createRoom(request):
  form = RoomForm()
  if request.method == 'POST':
    form = RoomForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('rooms')

  context = {'form': form}
  return render(request, 'base/room/add_edit_form.html', context)

def updateRoom(request, id):
  room = Room.objects.get(id=id)
  form = RoomForm(instance=room)
  if request.method == 'POST':
    form = RoomForm(request.POST, instance=room)
    if form.is_valid():
      form.save()
      return redirect('rooms')

  context = {'form': form}
  return render(request, 'base/room/add_edit_form.html', context)

def deleteRoom(request, id):
  try:
    room = Room.objects.get(id=id)
  except Room.DoesNotExist:
    room = None
  if (request.method == 'POST'):
    room.delete()
    return redirect('rooms')
  
  return render(request, 'base/room/delete-room.html', {'obj': room})

def about(request):
  return render(request, 'about.html')