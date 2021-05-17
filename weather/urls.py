
from django.contrib import admin
from django.urls import path
from .views import weather, chat, room


urlpatterns = [
    path('weather/', weather, name='weather'),
    path('chat/', chat, name='chat'),
    path('chat/<room>/', room, name='room'),

]