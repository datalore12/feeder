#!/usr/bin/env python
from gpiozero import LED, Buzzer
import time

bz=Buzzer(4)
led = LED(17)

led.on()
# beep(on_time=1, off_time=1, n=None, background=True)
# on_time = number of seconds on.  Defaults to 1 second
# off_time = number of seconds off. Defaults to 1 second
# n = number of times to buzz.  None (the default means forever)
# https://gpiozero.readthedocs.io/en/stable/api_output.html
bz.beep(0.5, 0.25, 8)
time.sleep(5)
led.off()
