import requests
import configparser
from django.shortcuts import render,redirect
from .models import City
from .forms import CityForm

config_file = r'C:\Users\GP.GP-PC-5001819\Desktop\AskWeather\src\config_file.conf'

config = configparser.ConfigParser()
config.read(config_file)


def index(request):
	url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=metric&appid='+config['API_KEY']['KEY']
	print(url)
	# import pdb
	# pdb.set_trace()
	err_msg = ''
	message = ''
	message_class = ''

	if request.method == 'POST':
		form = CityForm(request.POST)

		if form.is_valid():
			new_city = form.cleaned_data['name']
			existing_city_count = City.objects.filter(name=new_city).count()

			if existing_city_count == 0:
				r = requests.get(url.format(new_city)).json()
				# print(r)
				if r['cod'] == 200:
					form.save()
				else:
					err_msg = "City does not exist"
			else:
				err_msg = "City Already exists"

		if err_msg:
			message = err_msg
			message_class = 'is-danger'
		# else:
		# 	message = 'City added successfully'
		# 	message_class = 'is-success'
	# print(err_msg)

	form = CityForm()

	cities = City.objects.all()
	# print(cities)
	weather_data = []
	
	for city in cities:
		r=requests.get(url.format(city)).json()
		print(r)
		city_weather ={
			'city': city.name,
			'temperature': r['main']['temp'],
			'description': r['weather'][0]['description'],
			'icon': r['weather'][0]['icon'],
		}
		weather_data.append(city_weather)

	context = {
		'weather_data': weather_data,
		'form': form,
		'message': message,
		'message_class':message_class
	}
	return render(request, 'weatherapp/index.html', context)


def delete_city(request, city_name):
	City.objects.get(name=city_name).delete()
	return redirect('home')