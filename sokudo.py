#-*- coding: utf-8 -*-

import RPi.GPIO as GPIO
#from time import sleep
import time

GPIO.setmode(GPIO.BCM)

RF = 15
AD = 17

GPIO.setup(RF,GPIO.OUT)
#GPIO.setup(AD,GPIO.OUT)

RFlist = []#空のRFlistを用意
#ADlist = []#空のADlistを用意
with open("data.txt","r") as testdata: #data.txtを開く
	strRF = testdata.readline().rstrip('\n') #RFlistdata(1行目)をstrRFに代入
	#strAD = testdata.readline().rstrip('\n') #ADlistdata(2行目)をstrADに代入	
	for i in range(len(strRF)): #二つのdataが同じ長さなのでlenで長さ指定
		RFlist.append(int(strRF[i])) #dataをint型にしてRFlist配列に追加
		#ADlist.append(int(strAD[i])) 
	#print(strRF,strAD)				#確認用フィードバック
	#print(RFlist)
	#print(ADlist)

j = 0


start = time.time()

while j < len(RFlist):	
	if RFlist[j] == 0: #RFlistのi番目が0ならGPIOピンをLOW
		 	RFlight = 0 #タイムラグをなるべくなくすためRFlightという変数を用い後に出力
	elif RFlist[j] ==1:
			RFlight = 1
	'''if ADlist[j] == 0:
			ADlight = 0
	elif ADlist[j] ==1:
			ADlight = 1'''

	
	
	GPIO.output(RF,RFlight)
	#GPIO.output(AD,ADlight)
	
	j = j + 1
	#sleep(0.0001)	#動作を1[s]継続
end = time.time()
print(end-start)

GPIO.cleanup()

