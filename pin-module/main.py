import pin
import time

pin.load("config.json")
pin.Out("LED1",1)
pin.Out("LED2",1)
pin.Out("LED3",1)
pin.Out("LED4",1)
pin.Out("LED5",1)
time.sleep(5)
pin.cleanup()
        
