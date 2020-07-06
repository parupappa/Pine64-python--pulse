# -*- coding: utf-8 -*-

# 設定するパラメータ　PL AD DDS の繰り返し回数と　1カウントをどの長さにするかのカウント値部分

import csv
import pandas as pd
from time import sleep
import RPi.GPIO as GPIO
import platform
pf = platform.system()

# GPIO.setmode(GPIO.BCM)


if pf == 'Linux':
    csv_file = open(
        '/home/ubuntu/Documents/Python/Pine64-python--pulse/Pulsesimulator/pulse_simdata.csv')
elif pf == 'Darwin':
    csv_file = open(
        '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulsesimulator/pulse_simdata.csv')


PL = [17, 27, 22]

for i in range(len(PL)):
    GPIO.setup(PL[i], GPIO.OUT)


sc1 = []
bc1 = []
sc1_int = []
bc1_int = []

for row in csv.reader(csv_file):
    sc1.append(row[0])
print(sc1)
del sc1[0:3]
for i in range(len(sc1)):
    sc1_int.append(int(sc1[i]))
print(sc1_int)


"""
for cell_obj in list(ws.columns)[1]:
    bc1_value = cell_obj.value
    bc1.append(bc1_value)
del bc1[0:3]
bc1 = [x for x in bc1 if x is not None]
print(bc1)

"""

counter = 0
while counter < 30:
    if sc1[counter] == counter:
        GPIO.output(PL[0], HIGH)
        sleep(bc1[counter])
    else:
        print("待っています")
        sleep(1)
    counter += 1


GPIO.cleanup()
