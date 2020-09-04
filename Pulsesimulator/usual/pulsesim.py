# -*- coding: utf-8 -*-

# パルスシミュレーターの完成形プログラム

import csv
from time import sleep
import time
#import RPi.GPIO as GPIO
import platform
pf = platform.system()
# GPIO.setmode(GPIO.BCM)


fname_Lin = '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulsesimulator/usual/pulse_simdata.csv'
fname_Dar = '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulsesimulator/usual/pulse_simdata.csv'

if pf == 'Linux':
    pulse_csv = open(fname_Lin)
elif pf == 'Darwin':
    pulse_csv = open(fname_Dar)


###########################################################################################
# インデント減らしたい時、Shift + Tab

PL = [17, 27, 22]
'''
for i in PL:
    GPIO.setup(i, GPIO.OUT)
'''

PL1_sc1 = []
PL1_bc1 = []
PL2_sc2 = []
PL2_bc2 = []
PL3_sc3 = []
PL3_bc3 = []

PL_sc = [PL1_sc1, PL2_sc2, PL3_sc3]
PL_bc = [PL1_bc1, PL2_bc2, PL3_bc3]


sc_counter = 0
bc_counter = 0


for n in range(11):
    if n % 4 == 0:
        for row in csv.reader(pulse_csv):
            PL_sc[sc_counter].append(row[n])
        del PL_sc[sc_counter][0:3]
        # リスト内包表記 #リストにappend したい時
        PL_sc[sc_counter] = [int(s) for s in PL_sc[sc_counter]]
        sc_counter += 1
        print(sc_counter)

    elif n % 4 == 1:
        for row in csv.reader(pulse_csv):
            PL_bc[bc_counter].append(row[n])
        del PL_bc[bc_counter][0:3]
        PL_bc[bc_counter] = [int(s) for s in PL_bc[bc_counter]]
        sc_counter += 1
    else:
        pass


print(PL_sc)
print(PL_bc)

PL1_sc1 = []
PL2_sc2 = []
PL3_sc3 = []

PL_sc = [PL1_sc1, PL2_sc2, PL3_sc3]

'''
for row in csv.reader(pulse_csv):
    for i in range(3):
        PL_sc[i].append(row[i])
    print(i)
print(PL_sc)
'''

##################################################################################################
