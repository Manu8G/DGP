from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('chat_rooms', views.chat_rooms, name='chat_rooms'),
    path('room/<str:room_name>/', views.room, name="room"),
]
