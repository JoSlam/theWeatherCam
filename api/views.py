import datetime
import json
import decimal

from datetime import timedelta

from django.db.models import Avg, Max, Min
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_http_methods
from django.views.generic import View

#doc model imports
from .docModels import CityUploadDoc
#doc forms imports
from .forms import ArchivedDataForm, CityUploadForm
#model imports
from .models import City, Weather, WeatherImage
#module imports
from .modules import weather_updater


#renders home page with corresponding JavaScript, image and highcharts to be used
def index(request):                                             #home page
    try:
        latest = WeatherImage.objects.latest('created')
    except:
        latest = None

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
    form = ArchivedDataForm()
    if request.method == 'GET':
        form = ArchivedDataForm(request.GET)
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



class CityUploadView(View):
    template_name = 'upload/upload_cities.html'
    form_class = CityUploadForm

    def createCity(self, city_id, name, country, longitude, latitude):
        new_city, created = City.objects.get_or_create(
            city_id = city_id,
            defaults = {
                "name": name,
                "country": country,
                "longitude": longitude,
                "latitude": latitude
            }
        )
        return {
            'id': new_city.city_id,
             'name': new_city.name,
             'country': new_city.country,
             'created': created
             }

    def get(self, request):
        city_upload_form = self.form_class(None)
        return render(request, self.template_name, {'form': city_upload_form})


    def post(self, request):
        city_upload_form = self.form_class(request.POST, request.FILES)
        context = {
            "form": city_upload_form,
            "formSubmitted": 1
        }

        if city_upload_form.is_valid():
            doc_before_save = city_upload_form.save(commit=False)
            city_upload_form.save()
            with open(str(doc_before_save.document), 'r', encoding='utf-8') as city_file:
                city_file_json_data = json.load(city_file)
                city_list = list(map(lambda city_info: self.createCity(city_info['id'], city_info['name'], city_info['country'], city_info['coord']['lon'], city_info['coord']['lat']), city_file_json_data))
                context.update({"cityList": city_list})
        return render(request, self.template_name, context)




def show_weather(request):
    response = weather_updater.get_weather_json()
    print(response)
    return JsonResponse(response, json_dumps_params={'indent': 2})

def update_weather(request):
    res = weather_updater.update_forecast()
    print(res)
    return HttpResponse("hi")

def latest_update(request):
    latest_forecast = Weather.objects.latest('date')
    print(latest_forecast)
    city = latest_forecast.city.name
    temperature_in_c = latest_forecast.temp
    temperature_in_k = latest_forecast.temp + 273.15
    timestamp = "{t.year}/{t.month:02d}/{t.day:02d} - {t.hour:02d}:{t.minute:02d}:{t.second:02d}".format( t=latest_forecast.date)

    context = {
        'city':city,
        'temperature_in_c': temperature_in_c,
        'temperature_in_k': round(temperature_in_k,2),
        'utc_update_time': timestamp
        }
    return render(request, 'weather/latest_update.html', context)