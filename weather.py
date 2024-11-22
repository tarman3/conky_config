#!/usr/bin/env python
# -*- coding: utf-8 -*-

# ------------------------- Истоник данных -----------------------------

# https://open-meteo.com/en/docs#latitude=51.863&longitude=33.4698&current=temperature_2m&minutely_15=&hourly=&timezone=Europe%2FMoscow&forecast_days=1


# ------------------------- Импорт библиотек ---------------------------

import requests
from datetime import datetime, timedelta
import re

# ---------------------------- Параметры -------------------------------

url_api = 'https://api.open-meteo.com/v1/forecast?latitude=51.863&longitude=33.4698&current=temperature_2m,relative_humidity_2m,apparent_temperature,is_day,precipitation,rain,showers,snowfall,weather_code,cloud_cover,pressure_msl,surface_pressure,wind_speed_10m,wind_direction_10m,wind_gusts_10m&hourly=temperature_2m&timezone=Europe%2FMoscow&forecast_days=2'

# ----------------------------- Сенарий --------------------------------

def future_temp(hour):
    next_temp = data["hourly"]["temperature_2m"][hour]
    return round(next_temp)

now = datetime.now()

request_string = f'{url_api}'#?since={since}&page=1'
#print(request_string,'\n')

try:
    data = requests.get(request_string, timeout=5).json()
    # print(len(data))
except Exception:
    data = None
    exit()

hPa2mmHg = 0.75006375541921
current_temp = data["current"]["temperature_2m"]
relative_humidity = data["current"]["relative_humidity_2m"]
surface_pressure = data["current"]["surface_pressure"] * hPa2mmHg
# pressure_msl = data["current"]["pressure_msl"] * hPa2mmHg
wind_speed = data["current"]["wind_speed_10m"]
wind_direction = data["current"]["wind_direction_10m"]

if   (wind_direction > 360-22.5)  or (wind_direction <     22.5): wd = 'N'
elif (wind_direction >     22.5) and (wind_direction <  90-22.5): wd = 'NE'
elif (wind_direction >  90-22.5) and (wind_direction <  90+22.5): wd = 'E'
elif (wind_direction >  90+22.5) and (wind_direction < 180-22.5): wd = 'SE'
elif (wind_direction > 180-22.5) and (wind_direction < 180+22.5): wd = 'S'
elif (wind_direction > 180+22.5) and (wind_direction < 270-22.5): wd = 'SW'
elif (wind_direction > 270-22.5) and (wind_direction < 270+22.5): wd = 'W'
elif (wind_direction > 270+22.5) and (wind_direction < 360-22.5): wd = 'NW'

output = f'{current_temp}°C {future_temp(now.hour+6)} {future_temp(now.hour+12)} {future_temp(now.hour+18)}  {relative_humidity}%  {int(surface_pressure)}mmHg  {wd}{round(wind_speed)}km/h'
print(output)
