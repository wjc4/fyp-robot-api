#!/usr/bin/env python3
# ========================== IMPORTS ======================
# Import the system modules needed to run rpiMotorlib.py
import time
from .dc_motor import *
# import RPi.GPIO as GPIO

# ==================== CLASS SECTION ===============================

class MotionControl:
    def __init__(self, left_wheel = [7,11,12], right_wheel = [15,13,35]):
        """ init method
        (1) pin_one, type=int,  GPIO pin connected to IN1 or IN3
        (2) Pin two type=int, GPIO pin connected to IN2 or IN4
        (3) pwm_pin type=int, GPIO pin connected to EnA or ENB
        (4) freq in Hz default 100
        (5) verbose, type=bool  type=bool default=False
         help="Write pin actions"
        (6) name, type=string, name attribute
        """
        self.left_wheel = DCMotor(left_wheel[0],left_wheel[1],left_wheel[2])
        self.right_wheel = DCMotor(right_wheel[0],right_wheel[1],right_wheel[2])
        print("motion control intialised")

    # def clockwise(self, duty_cycle=50):
    #     """ Move motor forwards passed duty cycle for speed control """
    #     GPIO.output(self.pin_one, True)
    #     GPIO.output(self.pin_two, False)
    #     if self.verbose:
    #         print("Moving Motor Forward : Duty Cycle = {}".format(duty_cycle))
    #     if duty_cycle != self.last_pwm:
    #         self.my_pwm.ChangeDutyCycle(duty_cycle)
    #         self.last_pwm = duty_cycle
    
    def forward(self, duty_cycle=50):
        """ 
        Move vehicle forward
        Left wheel will turn anticlockwise
        Right wheel will turn clockwise      
        """
        self.left_wheel.set_anticlockwise()
        self.right_wheel.set_clockwise()
        self.left_wheel.accelerate()
        self.right_wheel.accelerate()

    def stop(self):
        """ 
        Move vehicle forward
        Left wheel will turn anticlockwise
        Right wheel will turn clockwise      
        """
        self.left_wheel.stop()
        self.right_wheel.stop()
    
    def reverse(self, duty_cycle=50):
        """ 
        Move vehicle forward
        Left wheel will turn clockwise
        Right wheel will turn anticlockwise      
        """
        self.right_wheel.set_anticlockwise()
        self.left_wheel.set_clockwise()
        self.left_wheel.accelerate()
        self.right_wheel.accelerate()

    def left(self, duty_cycle=10):
        """ 
        Move vehicle forward
        Left wheel will turn clockwise
        Right wheel will turn clockwise      
        """
        self.right_wheel.set_clockwise()
        self.left_wheel.set_clockwise()
        self.left_wheel.accelerate()
        self.right_wheel.accelerate()
    
    def right(self, duty_cycle=10):
        """ 
        Move vehicle forward
        Left wheel will turn anticlockwise
        Right wheel will turn anticlockwise      
        """
        self.right_wheel.set_anticlockwise()
        self.left_wheel.set_anticlockwise()
        self.left_wheel.accelerate()
        self.right_wheel.accelerate()
