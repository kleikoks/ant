from django.contrib.auth.decorators import login_required
from django.shortcuts import render
import requests
from decouple import config
from .models import City, UserCity


@login_required
def weather(request):
    user_cities = UserCity.objects.filter(user=request.user)
    cities = City.objects.all()
    user_cities_grip = [(c.city.city_id, c.city.title) for c in user_cities]
    cities_grip = [(c.city_id, c.title) for c in cities]
    handy_cities = [c for c in cities_grip if c not in user_cities_grip]
    api_key = config('WEATHER_API_KEY')
    data = []
    for city_id, city_name in user_cities_grip:
        schema = 'https'
        domain = 'api.openweathermap.org'
        api = f'data/2.5/weather?id={city_id}&appid={api_key}&lang=ua&units=metric'
        url = f'{schema}://{domain}/{api}'
        city_weather = requests.get(url).json()
        obj = {
            'city_id': city_id,
            'name': city_name,
            'icon': city_weather['weather'][0]['icon'],
            'temperature': int(city_weather['main']['temp']),
            'description': city_weather['weather'][0]['description']
        }
        data.append(obj)
    return render(request, 'weather/weather.html', context={
        'cities': data,
        'handy_cities': handy_cities
    })


