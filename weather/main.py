from datetime import datetime

import pytz
import requests


def parse_date(date: str) -> str:
    date_obj = datetime.strptime(date, "%Y-%m-%dT%H:%M")

    utc_date_obj = date_obj.replace(tzinfo=pytz.utc)

    bogota_tz = pytz.timezone("America/Bogota")
    bogota_date_obj = utc_date_obj.astimezone(bogota_tz)

    return bogota_date_obj.strftime("%B %d, %Y at %I:%M %p %Z")


city = input("Enter city name: ")

coordinatesResponse = requests.get(
    f"https://nominatim.openstreetmap.org/search?q={city}&format=json&limit=1"
)

coordinates = coordinatesResponse.json()

latitude = coordinates[0]["lat"]
longitude = coordinates[0]["lon"]

response = requests.get(
    f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m,wind_speed_10m&hourly=temperature_2m,relative_humidity_2m,wind_speed_10m"
)

data = response.json()

temperature = data["current"]["temperature_2m"]
time = data["current"]["time"]

print(
    "The temperature in",
    city,
    "is",
    temperature,
    "°C",
    "and the time is",
    parse_date(time),
)
