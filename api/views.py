from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from django.db.models import Avg, Max, Min
from datetime import timedelta
import datetime
import json

#model imports
from .models import Weather
from .models import WeatherImage
from .models import Archived_data_form


def test_render(request):
    return render(request, 'test_child.html');


#renders home page with corresponding JavaScript, image and highcharts to be used
def index(request):                                             #home page
    max_time = WeatherImage.objects.aggregate(Max('created'))   #select image with the latest time created
    latest = WeatherImage.objects.get(created=max_time['created__max']) #retrieve the filtered image url
    print(latest)
    return render(request, 'weather/home.html', {'latest': latest, 'page_selected': 'home'})


#returns aggregated data for highchart
def chart(request):
    return render(request, 'weather/chart.html', {'past_weather': aggregate()})


#renders gallery view and all images currently present in the database
def gallery(request):
    start = datetime.date.today() - timedelta(days=6)
    img_data = []
    for i in range(0,7):
        filtered_imgs = WeatherImage.objects.filter(created__date=start)
        img_data.append({'date': start, 'imgs': filtered_imgs})
        start += timedelta(days=1)
    return render(request, 'gallery/gallery.html', {'img_data': img_data, 'page_selected': 'gallery'})


#renders image and its corresponding details
def image_details(request, image_id):
    image = get_object_or_404(WeatherImage, pk=image_id)
    return render(request, 'gallery/detail.html', {'image': image, 'page_selected': 'detail'})


#processes archive form request
def archive(request):
    form = Archived_data_form()
    if request.method == 'GET':
        form = Archived_data_form(request.GET)
        if form.is_valid():
            weather_filter = Weather.objects.filter(date__date = request.GET['date']).order_by('-date')
            image_filter = WeatherImage.objects.filter(created__date = request.GET['date']).order_by('-created')
            return render(request, 'weather/archive.html', {'form': form, 'data': weather_filter, 'images': image_filter, 'page_selected': 'archive'})
    return render(request, 'weather/archive.html', {'form': form, 'page_selected': 'archive'})


def show_all(request):                          #displays all weather objects to user Note: only for testing purposes REMOVE
    if request.method == "GET":
        all = Weather.objects.all().values()
        all = list(all)
        all = {'data': all}
        return JsonResponse(all, safe=False)        


def chart_data(request):                                #aggregate and return aggregated json data | add starting day to data
    past_weather = aggregate()

    min_temps = []
    max_temps = []
    hums = []
    press = []
    winds = []

    for i in past_weather:
        min_temps.append(i['temp__min'])
        max_temps.append(i['temp__max'])
        hums.append(i['humidity__avg'])
        press.append(i['pressure__avg'])
        winds.append(i['wind_speed__avg'])

    #data for charts
    chart_data = {
        'Min Temperature': min_temps,
        'Max Temperature': max_temps,
        'Humidity': hums,
        'Wind Speed': winds,
        'Pressure': press
    }
    return JsonResponse(chart_data, safe=False)


#Summarizes data for the past 7 days and returns this collection of data to be rendered onto the web page
def aggregate():                                        
    past_weather = []
    start = datetime.date.today() - timedelta(days=7)
    for i in range(0, 7):
        day = {}

        #aggregated data
        day.update({'date': start})
        day.update(Weather.objects.filter(date__date=start).aggregate(Max('temp')))
        day.update(Weather.objects.filter(date__date=start).aggregate(Min('temp')))
        day.update(Weather.objects.filter(
            date__date=start).aggregate(Avg('pressure')))
        day.update(Weather.objects.filter(
            date__date=start).aggregate(Avg('humidity')))
        day.update(Weather.objects.filter(
            date__date=start).aggregate(Avg('wind_speed')))
        past_weather.append(day)
        start += timedelta(days=1)  # decrement date
    return past_weather
