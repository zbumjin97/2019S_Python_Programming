'''
학번: 2016116457
이름: 박범진
1. 서울 지하철 역에서 출근 시간대에 사람들이 가장 많이 내리는 역 5개를 막대 그래프로
표현하시오.
'''

import csv
import matplotlib.pyplot as plt
import platform

f = open('subwaytime.csv', encoding='utf-8')
data = csv.reader(f)
next(data)
next(data)
name = []
getout = []
subway_dict = dict()
xaxis = []
yaxis = []
for row in data:
    row[4:] = map(int, row[4:])
    num = 0
    for i in range(len(name)):
        if name[i] == row[3]:
            getout[i] += row[11] + row[13] + row[15]
            num = 1
            break
    if num == 0:
        name.append(row[3])
        getout.append(row[11] + row[13] + row[15])
if platform.system() == 'Windows':
    plt.rc('font', family='Malgun Gothic')
else:
    plt.rc('font', family='AppleGothic')
for i in range(len(name)):
    subway_dict[name[i]] = getout[i]
subway_dict = sorted(subway_dict.items(), key=(lambda x: x[1]), reverse=True)

for i in range(5):
    xaxis.append(subway_dict[i][0])
    yaxis.append(subway_dict[i][1])
    print("{0}: {1}".format(xaxis[i], format(yaxis[i], ',')))

plt.title("서울 지하철 출근 시간대 하차 인원 비교")
plt.bar(xaxis, yaxis, color='b')
plt.ylabel('인원')
plt.show()
