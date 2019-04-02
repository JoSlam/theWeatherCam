from django.db import models

class City(models.Model):
    city_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    longitude = models.FloatField()
    latitude = models.FloatField()
    

    class Meta:
        ordering = ('city_id', 'name','country')

    def __str__(self):
        return 'id: {0}, City: {1}, Country: {2}'.format(self.city_id, self.name, self.country)
    
