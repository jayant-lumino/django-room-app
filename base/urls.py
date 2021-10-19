from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.loginPage, name="login"),
    path('topics/', views.topics, name="topics"),
    path('topic/<str:id>/', views.topic, name="topic"),
    path('rooms/', views.rooms, name="rooms"),
    path('room/<str:id>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:id>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:id>/', views.deleteRoom, name="delete-room"),
    path('about/', views.about, name="about"),
]
