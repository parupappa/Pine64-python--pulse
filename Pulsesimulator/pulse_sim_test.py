# -*- coding: utf-8 -*-

# 設定するパラメータ　PL AD DDS の繰り返し回数と　1カウントをどの長さにするかのカウント値部分

import openpyxl as px
from time import sleep
import time
import RPi.GPIO as GPIO
import platform
pf = platform.system()

GPIO.setmode(GPIO.BCM)


if pf == 'Linux':
    wb = px.load_workbook(
        '/home/ubuntu/Documents/Python/Pine64-python--pulse/Pulsesimulator/pulse_simdata.xlsx')
    ws = wb.get_sheet_by_name('Pulseパラメータ')

elif pf == 'Darwin':
    wb = px.load_workbook(
        '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulsesimulator/pulse_simdata.xlsx')
    ws = wb.get_sheet_by_name('Pulseパラメータ')

PL = [17, 27, 22]

for i in range(len(PL)):
    GPIO.setup(PL[i], GPIO.OUt)


sc1 = []
bc1 = []

for cell_obj in list(ws.columns)[0]:
    sc1_value = cell_obj.value
    sc1.append(sc1_value)
del sc1[0:3]
sc1 = [x for x in sc1 if x is not None]
print(sc1)

for cell_obj in list(ws.columns)[1]:
    bc1_value = cell_obj.value
    bc1.append(bc1_value)
del bc1[0:3]
bc1 = [x for x in bc1 if x is not None]
print(bc1)


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
