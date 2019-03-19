# pin 7 ain1
# pin 11 ain2
# pin 12 pwma

import time
import RPi.GPIO as GPIO

# Declare the GPIO settings
GPIO.setmode(GPIO.BOARD)

PWMA = 12
AIN1 = 7
AIN2 = 11
PWMB = 35
BIN2 = 13
BIN1 = 15

# set up GPIO pins
GPIO.setup(PWMA, GPIO.OUT) # Connected to PWMA
GPIO.setup(AIN2, GPIO.OUT) # Connected to AIN2
GPIO.setup(AIN1, GPIO.OUT) # Connected to AIN1

# Drive the motor clockwise
GPIO.output(AIN1, GPIO.HIGH) # Set AIN1
GPIO.output(AIN2, GPIO.LOW) # Set AIN2

# Set the motor speed
# GPIO.output(PWMA, GPIO.HIGH) # Set PWMA
p1 = GPIO.PWM(PWMA, 100)
p1.start(0)
time.sleep(3)
p1.ChangeDutyCycle(50)       
time.sleep(3)
p1.ChangeDutyCycle(100)       

# Wait 5 seconds
time.sleep(3)

# # Reset all the GPIO pins by setting them to LOW
GPIO.output(AIN1, GPIO.LOW) # Set AIN1
GPIO.output(AIN2, GPIO.LOW) # Set AIN2
GPIO.output(PWMA, GPIO.LOW) # Set PWMA



# set up GPIO pins
GPIO.setup(PWMB, GPIO.OUT) # Connected to PWMA
GPIO.setup(BIN2, GPIO.OUT) # Connected to AIN2
GPIO.setup(BIN1, GPIO.OUT) # Connected to AIN1

# Drive the motor clockwise
GPIO.output(BIN1, GPIO.HIGH) # Set AIN1
GPIO.output(BIN2, GPIO.LOW) # Set AIN2

# Set the motor speed
# GPIO.output(PWMA, GPIO.HIGH) # Set PWMA
p1 = GPIO.PWM(PWMB, 100)
p1.start(0)
time.sleep(3)
p1.ChangeDutyCycle(50)       
time.sleep(3)
p1.ChangeDutyCycle(100)       

# Wait 5 seconds
time.sleep(3)

# # Reset all the GPIO pins by setting them to LOW
GPIO.output(BIN1, GPIO.LOW) # Set AIN1
GPIO.output(BIN2, GPIO.LOW) # Set AIN2
GPIO.output(PWMB, GPIO.LOW) # Set PWMA




GPIO.cleanup()