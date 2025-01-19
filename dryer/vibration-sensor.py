#!/usr/bin/python
# from https://piddlerintheroot.com/vibration-sensor/
#import RPi.GPIO as GPIO
#import time

#GPIO SETUP
#channel = 17
#GPIO.setmode(GPIO.BCM)
#GPIO.setup(channel, GPIO.IN)

#def callback(channel):
#        if GPIO.input(channel):
#                print("Movement Detected in if!")
#        else:
#                print("Movement Detected in else")

#GPIO.add_event_detect(channel, GPIO.BOTH, bouncetime=300)  # let us know when the pin goes HIGH or LOW
#GPIO.add_event_callback(channel, callback)  # assign function to GPIO PIN, Run function on change

# infinite loop
#try:
#        while True:
#                time.sleep(1)
#except KeyboardInterrupt:
#        print('Interrupted')
from gpiozero import InputDevice
import time

# Connect the digital output of the vibration sensor to GPIO17 on the Raspberry Pi
vibration_sensor = InputDevice(17)

count = 0;
# Continuous loop to read from the sensor
while count < 120:
    # Check if the sensor is active (no vibration detected)
    if vibration_sensor.is_active:
        print("Vibration detected!")
    else:
        # When the sensor is inactive (vibration detected)
        print("...")
    count += 1    
    # Wait for 1 second before reading the sensor again
    time.sleep(1)
