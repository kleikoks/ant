from django.shortcuts import render


def index(request):
    return render(request, 'project/index.html')

def login(request):
    return render(request, 'project/login.html')

def register(request):
    return render(request, 'project/register.html')