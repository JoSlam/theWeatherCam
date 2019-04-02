from django.contrib import admin
from api.models import Weather, WeatherImage, City

admin.site.register(Weather)
admin.site.register(WeatherImage)
admin.site.register(City)