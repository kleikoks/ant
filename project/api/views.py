from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, logout, authenticate
from django.db.models import Q
from django.contrib.auth import (authenticate, get_user_model, login, logout)
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt


def api_login(request):
    data = request.POST
    username = data.get('username')
    password = data.get('password')
    users = get_user_model().objects.filter(
        Q(username__iexact=username)
    ).distinct() 
    print(users)
    if not users.exists() and users.count() != 1:
        messages.add_message(request, messages.WARNING, "User doesn't exist!")
        return redirect(request.META.get('HTTP_REFERER', 'login'))
    user = users.first() 
    if not user.check_password(password):
        messages.add_message(request, messages.WARNING, "Incorrect password!")
        return redirect(request.META.get('HTTP_REFERER', 'login'))
    if not user.is_active:
        messages.add_message(request, messages.WARNING, "User disactivated!")
        return redirect(request.META.get('HTTP_REFERER', 'login'))
    user = authenticate(username=user.username, password=password)
    login(request, user)
    return redirect('weather')

def api_register(request):
    data = request.POST
    username = data.get('username')
    password = data.get('password')
    if password == '':
        messages.add_message(request, messages.WARNING, "Password, please!")
        return redirect(request.META.get('HTTP_REFERER', 'register'))
    username_qs = get_user_model().objects.filter(username=username)
    if username_qs.exists():
        messages.add_message(request, messages.WARNING, "User exist!")
        return redirect(request.META.get('HTTP_REFERER', 'register'))
    user = get_user_model().objects.create_user(
        username     = username
    )
    user.set_password(password)
    user.is_active = True 
    user.save() 
    new_user = authenticate(username=user.username, password=password)
    login(request, user, backend='django.contrib.auth.backends.ModelBackend')
    return redirect('weather')

def api_logout(request):
    logout(request)
    return redirect('index')
