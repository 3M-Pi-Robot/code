# car test with game

import pin
import time


pin.load("config.json")


queue = [[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]

inN = ["1N1","1N2","1N3","1N4"]

state = 0
position =0
destinationCount = 1024


while (position < destinationCount):
    # perfect place for loop!    
    for i in range(0,4):
        pin.Out(inN[i], queue[state][i])
    
    time.sleep(0.05)
    state+=1
    
    state =state % 4 # super fancy trick ... ;-)
        
    position+=1

pin.cleanup()            
