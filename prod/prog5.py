#!/usr/bin/env python
from gpiozero import LED, Buzzer, Button
import RPi.GPIO as GPIO
import time
import json
import datetime


bz=Buzzer(4)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
pwm=GPIO.PWM(17,50)




with open('scr.txt','r+') as f:
        f.readline()
        f.seek(0)
        f.truncate()

with open('scr.txt', mode='ab') as file:
        file.write('%s \n' % (datetime.datetime.now()))

bz.beep(0.5,0.25,10)
time.sleep(5)


pwm.start(5)
pwm.ChangeDutyCycle(15)
print "Duty15"
time.sleep(1)
pwm.ChangeDutyCycle(2)
print "Duty2"
time.sleep(3)
pwm.stop()

                        
