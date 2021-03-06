# -*- coding: utf-8 -*-

import csv


# カウント値操作部分

countlist = []

with open("pulsedata_in.csv", "r") as Pulsedata:
    for row in csv.reader(Pulsedata):
        countlist.append(row[0])
    del countlist[0]
    countlist = [int(i) for i in countlist]
    # print(countlist) #純粋なカウント値のみの配列

countlist1 = []

for k in range(len(countlist)):
    countlist1.append(countlist[k] * 10000)  # [us]単位のカウント値
    countlist1[k] = format(countlist1[k], 'b').zfill(
        32)  # 2進数に変換して32桁になるように0埋め
# print(countlist1) #カウント値　32桁の2進数表記


# 対象操作部分

targetlist = []

with open("pulsedata_in.csv", "r") as Pulsedata:
    for row in csv.reader(Pulsedata):
        targetlist.append(row[1])
    del targetlist[0]
    # print(targetlist) #純粋な対象部分のみの配列

targetRF = []
targetDDS = []
targetAD = []

for tl in targetlist:
    if 'RF' in tl:
        i = '1'
        targetRF.append(i)
    else:
        i = '0'
        targetRF.append(i)

    if 'DDS' in tl:
        j = '1'
        targetDDS.append(j)
    else:
        j = '0'
        targetDDS.append(j)

    if 'AD' in tl:
        k = '1'
        targetAD.append(k)
    else:
        k = '0'
        targetAD.append(k)

# print(targetRF)    RFがあれば1　なければ0の文字列の配列
# print(targetDDS)
# print(targetAD)

bitsdata = []

for b in range(len(targetRF)):
    s1 = targetRF[b]
    s2 = targetDDS[b]
    s3 = targetAD[b]
    s = s1 + s2 + s3
    bitsdata.append(s.zfill(32))  # 32桁　000000・・・・・RFDDSAD　あれば1　なければ0表示
# print(bitsdata)

# DDS動作部分

DDSdatalist = []
DDSdata = []

with open("pulsedata_in.csv", "r") as Pulsedata:
    for row in csv.reader(Pulsedata):
        DDSdatalist.append(row[2])
    del DDSdatalist[0]
    for n in DDSdatalist:
        if n != '':
            DDSdata.append(n.zfill(16))  # 16桁になるように0埋め
    # print(DDSdata)　#DDSのデータがある所に対して、16桁の16進数表記


DDSinfo = []
a = 1
for dl in targetlist:
    if 'DDS' in dl:
        a = a + 1
DDSinfo.append(format(a, 'x').zfill(16))  # 16進数で16桁表記
# print(DDSinfo) #DDSのデータ数＋1を16桁の16進数で表記


# データ連結部分
# データを16進数に変換

Pulsedata = []

for c in range(len(bitsdata)):
    P1 = countlist1[c]
    P2 = bitsdata[c]
    P = P2 + P1
    Pulsedata.append(P)
# print(Pulsedata) #64ビットの[bitsdata + countlist1]

hexdata = ''
Pulsedata_hex = []
n = 0
for m in range(len(Pulsedata)):
    str = Pulsedata[m]
    hexdata = ''
    n = 0
    while n + 3 < 64:
        four_str = str[n:n+4]
        four_int = int("0b"+four_str, 0)
        hex_str = format(four_int, 'x')
        hexdata = hexdata + hex_str
        n = n + 4
    Pulsedata_hex.append(hexdata)  # 4bitずつ16進数に変換
# print(Pulsedata_hex)  #64bitのPulsedataを16bitの16進数に変換


# アドレスデータ部分
addresslist = []
for d in range(1 + len(DDSdata) + len(Pulsedata_hex)):
    addresslist.append(format(d, 'x').zfill(5))
# print(addresslist) #5桁の16進数表記


# 全データを指定の二次元配列の形に直す部分
csvdata = []

start_csvlist = [addresslist[0], DDSinfo[0]]
csvdata.append(start_csvlist)
# print(csvdata) #先頭アドレスとDDSの数データ

for i in range(len(DDSdata)):
    csvdata0 = []
    csvdata0 = [addresslist[i+1], DDSdata[i]]
    csvdata.append(csvdata0)
# print(csvdata) #DDSの部分までのCSV


for j in range(len(Pulsedata_hex)):
    csvdata1 = []
    csvdata1 = [addresslist[len(DDSdata) + j + 1], Pulsedata_hex[j]]
    csvdata.append(csvdata1)
# print(csvdata) #全CSVdata


# CSVファイル生成部分

with open("pulsedata_out.csv", "w")as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerows(csvdata)


# GPIO.cleanup()
