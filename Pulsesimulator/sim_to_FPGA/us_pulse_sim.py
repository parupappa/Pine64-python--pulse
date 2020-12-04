# -*- coding: utf-8 -*-

import math
import platform
# import RPi.#GPIO as #GPIO
from time import sleep
# #GPIO.setmode(#GPIO.BCM)


data_port = 17
clk_port = 27
start_triger = 22
ADdata_port = 10
ADclk_port = 9
ADstart_triger = 11

through_port = 26


# #GPIO.setup(data_port, #GPIO.OUT)
# #GPIO.setup(clk_port, #GPIO.OUT)
# #GPIO.setup(start_triger, #GPIO.OUT)
# #GPIO.setup(through_port, #GPIO.OUT)
# #GPIO.setup(ADdata_port, #GPIO.OUT)
# #GPIO.setup(ADclk_port, #GPIO.OUT)
# #GPIO.setup(ADstart_triger, #GPIO.OUT)

#########################################################
# ADモジュール
# 必要なときに呼び出して使う。
AD_data = [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0]


def AD_pulse():
    for i in AD_data:
        if i == 1:
            pass
            # GPIO.output(ADdata_port, 1)
            # GPIO.output(ADclk_port, 1)
            # GPIO.output(ADclk_port, 0)

        else:
            pass
            # GPIO.output(ADdata_port, 0)
            # GPIO.output(ADclk_port, 1)
            # GPIO.output(ADclk_port, 0)

    AD_start_botn = input("Please enter ad : ")
    if AD_start_botn == "ad":
        pass
        # GPIO.output(ADstart_triger, 1)
        # GPIO.output(ADstart_triger, 0)
    else:
        print("Please enter ad")


##########################################################


s = "s"
ms = "ms"
us = "us"
t = "t"

pulse_info = []

# 変な関数


def bousenn():
    print("--------------------------------------------------")


for i in range(2):
    def_width_pulse = int(input("Please enter width_pulse only number : "))
    bousenn()
    def_unit = str(input("Please enter pulse unit(s,ms,us) : "))
    bousenn()
    def_through = int(input("if through ON enter 1 , through OFF enter 0 : "))
    bousenn()

    default_info = [def_width_pulse, def_unit, def_through]
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


def change_ms_to_s(widthpulse, unit, through):
    if through == 1:
        if unit == "s":
            return widthpulse
        elif unit == "ms":
            return (widthpulse / 1000)
    else:
        return change_format(change_unit(widthpulse, unit))


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
        while dataloop_counter < len(data_list):
            for j in data_list[dataloop_counter]:
                if j == 1:
                    pass
                    # GPIO.output(data_port, 1)
                    # GPIO.output(clk_port, 1)
                    # GPIO.output(clk_port, 0)
                else:
                    pass
                    # GPIO.output(data_port, 0)
                    # GPIO.output(clk_port, 1)
                    # GPIO.output(clk_port, 0)

            dataloop_counter += 1
            # print(dataloop_counter)

while through_OFFcounter + through_ONcounter < len(pulse_info):
    if pulse_info[through_ONcounter + through_OFFcounter][2] == 1:
        print()
        through_botn = input("Please enter  t  : ")
        if through_botn == "t":
            # GPIO.output(through_port, 1)
            sleep(through_widthpulse[through_ONcounter])
            # GPIO.output(through_port, 0)

        else:
            print("Please enter t")
            continue

        through_ONcounter += 1
        # print("through_ONcounter  : %d " % through_ONcounter)

    else:
        print()
        start_botn = input("Please enter s  : ")
        if start_botn == "s":
            pass
            # GPIO.output(start_triger, 1)
            # GPIO.output(start_triger, 0)
        else:
            print("Please enter s")
            continue

        through_OFFcounter += 1
        # print("through_OFFcounter  :  %d " % through_OFFcounter)

print()
bousenn()
print("How many times do you repeat ?")
loop_times = int(input("Please enter loop number : "))
bousenn()
print()

for i in range(loop_times):
    next_data = []  # 次のパルス情報を初期化
    next_width_pulse = int(input("Please enter width_pulse only number : "))
    bousenn()
    next_unit = str(input("Please enter pulse unit(s,ms,us) : "))
    bousenn()
    next_through = int(input("if through ON enter 1 , through OFF enter 0 : "))
    bousenn()

    next_info = [next_width_pulse, next_unit, next_through]
    print(next_info)

    valiable_num = change_ms_to_s(next_width_pulse, next_unit, next_through)
    if type(valiable_num) == list:
        next_data = valiable_num
        print(next_data)
    elif type(valiable_num) == int or type(valiable_num) == float:
        sleep_time = valiable_num
        print(str(next_width_pulse) + "[" + next_unit + "]" + "幅のパルスが出力されます")

    bousenn()

    for k in next_data:
        if k == 1:
            pass
            # GPIO.output(data_port, 1)
            # GPIO.output(clk_port, 1)
            # GPIO.output(clk_port, 0)

        else:
            pass
            # GPIO.output(data_port, 0)
            # GPIO.output(clk_port, 1)
            # GPIO.output(clk_port, 0)

    if next_through == 1:  # through ONのとき
        print()
        through_botn = input("Please enter  t  : ")
        print()
        if through_botn == "t":
            # GPIO.output(through_port, 1)
            sleep(sleep_time)
            # GPIO.output(through_port, 0)
        else:
            print("Please enter t")
            continue

    else:
        print()
        start_botn = input("Please enter s  : ")
        print()
        if start_botn == "s":
            pass
            # GPIO.output(start_triger, 1)
            # GPIO.output(start_triger, 0)
        else:
            print("Please enter s")
            continue


# #GPIO.cleanup()
