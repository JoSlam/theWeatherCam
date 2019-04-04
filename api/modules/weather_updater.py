from api.models import Weather, City
import requests



def get_weather_json():
    url = 'http://api.openweathermap.org/data/2.5/weather'
    search_type = "q"
    search_params = "curepe,tt"
    access_token ='13ceb7203fe9f550a498f8e24d080268'
    units = 'metric'
    search_area = '#find city_id from list based on name & country code'

    #go with city name and or country code, city id and lon & lat

    url += "?" + search_type + "=" + search_params + "&APPID=" + access_token + "&units=" + units
    req = requests.get(url)

    try:
        req.raise_for_status()
        return req.json()
    except:
        return None

      
def update_forecast():
    json = get_weather_json()
    if json is not None:
        try:
            city = None
            city = City.objects.get(city_id=json['id'])

            new_weather = Weather()
            new_weather.temp = json['main']['temp'] - 273.15
            new_weather.wind_speed = json['wind']['speed']
            new_weather.humidity = json['main']['humidity']
            new_weather.pressure = json['main']['pressure']
            new_weather.city = city 
            new_weather.save()
            print("saving...", new_weather)
            return new_weather
        except Exception as e:
            print("Error: ", e)
            return None