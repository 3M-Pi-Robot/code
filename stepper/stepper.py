# car test with game

import pin
import time


pin.load("config.json")


queue = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,1,0]]

state = 0
position =0
destinationCount = 1024


while (position < destinationCount):
    pin.Out("1N1", queue[state][0])
    pin.Out("1N2", queue[state][1])
    pin.Out("1N3", queue[state][2])
    pin.Out("1N4", queue[state][3])
    time.sleep(0.005)
    state+=1
    if(state>3):
        state=0
    position+=1

pin.cleanup()            
