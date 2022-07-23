
# AskWeather

This web app is capable of showing current temperature and a little description of the present weather. This is an integration of OpenWeatherMapApi using Django.

## Screenshots

![Screenshot](https://user-images.githubusercontent.com/25238920/180603717-f19e0559-e2bb-4a41-8afe-6543664d169a.png)

## Requirments

The following are required to run this site in development

* [Python](https://www.python.org/downloads/release/python-374/)
* [Django](https://docs.djangoproject.com/en/4.0/releases/2.2/)
* [OpenWeatherMapApi](https://openweathermap.org/)

## Run Locally
[Install Python Locally](https://realpython.com/installing-python/) 

Make a project directory

```bash
    mkdir <directory_name>
```

Go to the project directory

```bash
  cd <directory_name>
```

Install a virtual environment

```bash
  python -m venv <venv_name>
```
Activate the virtual environment

```bash
  <venv_name>\Scripts\activate # Windows
  source <venv_name>/bin/activate # Linux or Mac

```
Clone the project

```bash
  git clone https://github.com/shovon74/Ask-Weather-Api-Django-OpenWeatherMap.git
```
Go to the cloned directory

```bash
  cd Ask-Weather-Api-Django-OpenWeatherMap
```

Install dependencies

```bash
  pip install requirement.txt
```

Modify config file path

```
In views.py change the <config_file_path> as per local system
```
Modify API key

Pick an API key from [OpenWeatherMapApi](https://openweathermap.org/api)

```
Update API_KEY in config_file.conf file
```

Start the server

```bash
  python manage.py runserver 127.0.0.1:8000
```

