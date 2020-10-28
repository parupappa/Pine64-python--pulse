
import struct
import math
import platform
#import RPi.GPIO as GPIO
from time import sleep
# GPIO.setmode(GPIO.BCM)

data_poat = 17
enable_poat = 27
start_poat = 22

#GPIO.setup(data_poat, GPIO.OUT)
#GPIO.setup(enable_poat, GPIO.OUT)
#GPIO.setup(start_poat, GPIO.OUT)

width_pulse = int(input("出力したいパルス幅を数字のみで入力してください : "))
print("パルス幅:%d" % width_pulse)
print("--------------------------------------------------")
unit = input("パルス幅の単位を入力してください(s,ms,us,ns) : ")

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

for i in data_16bit:
    #GPIO.output(data_poat, int(i))
    sleep(0.01)
#GPIO.output(enable_poat, 1)
print("データ送信とFPGAへのデータセットをしました")
print("--------------------------------------------------")


print("start信号を送信します")
print("--------------------------------------------------")

#GPIO.output(start_poat, 1)
print("送信しました")
print("--------------------------------------------------")
