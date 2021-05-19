from django.apps import AppConfig


class WeatherConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'weather'
    verbose_name = 'Погода'
    
    def ready(self):
        import weather.signals

default_app_config = 'weather.WeatherConfig'