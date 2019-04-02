from django.db import models

from datetime import datetime

class Weather(models.Model):
    date = models.DateTimeField()
    wind_speed = models.FloatField()
    temp = models.FloatField()
    humidity = models.IntegerField()
    pressure = models.FloatField()
    city = models.ForeignKey('api.City', on_delete=models.CASCADE, default=None)
    
    class Meta:
        ordering = ('date',)


    def __str__(self):
        return '{0}'.format(self.date)

