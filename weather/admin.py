from django.contrib import admin
from .models import City, UserCity


@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'city_id']
    list_editable = ['title', 'city_id']

@admin.register(UserCity)
class CityAdmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'city']
    list_display_links = ['id', 'user', 'city']