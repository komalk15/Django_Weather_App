from django.shortcuts import render
from django.http import HttpResponse
import requests
import datetime

def home(request):
    if 'city' in request.POST:
        city = request.POST['city']
    else:
        city = 'Dehradun'

    url = 'https://api.openweathermap.org/data/2.5/weather'
    PARAMS = {
        'q': city,
        'appid': 'dd3c35d9d7a23ca8e91f352c6d689cd2',
        'units': 'metric'
    }

    data = requests.get(url, params=PARAMS).json()

    description = data['weather'][0]['description']
    icon = data['weather'][0]['icon']
    temp = data['main']['temp']

    day = datetime.date.today()

    return render(
        request,
        'index.html',
        {
            'description': description,
            'icon': icon,
            'temp': temp,
            'day': day,
            'city': city
        }
    )
