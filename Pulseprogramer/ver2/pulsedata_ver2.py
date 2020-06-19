# -*- coding: utf-8 -*-

# 設定するパラメータ　PL AD DDS の繰り返し回数と　1カウントをどの長さにするかのカウント値部分

import csv
import xlrd
import pprint
import platform

pf = platform.system()

if pf == 'Windows':
    wb = xlrd.open_workbook(
        'C:/Users/NITGC-E/Desktop/Tokken/Python/Pine64-python--pulse/Pulseprogramer/ver2/pulsedata.xlsx')
# print(pattern(wb))  #Bookオブジェクトを取得
    sheet1 = wb.sheet_by_name('Pulseパラメータ')

elif pf == 'Darwin':
    wb = xlrd.open_workbook(
        '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulseprogramer/ver2/pulsedata.xlsx')
# print(pattern(wb))  #Bookオブジェクトを取得
    sheet1 = wb.sheet_by_name('Pulseパラメータ')
# print(pattern(sheet)) #sheetオブジェクトを取得


# Excelファイルの行(row)列(col)の先頭は0行0列

# まずはver1のプログラムを生かせる形にExcelファイルを読み込む

# PLの部分のみについて取り出しとsortを行う
PL1 = 'PL1'
PL2 = 'PL2'
PL3 = 'PL3'
PLnamelist = [PL1, PL2, PL3]

col_nvalue = []
PL_scset = []
PL_nscset = []
PL_ecset = []
PL_necset = []

for n in range(3):  # 3,7,11を指定すれば繰り返し回数、つまりPLの個数を指定出来る
    if n % 4 == 0:  # sc 0,4,8行目
        # col_valuesの長さは常にsheet.nrowsに等しい 。つまり、sheetの一番下の行数となってしまう
        col_value = sheet1.col_values(int(n))
        del col_value[0:3]
        col_nvalue = [s for s in col_value if s != '']  # col_value内の’’を削除
        # print(col_nvalue)
        for m in range(len(col_nvalue)):
            a = col_nvalue[m]
            b = int(a)
            PL_scset.append(PLnamelist[int(n/4)])
            PL_scset.append(b)
            PL_nscset.append(PL_scset)
            PL_scset = []
        # print(PL_nscset) #PLのsc部分のデータ [[PL1,0],...[PL3,12]]

    elif (n - 2) % 4 == 0:  # ec 2,6,10行目
        col_value = sheet1.col_values(int(n))
        del col_value[0:3]
        col_nvalue = [s for s in col_value if s != '']
        # print(col_nvalue)
        for m in range(len(col_nvalue)):
            c = col_nvalue[m]
            d = int(c)
            PL_ecset.append('')  # ecの方は何も入れない
            PL_ecset.append(d)
            PL_necset.append(PL_ecset)
            PL_ecset = []
        # print(PL_necset)  #PLのec部分のデータ　[['',2],...['',18]]

allPLdatalist = PL_nscset + PL_necset
# print(allPLdatalist)  # [['PL1', 0], ['', 2], ... ['', 18]]


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
        col_value = sheet1.col_values(int(n))
        del col_value[0:3]
        col_nvalue = [s for s in col_value if s != '']  # col_value内の’’を削除
        for m in range(len(col_nvalue)):
            a = col_nvalue[m]
            b = int(a)
            AD_scset.append(ADnamelist[int(n/4 - 3)])
            AD_scset.append(b)
            AD_nscset.append(AD_scset)
            AD_scset = []
        # print(AD_nscset)  # PLのsc部分のデータ [[PL1,0],...[PL3,12]]

    elif (n - 2) % 4 == 0:  # ec 14,18,22行目
        col_value = sheet1.col_values(int(n))
        del col_value[0:3]
        col_nvalue = [s for s in col_value if s != '']  # col_value内の’’を削除
        for m in range(len(col_nvalue)):
            c = col_nvalue[m]
            d = int(c)
            AD_ecset.append('')  # ecの方は何も入れない
            AD_ecset.append(d)
            AD_necset.append(AD_ecset)
            AD_ecset = []
        # print(AD_necset)  # PLのec部分のデータ　[['',2],...['',18]]

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
patternnamelist0 = []
patternnamelist = []
patternnamelist_int = []


if pf == 'Windows':
    wb = xlrd.open_workbook(
        'C:/Users/NITGC-E/Desktop/Tokken/Python/Pine64-python--pulse/Pulseprogramer/ver2/pulsedata.xlsx')
# print(pattern(wb))  #Bookオブジェクトを取得
    sheet2 = wb.sheet_by_name('DDSパラメータ')

elif pf == 'Darwin':
    wb = xlrd.open_workbook(
        '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulseprogramer/ver2/pulsedata.xlsx')
# print(pattern(wb))  #Bookオブジェクトを取得
    sheet2 = wb.sheet_by_name('DDSパラメータ')
# print(pattern(sheet)) #sheetオブジェクトを取得


"""
wb = xlrd.open_workbook(
    '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulseprogramer/ver2/pulsedata.xlsx')
# print(pattern(wb))  #Bookオブジェクトを取得
sheet2 = wb.sheet_by_name('DDSパラメータ')
"""
for n in range(7):  # 7だけか、右の値 0, 14 を指定すれば繰り返し回数、つまりDDSの個数を指定出来る
    if n % 8 == 0:  # 0(A),8(I)行目
        col_value = sheet2.col_values(int(n))
        del col_value[0:3]
        col_nvalue = [s for s in col_value if s != '']  # col_value内の’’を削除
        for m in range(len(col_nvalue)):
            a = col_nvalue[m]
            b = int(a)
            DDS_scset.append(DDSnamelist[int(n/8)])
            DDS_scset.append(b)
            DDS_nscset.append(DDS_scset)
            DDS_scset = []
        # print(DDS_nscset)  # PLのsc部分のデータ [[PL1,0],...[PL3,12]]

    elif n % 8 == 4:  # 40bitdata 4(E),12(M)行目
        col_value = sheet2.col_values(int(n))
        del col_value[0:3]
        col_nvalue = [s for s in col_value if s != '']  # col_value内の’’を削除
        for m in range(len(col_nvalue)):
            bitdata_40 = col_nvalue[m]
            DDS_40set.append(bitdata_40)
        # print(DDS_40set)  # DDSの40bit部分のデータ

    elif n % 8 == 5:  # DDSとpatternnameの文字列を合体させる
        col_value = sheet2.col_values(int(n))
        del col_value[0:3]
        # col_value内の’’を削除
        patternnamelist0 = [s for s in col_value if s != '']
        patternnamelist_int = [int(m) for m in patternnamelist0]
        patternnamelist_str = [str(l) for l in patternnamelist_int]
        patternnamelist.append(patternnamelist_str)
        patternnamelist = [
            s for row in patternnamelist for s in row]  # リスト内リストを外す
        # print(patternnamelist)

for m in range(len(patternnamelist)):
    DDSname = DDS_nscset[m][0]
    DDS_nscset[m][0] = (DDSname + patternnamelist[m])
# [['DDS11', 20], ['DDS12', 24], ['DDS21', 20], ['DDS22', 80]]
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

# PL,AD,DDSの統合を行う

allPLADDDSdatalist = allPLdatalist + allADdatalist + DDS_nscset
allPLADDDSdatalist.sort(key=lambda count: count[1])  # count順になるようにsort
# [['PL1', 0], ['', 2]....['DDS1', 20], ['DDS2', 20], ['DDS1', 24], ['DDS2', 80]]
# print(allPLADDDSdatalist)


#################################################################################################
# allPLADDDSdatalistの被り部分を統合

allPLADDDSdatalist_new = []

i = 0
while i < len(allPLADDDSdatalist):
    j = 1
    while i + j < len(allPLADDDSdatalist):
        if allPLADDDSdatalist[i + j][1] != allPLADDDSdatalist[i][1]:
            break
        allPLADDDSdatalist[i][0] = allPLADDDSdatalist[i][0] + \
            allPLADDDSdatalist[i + j][0]
        j += 1
    allPLADDDSdatalist_new.append(allPLADDDSdatalist[i])
    i = i + j
# print(allPLADDDSdatalist_new)

#################################################################################################

# 対象とカウント値に分割
targetlist0 = []
countlist0 = []

for n in range(len(allPLADDDSdatalist_new)):
    targetlist0.append(allPLADDDSdatalist_new[n][0])
    countlist0.append(allPLADDDSdatalist_new[n][1])

# print(targetlist0)  # ['PL1', '', 'PL1', '', 'AD1', '']
# print(countlist0)  # [0, 2, 5, 9, 10, 11]


#######################################################################################################


# カウント値操作部分

countlist = []

for k in range(len(countlist0)):
    # *100:[1us]単位のカウント値 *10000:[1カウント100us] *100000000[1count :1s]
    countlist.append(countlist0[k] * 100000000)
    countlist[k] = format(countlist[k], 'b').zfill(32)  # 2進数に変換して32桁になるように0埋め
# print(countlist) #カウント値　32桁の2進数表記

#################################################################################################


# 対象操作部分

targetPL1 = []
targetPL2 = []
targetPL3 = []
targetAD1 = []
targetAD2 = []
targetAD3 = []
targetDDS11 = []
targetDDS12 = []
targetDDS13 = []
targetDDS14 = []
targetDDS15 = []
targetDDS16 = []
targetDDS17 = []
targetDDS18 = []
targetDDS21 = []
targetDDS22 = []
targetDDS23 = []
targetDDS24 = []
targetDDS25 = []
targetDDS26 = []
targetDDS27 = []
targetDDS28 = []


for tl in targetlist0:
    if 'PL1' in tl:
        a = '1'
        targetPL1.append(a)
    else:
        a = '0'
        targetPL1.append(a)
    if 'PL2' in tl:
        b = '1'
        targetPL2.append(b)
    else:
        b = '0'
        targetPL2.append(b)
    if 'PL3' in tl:
        c = '1'
        targetPL3.append(c)
    else:
        c = '0'
        targetPL3.append(c)

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

    if 'DDS11' in tl:
        g = '1'
        targetDDS11.append(g)
    else:
        g = '0'
        targetDDS11.append(g)
    if 'DDS12' in tl:
        h = '1'
        targetDDS12.append(h)
    else:
        h = '0'
        targetDDS12.append(h)
    if 'DDS13' in tl:
        i = '1'
        targetDDS13.append(i)
    else:
        i = '0'
        targetDDS13.append(i)
    if 'DDS14' in tl:
        k = '1'
        targetDDS14.append(k)
    else:
        k = '0'
        targetDDS14.append(k)
    if 'DDS15' in tl:
        l = '1'
        targetDDS15.append(l)
    else:
        l = '0'
        targetDDS15.append(l)
    if 'DDS16' in tl:
        l = '1'
        targetDDS16.append(l)
    else:
        l = '0'
        targetDDS16.append(l)
    if 'DDS17' in tl:
        l = '1'
        targetDDS17.append(l)
    else:
        l = '0'
        targetDDS17.append(l)
    if 'DDS18' in tl:
        l = '1'
        targetDDS18.append(l)
    else:
        l = '0'
        targetDDS18.append(l)

    if 'DDS21' in tl:
        m = '1'
        targetDDS21.append(m)
    else:
        m = '0'
        targetDDS21.append(m)
    if 'DDS22' in tl:
        n = '1'
        targetDDS22.append(n)
    else:
        n = '0'
        targetDDS22.append(n)
    if 'DDS23' in tl:
        o = '1'
        targetDDS23.append(o)
    else:
        o = '0'
        targetDDS23.append(o)
    if 'DDS24' in tl:
        p = '1'
        targetDDS24.append(p)
    else:
        p = '0'
        targetDDS24.append(p)
    if 'DDS25' in tl:
        q = '1'
        targetDDS25.append(q)
    else:
        q = '0'
        targetDDS25.append(q)
    if 'DDS26' in tl:
        q = '1'
        targetDDS26.append(q)
    else:
        q = '0'
        targetDDS26.append(q)
    if 'DDS27' in tl:
        q = '1'
        targetDDS27.append(q)
    else:
        q = '0'
        targetDDS27.append(q)
    if 'DDS28' in tl:
        q = '1'
        targetDDS28.append(q)
    else:
        q = '0'
        targetDDS28.append(q)


bitsdata = []

for j in range(len(targetlist0)):
    v_data = targetDDS28[j] + targetDDS27[j] + targetDDS26[j] + targetDDS25[j] + targetDDS24[j] + targetDDS23[j] + targetDDS22[j] + targetDDS21[j] + \
        targetDDS18[j] + targetDDS17[j] + targetDDS16[j] + targetDDS15[j] + targetDDS14[j] + targetDDS13[j] + targetDDS12[j] + targetDDS11[j] + \
        targetAD3[j] + targetAD2[j] + targetAD1[j] + \
        targetPL3[j] + targetPL2[j] + targetPL1[j]
    bitsdata.append(v_data.zfill(32))  # 32桁　000000・・・・　あれば1　なければ0表示
print(bitsdata)

################################################################################################
"""
DDSinfo = []  # DDSのデータ数＋1を16桁の16進数で表記
l_start = [s for s in targetlist0 if s.startswith('D')]
DDScounter = len(l_start) + 1
DDSinfo.append(format(DDScounter, 'x').zfill(16))  # 16進数で16桁表記
# print(DDSinfo)
"""
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
# print(Pulsedata_hex)  # 64bitのPulsedataを16bitの16進数に変換

################################################################################################

# アドレスデータ部分
addresslist = []
for d in range(16 + len(Pulsedata_hex)):
    addresslist.append(format(d, 'x').zfill(5))
# print(addresslist)  # 5桁の16進数表記


#############################################################################################

# 全データを指定の二次元配列の形に直す部分
csvdata = []
"""
start_csvlist = [addresslist[0], DDSinfo[0]]
csvdata.append(start_csvlist)
# print(csvdata) #先頭アドレスとDDSの数データ
"""

for i in range(len(DDSdata_hex)):
    csvdata0 = []
    csvdata0 = [addresslist[i], DDSdata[i]]
    csvdata.append(csvdata0)
# print(csvdata)  # DDSの部分までのCSV


for j in range(len(Pulsedata_hex)):
    csvdata1 = []
    csvdata1 = [addresslist[16 + j], Pulsedata_hex[j]]
    csvdata.append(csvdata1)
# print(csvdata) #全CSVdata


# CSVファイル生成部分

with open("outdata_ver2.csv", "w")as f:
    writer = csv.writer(f, lineterminator="\n")
    writer.writerows(csvdata)
