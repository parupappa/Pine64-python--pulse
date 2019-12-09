#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep
import time

GPIO.setmode(GPIO.BCM)

RF = 15
AD = 11

GPIO.setup(RF,GPIO.OUT)
GPIO.setup(AD,GPIO.OUT)


count = 0



starttime = time.time()

for counter in range(10):		
	if count == 3:
		GPIO.output(RF,1)			
		sleep(0.1)
			
				
	elif count == 5:
		GPIO.output(AD,1)			
		sleep(0.1)
		
	else :  
		GPIO.output(RF,0)
		GPIO.output(AD,0)
		sleep(0.1)
	
		
	count = count + 1
	print(count)

endtime = time.time()
print(endtime - starttime)
	



GPIO.cleanup()

