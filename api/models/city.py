from django.db import models

class City(models.Model):
    name = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    longitude = models.FloatField()
    latitude = models.FloatField()
    

    class Meta:
        ordering = ('name','country')

    def __str__(self):
        return '{0}{1}'.format(self.name, self.country)
    
