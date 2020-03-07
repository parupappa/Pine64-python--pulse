#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep
import time

GPIO.setmode(GPIO.BCM)

RF = 15
AD = 11

GPIO.setup(RF,GPIO.OUT)
GPIO.setup(AD,GPIO.OUT)

starttime = time.time()

for counter in range(10):		
	if counter == 3:
		GPIO.output(RF,1)			
		sleep(0.01)
			
				
	elif counter == 5:
		GPIO.output(AD,1)			
		sleep(0.01)
		
	else :  
		GPIO.output(RF,0)
		GPIO.output(AD,0)
		sleep(0.01)
	
		
	print(counter)

endtime = time.time()
print(endtime - starttime)
	


GPIO.cleanup()

