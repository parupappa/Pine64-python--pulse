import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(15,GPIO.OUT)

flag = 1
while True:
    GPIO.output(15,flag)
    flag = flag ^ 1
    time.sleep(1)

GPIO.cleanup()

