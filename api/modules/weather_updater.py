from api.models import Weather
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
            new_weather = Weather()
            
            # open weather map gives temps in Kelvin. We want celsius.              
            temp_in_celsius = json['main']['temp'] - 273.15
            new_weather.temp = temp_in_celsius
            new_weather.city = json['name']
            new_weather.save()
            print("saving...\n" + new_weather)
        except:
            pass