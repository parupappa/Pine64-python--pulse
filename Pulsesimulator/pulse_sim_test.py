# -*- coding: utf-8 -*-

# PLとDDSの1チャネルのシミュレーションプログラム

import sys  # sys.exit()でここまでのプログラムを実行
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
# print(sc1_int)
# print(bc1_int)


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
DDS_list = []

for i in range(len(DDS)):
    GPIO.setup(DDS[i], GPIO.OUT)


for row in csv.reader(dds_csv):
    DDS_sc1.append(row[0])
    DDS_data.append(row[4])
del DDS_sc1[0:3]
del DDS_data[0:3]

# 読み込んだデータをint型に変換
for i in range(len(DDS_sc1)):
    DDSsc1_int.append(int(DDS_sc1[i]))

    # 40bitdataを一文字ずつにして配列に格納
    chars = list(DDS_data[i].strip())
    DDS_list.append(chars)
# 読み込んだ配列をint型に変換
for j in range(len(DDS_list)):
    for i in range(len(DDS_list[0])):
        if str == type(DDS_list[j][i]):
            DDS_list[j][i] = (int(DDS_list[j][i]))
# print(DDS_list)


##################################################################################################


counter = 0
j = 0  # sc1_intのインデックス
k = 0  # DDSsc1_intのインデックス

while True:
    while counter <= max(sc1_int[-1], DDSsc1_int[-1]):
        if counter <= sc1_int[-1]:
            if sc1_int[j] == counter:
                GPIO.output(PL[0], 1)
                sleep(bc1_int[j] * 0.25)
                j += 1
            else:
                pass

        if DDSsc1_int[k] == counter:
            for m in range(len(DDS_list[k])):
                GPIO.output(DDS[0], DDS_list[k][m])
                sleep(0.25)
            k += 1

        else:
            GPIO.output(PL[0], 0)
            GPIO.output(DDS[0], 0)
            sleep(0.1)
            print("待機中")
        counter += 1
        print(counter)
    else:
        counter = 0
        j = 0
        k = 0


GPIO.cleanup()
