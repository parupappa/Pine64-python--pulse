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




#カウント値操作部分

countlist = []
targetlist  = []
DDSdatalist = []
DDSdata = []




with open("pulsedata.csv","r") as Pulsedata: 
    for row in csv.reader(Pulsedata):
        countlist.append(row[0])
    del countlist[0]
    countlist = [int(i) for i in countlist]
    #print(countlist)

countlist1 = []

for k in range(len(countlist)):
    countlist1.append(countlist[k] * 100000) #[ms]単位のカウント値
    countlist1[k] = format(countlist1[k],'b').zfill(32)
#print(countlist1)








#対象操作部分

with open("pulsedata.csv","r") as Pulsedata:    
    for row in csv.reader(Pulsedata):
        targetlist.append(row[1])
    del targetlist[0]
    #print(targetlist)


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
#print(bitsdata)










#DDS動作部分


with open("pulsedata.csv","r") as Pulsedata:    
    for row in csv.reader(Pulsedata):
        DDSdatalist.append(row[2])
    del DDSdatalist[0]
    for n in DDSdatalist:
        if n != '':
            DDSdata.append(n)   
    #print(DDSdata)


DDSinfo = []
a = 1
for dl in targetlist :
    if 'DDS' in dl:
        a = a + 1            
DDSinfo.append(format(a,'x').zfill(16))        
print(DDSinfo)








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
print(Pulsedata_hex)
   



#アドレスデータ部分

addresslist = []
for d in range(len(countlist) + 1):
    addresslist.append(format(d,'x').zfill(5))    
print(addresslist)    



csvdata = []
start = DDSinfo + addresslist[0]



print(start)

#GPIO.cleanup()

