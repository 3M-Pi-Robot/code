# car test

import pin
import time

pin.load("config.json")

pin.Out("ENA",1)
pin.Out("IN1",0)
pin.Out("IN2",1)

time.sleep(5)

pin.cleanup()
