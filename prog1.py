#!/usr/bin/env python
from gpiozero import LED, Buzzer, Button
import time
import requests
import json


bz=Buzzer(4)
led = LED(17)
button = Button(21)

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
	led.on()
	bz.beep(0.5, 0.25, 10)
	time.sleep(5)
	led.off()
	
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
	



if __name__=="__main__":
	hue_timer(15)



