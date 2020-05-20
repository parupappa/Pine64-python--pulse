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
allRFdatalist.sort(key=lambda num: num[1])  # count順になるようにsort
# print(allRFdatalist)  # [['RF1', 0], ['', 2], ... ['', 18]]

RFlist = []
RFcountlist = []
for n in range(len(allRFdatalist)):  # RFとカウント値に分割
    RFlist.append(allRFdatalist[n][0])
    RFcountlist.append(allRFdatalist[n][1])
print(RFlist)  # ['RF1', '', 'RF1', '', 'RF1', '']
print(RFcountlist)  # [0, 2, 5, 9, 12, 18]


##################################################################

# ADの部分のみについて取り出し、sortを行う
n = 0
m = 0
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
            AD_scset.append(ADnamelist[m])
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
allADdatalist.sort(key=lambda num: num[1])  # count順になるようにsort
# print(allADdatalist)  # [['AD1', 0], ['', 2], ... ['', 18]]


ADlist = []
ADcountlist = []
for n in range(len(allADdatalist)):  # RFとカウント値に分割
    ADlist.append(allADdatalist[n][0])
    ADcountlist.append(allADdatalist[n][1])
print(ADlist)  # ['RF1', '', 'RF1', '', 'RF1', '']
print(ADcountlist)  # [0, 2, 5, 9, 12, 18]

#####################################################################################