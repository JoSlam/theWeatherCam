from django.core.management.base import BaseCommand, CommandError
from datetime import datetime
from subprocess import Popen
import shlex
import urllib3
import json
import os

# model import
from api.models import WeatherImage 

url = 'http://api.openweathermap.org/data/2.5/weather?q=curepe,tt&APPID=13ceb7203fe9f550a498f8e24d080268&units=metric'
http = urllib3.PoolManager()

class Command(BaseCommand):
    help = 'Uploads new weather data'
    
    def handle(self, *args, **options):
        path = 'C:/Users/Joshua/Desktop/Project/weather(this1)/api/static/weather_images/'
        for file in os.listdir(path):
            line = 'python manage.py upload_img ' + file
            args = shlex.split(line)
            proc = Popen(args)