import requests
from Klase import *


# def get_IP_adress():
#     URL = "https://api64.ipify.org/?format=json"
#     api_data = requests.get(URL).json()
#     ip_data = api_data["ip"]
#     return ip_data

# def get_location_by_IP_adress():
#     ip_adress = get_IP_adress()
#     URL = f"http://ip-api.com/json/{ip_adress}"
#     response = requests.get(URL)
#     api_data = response.json()
#     location = api_data["city"]
#     return location

    
def retrieve_data_weather():
    URL_1 = f"https://goweather.herokuapp.com/weather/Zagreb"
    URL_2 = f"https://api.open-meteo.com/v1/forecast?latitude=45.81&longitude=15.98&hourly=is_day&current_weather=true&forecast_days=1&timezone=Europe%2FBerlin"
    response_1 = requests.get(URL_1)
    api_data_1 = response_1.json()
    response_2 = requests.get(URL_2)
    api_data_2 = response_2.json()
    temp = api_data_1["temperature"]
    wind = api_data_1["wind"]
    description = api_data_1["description"]
    is_day = api_data_2["current_weather"]["is_day"]
    data = Weather(temp, wind, "Zagreb", description, is_day) #description Sunny, Partly cloudy, Clear, Rain, light rain, Cloudy
    return data











