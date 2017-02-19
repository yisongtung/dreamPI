import RPi.GPIO as GPIO
from datetime import datetime

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

while True:
    if(GPIO.input(17) ==1):
        print 1
        print datetime.now()
    else:
	    print 0
