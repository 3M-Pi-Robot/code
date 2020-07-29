import pin
import time

pin.load("config2.json")

# everything ON
pin.Out("LED1",1)
pin.Out("LED2",1)
pin.Out("LED3",1)
pin.Out("LED4",1)

time.sleep(2)

# everything OFF
pin.Out("LED1",0)
pin.Out("LED2",0)
pin.Out("LED3",0)
pin.Out("LED4",0)

time.sleep(0.2)

# dim the LED5
for i in range(0,100):
    time.sleep(0.02)
    pin.Level("LED5",i)

for i in range(100,0,-1):
    time.sleep(0.02)
    pin.Level("LED5",i)   

# cleanup
pin.cleanup()
        
