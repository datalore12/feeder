#!/usr/bin/env python
from gpiozero import LED, Buzzer, Button
import time

bz=Buzzer(4)
led = LED(17)
button = Button(21)

def feature(n):
	led.on()
	bz.beep(0.5, 0.25, n*2)
	time.sleep(n)
	led.off()

while True:
	if button.is_pressed:
		feature(4)
		
