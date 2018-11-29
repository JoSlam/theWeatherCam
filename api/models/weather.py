from django.db import models

class Weather(models.Model):
    date = models.DateTimeField()
    wind_speed = models.FloatField()
    temp = models.FloatField()
    humidity = models.IntegerField()
    pressure = models.FloatField()

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return '{0}'.format(self.date)
    
