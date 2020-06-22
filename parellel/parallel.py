# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
import time
from time import sleep

GPIO.setmode(GPIO.BCM)

Ready = 18
D = [17, 27, 22, 5, 6, 13, 19, 26]

GPIO.setup(Ready, GPIO.IN)

for i in range(len(D)):
    GPIO.setup(D[i], GPIO.OUT)

Datalist0 = []
Datalist1 = []
Datalist2 = []
Datalist3 = []
Datalist4 = []
Datalist5 = []
Datalist6 = []
Datalist7 = []

with open("data.txt", "r") as testdata:  # data.txtを開く
    strData = testdata.read().splitlines()
#print(strData)


############
j = 0
while j < len(strData):
    while GPIO.input(Ready) != 0:
        ''' WAIT '''
        sleep(3)
    print("OK")

    outstr = list(strData[j])
    for i in range(0, 8):
        GPIO.output(D[i], int(outstr[i]))

    j += 1

GPIO.cleanup()
