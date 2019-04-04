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

    def save(self, *args, **kwargs):
        if not self.id:
            self.date = datetime.utcnow()
        return super(Weather, self).save(*args, **kwargs)
