#-*- coding: utf-8 -*-

'''

import RPi.GPIO as GPIO
from time import sleep
import time
'''
import csv


'''
GPIO.setmode(GPIO.BCM)

RF = 15
AD = 11
DDS = 8



GPIO.setup(RF,GPIO.OUT)
GPIO.setup(AD,GPIO.OUT)
GPIO.setup(DDS,GPIO.OUT)

'''

countlist = []
targetlist  = []
DDSdatalist = []
DDSdata = []




with open("pulsedata.csv","r") as Pulsedata: 
    for row in csv.reader(Pulsedata):
        countlist.append(row[0])
    del countlist[0]
    countlist = [int(i) for i in countlist]
    print(countlist)


countlist1 = []

for k in range(len(countlist)):
    countlist1.append(countlist[k] * 1000000)
    countlist1[k] = format(countlist1[k],'b').zfill(32)
print(countlist1)





with open("pulsedata.csv","r") as Pulsedata:    
    for row in csv.reader(Pulsedata):
        targetlist.append(row[1])
    del targetlist[0]
    print(targetlist)


targetRF = []
targetDDS = []
targetAD = []

for tl in targetlist :
    if 'RF' in tl:
        i = '1'
        targetRF.append(i)
    else:
        i = '0'
        targetRF.append(i)
    
    if 'DDS' in tl:
        j = '1'
        targetDDS.append(j)
    else:
        j = '0'
        targetDDS.append(j)

    if 'AD' in tl:
        k = '1'
        targetAD.append(k)
    else:
        k = '0'
        targetAD.append(k)
        
#print(targetRF)
#print(targetDDS)
#print(targetAD)


bitsdata = []

for b in range(len(targetRF)):
    s1 = targetRF[b]
    s2 = targetDDS[b]
    s3 = targetAD[b]
    s = s1 + s2 + s3
    bitsdata.append(s.zfill(32))
print(bitsdata)




with open("pulsedata.csv","r") as Pulsedata:    
    for row in csv.reader(Pulsedata):
        DDSdatalist.append(row[2])
    del DDSdatalist[0]
    for n in DDSdatalist:
        if n != '':
            DDSdata.append(n)   
    print(DDSdata)





Pulsedata = []









#GPIO.cleanup()

