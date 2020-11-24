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


s = "s"
"""
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


data_16bit = list(format(count_value, 'b').zfill(16))
print(data_16bit)
"""

test_data = [1,0,1,0,1,0,1,0,1,0,1,0,1,0,1,0]

for i in test_data:
    if i == 1:
        GPIO.output(data_poat, 1)
        sleep(0.1)
        
        GPIO.output(enable_poat, 1)
        sleep(1)
        GPIO.output(enable_poat, 0)
        sleep(1)
        
        
        
    else:
        GPIO.output(data_poat, 0)
        sleep(0.1)
        
        GPIO.output(enable_poat, 1)
        sleep(1)
        GPIO.output(enable_poat, 0)
        sleep(1)
        
    
start_botn = input("please push s  : " )
if start_botn == "s":
    GPIO.output(start_poat, 1)
    sleep(1)
    GPIO.output(start_poat, 0)

else:
    print("plese push s")





GPIO.cleanup()
