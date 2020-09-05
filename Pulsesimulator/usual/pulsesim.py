# -*- coding: utf-8 -*-
# パルスシミュレーターの完成形プログラム

import pandas as pd
import csv
from time import sleep  # time モジュールから sleep メソッドを取得
#import RPi.GPIO as GPIO
import platform
# GPIO.setmode(GPIO.BCM)

# pandas でcsvデータの二次元表を取得
csv_dataframe = pd.read_csv(
    '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulsesimulator/usual/pulse_simdata.csv', sep=',', encoding='utf-8', index_col=False, header=None)

pf = platform.system()

fname_Lin = '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulsesimulator/usual/pulse_simdata.csv'
fname_Dar = '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulsesimulator/usual/pulse_simdata.csv'

if pf == 'Linux':
    pulse_csv = open(fname_Lin)
elif pf == 'Darwin':
    pulse_csv = open(fname_Dar)


###########################################################################################
# インデント減らしたい時、Shift + Tab

PL = [17, 27, 22]

# for i in PL:
#GPIO.setup(i, GPIO.OUT)


PL1_sc1 = []
PL1_bc1 = []
PL2_sc2 = []
PL2_bc2 = []
PL3_sc3 = []
PL3_bc3 = []

PL_sc = [PL1_sc1, PL2_sc2, PL3_sc3]
PL_bc = [PL1_bc1, PL2_bc2, PL3_bc3]


index_PLsc = 0
index_PLbc = 0

for n in range(11):
    if n % 4 == 0:
        PL_sc[index_PLsc] = list(csv_dataframe[n])
        del PL_sc[index_PLsc][0:3]
        # replace で文字列内の余分な空白を削除
        PL_sc[index_PLsc] = [t.replace(" ", "") for t in PL_sc[index_PLsc]]
        PL_sc[index_PLsc] = [a for a in PL_sc[index_PLsc]
                             if a != '']  # リスト内の空白要素を削除
        PL_sc[index_PLsc] = [int(s)
                             for s in PL_sc[index_PLsc]]  # リスト要素 str を intに変換
        index_PLsc += 1

    elif n % 4 == 1:
        PL_bc[index_PLbc] = list(csv_dataframe[n])
        del PL_bc[index_PLbc][0:3]
        PL_bc[index_PLbc] = [t.replace(" ", "") for t in PL_bc[index_PLbc]]
        PL_bc[index_PLbc] = [a for a in PL_bc[index_PLbc] if a != '']
        PL_bc[index_PLbc] = [int(s) for s in PL_bc[index_PLbc]]
        index_PLbc += 1
    else:
        pass


# print(PL_sc)
# print(PL_bc)


'''
# 全ての行と 1-3 列目を取得
aiu = csv_dataframe.iloc[:, 0:2]
# print(aiu)

print(list(aiu[1]))
'''

########################################################################
# インデント減らしたい時、Shift + Tab

AD = [10, 9, 11]

# for i in AD:
#GPIO.setup(i, GPIO.OUT)

AD1_sc1 = []
AD1_bc1 = []
AD2_sc2 = []
AD2_bc2 = []
AD3_sc3 = []
AD3_bc3 = []

AD_sc = [AD1_sc1, AD2_sc2, AD3_sc3]
AD_bc = [AD1_bc1, AD2_bc2, AD3_bc3]

index_ADsc = 0
index_ADbc = 0

for n in range(13, 24):
    if n % 4 == 0:
        AD_sc[index_ADsc] = list(csv_dataframe[n])
        del AD_sc[index_ADsc][0:3]
        # reADace で文字列内の余分な空白を削除
        AD_sc[index_ADsc] = [t.replace(" ", "") for t in AD_sc[index_ADsc]]
        AD_sc[index_ADsc] = [a for a in AD_sc[index_ADsc]
                             if a != '']  # リスト内の空白要素を削除
        AD_sc[index_ADsc] = [int(s)
                             for s in AD_sc[index_ADsc]]  # リスト要素 str を intに変換
        index_ADsc += 1

    elif n % 4 == 1:
        AD_bc[index_ADbc] = list(csv_dataframe[n])
        del AD_bc[index_ADbc][0:3]
        AD_bc[index_ADbc] = [t.replace(" ", "") for t in AD_bc[index_ADbc]]
        AD_bc[index_ADbc] = [a for a in AD_bc[index_ADbc] if a != '']
        AD_bc[index_ADbc] = [int(s) for s in AD_bc[index_ADbc]]
        index_ADbc += 1
    else:
        pass

print(AD_sc)
print(AD_bc)

###########################################################################
# DDS40bit  データのシミュレーション

# pandas でcsvデータの二次元表を取得
csv_DDSdataframe = pd.read_csv(
    '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulsesimulator/usual/pulse_simdata.csv', sep=',', encoding='utf-8', index_col=False, header=None)


if pf == 'Linux':
    dds_csv = open(
        '/home/ubuntu/Documents/Python/Pine64-python--pulse/Pulsesimulator/pulse_simDDSdata.csv')
elif pf == 'Darwin':
    dds_csv = open(
        '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulsesimulator/pulse_simDDSdata.csv')

DDS = [26, 19]


'''
for i in range(len(DDS)):
    GPIO.setup(DDS[i], GPIO.OUT)
'''


DDS1_sc = []
DDS1_bc = []
DDS2_sc = []
DDS2_bc = []

DDS_sc = [DDS1_sc, DDS2_sc]
DDS_bc = [DDS1_bc, DDS2_bc]


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
