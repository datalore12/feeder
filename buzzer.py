#!/usr/bin/env python
from gpiozero import LED, Buzzer
import time

bz=Buzzer(4)
led = LED(17)

led.on()
bz.beep(0.5, 0.25, 8)
time.sleep(4)
led.off()
