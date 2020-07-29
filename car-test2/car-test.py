# car test

import pin
import time

pin.load("config.json")

time.sleep(4) # for taking a video...

# set to zero
pin.Out("ENA",0)
pin.Out("ENB",0)

pin.Out("ENA",1)
pin.Out("IN1",0)
pin.Out("IN2",1)

time.sleep(1)
pin.Out("ENA",0)


time.sleep(0.5)

pin.Out("ENB",1)
pin.Out("IN3",1)
pin.Out("IN4",0)

time.sleep(1)
pin.Out("ENB",0)

pin.cleanup()
