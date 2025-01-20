#!/usr/bin/python
# from https://docs.sunfounder.com/projects/umsk/en/latest/05_raspberry_pi/pi_lesson24_vibration_sensor.html

from gpiozero import InputDevice

import datetime
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
        print(f"An error occurred: {e}")

prev_state = False;
duration = 0; # will be in minutes
status = "not running"

count = 0;
# Continuous loop to read from the sensor
#while True:
while count < 120:
  # Check if the sensor is active (vibration detected)
  state = vibration_sensor.is_active
  if state:
      status = "running"
  else:
      status = "not running"
      
  if state == prev_state:
      duration += 1
  else:
      duration = 1
      prev_state = state
  
  # Get the current date and time
  now = datetime.datetime.now()
  # Format the timestamp
  timestamp = now.strftime("%Y-%m-%d %h:%M")

  message = f"{timestamp} {status} {duration} minutes"
  write_to_file(message)
    
  count += 1
  #time.sleep(60)
  time.sleep(1)
