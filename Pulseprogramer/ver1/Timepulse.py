#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep
import time

GPIO.setmode(GPIO.BCM)

RF = 15
AD = 11
DDS = 8

GPIO.setup(RF,GPIO.OUT)
GPIO.setup(AD,GPIO.OUT)
GPIO.setup(DDS,GPIO.OUT)


Timedata = []

with open("Timedata.txt","r") as testdata: 
		strTimedata = testdata.readline().rstrip('\n') #をstrTimedataに代入
		for i in range(len(strTimedata)):
			Timedata.append(int(strTimedata[i])) #dataをint型にしてTimedata配列に追加
			#print(Timedata)



starttime = time.time()

for counter in range(10):			
	if counter == Timedata[1]:
		GPIO.output(RF,1)			
		sleep(0.01)
						
	elif counter == Timedata[2]:
		GPIO.output(RF,0)			
		sleep(0.01)
		
	elif counter == Timedata[3]:
		GPIO.output(DDS,1)			
		sleep(0.01)

	elif counter == Timedata[5]:
		GPIO.output(RF,1)			
		sleep(0.01)

	elif counter == Timedata[7]:
		GPIO.output(RF,0)			
		sleep(0.01)

	elif counter == Timedata[8]:
		GPIO.output(DDS,1)			
		sleep(0.01)

	elif counter == Timedata[9]:
		GPIO.output(AD,1)			
		sleep(0.01)

	else:
		GPIO.output(RF,0)
		GPIO.output(AD,0)
		GPIO.output(DDS,0)
		sleep(0.01)


	print(counter)


endtime = time.time()
print(endtime - starttime)
	


GPIO.cleanup()

