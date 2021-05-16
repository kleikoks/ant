from django.contrib import admin
from django.urls import path
from django.urls.conf import include
from .views import index, login, register


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('login/', login, name='login'),
    path('register/', register, name='register'),
    path('', include('weather.urls')),
    #API
    path('api/', include('weather.api.urls')),
    path('api/', include('project.api.urls')),
]
