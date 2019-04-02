from django.db import models

class CityUploadDoc(models.Model):
    document = models.FileField(upload_to='documents/city/%Y/%m/%d')
    