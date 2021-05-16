from django.urls import path
from .views import add_user_city, del_user_city

urlpatterns = [
    path('add_user_city/', add_user_city, name='add_user_city'),
    path('del_user_city/', del_user_city, name='del_user_city'),
]
