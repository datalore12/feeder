#!/usr/bin/env python
from gpiozero import Buzzer
import time

bz=Buzzer(4)
x = 0

while x < 5:
  bz.beep(0.5, 0.25, 8)
  time.sleep(5)
  x = x + 1
