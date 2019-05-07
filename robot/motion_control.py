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

    def duty_cycle_calc(self, multiplier, duty_cycle):
        return min(multiplier*duty_cycle, 100)
    
    def forward(self, multiplier=1, duty_cycle=50):
        """ 
        Move vehicle forward
        Left wheel will turn anticlockwise
        Right wheel will turn clockwise      
        """
        duty_cycle = self.duty_cycle_calc(multiplier, duty_cycle)
        self.left_wheel.set_anticlockwise()
        self.right_wheel.set_clockwise()
        self.left_wheel.accelerate(duty_cycle)
        self.right_wheel.accelerate(duty_cycle)

    def stop(self, multiplier=1, duty_cycle=50):
        """ 
        Move vehicle forward
        Left wheel will turn anticlockwise
        Right wheel will turn clockwise      
        """
        self.left_wheel.stop()
        self.right_wheel.stop()
    
    def reverse(self, multiplier=1, duty_cycle=50):
        """ 
        Move vehicle forward
        Left wheel will turn clockwise
        Right wheel will turn anticlockwise      
        """
        duty_cycle = self.duty_cycle_calc(multiplier, duty_cycle)
        self.right_wheel.set_anticlockwise()
        self.left_wheel.set_clockwise()
        self.left_wheel.accelerate(duty_cycle)
        self.right_wheel.accelerate(duty_cycle)

    def left(self, multiplier=1, duty_cycle=50):
        """ 
        Move vehicle forward
        Left wheel will turn clockwise
        Right wheel will turn clockwise      
        """
        duty_cycle = self.duty_cycle_calc(multiplier, duty_cycle)
        self.right_wheel.set_clockwise()
        self.left_wheel.set_clockwise()
        self.left_wheel.accelerate(duty_cycle)
        self.right_wheel.accelerate(duty_cycle)
    
    def right(self, multiplier=1, duty_cycle=50):
        """ 
        Move vehicle forward
        Left wheel will turn anticlockwise
        Right wheel will turn anticlockwise      
        """
        duty_cycle = self.duty_cycle_calc(multiplier, duty_cycle)
        self.right_wheel.set_anticlockwise()
        self.left_wheel.set_anticlockwise()
        self.left_wheel.accelerate(duty_cycle)
        self.right_wheel.accelerate(duty_cycle)

    def steer_forward(self, degree=0, gas=1, multiplier=1, duty_cycle=50):
        ceiling = 50
        floor = 0
        mid = (ceiling+floor)/2
        diff = (ceiling-floor)/2
        bias = diff * degree 
        self.left_wheel.set_anticlockwise()
        self.right_wheel.set_clockwise()
        self.left_wheel.accelerate(mid + bias)
        self.right_wheel.accelerate(mid - bias)

    def steer_reverse(self, degree=0, gas=1, multiplier=1, duty_cycle=50):
        ceiling = 50
        floor = 0
        mid = (ceiling+floor)/2
        diff = (ceiling-floor)/2
        bias = diff * degree 
        self.left_wheel.set_anticlockwise()
        self.right_wheel.set_clockwise()
        self.left_wheel.accelerate(mid + bias)
        self.right_wheel.accelerate(mid - bias)

    def steer_forward_2(self, degree=0, gas=1, multiplier=1, duty_cycle=50):
        duty_cycle = min(duty_cycle*gas*multiplier, 100)
        if degree == 0:
            self.left_wheel.set_anticlockwise()
            self.right_wheel.set_clockwise()
            self.left_wheel.accelerate(duty_cycle)
            self.right_wheel.accelerate(duty_cycle)
        elif degree > 0:
            new_cycle = duty_cycle - ((duty_cycle*2) * abs(degree))
            if new_cycle < 0:
                self.left_wheel.set_clockwise()
            else:
                self.left_wheel.set_anticlockwise()
            self.right_wheel.set_clockwise()
            
            self.left_wheel.accelerate(max(abs(new_cycle),10))
            self.right_wheel.accelerate(duty_cycle)
        else:
            new_cycle = duty_cycle - ((duty_cycle*2) * abs(degree))
            if new_cycle < 0:
                self.right_wheel.set_anticlockwise()
            else:
                self.right_wheel.set_clockwise()
            self.left_wheel.set_anticlockwise()

            self.left_wheel.accelerate(duty_cycle)
            self.right_wheel.accelerate(max(abs(new_cycle),10))

    def steer_reverse_2(self, degree=0, gas=1, multiplier=1, duty_cycle=50):
        duty_cycle = min(duty_cycle*gas*multiplier, 100)
        if degree == 0:
            self.right_wheel.set_anticlockwise()
            self.left_wheel.set_clockwise()
            self.left_wheel.accelerate(duty_cycle)
            self.right_wheel.accelerate(duty_cycle)
        elif degree > 0:
            new_cycle = duty_cycle - ((duty_cycle*2) * abs(degree))
            if new_cycle < 0:
                self.left_wheel.set_anticlockwise()
            else:
                self.left_wheel.set_clockwise()
            self.right_wheel.set_anticlockwise()
            
            self.left_wheel.accelerate(max(abs(new_cycle),10))
            self.right_wheel.accelerate(duty_cycle)
        else:
            new_cycle = duty_cycle - ((duty_cycle*2) * abs(degree))
            if new_cycle < 0:
                self.right_wheel.set_clockwise()
            else:
                self.right_wheel.set_anticlockwise()
            self.left_wheel.set_clockwise()

            self.left_wheel.accelerate(duty_cycle)
            self.right_wheel.accelerate(max(abs(new_cycle),10))