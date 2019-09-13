import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(13,GPIO.OUT)

flag = 1
while True:
    GPIO.output(13,flag)
    flag = flag ^ 1
    time.sleep(1)
    