# from https://www.uugear.com/portfolio/using-light-sensor-module-with-raspberry-pi/
import RPi.GPIO as GPIO

import datetime
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

# Function to write data to a file
def write_to_file(data, file_path='/var/www/html/washer_data.txt'):
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
  # light is off when input is high and light is on when input is low
  state = GPIO.input(4)
  if state:
      status = "not running"
  else:
      status = "running"
      
  if state == prev_state:
      duration += 1
  else:
      duration = 1
      prev_state = state
  
  # Get the current date and time
  now = datetime.datetime.now()
  # Format the timestamp
  timestamp = now.strftime("%Y-%m-%d %H:%M")

  message = f"{timestamp} {status} {duration}"
  write_to_file(message)
    
  count += 1
  #time.sleep(60)
  time.sleep(1)
