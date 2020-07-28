import json
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

pinItems = {} 

def load(filename):
    with open(filename, "r") as file:            
        items = json.loads(file.read())

    global  pinItems
    for item in items:
        pin = item["pin"]
        pinItems[item["name"]] = item
        if(item["io"] == "in"):
            GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        if(item["io"] == "out"):
            GPIO.setup(pin, GPIO.OUT)

def In(name):
    global pinItems    
    return GPIO.input(pinItems[name]["pin"])

def Out(name,state):
    global pinItems
    GPIO.output(pinItems[name]["pin"], state)

def cleanup():
    GPIO.cleanup()
