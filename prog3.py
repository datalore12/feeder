#!/usr/bin/env python
from gpiozero import LED, Buzzer, Button
import RPi.GPIO as GPIO
import time
import requests
import json
import datetime


bz=Buzzer(4)
button = Button(21)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17,GPIO.OUT)
pwm=GPIO.PWM(17,50)


def timestamp():
	with open('scr.txt','r+') as f:
		f.readline()
		f.seek(0)
		f.truncate()

	with open('scr.txt', mode='a') as file:
		file.write('%s \n' % (datetime.datetime.now()))

def hue_timer(n):
	response = requests.put(
            url="http://192.168.1.70/api/qG5Y5IyFuKus5eia9-7XPnISd4hhWiHfZd-KS5Ve/lights/2/state",
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps({
				"ct":233,
                "bri": 254,
                "on": True
            })
        )
	bz.beep(0.5, 0.25, 10)
	time.sleep(5)

	for t in range(0, n, 1):
#		print(time.strftime("%H:%M:%S"))
		time.sleep(1)
	response = requests.put(
            url="http://192.168.1.70/api/qG5Y5IyFuKus5eia9-7XPnISd4hhWiHfZd-KS5Ve/lights/2/state",
            headers={
                "Content-Type": "application/json",
            },
            data=json.dumps({
                "on": False
            })
        )

def servo():
	pwm.start(5)
	pwm.ChangeDutyCycle(15)
	print "Duty15"
	time.sleep(1)
	pwm.ChangeDutyCycle(2)
	print "Duty2"
	time.sleep(3)
	pwm.stop()
	GPIO.cleanup()



if __name__=="__main__":
	timestamp()
	servo()
	hue_timer(15)


