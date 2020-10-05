# -*- coding: utf-8 -*-
# パルスシミュレーターの完成形プログラム

from sys import exit
import csv
from time import sleep  # time モジュールから sleep メソッドを取得
import RPi.GPIO as GPIO
import platform
GPIO.setmode(GPIO.BCM)


pf = platform.system()

Linux_pass = '/home/ubuntu/Documents/Python/Pine64-python--pulse/Pulsesimulator/usual/pulse_simdata.csv'
Mac_pass = '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulsesimulator/usual/pulse_simdata.csv'
Rasberrypi_pass = '/home/pi/python/Pine64-python--pulse/Pulsesimulator/usual/pulse_simdata.csv'


if pf == 'Linux':
    pulse_csv = open(Rasberrypi_pass)
elif pf == 'Darwin':
    pulse_csv = open(Mac_pass)

###########################################################################################
# インデント減らしたい時、Shift + Tab

PLpoat = [17, 27, 22]

for i in PLpoat:
    GPIO.setup(i, GPIO.OUT)


PL1_sc1, PL1_bc1, PL2_sc2, PL2_bc2, PL3_sc3, PL3_bc3 = [], [], [], [], [], []
PL1_nsc1, PL1_nbc1, PL2_nsc2, PL2_nbc2, PL3_nsc3, PL3_nbc3 = [], [], [], [], [], []

PL_sc = [PL1_sc1, PL2_sc2, PL3_sc3]
PL_bc = [PL1_bc1, PL2_bc2, PL3_bc3]

PL_nsc = [PL1_nsc1, PL2_nsc2, PL3_nsc3]
PL_nbc = [PL1_nbc1, PL2_nbc2, PL3_nbc3]


index_PLsc = 0
index_PLbc = 0

for row in csv.reader(pulse_csv):
    for i in range(3):
        PL_sc[i].append(row[4 * i])
        PL_bc[i].append(row[4 * i + 1])


for n in range(11):
    if n % 4 == 0:
        del PL_sc[index_PLsc][0:3]
        # replace で文字列内の余分な空白を削除
        PL_sc[index_PLsc] = [t.replace(" ", "") for t in PL_sc[index_PLsc]]
        PL_sc[index_PLsc] = [a for a in PL_sc[index_PLsc]
                             if a != '']  # リスト内の空白要素を削除
        PL_sc[index_PLsc] = [int(s)
                             for s in PL_sc[index_PLsc]]  # リスト要素 str を intに変換
        for i in PL_sc[index_PLsc]:
            PL_nsc[index_PLsc].append(i)
        index_PLsc += 1

    elif n % 4 == 1:
        del PL_bc[index_PLbc][0:3]
        PL_bc[index_PLbc] = [t.replace(" ", "") for t in PL_bc[index_PLbc]]
        PL_bc[index_PLbc] = [a for a in PL_bc[index_PLbc] if a != '']
        PL_bc[index_PLbc] = [int(s) for s in PL_bc[index_PLbc]]
        for i in PL_bc[index_PLbc]:
            PL_nbc[index_PLbc].append(i)
        index_PLbc += 1
    else:
        pass


# print(PL_nsc)
# print(PL_nbc)

########################################################################

ADpoat = [10, 9, 11]

for i in ADpoat:
    GPIO.setup(i, GPIO.OUT)

if pf == 'Linux':
    pulse_csv = open(Rasberrypi_pass)
elif pf == 'Darwin':
    pulse_csv = open(Mac_pass)


AD1_sc1, AD1_bc1, AD2_sc2, AD2_bc2, AD3_sc3, AD3_bc3 = [], [], [], [], [], []
AD1_nsc1, AD1_nbc1, AD2_nsc2, AD2_nbc2, AD3_nsc3, AD3_nbc3 = [], [], [], [],  [], []


AD_sc = [AD1_sc1, AD2_sc2, AD3_sc3]
AD_bc = [AD1_bc1, AD2_bc2, AD3_bc3]
AD_nsc = [AD1_nsc1, AD2_nsc2, AD3_nsc3]
AD_nbc = [AD1_nbc1, AD2_nbc2, AD3_nbc3]


index_ADsc = 0
index_ADbc = 0


for row in csv.reader(pulse_csv):
    for i in range(3):
        AD_sc[i].append(row[4 * i + 12])
        AD_bc[i].append(row[4 * i + 13])

for n in range(12, 24):
    if n % 4 == 0:
        del AD_sc[index_ADsc][0:3]
        # reADace で文字列内の余分な空白を削除
        AD_sc[index_ADsc] = [t.replace(" ", "") for t in AD_sc[index_ADsc]]
        AD_sc[index_ADsc] = [a for a in AD_sc[index_ADsc]
                             if a != '']  # リスト内の空白要素を削除
        AD_sc[index_ADsc] = [int(s)
                             for s in AD_sc[index_ADsc]]  # リスト要素 str を intに変換
        for i in AD_sc[index_ADsc]:
            AD_nsc[index_ADsc].append(i)
        index_ADsc += 1

    elif n % 4 == 1:
        del AD_bc[index_ADbc][0:3]
        AD_bc[index_ADbc] = [t.replace(" ", "") for t in AD_bc[index_ADbc]]
        AD_bc[index_ADbc] = [a for a in AD_bc[index_ADbc] if a != '']
        AD_bc[index_ADbc] = [int(s) for s in AD_bc[index_ADbc]]
        for i in AD_bc[index_ADbc]:
            AD_nbc[index_ADbc].append(i)
        index_ADbc += 1
    else:
        pass

# print(AD_nsc)
# print(AD_nbc)
###########################################################################
# DDS40bit  データのシミュレーション


Lindds_pass = '/home/ubuntu/Documents/Python/Pine64-python--pulse/Pulsesimulator/usual/pulse_simDDSdata.csv'
Macdds_pass = '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulsesimulator/usual/pulse_simDDSdata.csv'
Rasdds_pass = '/home/pi/python/Pine64-python--pulse/Pulsesimulator/usual/pulse_simDDSdata.csv'

if pf == 'Linux':
    DDS_csv = open(Rasdds_pass)
elif pf == 'Darwin':
    DDS_csv = open(Macdds_pass)

DDSpoat = [19, 26]

for i in range(len(DDSpoat)):
    GPIO.setup(DDSpoat[i], GPIO.OUT)


DDS1_sc, DDS1_data, DDS2_sc, DDS2_data = [], [], [], []
DDS1_nsc, DDS1_ndata, DDS2_nsc, DDS2_ndata = [], [], [], []

DDS_sc = [DDS1_sc, DDS2_sc]
DDS_data = [DDS1_data, DDS2_data]
DDS_nsc = [DDS1_nsc, DDS2_nsc]
DDS_ndata = [DDS1_ndata, DDS2_ndata]


index_DDSsc = 0
index_DDSdata = 0

hinann = []

for row in csv.reader(DDS_csv):
    for i in range(2):
        DDS_sc[i].append(row[8 * i])
        DDS_data[i].append(row[8 * i + 4])


for n in range(14):
    if n % 8 == 0:  # DDSscについての記述
        del DDS_sc[index_DDSsc][0:3]
        DDS_sc[index_DDSsc] = [t.replace(" ", "") for t in DDS_sc[index_DDSsc]]
        DDS_sc[index_DDSsc] = [a for a in DDS_sc[index_DDSsc]
                               if a != '']
        DDS_sc[index_DDSsc] = [int(s)
                               for s in DDS_sc[index_DDSsc]]  # リスト要素 str を intに変換
        for i in DDS_sc[index_DDSsc]:
            DDS_nsc[index_DDSsc].append(i)
        index_DDSsc += 1

    elif n % 8 == 4:
        del DDS_data[index_DDSdata][0:3]
        for i in range(len(DDS_data[index_DDSdata])):
            chars = DDS_data[index_DDSdata][i]

            DDS_data[index_DDSdata][i] = list(chars)
            hinann.append(DDS_data[index_DDSdata][i])
            DDS_data[index_DDSdata][i] = [a for a in hinann[-1]
                                          if a != ' ']
            hinann = []
            DDS_data[index_DDSdata][i] = [int(s)
                                          for s in DDS_data[index_DDSdata][i]]
            DDS_ndata[index_DDSdata].append(DDS_data[index_DDSdata][i])

        index_DDSdata += 1

    else:
        pass


# print(DDS_nsc)
# print(DDS_ndata)


########################################################################################


counter = 0
index = [0 for i in range(8)]
j, k = 0, 0

GPIO.output(PLpoat[0], 0)
GPIO.output(PLpoat[1], 0)
GPIO.output(PLpoat[2], 0)

GPIO.output(ADpoat[0], 0)
GPIO.output(ADpoat[1], 0)
GPIO.output(ADpoat[2], 0)

GPIO.output(DDSpoat[0], 0)
GPIO.output(DDSpoat[1], 0)


while counter <= max(max((max(PL_nsc), max(AD_nsc), max(DDS_nsc)))):
    if counter <= int(PL1_nsc1[-1]):
        if PL1_nsc1[index[0]] == counter:
            GPIO.output(PLpoat[0], 1)
            sleep(PL1_nbc1[index[0]] * 1)
            index[0] += 1
            print('%d' % counter)  # end=':PL1出力中')
        else:
            GPIO.output(PLpoat[0], 0)
            sleep(0.5)
    else:
        GPIO.output(PLpoat[0], 0)


        '''
    elif counter <= int(PL2_nsc2[-1]):
        if PL2_nsc2[index[1]] == counter:
            GPIO.output(PLpoat[1], 1)
            sleep(PL2_nbc2[index[1]] * 0.5)
            index[1] += 1
            print('%d' % counter)  # end=':PL2出力中')
        else:
            GPIO.output(PLpoat[1], 0)
            sleep(0.5)

    elif counter <= int(PL3_nsc3[-1]):
        if PL3_nsc3[index[2]] == counter:
            GPIO.output(PLpoat[2], 1)
            sleep(PL3_nbc3[index[2]] * 0.5)
            index[2] += 1
            print('%d' % counter)  # end=':PL3出力中')
        else:
            GPIO.output(PLpoat[2], 0)
            sleep(0.5)
'''

#############################################################

    if counter <= int(AD1_nsc1[-1]):
        if AD1_nsc1[index[3]] == counter:
            GPIO.output(ADpoat[0], 1)
            sleep(AD1_nbc1[index[3]] * 0.5)
            index[3] += 1
            print('%d' % counter)  # end=':AD1出力中')
        else:
            GPIO.output(ADpoat[0], 0)
            sleep(0.5)

    else:
        GPIO.output(ADpoat[0], 0)


        '''
    elif counter <= int(AD2_nsc2[-1]):
        if AD2_nsc2[index[4]] == counter:
            GPIO.output(ADpoat[1], 1)
            sleep(AD2_nbc2[index[4]] * 0.5)
            index[4] += 1
            print('%d' % counter)  # end=':AD2出力中')
        else:
            GPIO.output(ADpoat[1], 0)
            sleep(0.5)

    elif counter <= int(AD3_nsc3[-1]):
        if AD3_nsc3[index[5]] == counter:
            GPIO.output(ADpoat[2], 1)
            sleep(AD3_nbc3[index[5]] * 0.5)
            index[5] += 1
            print('%d' % counter)  # end=':AD3出力中')
        else:
            GPIO.output(ADpoat[2], 0)
            sleep(0.5)

'''
##############################################################
    if k <= len(DDS1_nsc)-1:
        if DDS1_nsc[k] == counter:
            for m in range(len(DDS1_ndata[k])):
                GPIO.output(DDSpoat[0], DDS1_ndata[k][m])
                sleep(0.5)
                print('%d' % counter)  # end=':DDS1出力中')
            k += 1
        '''
    if j <= len(DDS2_nsc) - 1:
        if DDS2_nsc[j] == counter:
            for m in range(len(DDS2_ndata[j])):
                GPIO.output(DDSpoat[1], DDS2_ndata[j][m])
                sleep(0.5)
                print('%d' % counter)  # end=':DDS2出力中')
            j += 1
'''
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

    counter += 1
    print(counter)
else:
    counter = 0
    index = [0 for i in range(8)]
    k = 0
    j = 0

GPIO.cleanup()
