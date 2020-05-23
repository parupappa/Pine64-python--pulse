# -*- coding: utf-8 -*-

import xlrd
import pprint


wb = xlrd.open_workbook(
    '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulseprogramer/ver2/pulsedata.xlsm')
# print(type(wb))  #Bookオブジェクトを取得
sheet = wb.sheet_by_name('Sheet1')
# print(type(sheet)) #sheetオブジェクトを取得

# Excelファイルの行(row)列(col)の先頭は0行0列

# まずはver1のプログラムを生かせる形にExcelファイルを読み込む

# RFの部分のみについて取り出しとsortを行う
RF1 = 'RF1'
RF2 = 'RF2'
RF3 = 'RF3'
RFnamelist = [RF1, RF2, RF3]

col_nvalue = []
RF_scset = []
RF_nscset = []
RF_ecset = []
RF_necset = []

for n in range(3):  # 3,7,11を指定すれば繰り返し回数、つまりRFの個数を指定出来る
    if n % 4 == 0:  # sc 0,4,8行目
        # col_valuesの長さは常にsheet.nrowsに等しい 。つまり、sheetの一番下の行数となってしまう
        col_value = sheet.col_values(int(n))
        del col_value[0:3]
        col_nvalue = [s for s in col_value if s != '']  # col_value内の’’を削除
        # print(col_nvalue)
        for m in range(len(col_nvalue)):
            a = col_nvalue[m]
            b = int(a)
            RF_scset.append(RFnamelist[int(n/4)])
            RF_scset.append(b)
            RF_nscset.append(RF_scset)
            RF_scset = []
        # print(RF_nscset) #RFのsc部分のデータ [[RF1,0],...[RF3,12]]

    elif (n - 2) % 4 == 0:  # ec 2,6,10行目
        col_value = sheet.col_values(int(n))
        del col_value[0:3]
        col_nvalue = [s for s in col_value if s != '']
        # print(col_nvalue)
        for m in range(len(col_nvalue)):
            c = col_nvalue[m]
            d = int(c)
            RF_ecset.append('')  # ecの方は何も入れない
            RF_ecset.append(d)
            RF_necset.append(RF_ecset)
            RF_ecset = []
        # print(RF_necset)  #RFのec部分のデータ　[['',2],...['',18]]

allRFdatalist = RF_nscset + RF_necset
# print(allRFdatalist)  # [['RF1', 0], ['', 2], ... ['', 18]]


##################################################################

# ADの部分のみについて取り出し、sortを行う

AD1 = 'AD1'
AD2 = 'AD2'
AD3 = 'AD3'
ADnamelist = [AD1, AD2, AD3]

col_nvalue = []
AD_scset = []
AD_nscset = []
AD_ecset = []
AD_necset = []

for n in range(12, 15):  # 右の値15,19,23を指定すれば繰り返し回数、つまりADの個数を指定出来る
    if n % 4 == 0:  # sc 12,16,20行目
        col_value = sheet.col_values(int(n))
        del col_value[0:3]
        col_nvalue = [s for s in col_value if s != '']  # col_value内の’’を削除
        for m in range(len(col_nvalue)):
            a = col_nvalue[m]
            b = int(a)
            AD_scset.append(ADnamelist[int(n/4 - 3)])
            AD_scset.append(b)
            AD_nscset.append(AD_scset)
            AD_scset = []
        # print(AD_nscset)  # RFのsc部分のデータ [[RF1,0],...[RF3,12]]

    elif (n - 2) % 4 == 0:  # ec 14,18,22行目
        col_value = sheet.col_values(int(n))
        del col_value[0:3]
        col_nvalue = [s for s in col_value if s != '']  # col_value内の’’を削除
        for m in range(len(col_nvalue)):
            c = col_nvalue[m]
            d = int(c)
            AD_ecset.append('')  # ecの方は何も入れない
            AD_ecset.append(d)
            AD_necset.append(AD_ecset)
            AD_ecset = []
        # print(AD_necset)  # RFのec部分のデータ　[['',2],...['',18]]

allADdatalist = AD_nscset + AD_necset
# print(allADdatalist)  # [['AD1', 10], ['', 1], ... ]

#####################################################################################


# DDSの部分のみについて取り出し、scと40bitデータを16進数に直し分けて格納

DDS1 = 'DDS1'
DDS2 = 'DDS2'
DDSnamelist = [DDS1, DDS2]

col_nvalue = []
DDS_scset = []
DDS_nscset = []
DDS_40set = []


for n in range(24, 37):  # 右の値29,37を指定すれば繰り返し回数、つまりDDSの個数を指定出来る
    if n % 8 == 0:  # 24(Y),32(AG)行目 #8にしないと28（AC）が含まれちゃう
        col_value = sheet.col_values(int(n))
        del col_value[0:3]
        col_nvalue = [s for s in col_value if s != '']  # col_value内の’’を削除
        for m in range(len(col_nvalue)):
            a = col_nvalue[m]
            b = int(a)
            DDS_scset.append(DDSnamelist[int(n/8 - 3)])
            DDS_scset.append(b)
            DDS_nscset.append(DDS_scset)
            DDS_scset = []
        # print(DDS_nscset)  # RFのsc部分のデータ [[RF1,0],...[RF3,12]]

    elif n % 8 == 4:  # 40bitdata 28(AC),36(AK)行目
        col_value = sheet.col_values(int(n))
        del col_value[0:3]
        col_nvalue = [s for s in col_value if s != '']  # col_value内の’’を削除
        for m in range(len(col_nvalue)):
            bitdata_40 = col_nvalue[m]
            DDS_40set.append(bitdata_40)
        print(DDS_40set)  # DDSの40bit部分のデータ


# 40bitのDDSdataを16進数10bitに変換

hexdata = ''
DDSdata_hex = []  # 16進数10bitのDDSdata
n = 0
for m in range(len(DDS_40set)):
    str = DDS_40set[m]
    hexdata = ''
    n = 0
    while n + 3 < 40:
        four_str = str[n:n + 4]
        four_int = int("0b"+four_str, 0)  # 2進数four_strを数値に変換
        hex_str = format(four_int, 'x')  # 数値four_intを16進数に変換
        hexdata = hexdata + hex_str
        n = n + 4
    DDSdata_hex.append(hexdata)  # 4bitずつ16進数に変換
print(DDSdata_hex)  # 40bitのDDS_40setを10bitの16進数に変換


####################################################################################################

# RF,AD,DDSの統合を行う

allRFADDDSdatalist = allRFdatalist + allADdatalist + DDS_nscset
allRFADDDSdatalist.sort(key=lambda count: count[1])  # count順になるようにsort
# print(allRFADDDSdatalist) # [['RF1', 0], ['', 2]....['DDS1', 20], ['DDS2', 20], ['DDS1', 24], ['DDS2', 80]]


# 対象とカウント値に分割
targetlist0 = []
countlist0 = []

for n in range(len(allRFADDDSdatalist)):
    targetlist0.append(allRFADDDSdatalist[n][0])
    countlist0.append(allRFADDDSdatalist[n][1])

# print(targetlist0)  # ['RF1', '', 'RF1', '', 'AD1', '']
# print(countlist0)  # [0, 2, 5, 9, 10, 11]
