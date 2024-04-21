#!/usr/.venv/bme280/bin/env python

import time
import datetime

from smbus2 import SMBus
from bme280 import BME280

print(
    """all-values.py - Read temperature, pressure, and humidity

Press Ctrl+C to exit!

"""
)

# Initialise the BME280
bus = SMBus(1)
bme280 = BME280(i2c_dev=bus)
bme280.setup(mode="forced")
bme280.setup(temperature_oversampling = 1, pressure_oversampling = 1, humidity_oversampling = 1)


while True:
    temperature = bme280.get_temperature()
    pressure = bme280.get_pressure()
    humidity = bme280.get_humidity()
    print(f"{temperature:05.2f}°C {pressure:05.2f}hPa {humidity:05.2f}%")
    now = datetime.datetime.now()
    with open("temp_data.csv", 'a') as file:
        file.write(f"{temperature:05.2f}°C,{pressure:05.2f}hPa,{humidity:05.2f}%,{now.strftime('%d-%m-%Y')}\n")
    time.sleep(10*60)
