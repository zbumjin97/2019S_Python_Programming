import csv
import matplotlib.pyplot as plt

male_count = []
female_count = []
district_list = ['대구광역시 중구', '대구광역시 동구', '대구광역시 서구', '대구광역시 남구', '대구광역시 북구',
                 '대구광역시 수성구', '대구광역시 달서구', '대구광역시']
population_list = []
for i in range(len(district_list)):
    f = open('gender.csv')
    data = csv.reader(f)
    for row in data:
        if district_list[i] in row[0]:
            male_count.append(int(row[1].replace(',', '')))
            female_count.append(int(row[104].replace(',', '')))
            break
    f.close()

population_list = [[0 for col in range(2)] for row in range(8)]
for i in range(8):
    population_list[i][0] = male_count[i]
    population_list[i][1] = female_count[i]

plt.rc('font', family='Malgun Gothic')
fig, axes = plt.subplots(2, 4, figsize=(12, 6), sharex=True, sharey=True)
fig.suptitle('대구 남녀 인구 비율', fontsize=20)
color = ['cornflowerblue', 'tomato']
for i in range(8):
    if 0 <= i <= 3:
        axes[0, i].pie(population_list[i], labels=['남성', '여성'], autopct='%.1f%%', colors=color, startangle=90)
        axes[0, i].set_title(district_list[i])
    else:
        axes[1, i-4].pie(population_list[i], labels=['남성', '여성'], autopct='%.1f%%', colors=color, startangle=90)
        if i == 7:
            axes[1, i-4].set_title(district_list[i] + "전체")
        else:
            axes[1, i-4].set_title(district_list[i])

plt.show()
