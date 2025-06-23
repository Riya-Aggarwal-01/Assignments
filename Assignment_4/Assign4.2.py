# api.openweathermap.org/data/2.5/forecast?q=jaipur&appid=7bc0e9d6552a10e787ed494a3693f0e1&unit=metric

# This script fetches 5-day (3-hour interval) weather forecast for a city
# and saves it to a CSV file viewable in Excel.

import csv
import requests

def forecast_to_csv(city):
    api = "7bc0e9d6552a10e787ed494a3693f0e1"
    url = f"https://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api}&units=metric"
    try:
        response=requests.get(url)
        response.raise_for_status()
        data = response.json()

        file = f"{city.lower()}_forecast.csv"
        with open(file,'w',newline="") as f:
            writer = csv.writer(f)

            writer.writerow([
            "Date & Time", "Temp (°C)", "Feels Like (°C)", "Min Temp (°C)", "Max Temp (°C)",
            "Weather", "Humidity (%)"
            ])

            for cast in data["list"]:
                dt_txt=cast["dt_txt"]
                temp = cast["main"]["temp"]
                feels_like = cast["main"]["feels_like"]
                temp_min = cast["main"]["temp_min"]
                temp_max = cast["main"]["temp_max"]
                description = cast["weather"][0]["description"]
                humidity = cast["main"]["humidity"]

                writer.writerow([
                   dt_txt, temp, feels_like, temp_min, temp_max,
                   description, humidity
                ])
        print("Forecast saved successfully to ",{file})
    except requests.exceptions.RequestException as e:
        print(f"Error : {e}")

city = input("Enter city name: ")
forecast_to_csv(city)







