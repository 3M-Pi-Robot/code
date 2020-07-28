import RPi.GPIO as GPIO
import time


leds = [2, 3, 4, 17, 27]
switches = [14, 15]

GPIO.setmode(GPIO.BCM)

#init
for led in leds:
    GPIO.setup(led,GPIO.OUT)
    GPIO.output(led,GPIO.LOW)

for switch in switches:    
    GPIO.setup(switch, GPIO.IN, pull_up_down=GPIO.PUD_UP)

i=0
while i <30:
    for led in leds:
        GPIO.output(led,GPIO.LOW)
    
    # check status
    status1 = GPIO.input(switches[0])
    status2 = GPIO.input(switches[1])
    
    # switches
    if status1==0:
        GPIO.output(leds[0],GPIO.HIGH)
        GPIO.output(leds[1],GPIO.LOW)
        GPIO.output(leds[2],GPIO.HIGH)
        GPIO.output(leds[3],GPIO.LOW)
        GPIO.output(leds[4],GPIO.HIGH)
    elif status2==0:
        GPIO.output(leds[0],GPIO.LOW)
        GPIO.output(leds[1],GPIO.HIGH)
        GPIO.output(leds[2],GPIO.LOW)
        GPIO.output(leds[3],GPIO.HIGH)
        GPIO.output(leds[4],GPIO.LOW)
    else:    
        for led in leds:
            GPIO.output(led,GPIO.HIGH)
            time.sleep(0.5)
            GPIO.output(led,GPIO.LOW)
        i+=1


GPIO.cleanup()
