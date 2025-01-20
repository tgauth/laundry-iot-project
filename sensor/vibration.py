#!/usr/bin/python
# from https://docs.sunfounder.com/projects/umsk/en/latest/05_raspberry_pi/pi_lesson24_vibration_sensor.html

from gpiozero import InputDevice

import requests
import time

# Connect the digital output of the vibration sensor to GPIO17 on the Raspberry Pi
vibration_sensor = InputDevice(17)

# Function to write data to a file
def write_to_file(data, file_path='/var/www/html/dryer_data.txt'):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
    except Exception as e:

count = 0;
# Continuous loop to read from the sensor
#while True:
while count < 120:
    # Check if the sensor is active (no vibration detected)
    dryer_status = "Running" if vibration_sensor.is_active else "Not Running"
    print(f"status: {dryer_status}")
    # Call the function to write data to the file
    write_to_file(dryer_status)
    count += 1    
    # Wait for 1 second before reading the sensor again
    time.sleep(1)
