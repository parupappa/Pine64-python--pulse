# -*- coding: utf-8 -*-

import math
import platform
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)


data_port = 17
enable_port = 27
start_port = 22
through_port = 26


GPIO.setup(data_port, GPIO.OUT)
GPIO.setup(enable_port, GPIO.OUT)
GPIO.setup(start_port, GPIO.OUT)
GPIO.setup(through_port, GPIO.OUT)


s = "s"
ms = "ms"
us = "us"
t = "t"

pulse_info = []

# 変な関数


def bousenn():
    print("--------------------------------------------------")


for i in range(2):
    width_pulse = int(input("Please enter width_pulse only number : "))
    bousenn()
    unit = str(input("Please enter pulse unit(s,ms,us) : "))
    bousenn()
    through = int(input("if through ON enter 1 , through OFF enter 0 : "))
    bousenn()

    default_info = [width_pulse, unit, through]
    print(default_info)
    bousenn()
    pulse_info.append(default_info)


# 単位変換関数
def change_unit(width_pulse, unit):
    if unit == "s":
        count_value = width_pulse * (10**6) * 10
    elif unit == "ms":
        count_value = width_pulse * (10 ** 3) * 10
    elif unit == "us":
        count_value = width_pulse * 10

    return count_value


# format変換関数
def change_format(count):
    data_16bit = list(format(count, 'b').zfill(16))
    data_16bit_int = [int(s) for s in data_16bit]
    return data_16bit_int


data_list = []
through_widthpulse = []

for info in pulse_info:
    if info[2] == 1:
        if info[1] == "s":
            through_widthpulse.append(info[0])
        elif info[1] == "ms":
            through_widthpulse.append(info[0] / (1000))

    else:
        data_list.append(change_format(change_unit(info[0], info[1])))

print(through_widthpulse)
print(data_list)
print(pulse_info)

through_OFFcounter = 0
through_ONcounter = 0
dataloop_counter = 0

for out_info in pulse_info:
    if out_info[2] == 0:
        while through_OFFcounter < len(data_list):
            for j in data_list[dataloop_counter]:
                if j == 1:
                    GPIO.output(data_port, 1)
                    GPIO.output(enable_port, 1)
                    GPIO.output(enable_port, 0)

                else:
                    GPIO.output(data_port, 0)
                    GPIO.output(enable_port, 1)
                    GPIO.output(enable_port, 0)

            dataloop_counter += 1
            print(dataloop_counter)


while through_OFFcounter + through_ONcounter <= len(pulse_info):
    if pulse_info[through_ONcounter][2] == 1:
        through_botn = input("Please enter  t  : ")
        if through_botn == "t":
            GPIO.output(through_port, 1)
            sleep(through_widthpulse[through_ONcounter])

        else:
            print("Please enter t")
            continue

        through_ONcounter += 1
        print(through_ONcounter)

    else:
        for i in range(through_OFFcounter):
            start_botn = input("Please enter s  : ")
            if start_botn == "s":
                GPIO.output(start_port, 1)
                GPIO.output(start_port, 0)
            else:
                print("Please enter s")
                continue

        through_OFFcounter += 1
        print(through_OFFcounter)


GPIO.cleanup()
