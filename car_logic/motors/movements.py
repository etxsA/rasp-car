from typing import List
from time import sleep

import RPi.GPIO as GPIO
from car_logic import setGPIO as sg

class MovementController:

    WAIT_TIME = 0.5 

    def __init__(self,
                  ENA:int=32, IN1:int=35, IN2:int=37,
                  ENB:int=40, IN3:int=36, IN4:int=38, p:bool=True) -> None:
        """Constructor Setup GPIO for movement to work

        Args:
            ENA (int, optional): Enable pin for Motor 1. Defaults to 32.
            IN1 (int, optional): IN1 pin for Motor 1. Defaults to 35.
            IN2 (int, optional): IN2 pin for Motor 1. Defaults to 37.
            ENB (int, optional): Enable pin for Motor 2. Defaults to 40.
            IN3 (int, optional): IN3 pin for Motor 2. Defaults to 36.
            IN4 (int, optional): IN4 pin for motor 2. Defaults to 38.
            p (bool, optional): If True prints procedure. Defaults to True.

        Raises:
            Exception: In case that setup fails
        """
        self.p: bool = p
        self.pins: List[int] = [ENA, IN1, IN2, ENB, IN3, IN4]; 

        sg.setGPIOmode(self.p)
        if(sg.setPinsAsOut(self.pins, self.p)):
            if(self.p):
                print("Movement Controller Created Successfully")
        else :
            raise Exception("Couldn't config movement controller"); 
    
    def __del__(self):
        if(self.p):
            print("Movement Controller Destroyed !!")
        # Just make GPIO CleanUp
        GPIO.cleanup()

    def foward(self, time=WAIT_TIME) -> None:
        """Sets pins to move foward

        Args:
            time (float, optional): Wait time at the of setting pins. Defaults to 0.5.
        """
        sg.setOutput(self.pins, [1,1,0,1,1,0]);

        if(self.p):
            print("Moving Foward")

        sleep(time)
        return 
    
    def backwards(self, time=WAIT_TIME) -> None:
        """Sets pins to move backwards

        Args:
            time (float, optional): Wait time at the of setting pins. Defaults to 0.5.
        """
        sg.setOutput(self.pins, [1,0,1,1,0,1])
        
        if(self.p):
            print("Moving Backwards")

        sleep(time)
        return 
    
    def right(self, time=WAIT_TIME) -> None:
        """Sets pins to move right(Relative to Motor A-Right)

        Args:
            time (float, optional): Wait time at the of setting pins. Defaults to 0.5.
        """
        sg.setOutput(self.pins, [1,1,0,0,0,0])
        
        if(self.p):
            print("Moving Right")
        sleep(time)
        return 
    
    def left(self, time=WAIT_TIME) -> None:
        """Sets pins to move left(Relative to Motor A-Right)

        Args:
            time (float, optional): Wait time at the of setting pins. Defaults to 0.5.
        """
        sg.setOutput(self.pins, [0,0,0,1,1,0])
        
        if(self.p):
            print("Moving Left")

        sleep(time)
        return 
    
    def spinRight(self, time=WAIT_TIME) -> None:
        """Sets pins to spin to the right(Relative to Motor A-Right)

        Args:
            time (float, optional): Wait time at the of setting pins. Defaults to 0.5.
        """
        sg.setOutput(self.pins, [1,1,0,1,0,1])
        
        if(self.p):
            print("Spinning Right")
        sleep(time)
        return 
    
    def spinLeft(self, time=WAIT_TIME) -> None:
        """Sets pins to spin to the left(Relative to Motor A-Right)

        Args:
            time (float, optional): Wait time at the of setting pins. Defaults to 0.5.
        """
        sg.setOutput(self.pins, [1,0,1,1,1,0])
        
        if(self.p):
            print("Spinning Left")
        sleep(time)
        return 
    
    def stop(self, time=WAIT_TIME) -> None:
        """Sets pins to execute a stop

        Args:
            time (float, optional): Wait time at the of setting pins. Defaults to 0.5.
        """
        sg.setOutput(self.pins, [0,0,0,0,0,0])
        if(self.p):
            print("Stopping")
        sleep(time)
        return 





