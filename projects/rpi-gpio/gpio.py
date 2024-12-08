from time import sleep

import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

GPIO.setup(20, GPIO.OUT)
GPIO.setup(26, GPIO.IN)

GPIO.output(20, GPIO.HIGH)

v_26 = GPIO.input(26)
print(f'Pin 26 value: {v_26}')

GPIO.cleanup()
