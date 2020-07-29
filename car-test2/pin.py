import json
import RPi.GPIO as GPIO

# set the mode to BCM (according to our GPIO sheet)
GPIO.setmode(GPIO.BCM)
# disable the warnings
GPIO.setwarnings(False)

# the "module" global variable to store the "treasure map" (config.json)
pinItems = {} 

# loading the configuration file
# should be placed in the same folder
def load(filename):
    with open(filename, "r") as file:            
        items = json.loads(file.read())

    # use global to access the global variable in this function
    global  pinItems
    for item in items:
        # number of the pin
        pin = item["pin"]
        # read the complete object {} to the global variable
        pinItems[item["name"]] = item
        if(item["io"] == "in"):
            GPIO.setup(pin, GPIO.IN, pull_up_down = GPIO.PUD_UP)
        if(item["io"] == "out"):
            GPIO.setup(pin, GPIO.OUT)
        if(item["io"] == "pwm"):
            GPIO.setup(pin, GPIO.OUT)
            pinItems[item["name"]]=GPIO.PWM(pin,500)  


# this is how to read a "switch"
def In(name):
    global pinItems    
    return GPIO.input(pinItems[name]["pin"])

# this is to set outputs
def Out(name,state):
    global pinItems
    GPIO.output(pinItems[name]["pin"], state)

# used for pulse width modulation
# meas: any value between low and high
def Level(name, level):
    global pinItems   
    if(level == 0):
        pinItems[name].stop()
    else:
        pinItems[name].start(0)
        pinItems[name].ChangeDutyCycle(level)

# used for cleanup 
def cleanup():
    GPIO.cleanup()
