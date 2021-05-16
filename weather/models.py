from django.db import models
from django.conf import settings

class City(models.Model):
    class Meta:
        verbose_name = 'Місто'
        verbose_name_plural = 'Міста'
    
    title = models.CharField(verbose_name='Місто', max_length=128, blank=False)
    city_id = models.IntegerField(verbose_name='ID міста', blank=False, unique=True)

    def __str__(self):
        return f'{self.title}'



class UserCity(models.Model):
    class Meta:
        verbose_name = 'Міста користувачів'
        verbose_name_plural = 'Міста користувачів'
        unique_together = ('user', 'city')
    
    user = models.ForeignKey(verbose_name='Користувач', to=settings.AUTH_USER_MODEL, blank=False, on_delete=models.CASCADE)
    city = models.ForeignKey(verbose_name='Місто', to='City', blank=False, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.user} {self.city}'