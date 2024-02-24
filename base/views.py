from django.shortcuts import render
import urllib.request
import json

def home(request):
    if request.method == 'POST':  # Corrected this line
        city = request.POST['city']
        source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q='+city+'&units=metric&appid=312b5d1605ea1f1bd2f536306b8d3d1c').read()
        list_of_data = json.loads(source)

        data ={
            'country_code': str(list_of_data['sys']['country']),
            'cor': str(list_of_data["coord"]["lon"]) + " " + str(list_of_data["coord"]["lat"]),
            'temp': str(list_of_data["main"]['temp']),
            'pressure': str(list_of_data['main']["pressure"]),
            'humidity': str(list_of_data['main']['humidity']),
            'main': str(list_of_data["weather"][0]['main']),
            'description': str(list_of_data["weather"][0]['description']),
            'icon': list_of_data["weather"][0]['icon'],
            'city': city
        }
    else:
        data = {}
    return render(request, 'base/index.html', data)
