#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep
import time

GPIO.setmode(GPIO.BCM)

RF = 15

GPIO.setup(RF,GPIO.OUT)

RFlist = []#空のRFlistを用意

with open("data.txt","r") as testdata: #data.txtを開く
	strRF = testdata.readline().rstrip('\n') #RFlistdata(1行目)をstrRFに代入

	for i in range(len(strRF)): #二つのdataが同じ長さなのでlenで長さ指定
		RFlist.append(int(strRF[i])) #dataをint型にしてRFlist配列に追加

j = 0

while j < len(RFlist):
	if RFlist[j] == 0: #RFlistのi番目が0ならGPIOピンをLOW
		 	RFlight = 0 #タイムラグをなるべくなくすためRFlightという変数を用い後に出力
	elif RFlist[j] ==1:
			RFlight = 1

	start = time.time()

	GPIO.output(RF,RFlight)

	sleep(0.00001)

	end = time.time()
	print(end-start)

	j = j + 1

GPIO.cleanup()

