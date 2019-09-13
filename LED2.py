import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
GPIO.setup(15,GPIO.OUT)

GPIO.output(15,True)
sleep(1)


GPIO.cleanup()


