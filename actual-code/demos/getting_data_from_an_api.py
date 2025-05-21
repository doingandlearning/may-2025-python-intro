import requests
import csv

url = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 46.2,
    "longitude": 6.1,
    "hourly": "temperature_2m",
    "timezone": "Europe/Zurich"
}

response = requests.get(url, params=params)
data = response.json()

times = data["hourly"]["time"]
temps = data["hourly"]["temperature_2m"]

weather_data = list(zip(times, temps))

with open("weather.csv", "w") as file:
    writer = csv.writer(file)
    writer.writerow(["Date/Time", "Temperture(c)"])
    for data in weather_data:
        writer.writerow(data)

# https://google.com?q=cern&origin=geneva