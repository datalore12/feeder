#!/usr/bin/env python

import time
import requests
import json

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
	for t in range(0, n, 1):
		print(time.strftime("%H:%M:%S"))
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
hue_timer(15)
