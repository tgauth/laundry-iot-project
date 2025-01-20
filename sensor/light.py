# from https://www.uugear.com/portfolio/using-light-sensor-module-with-raspberry-pi/
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

# Function to write data to a file
def write_to_file(data, file_path='/var/www/html/washer_data.txt'):
    try:
        with open(file_path, 'w') as file:
            file.write(data)
            print(f"Data written to {file_path} successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")

count = 0;
# Continuous loop to read from the sensor
#while True:
while count < 120:
  # light is off when input is high and light is on when input is low
  status = "Not Running" if GPIO.input(4) else "Running"
  write_to_file(status)
  count += 1
  time.sleep(1)
