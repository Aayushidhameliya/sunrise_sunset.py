import requests
from datetime import datetime

MY_LAT = 20.593683
MY_LONG = 78.962883
parameter = {"lat": MY_LAT, "lng": MY_LONG, "formatted": 0,}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameter)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunset)
print(sunrise)
time_now = datetime.now()
print(time_now.hour)