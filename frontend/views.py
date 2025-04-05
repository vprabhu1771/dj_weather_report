# from django.shortcuts import render

import os

# Create your views here.
# def home(request):
#     port = os.getenv('PORT', 9000)
#     print(port)
#     return render(request,'frontend/home.html')

from django.shortcuts import render
from dotenv import load_dotenv

load_dotenv()  # take environment variables

# Access the variables
API_KEY = os.getenv('API_KEY')

def home(request):
    import requests
    import json

    if request.method == 'POST':

        location = request.POST['location']

        print(location)

        url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query=" + location

        weather_request = requests.get(url)
        weather_api = json.loads(weather_request.text)

        print(weather_api)
        return render(request, "frontend/home.html", {'weather_api': weather_api})

    else:

        url = f"http://api.weatherstack.com/current?access_key={API_KEY}&query=New%20York"

        weather_request = requests.get(url)
        weather_api = json.loads(weather_request.text)

        return render(request, "frontend/home.html", {'weather_api': weather_api})