from gpiozero import MotionSensor, Buzzer
import time
import RPi.GPIO as GPIO

pir = MotionSensor(4)
bz = Buzzer(3)



try:
	print("Waiting for PIR to settle")
	pir.wait_for_no_motion()
	while True:
	        print("Ready")
	        pir.wait_for_motion()
	        print("Motion detected!")
	        bz.beep(0.5,0.25,8)
	        time.sleep(3)

except KeyboardInterrupt:
	GPIO.cleanup()
