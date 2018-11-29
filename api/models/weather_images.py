from django.db import models
from django.db.models import (
    DateTimeField,
    CharField
)

class WeatherImage(models.Model):
    created = DateTimeField()
    url = CharField(max_length=250)

    def __str__(self):
        return '{}'.format(self.url)
        
    class Meta:
        ordering = ('created',)