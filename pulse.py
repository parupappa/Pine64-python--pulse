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

for counter in range(10):
	
	if count == 3:
		j = 0
		while j < len(RFlist):	
			if RFlist[j] == 0: #RFlistのi番目が0ならGPIOピンをLOW
			  RFlight = 0 #タイムラグをなるべくなくすためRFlightという変数を用い後に出力
			elif RFlist[j] == 1:
				RFlight = 1
			

			starttime = time.time()

			GPIO.output(RF,RFlight)			
			sleep(0.1)
			endtime = time.time()
			print(endtime - starttime)
			j = j + 1

	elif count != 3:  
		sleep(0.1)
		
	count = count + 1
	print(count)
	
	



GPIO.cleanup()

