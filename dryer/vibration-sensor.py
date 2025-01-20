#!/usr/bin/python
# from https://docs.sunfounder.com/projects/umsk/en/latest/05_raspberry_pi/pi_lesson24_vibration_sensor.html

from gpiozero import InputDevice

import requests
import time

# Connect the digital output of the vibration sensor to GPIO17 on the Raspberry Pi
vibration_sensor = InputDevice(17)

# URL of the PHP script
php_url = "http://rpi-laundry/request_handler.php"

count = 0;
# Continuous loop to read from the sensor
#while True:
while count < 120:
    # Check if the sensor is active (no vibration detected)
    dryer_status = "Running" if vibration_sensor.is_active else "Not Running"
    print(f"status: {dryer_status}")
    # Send update to the PHP script
    data = {
        'dryer_status': dryer_status
    }
    response = requests.post(php_url, data=data)
    if response.status_code == 200:
        print("Status update sent successfully.")
    else:
        print("Failed to send status update.")
    count += 1    
    # Wait for 1 second before reading the sensor again
    time.sleep(1)
