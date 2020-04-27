#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep
import time

GPIO.setmode(GPIO.BCM)

RF = 15
#AD = 17

GPIO.setup(RF,GPIO.OUT)
#GPIO.setup(AD,GPIO.OUT)

RFlist = []#空のRFlistを用意
#ADlist = []#空のADlistを用意

with open("pulsedata.txt","r") as testdata: 
	strRF = testdata.readline().rstrip('\n') #RFlistdata(1行目)をstrRFに代入
	#strAD = testdata.readline().rstrip('\n') #ADlistdata(2行目)をstrADに代入	
	for i in range(len(strRF)): #二つのdataが同じ長さなのでlenで長さ指定
		RFlist.append(int(strRF[i])) #dataをint型にしてRFlist配列に追加
		#ADlist.append(int(strAD[i])) 
	print(RFlist)



count = 0
j = 0

starttime = time.time()

while j < len(RFlist):	
	
	for counter in range(10):	
		RFlight = RFlist[j]

		if count == 3:
			GPIO.output(RF,RFlight)			
			sleep(0.01)	
				
		elif count != 3:  
			GPIO.output(RF,0)
			sleep(0.01)
			
		
		count = count + 1
		print(count)
	j = j + 1
endtime = time.time()
print(endtime - starttime)
	



GPIO.cleanup()

