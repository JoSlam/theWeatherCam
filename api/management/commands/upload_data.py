from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
import urllib3
import json
import os

# model import
from api.models import Weather 

url = 'http://api.openweathermap.org/data/2.5/weather?q=curepe,tt&APPID=13ceb7203fe9f550a498f8e24d080268&units=metric'
http = urllib3.PoolManager()

class Command(BaseCommand):
    help = 'Uploads new weather data'
    
    def handle(self, *args, **options):
        req = http.request('GET', url)
        json_dat = json.loads(req.data.decode())
        new_weather = Weather(
            date=datetime.fromtimestamp(json_dat['dt']),
            wind_speed=json_dat['wind']['speed'],
            temp=json_dat['main']['temp'],
            humidity=json_dat['main']['humidity'],
            pressure=json_dat['main']['pressure']
        )
        new_weather.save()
        print(new_weather)