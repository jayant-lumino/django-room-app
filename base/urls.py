from django.urls import path
from . import views

urlpatterns = [
    # Auth Routes
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),

    # Web Routes
    path('', views.home, name="home"),
    # Topics
    path('topics/', views.topics, name="topics"),
    path('topic/<str:id>/', views.topic, name="topic"),
    # Rooms
    path('rooms/', views.rooms, name="rooms"),
    path('room/<str:id>/', views.room, name="room"),
    path('create-room/', views.createRoom, name="create-room"),
    path('update-room/<str:id>/', views.updateRoom, name="update-room"),
    path('delete-room/<str:id>/', views.deleteRoom, name="delete-room"),
    path('delete-message/<str:id>/', views.deleteMessage, name="delete-message"),
    # Pages
    path('about/', views.about, name="about"),
]
