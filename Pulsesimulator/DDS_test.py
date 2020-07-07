# -*- coding: utf-8 -*-
import platform
import csv
pf = platform.system()


if pf == 'Linux':
    dds_csv = open(
        '/home/ubuntu/Documents/Python/Pine64-python--pulse/Pulsesimulator/pulse_simDDSdata.csv')
elif pf == 'Darwin':
    dds_csv = open(
        '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulsesimulator/pulse_simDDSdata.csv')


DDS = [26]
DDS_sc1 = []
DDSsc1_int = []
DDS_data = []
chars_new = []

for row in csv.reader(dds_csv):
    DDS_sc1.append(row[0])
    DDS_data.append(row[4])
del DDS_sc1[0:3]
del DDS_data[0:3]

for i in range(len(DDS_data)):
    DDSsc1_int.append(int(DDS_sc1[i]))

    chars = list(DDS_data[i].strip())
    chars_new.append(chars)
# print(chars_new)
chars_int = [int(s) for s in chars_new]
print(chars_int)


for i in range(len(chars_new)):
    for j in range(len(chars)):
        #GPIO.output(DDS[0], chars_new[i][j])
        print("%d回目です" % j)
