# from https://www.uugear.com/portfolio/using-light-sensor-module-with-raspberry-pi/
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
GPIO.setup(4,GPIO.IN)

count = 0
while count < 120:
  if GPIO.input(4):
    print("TRUE")
  else:
    print("FALSE")
  count += 1
  time.sleep(1)
