import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.IN)

while True:
    if(GPIO.input(17) ==1):
        print 1
    else:
	    print 0
