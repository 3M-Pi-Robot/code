# car test

import pin
import time

pin.load("config.json")

time.sleep(1) # for taking a video...

# set to zero
pin.Level("ENA",0)
pin.Level("ENB",0)

pin.Level("ENA",60)
pin.Out("IN1",0)
pin.Out("IN2",1)

time.sleep(1)
pin.Level("ENA",0)


time.sleep(0.5)

pin.Level("ENB",50)
pin.Out("IN3",1)
pin.Out("IN4",0)

time.sleep(1)
pin.Level("ENB",0)

pin.cleanup()
