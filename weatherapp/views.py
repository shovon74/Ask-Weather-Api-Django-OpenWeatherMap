import requests
from django.shortcuts import render
from .models import City
from .forms import CityForm

def index(request):

	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid=e2982aab2c245465921e2cde7c21cc4e'


	if request.method == 'POST':
		form = CityForm(request.POST)
		form.save()

	form = CityForm()

	cities = City.objects.all()

	weather_data = []
	
	for city in cities:
		r=requests.get(url.format(city)).json()
		

		city_weather ={
			'city': city.name,
			'temparature': r['main']['temp'],
			'description':r['weather'][0]['description'],
			'icon': r['weather'][0]['icon'],
		}
		weather_data.append(city_weather)



	print(weather_data)
	context = {'weather_data': weather_data, 'form': form}
	print(context)
	return render(request, 'weatherapp/index.html', context)

# Create your views here.
