#!/usr/bin/env python
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(11,GPIO.OUT)

pwm=GPIO.PWM(11,50)

pwm.start(5)

pwm.ChangeDutyCycle(15)
print "Duty15"
time.sleep(1)
pwm.ChangeDutyCycle(3)
print "Duty2"
time.sleep(3)

pwm.stop()
GPIO.cleanup()
