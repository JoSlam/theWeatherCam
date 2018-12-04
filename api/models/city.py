from django.db import models

class City(models.Model):
    date = models.DateTimeField()
    

    class Meta:
        ordering = ('date',)

    def __str__(self):
        return '{0}'.format(self.date)
    
