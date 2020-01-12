#-*- coding: utf-8 -*-


import RPi.GPIO as GPIO
from time import sleep
import time
import csv

GPIO.setmode(GPIO.BCM)

RF = 15
AD = 17
DDS = 27

GPIO.setup(RF,GPIO.OUT)
GPIO.setup(AD,GPIO.OUT)
GPIO.setup(DDS,GPIO.OUT)



#カウント値操作部分

countlist = []

with open("pulsedata_pine_in.csv","r") as Pulsedata: 
    for row in csv.reader(Pulsedata):
        countlist.append(row[0])
    del countlist[0]
    countlist = [int(i) for i in countlist]
    print(countlist)



#対象操作部分

targetlist  = []

with open("pulsedata_pine_in.csv","r") as Pulsedata:    
    for row in csv.reader(Pulsedata):
        targetlist.append(row[1])
    del targetlist[0]
    print(targetlist)

targetRF = []
targetDDS = []
targetAD = []

for tl in targetlist :
    if 'RF' in tl:
        i = 1
        targetRF.append(i)
    else:
        i = 0
        targetRF.append(i)
    
    if 'DDS' in tl:
        j = 1
        targetDDS.append(j)
    else:
        j = 0
        targetDDS.append(j)

    if 'AD' in tl:
        k = 1
        targetAD.append(k)
    else:
        k = 0
        targetAD.append(k)
        
print(targetRF)
print(targetDDS)
print(targetAD)

while True:
	a = 0
	counter = 0
	while counter <=100:
		if counter == countlist[a]:
			GPIO.output(RF,targetRF[a])
			GPIO.output(DDS,targetDDS[a])
			GPIO.output(AD,targetAD[a])
			sleep(0.1)
			a = a + 1
		counter = counter + 1
	
	print(counter)   





'''

#DDS動作部分

DDSdatalist = []
DDSdata = []

with open("pulsedata_in.csv","r") as Pulsedata:    
    for row in csv.reader(Pulsedata):
        DDSdatalist.append(row[2])
    del DDSdatalist[0]
    for n in DDSdatalist:
        if n != '':
            DDSdata.append(n.zfill(16))   
    #print(DDSdata)


DDSinfo = []
a = 1
for dl in targetlist :
    if 'DDS' in dl:
        a = a + 1            
DDSinfo.append(format(a,'x').zfill(16))        
#print(DDSinfo)



#データ連結部分
#データを16進数に変換

Pulsedata = []

for c in range(len(bitsdata)) :
    P1 = countlist1[c] 
    P2 = bitsdata[c]
    P = P2 + P1
    Pulsedata.append(P)
#print(Pulsedata)

hexdata = ''
Pulsedata_hex =[]
n = 0
for m in range(len(Pulsedata)):
    str = Pulsedata[m]
    hexdata = ''
    n = 0
    while n + 3 < 64:
        four_str = str[n:n+4]
        four_int = int("0b"+four_str, 0)
        hex_str = format(four_int,'x')
        hexdata = hexdata + hex_str
        n = n + 4
    Pulsedata_hex.append(hexdata)
#print(Pulsedata_hex)
   
'''







GPIO.cleanup()

