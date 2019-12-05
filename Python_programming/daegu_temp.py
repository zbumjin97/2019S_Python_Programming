'''
학번: 2016116457
이름: 박범진
대구의 기온 분석
'''

import csv

f = open('daegu.csv', encoding='euc_kr')
data = csv.reader(f)
header = next(data)
jun = 0
jun_temp = 0
jul = 0
jul_temp = 0
aug = 0
aug_temp = 0
sep = 0
sep_temp = 0
dec = 0
dec_temp = 0
jan = 0
jan_temp = 0
feb = 0
feb_temp = 0
for row in data:
    if 1970 <= int(row[0].split(".")[0]) <= 2018:
        if int(row[0].split(".")[1]) == 6:
            if row[4] != "":
                jun_temp += float(row[4])
                jun += 1
        elif int(row[0].split(".")[1]) == 7:
            if row[4] != "":
                jul_temp += float(row[4])
                jul += 1
        elif int(row[0].split(".")[1]) == 8:
            if row[4] != "":
                aug_temp += float(row[4])
                aug += 1
        elif int(row[0].split(".")[1]) == 9:
            if row[4] != "":
                sep_temp += float(row[4])
                sep += 1
        elif int(row[0].split(".")[1]) == 12:
            if row[3] != "":
                dec_temp += float(row[3])
                dec += 1
        elif int(row[0].split(".")[1]) == 1:
            if row[3] != "":
                jan_temp += float(row[3])
                jan += 1
        elif int(row[0].split(".")[1]) == 2:
            if row[3] != "":
                feb_temp += float(row[3])
                feb += 1
        else:
            continue
f.close()

avg_hightemp = []
avg_lowtemp = []
avg_hightemp.append(round(jun_temp / jun, 2))
avg_hightemp.append(round(jul_temp / jul, 2))
avg_hightemp.append(round(aug_temp / aug, 2))
avg_hightemp.append(round(sep_temp / sep, 2))
avg_lowtemp.append(round(dec_temp / dec, 2))
avg_lowtemp.append(round(jan_temp / jan, 2))
avg_lowtemp.append(round(feb_temp / feb, 2))

for i in range(len(avg_hightemp)):
    if avg_hightemp[i] == max(avg_hightemp):
        mon_hightemp = i + 6
for i in range(len(avg_lowtemp)):
    if avg_lowtemp[i] == min(avg_lowtemp):
        if i == 0:
            mon_lowtemp = 12
        else:
            mon_lowtemp = i

print("여름철 평균기온:")
print("6월 평균 기온:", avg_hightemp[0], "도")
print("7월 평균 기온:", avg_hightemp[1], "도")
print("8월 평균 기온:", avg_hightemp[2], "도")
print("9월 평균 기온:", avg_hightemp[3], "도")
print("대구에서 가장 더운 달은 %d월이고, 평균기온은 %.2f도 였습니다." % (mon_hightemp, round(max(avg_hightemp), 2)))
print()

print("겨울철 평균 기온:")
print("12월 평균 기온:", avg_lowtemp[0], "도")
print("1월 평균 기온:", avg_lowtemp[1], "도")
print("2월 평균 기온:", avg_lowtemp[2], "도")
print("대구에서 가장 추운 달은 %d월이고, 평균기온은 %.2f도 였습니다." % (mon_lowtemp, round(min(avg_lowtemp), 2)))
