# -*- coding: utf-8 -*-

import csv
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
typenamelist0 = []
typenamelist = []


for n in range(24, 38):  # 右の値30,38を指定すれば繰り返し回数、つまりDDSの個数を指定出来る
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
        # print(DDS_40set)  # DDSの40bit部分のデータ

    elif n % 8 == 5:  # DDSとtypenameの文字列を合体させる
        col_value = sheet.col_values(int(n))
        del col_value[0:3]
        typenamelist0 = [s for s in col_value if s != '']  # col_value内の’’を削除
        typenamelist.append(typenamelist0)
        typenamelist = [s for row in typenamelist for s in row]  # リスト内リストを外す
        # print(typenamelist)

for m in range(len(typenamelist)):
    DDSname = DDS_nscset[m][0]
    DDS_nscset[m][0] = (DDSname + typenamelist[m])
# [['DDS1A', 20], ['DDS1B', 24], ['DDS2A', 20], ['DDS2B', 80]]
# print(DDS_nscset)


# 40bitのDDSdataを16進数10bitに変換

hexdata = ''  # hexは16進の意味
DDSdata_hex = []  # 16進数10bitのDDSdata
DDSdata = []  # 0埋めした16進数16bitのDDSdata
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

for n in range(len(DDSdata_hex)):
    DDSdata.append(DDSdata_hex[n].zfill(16))
# print(DDSdata)


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


#######################################################################################################


# カウント値操作部分

countlist = []

for k in range(len(countlist0)):
    # *100:[1us]単位のカウント値 *10000:[1カウント100us] *
    countlist.append(countlist0[k] * 10000)
    countlist[k] = format(countlist[k], 'b').zfill(32)  # 2進数に変換して32桁になるように0埋め
# print(countlist) #カウント値　32桁の2進数表記

#################################################################################################


# 対象操作部分

targetRF1 = []
targetRF2 = []
targetRF3 = []
targetAD1 = []
targetAD2 = []
targetAD3 = []
targetDDS1A = []
targetDDS1B = []
targetDDS1C = []
targetDDS1D = []
targetDDS1E = []
targetDDS2A = []
targetDDS2B = []
targetDDS2C = []
targetDDS2D = []
targetDDS2E = []

for tl in targetlist0:
    if 'RF1' in tl:
        a = '1'
        targetRF1.append(a)
    else:
        a = '0'
        targetRF1.append(a)
    if 'RF2' in tl:
        b = '1'
        targetRF2.append(b)
    else:
        b = '0'
        targetRF2.append(b)
    if 'RF3' in tl:
        c = '1'
        targetRF3.append(c)
    else:
        c = '0'
        targetRF3.append(c)

    if 'AD1' in tl:
        d = '1'
        targetAD1.append(d)
    else:
        d = '0'
        targetAD1.append(d)
    if 'AD2' in tl:
        e = '1'
        targetAD2.append(e)
    else:
        e = '0'
        targetAD2.append(e)
    if 'AD3' in tl:
        f = '1'
        targetAD3.append(f)
    else:
        f = '0'
        targetAD3.append(f)

    if 'DDS1A' in tl:
        g = '1'
        targetDDS1A.append(g)
    else:
        g = '0'
        targetDDS1A.append(g)
    if 'DDS1B' in tl:
        h = '1'
        targetDDS1B.append(h)
    else:
        h = '0'
        targetDDS1B.append(h)
    if 'DDS1C' in tl:
        i = '1'
        targetDDS1C.append(i)
    else:
        i = '0'
        targetDDS1C.append(i)
    if 'DDS1D' in tl:
        k = '1'
        targetDDS1D.append(k)
    else:
        k = '0'
        targetDDS1D.append(k)
    if 'DDS1E' in tl:
        l = '1'
        targetDDS1E.append(l)
    else:
        l = '0'
        targetDDS1E.append(l)

    if 'DDS2A' in tl:
        m = '1'
        targetDDS2A.append(m)
    else:
        m = '0'
        targetDDS2A.append(m)
    if 'DDS2B' in tl:
        n = '1'
        targetDDS2B.append(n)
    else:
        n = '0'
        targetDDS2B.append(n)
    if 'DDS2C' in tl:
        o = '1'
        targetDDS2C.append(o)
    else:
        o = '0'
        targetDDS2C.append(o)
    if 'DDS2D' in tl:
        p = '1'
        targetDDS2D.append(p)
    else:
        p = '0'
        targetDDS2D.append(p)
    if 'DDS2E' in tl:
        q = '1'
        targetDDS2E.append(q)
    else:
        q = '0'
        targetDDS2E.append(q)


bitsdata = []

for j in range(len(targetlist0)):
    v_data = targetDDS2E[j] + targetDDS2D[j] + targetDDS2C[j] + targetDDS2B[j] + targetDDS2A[j] + \
        targetDDS1E[j] + targetDDS1D[j] + targetDDS1C[j] + targetDDS1B[j] + targetDDS1A[j] + \
        targetAD3[j] + targetAD2[j] + targetAD1[j] + \
        targetRF3[j] + targetRF2[j] + targetRF1[j]
    bitsdata.append(v_data.zfill(32))  # 32桁　000000・・・・　あれば1　なければ0表示
# print(bitsdata)

################################################################################################

DDSinfo = []  # DDSのデータ数＋1を16桁の16進数で表記
l_start = [s for s in targetlist0 if s.startswith('D')]
DDScounter = len(l_start) + 1
DDSinfo.append(format(DDScounter, 'x').zfill(16))  # 16進数で16桁表記
# print(DDSinfo)

###################################################################################################

# データ連結部分
# データを16進数に変換

# bitsdata[32bit] + countlist[32bit]を合体させ64bitのデータを生成

Pulsedata = []

for c in range(len(bitsdata)):
    pulsedata = (bitsdata[c] + countlist[c])
    Pulsedata.append(pulsedata)
# print(Pulsedata) #64ビットの[bitsdata + countlist0]

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
print(Pulsedata_hex)  # 64bitのPulsedataを16bitの16進数に変換

################################################################################################

# アドレスデータ部分
addresslist = []
for d in range(1 + len(DDSdata) + len(Pulsedata_hex)):
    addresslist.append(format(d, 'x').zfill(5))
print(addresslist)  # 5桁の16進数表記


# 全データを指定の二次元配列の形に直す部分
csvdata = []

start_csvlist = [addresslist[0], DDSinfo[0]]
csvdata.append(start_csvlist)
# print(csvdata) #先頭アドレスとDDSの数データ

for i in range(len(DDSdata_hex)):
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
