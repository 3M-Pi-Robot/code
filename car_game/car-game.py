# car test with game

import pin
import time
import sys, pygame
from  pygame.locals import *

pygame.init()

ena=0
enb=0

trimfactor_ena = 1.01
trimfactor_enb = 1.01

pin.load("config.json")

size = width, height =600,400
screen = pygame.display.set_mode(size)

while True:
    time.sleep(0.1)
    for event in pygame.event.get():
        if event.type == KEYDOWN and event.key == K_ESCAPE:
            pin.Level("ENA",0)
            pin.Level("ENB",0)
            pin.cleanup()
            pygame.display.quit()
            sys.exit
        elif event.type == KEYDOWN and event.key == K_w: # foreward
            print("w - foreward")
            ena +=15
            enb +=15
        elif event.type == KEYDOWN and event.key == K_s: # backward
            print("s - backward")
            ena -=15
            enb -=15
        elif event.type == KEYDOWN and event.key == K_a: # left
            print("a-left")
            ena +=5
            enb -=5
        elif event.type == KEYDOWN and event.key == K_d: # right
            print("d-right")
            ena -=5
            enb +=5
        elif event.type == KEYDOWN:
            ena=0
            enb=0

        # set the motor speed    
        if(ena>=0):            
            ena_trim=ena*trimfactor_ena
            ena_trim = min(ena_trim, 100)
            pin.Level("ENA",ena_trim)
            pin.Out("IN1",0)
            pin.Out("IN2",1)
        else:
            ena_minus = abs(ena) 
            ena_minus = min(ena_minus, 100)
            pin.Level("ENA",ena_minus)
            pin.Out("IN1",1)
            pin.Out("IN2",0)
        if(enb>=0):
            enb = min(enb, 100)
            pin.Level("ENB",enb)
            pin.Out("IN3",1)
            pin.Out("IN4",0)
        else:
            enb_minus = abs(enb)
            ena_minus *= trimfactor_enb
            enb_minus = min(enb_minus, 100)
            pin.Level("ENB",enb_minus)
            pin.Out("IN3",0)
            pin.Out("IN4",1)
       


