import random

count = int(input("주사위를 던질 회수를 입력하세요 (100 이상): "))
if count >= 100:
    sum1 = 0
    sum2 = 0
    sum3 = 0
    sum4 = 0
    sum5 = 0
    sum6 = 0
    for i in range(count):
        num = random.randint(1, 6)
        if num == 1:
            sum1 += 1
        if num == 2:
            sum2 += 1
        if num == 3:
            sum3 += 1
        if num == 4:
            sum4 += 1
        if num == 5:
            sum5 += 1
        if num == 6:
            sum6 += 1
    print("주사위면 1: {0}회/{1}, 확률: {2}".format(sum1, count, round(sum1 / count, 3)))
    print("주사위면 2: {0}회/{1}, 확률: {2}".format(sum2, count, round(sum2 / count, 3)))
    print("주사위면 3: {0}회/{1}, 확률: {2}".format(sum3, count, round(sum3 / count, 3)))
    print("주사위면 4: {0}회/{1}, 확률: {2}".format(sum4, count, round(sum4 / count, 3)))
    print("주사위면 5: {0}회/{1}, 확률: {2}".format(sum5, count, round(sum5 / count, 3)))
    print("주사위면 6: {0}회/{1}, 확률: {2}".format(sum6, count, round(sum6 / count, 3)))
else:
    print("100 이상의 숫자를 입력하세요. 종료합니다.")