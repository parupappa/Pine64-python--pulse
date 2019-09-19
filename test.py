import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

RF = 15
AD = 17


GPIO.setup(RF,GPIO.OUT)
GPIO.setup(AD,GPIO.OUT)


RFlist = []
ADlist = []
with open("data.txt","r") as testdata:
	strRF = testdata.readline().rstrip('\n')
	strAD = testdata.readline().rstrip('\n')	
	for i in range(len(strRF)):
		RFlist.append(int(strRF[i]))
		ADlist.append(int(strAD[i]))
	print(strRF,strAD)
	print(RFlist)
	print(ADlist)

j = 0

while j < len(RFlist):
	if RFlist[j] == 0:
		 	RFlight = 0
	elif RFlist[j] ==1:
			RFlight = 1
	if ADlist[j] == 0:
			ADlight = 0
	elif ADlist[j] ==1:
			ADlight = 1	
	GPIO.output(RF, RFlight);
	GPIO.output(AD, ADlight);
	
	j = j + 1
	sleep(1)

	



GPIO.cleanup()


