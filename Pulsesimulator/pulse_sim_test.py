# -*- coding: utf-8 -*-

# 設定するパラメータ　PL AD DDS の繰り返し回数と　1カウントをどの長さにするかのカウント値部分

import csv
import pandas as pd
from time import sleep
import time
import RPi.GPIO as GPIO
import platform
pf = platform.system()

GPIO.setmode(GPIO.BCM)


if pf == 'Linux':
    pulse_csv = open(
        '/home/ubuntu/Documents/Python/Pine64-python--pulse/Pulsesimulator/pulse_simdata.csv')
elif pf == 'Darwin':
    pulse_csv = open(
        '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulsesimulator/pulse_simdata.csv')


###########################################################################################

PL = [17, 27, 22]

for i in range(len(PL)):
    GPIO.setup(PL[i], GPIO.OUT)


sc1 = []
bc1 = []
sc1_int = []
bc1_int = []


for row in csv.reader(pulse_csv):
    sc1.append(row[0])
    bc1.append(row[1])
del sc1[0:3]
del bc1[0:3]
for i in range(len(sc1)):
    sc1_int.append(int(sc1[i]))
    bc1_int.append(int(bc1[i]))
print(sc1_int)
print(bc1_int)


##################################################################################################
# DDS40bit  データのシミュレーション
if pf == 'Linux':
    dds_csv = open(
        '/home/ubuntu/Documents/Python/Pine64-python--pulse/Pulsesimulator/pulse_simDDSdata.csv')
elif pf == 'Darwin':
    dds_csv = open(
        '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulsesimulator/pulse_simDDSdata.csv')

DDS = [26, 19]
DDS_sc1 = []
DDSsc1_int = []
DDS_data = []
chars_new = []

for i in range(len(DDS)):
    GPIO.setup(DDS[i], GPIO.OUT)

for row in csv.reader(dds_csv):
    DDS_sc1.append(row[0])
    DDS_data.append(row[4])
del DDS_sc1[0:3]
del DDS_data[0:3]
for i in range(len(DDS_sc1)):
    DDSsc1_int.append(int(DDS_sc1[i]))


for i in range(len(DDS_data)):
    DDSsc1_int.append(int(DDS_sc1[i]))

    chars = list(DDS_data[i].strip())
    chars_new.append(chars)
chars_int = map((lambda x: int(x)), chars_new)
print(chars_new)

##################################################################################################


counter = 0
j = 0  # sc1_intのインデックス
k = 0
while counter < max(int(sc1_int[-1]), int(DDS_sc1[-1])):
    if sc1_int[j] == counter:
        GPIO.output(PL[0], 1)
        sleep(bc1_int[j])
        j += 1

    if DDSsc1_int[k] == counter:
        for n in range(len(chars_new)):
            for m in range(len(chars)):
                GPIO.output(DDS[0], chars_new[n][m])
                sleep(1)
        k += 1

    else:
        GPIO.output(PL[0], 0)
        sleep(0.1)
        print("待機中")
    counter += 1
    print(counter)


GPIO.cleanup()
