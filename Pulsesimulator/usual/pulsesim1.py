# DDS40bit  データのシミュレーション
if pf == 'Linux':
    dds_csv = open(
        '/home/ubuntu/Documents/Python/Pine64-python--pulse/Pulsesimulator/pulse_simDDSdata.csv')
elif pf == 'Darwin':
    dds_csv = open(
        '/Users/yokooannosuke/Cording/Pine64-python--pulse/Pulsesimulator/pulse_simDDSdata.csv')

DDS = [26, 19]
DDS_sc1 = []
DDSsc1_int = []
DDS_data = []
DDS_list = []

for i in range(len(DDS)):
    GPIO.setup(DDS[i], GPIO.OUT)


for row in csv.reader(dds_csv):
    DDS_sc1.append(row[0])
    DDS_data.append(row[4])
del DDS_sc1[0:3]
del DDS_data[0:3]

# 読み込んだデータをint型に変換
for i in range(len(DDS_sc1)):
    DDSsc1_int.append(int(DDS_sc1[i]))

    # 40bitdataを一文字ずつにして配列に格納
    chars = list(DDS_data[i].strip())
    DDS_list.append(chars)
# 読み込んだ配列をint型に変換
for j in range(len(DDS_list)):
    for i in range(len(DDS_list[0])):
        if str == type(DDS_list[j][i]):
            DDS_list[j][i] = (int(DDS_list[j][i]))
# print(DDS_list)