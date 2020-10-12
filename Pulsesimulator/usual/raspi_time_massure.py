# -*- coding: utf-8 -*-


import sys  # sys.exit()でここまでのプログラムを実行

from time import sleep
import RPi.GPIO as GPIO
from random import randint

#data = [randint(0,1) for i in range(20)]
data = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
print(data)

GPIO.setmode(GPIO.BCM)
GPIO.setup(17, GPIO.OUT)


for i in data:
    GPIO.output(17, i)
    print(i)

GPIO.cleanup()
