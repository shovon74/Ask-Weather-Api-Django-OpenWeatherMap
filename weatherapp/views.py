import requests
from django.shortcuts import render


def index(request):

	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=e2982aab2c245465921e2cde7c21cc4e'

	city = 'Dhaka'

	r=requests.get(url.format(city)).json()
	# print(r)

	city_weather ={
		'city': city,
		'temparature': r['main']['temp'],
		'description':r['weather'][0]['description'],
		'icon': r['weather'][0]['icon'],
	}

	# print(city_weather)
	context = {'city_weather': city_weather}
	return render(request, 'weatherapp/index.html', context)

# Create your views here.
