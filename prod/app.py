# Install the Python Requests library:
# `pip install requests`

from flask import Flask
app = Flask(__name__)
from gpiozero import LED, Buzzer, Button
import RPi.GPIO as GPIO
import time
import json
import datetime

GPIO.setmode(GPIO.BCM)

@app.route('/feeder')
def feeder():
    GPIO.setmode(GPIO.BCM)
    bz=Buzzer(4)
    GPIO.setup(17,GPIO.OUT)
    pwm=GPIO.PWM(17,50)

    with open('/home/pi/feeder/prod/scr.txt','r+') as f:
        f.readline()
        f.seek(0)
        f.truncate()
    
    with open('/home/pi/feeder/prod/scr.txt',mode='a') as file:
        file.write('%s \n'  % (datetime.datetime.now()))

    bz.beep(0.5,0.25,10)
    time.sleep(5)

    pwm.start(5)
    pwm.ChangeDutyCycle(15)
#    print "Duty15"
    time.sleep(1)
    pwm.ChangeDutyCycle(2)
#    print "Duty2"
    time.sleep(3)
    pwm.stop()
    GPIO.cleanup()

if __name__ == '__main__':
    port = 8551 #the custom port you want
    app.run(host='0.0.0.0', port=port)

