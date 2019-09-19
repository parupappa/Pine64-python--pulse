import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

RF = 15

GPIO.setup(RF,GPIO.OUT)

list = [1,0,1,0,1,0,1,0,1,0]
i = 0


for j in list:
	if list[i] == 0:
		GPIO.output(RF,0)
	elif list[i] == 1:
			GPIO.output(RF,1)
	print(i)	
	i = i+1	
	sleep(0.001)
	
GPIO.cleanup()
