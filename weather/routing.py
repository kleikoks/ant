from django.urls import path
from .consumers import WeatherConsumer
from django.urls import re_path

ws_urlpatterns = [
    path('ws/weather/', WeatherConsumer.as_asgi()),
]