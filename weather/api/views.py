from django.shortcuts import redirect
from django.urls import reverse
from ..models import City, UserCity
from django.contrib import messages
from django.shortcuts import get_object_or_404

def add_user_city(request):
    data = request.POST
    city_id = data.get('city')
    city = get_object_or_404(City, city_id=city_id)
    if request.user.is_authenticated:
        if UserCity.objects.filter(user=request.user).count() == 5:
            messages.add_message(request, messages.WARNING, 'Maximum of 5 items allowed')
        else:
            user_city, c = UserCity.objects.get_or_create(user=request.user, city=city)
            if c == False:
                messages.add_message(request, messages.WARNING, 'No copy allowed!')
    return redirect(reverse('weather'))

def del_user_city(request):
    data = request.POST
    user = request.user
    city_id = data.get('city_id')
    user_city = get_object_or_404(UserCity, user=user, city__city_id=city_id)
    user_city.delete()
    return redirect(reverse('weather'))
