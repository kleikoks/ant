from .views import *
from django.urls.conf import include, path
from .views import api_login, api_register


urlpatterns = [
    path('login', api_login, name='api_login'),
    path('register/', api_register, name='api_register'),
    path('api_logout/', api_logout, name='api_logout'),
]