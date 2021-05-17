from django.urls import path
from .consumers import WSConsumer
from django.urls import re_path

ws_urlpatterns = [
    path('ws/chat/<room_name>/', WSConsumer.as_asgi())
]