from django.apps import AppConfig


class WeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather'
    verbose_name = 'Погода'

default_app_config = 'weather.WeatherConfig'