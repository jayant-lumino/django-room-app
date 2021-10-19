from django.shortcuts import render, redirect
from .models import Room, Topic
from .forms import RoomForm, TopicForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def registerPage(request):
  form = UserCreationForm()
  if request.method == 'POST':
    form = UserCreationForm(request.POST)
    if form.is_valid():
      user = form.save(commit=False)
      user.username = user.username.lower()
      user.save()

      login(request, user)
      return redirect('home')
    else:
      messages.error(request, 'An error occured while registering. Please try again')

  context = {'form': form}
  return render(request, 'base/auth/register.html', context)

def loginPage(request):
  # If user logged in already
  if request.user.is_authenticated:
    return redirect('home')

  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')

    # If username is empty
    if username == '':
      messages.error(request, 'Please fill the details to login.')
      return redirect('login')

    # Check if user exists
    try:
      user = User.objects.get(username=username)
    except User.DoesNotExist:
      messages.error(request, 'User not found with given username.')
      return redirect('login')

    # Authenticate User if exists
    user = authenticate(request, username=username, password=password)

    if user is not None:
      login(request, user)
      return redirect('home')
    else:
      messages.error(request, 'Invalid Credentials.')

  return render(request, 'base/auth/login.html')

def logoutPage(request):
  logout(request)
  return redirect('home')

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
  messages = room.message_set.all()
  context = {'room': room, 'messages': messages}

  return render(request, 'base/room/room.html', context)

@login_required(login_url="login")
def createRoom(request):
  form = RoomForm()
  if request.method == 'POST':
    form = RoomForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect('rooms')

  context = {'form': form}
  return render(request, 'base/room/add_edit_form.html', context)

@login_required(login_url="login")
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

@login_required(login_url="login")
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