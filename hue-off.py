#!/usr/bin/env python
import requests
import json


r = requests.put(url = "http://192.168.1.70/api/qG5Y5IyFuKus5eia9-7XPnISd4hhWiHfZd-KS5Ve/lights/2/state",
				 headers = {"Content-Type": "application/json"
				 },
				 data = json.dumps({
               		 		"on": False
				 	})
				)
#print r.json
