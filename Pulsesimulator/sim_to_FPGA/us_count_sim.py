# -*- coding: utf-8 -*-

import math
import platform
import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BCM)

data_poat = 17
enable_poat = 27
start_poat = 22


GPIO.setup(data_poat, GPIO.OUT)
GPIO.setup(enable_poat, GPIO.OUT)
GPIO.setup(start_poat, GPIO.OUT)

"""
s = "s"
ms = "ms"
us = "us"

width_pulse = int(input("please input width_pulse only number : " ))
print("width_pulse:%d" % width_pulse)
print("--------------------------------------------------")
unit = str(input("please input pulse unit(s,ms,us,ns) : "))

if unit == "s":
    count_value = width_pulse * (10**6) * 10
elif unit == "ms":
    count_value = width_pulse * (10 ** 3) * 10
elif unit == "us":
    count_value = width_pulse * 10
elif unit == "ns":
    count_value = width_pulse / 100


data_8bit = list(format(count_value, 'b').zfill(8))

print(data_8bit)

"""

test_data = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]

for i in test_data:
    GPIO.output(data_poat, int(i))
    sleep(0.5)
    GPIO.output(enable_poat, 1)
    print("enable_poat output")

print("set of permit_data ")
print("--------------------------------------------------")


print("will translate start_signal")
print("--------------------------------------------------")

GPIO.output(start_poat, 1)
print("done")
print("--------------------------------------------------")

GPIO.output(data_poat, 0)
GPIO.output(enable_poat, 0)
GPIO.output(start_poat, 0)

GPIO.cleanup()
