# -*- coding: utf-8 -*-



import sys  # sys.exit()でここまでのプログラムを実行

from time import sleep
import RPi.GPIO as GPIO
from random import randint

data = [randint(0,1) for i in range(20)]
print(data)

GPIO.setmode(GPIO.BCM)
PL = [17]


for i in data:
    GPIO.output(PL[0], data )
    print(data)

GPIO.cleanup()
