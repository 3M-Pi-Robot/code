import RPi.GPIO as GPIO
import time


leds = [2,3,4,17,27]

GPIO.setmode(GPIO.BCM)

for led in leds:
    GPIO.setup(led,GPIO.OUT)
    GPIO.output(led,GPIO.LOW)

i=0
while i <30:
    for led in leds:
        GPIO.output(led,GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(led,GPIO.LOW)
    i+=1 # i = i + 1

GPIO.cleanup()
