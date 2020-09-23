import csv

fname_Dar = '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulsesimulator/usual/pulse_simdata.csv'
csvfile = open(fname_Dar)

a = []
for row in csv.reader(csvfile):
    a.append(row[1])  # 取得したい列番号を指定（0始まり）
print(a)
