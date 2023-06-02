"""
Copyright (C) 2023 . All Rights Reserved. Mechmet Engineers

File : ISR.py

Description : This file contains backend configuration for the interrupt service routine
                integrated with Controller.py

Created on 02-06-2023

Last modified at : 02-06-2023
"""

from __future__ import (unicode_literals)

__author__ = "Ananth T"
__version__ = 0.1

import Jetson.GPIO as io



class GPIO_setup():
   
    def __init__(self,relay_1,relay_2,sensor) -> None:

        self.relay_one = relay_1
        self.relay_two = relay_2
        self.sensor = sensor

        io.setup(self.relay_one,io.OUT,initial=io.LOW)
        io.setup(self.relay_two,io.OUT,initial=io.LOW)
        io.setup(self.sensor,io.input)

        
        io.setwarnings(True)
        io.setmode(io.BCM)

    def readSensor(self):

        return io.input(self.sensor) 
       
       
    def setRelayOne(self,OUTPUT):
        
        if OUTPUT == "HIGH":
            io.output(self.relay_one,io.HIGH)

        else:
            io.output(self.relay_one,io.LOW)


    
    def setRelayTwo(self,OUTPUT):

        if OUTPUT == "HIGH":
            io.output(self.relay_two,io.HIGH)

        else:
            io.output(self.relay_two,io.LOW)

    def setInterruptServiceRotine(self):
        