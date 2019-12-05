'''
학번: 2016116457
이름: 박범진
대구 일교차분석
'''

import csv
import matplotlib.pyplot as plt

f = open('daegu.csv', encoding='euc_kr')
data = csv.reader(f)
header = next(data)
temp = 0
divisor = 0
matrix = [[0 for col in range(12)] for row in range(10)]
i = 1
j = 2009
for row in data:
    year = int(row[0].split(".")[0])
    month = int(row[0].split(".")[1])
    day = int(row[0].split(".")[2])
    if 2009 <= year <= 2018:
        if i != month:
            if j == year:
                matrix[year - 2009][month - 2] = round(temp / divisor, 1)
            else:
                matrix[year - 2010][11] = round(temp / divisor, 1)
                j = year
            i = month
            temp = 0
            divisor = 0
        if row[3] != "" and row[4] != "":
            temp += float(row[4]) - float(row[3])
            divisor += 1
f.close()

xaxis = []
for p in range(len(matrix)):
    for q in range(len(matrix[p])):
        if max(matrix[p]) == matrix[p][q]:
            xaxis.append("{0}.{1}".format(p + 2009, q + 1))
list = []
print("대구 월별 평균 일교차")
for i in range(10):
    list.append(max(matrix[i]))
    print("{0}: {1}".format(xaxis[i], list[i]))

plt.rc('font', family='Malgun Gothic')
plt.title("2009년부터 2018년까지 대구의 평균 일교차가 가장 큰 달")
plt.rcParams['axes.unicode_minus'] = False
plt.bar(xaxis, list, color='b')
plt.show()
