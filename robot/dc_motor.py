#!/usr/bin/env python3
# ========================== IMPORTS ======================
# Import the system modules needed to run rpiMotorlib.py
import time
import RPi.GPIO as GPIO

# ==================== CLASS SECTION ===============================

class DCMotor:

    def __init__(self, pin_one, pin_two,
                 pwm_pin, freq=100, verbose=False, name="DCMotor"):
        """ init method
        (1) pin_one, type=int,  GPIO pin connected to IN1 or IN3
        (2) Pin two type=int, GPIO pin connected to IN2 or IN4
        (3) pwm_pin type=int, GPIO pin connected to EnA or ENB
        (4) freq in Hz default 100
        (5) verbose, type=bool  type=bool default=False
         help="Write pin actions"
        (6) name, type=string, name attribute
        """
        self.name = name
        self.pin_one = pin_one
        self.pin_two = pin_two
        self.pwm_pin = pwm_pin
        self.freq = freq
        self.verbose = verbose

        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(self.pin_one, GPIO.OUT)
        GPIO.setup(self.pin_two, GPIO.OUT)
        GPIO.setup(self.pwm_pin, GPIO.OUT)

        self.my_pwm = GPIO.PWM(self.pwm_pin, self.freq)
        self.last_pwm = 0
        self.my_pwm.start(self.last_pwm)
        if self.verbose:
            print(" Motor initialized named: {} ".format(self.name))
            print(" Pin one In1 or In3:  {}".format(self.pin_one))
            print(" Pin two In2 or in4:  {}".format(self.pin_two))
            print(" Pin pwm enA or enB:  {}".format(self.pwm_pin))
            print(" Frequency: {} ".format(self.freq))

    def clockwise(self, duty_cycle=50):
        """ Move motor forwards passed duty cycle for speed control """
        GPIO.output(self.pin_one, True)
        GPIO.output(self.pin_two, False)
        if self.verbose:
            print("Moving Motor Forward : Duty Cycle = {}".format(duty_cycle))
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def anticlockwise(self, duty_cycle=50):
        """ Move motor backwards passed duty cycle for speed control"""
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, True)
        if self.verbose:
            print("Moving Motor Backward : Duty Cycle = {}".format(duty_cycle))
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def stop(self, duty_cycle=0):
        """ Stop motor"""
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, False)
        if self.verbose:
            print("Stoping Motor : Duty Cycle = {}".format(duty_cycle))
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def brake(self, duty_cycle=100):
        """ brake motor"""
        GPIO.output(self.pin_one, True)
        GPIO.output(self.pin_two, True)
        if self.verbose:
            print("Braking Motor : Duty Cycle = {}".format(duty_cycle))
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle

    def cleanup(self, clean_up=False):
        """ cleanup all GPIO connections used in event of error by lib user"""
        if self.verbose:
            print("rpi_dc_lib.py : Cleaning up")
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, False)
        self.my_pwm.ChangeDutyCycle(0)
        if clean_up:
            GPIO.cleanup()

    def set_clockwise(self):
        """ Move motor forwards passed duty cycle for speed control """
        GPIO.output(self.pin_one, True)
        GPIO.output(self.pin_two, False)

    def set_anticlockwise(self):
        """ Move motor backwards passed duty cycle for speed control"""
        GPIO.output(self.pin_one, False)
        GPIO.output(self.pin_two, True)
    
    def accelerate(self, duty_cycle=50):
        """ Move motor backwards passed duty cycle for speed control"""
        if self.verbose:
            print("Moving Motor: Duty Cycle = {}".format(duty_cycle))
        if duty_cycle != self.last_pwm:
            self.my_pwm.ChangeDutyCycle(duty_cycle)
            self.last_pwm = duty_cycle
        