from django.core.management.base import BaseCommand, CommandError
from api.models import WeatherImage
from datetime import datetime
import os

class Command(BaseCommand):
    help = 'Uploads new image url'
    
    def add_arguments(self, parser):
        parser.add_argument('name', type=str)

    def handle(self, *args, **options):
        name = options['name']
        url, ext = os.path.splitext(name)
        date_created = datetime.strptime(url, "%d-%m-%Y-%H-%M")
        new_image = WeatherImage(created=date_created, url=name)
        new_image.save()
        print(new_image)


    # def log_images(self):
    #     path = '../static/weather_images/'
    #     oldprefix = '.JPG'
    #     for file in os.listdir(path):
    #         print(file)


    #          if file.startswith(oldprefix):
    #              os.rename(file, file.replace(oldprefix, '.jpg', 1))