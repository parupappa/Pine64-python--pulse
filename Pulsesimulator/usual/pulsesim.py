# -*- coding: utf-8 -*-
# パルスシミュレーターの完成形プログラム


import pandas as pd
import csv
from time import sleep  # time モジュールから sleep メソッドを取得
# import RPi.GPIO as GPIO
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

PLpoat = [17, 27, 22]

for i in PLpoat:
    GPIO.setup(i, GPIO.OUT)


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

########################################################################
# インデント減らしたい時、Shift + Tab

ADpoat = [10, 9, 11]

for i in ADpoat:
    GPIO.setup(i, GPIO.OUT)

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

# print(AD_sc)
# print(AD_bc)

###########################################################################
# DDS40bit  データのシミュレーション

# pandas でcsvデータの二次元表を取得
csv_DDSdataframe = pd.read_csv(
    '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulsesimulator/usual/pulse_simDDSdata.csv', sep=',', encoding='utf-8', index_col=False, header=None)


if pf == 'Linux':
    dds_csv = open(
        '/home/ubuntu/Documents/Python/Pine64-python--pulse/Pulsesimulator/usual/pulse_simDDSdata.csv')
elif pf == 'Darwin':
    dds_csv = open(
        '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulsesimulator/usual/pulse_simDDSdata.csv')

DDSpoat = [26, 19]


for i in range(len(DDSpoat)):
    GPIO.setup(DDSpoat[i], GPIO.OUT)


DDS1_sc = []
DDS1_data = []
DDS2_sc = []
DDS2_data = []

DDS_sc = [DDS1_sc, DDS2_sc]
DDS_data = [DDS1_data, DDS2_data]

index_DDSsc = 0
index_DDSdata = 0

hinann = []

for n in range(14):
    if n % 8 == 0:  # DDSscについての記述
        DDS_sc[index_DDSsc] = list(csv_DDSdataframe[n])
        del DDS_sc[index_DDSsc][0:3]
        DDS_sc[index_DDSsc] = [t.replace(" ", "") for t in DDS_sc[index_DDSsc]]
        DDS_sc[index_DDSsc] = [a for a in DDS_sc[index_DDSsc]
                               if a != '']
        DDS_sc[index_DDSsc] = [int(s)
                               for s in DDS_sc[index_DDSsc]]  # リスト要素 str を intに変換
        index_DDSsc += 1

    elif n % 8 == 4:
        DDS_data[index_DDSdata] = list(csv_DDSdataframe[n])
        del DDS_data[index_DDSdata][0:3]

        for i in range(len(DDS_data[index_DDSdata])):
            chars = DDS_data[index_DDSdata][i]

            DDS_data[index_DDSdata][i] = list(chars)
            hinann.append(DDS_data[index_DDSdata][i])
            DDS_data[index_DDSdata][i] = [a for a in hinann[-1]
                                          if a != ' ']
            DDS_data[index_DDSdata][i] = [int(s)
                                          for s in DDS_data[index_DDSdata][i]]
        index_DDSdata += 1

    else:
        pass

# print(DDS_sc)
# print(DDS_data)

########################################################################################


counter = 0
index = [0 for i in range(8)]
x = 0  # sc1_intのインデックス
k = 0  # DDSsc1_intのインデックス

while True:
    while counter <= max(max(PL_sc, AD_sc, DDS_sc, key=max)):
        if counter <= PL1_sc1[-1]:
            if PL1_sc1[index[0]] == counter:
                GPIO.output(PLpoat[0], 1)
                sleep(PL1_bc1[index[0]] * 0.001)
                index[0] += 1
                print('%d' % counter)  # end=':PL1出力中')

        if counter <= PL2_sc2[-1]:
            if PL2_sc2[index[1]] == counter:
                GPIO.output(PLpoat[1], 1)
                sleep(PL2_bc2[index[1]] * 0.001)
                index[1] += 1
                print('%d' % counter)  # end=':PL2出力中')

        if counter <= PL3_sc3[-1]:
            if PL3_sc3[index[2]] == counter:
                GPIO.output(PLpoat[2], 1)
                sleep(PL3_bc3[index[2]] * 0.001)
                index[2] += 1
                print('%d' % counter)  # end=':PL3出力中')


#############################################################

        if counter <= AD1_sc1[-1]:
            if AD1_sc1[index[3]] == counter:
                GPIO.output(ADpoat[0], 1)
                sleep(AD1_bc1[index[3]] * 0.001)
                index[3] += 1
                print('%d' % counter)  # end=':AD1出力中')

        if counter <= AD2_sc2[-1]:
            if AD2_sc2[index[4]] == counter:
                GPIO.output(ADpoat[1], 1)
                sleep(AD2_bc2[index[4]] * 0.001)
                index[4] += 1
                print('%d' % counter)  # end=':AD2出力中')

        if counter <= AD3_sc3[-1]:
            if AD3_sc3[index[5]] == counter:
                GPIO.output(ADpoat[2], 1)
                sleep(AD3_bc3[index[5]] * 0.001)
                index[5] += 1
                print('%d' % counter)  # end=':AD3出力中')


##############################################################

        if DDS1_sc[k] == counter:
            for m in range(len(DDS1_data[k])):
                GPIO.output(DDSpoat[0], DDS1_data[k][m])
                sleep(0.5)
                print('%d' % counter)  # end=':DDS1出力中')

            k += 1

        if DDS2_sc[x] == counter:
            for m in range(len(DDS2_data[x])):
                GPIO.output(DDSpoat[1], DDS2_data[x][m])
                sleep(0.5)
                print('%d' % counter)  # end=':DDS2出力中')

            x += 1

        else:
            GPIO.output(PLpoat[0], 0)
            GPIO.output(PLpoat[1], 0)
            GPIO.output(PLpoat[2], 0)

            GPIO.output(ADpoat[0], 0)
            GPIO.output(ADpoat[1], 0)
            GPIO.output(ADpoat[2], 0)

            GPIO.output(DDSpoat[0], 0)
            GPIO.output(DDSpoat[1], 0)

            sleep(0.5)
            print('%d' % counter)  # end=':LOWlevel')

        counter += 1
        # print(counter)
    else:
        counter = 0
        index = [0 for i in range(8)]
        k = 0
        x = 0


GPIO.cleanup()
