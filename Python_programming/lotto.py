'''
학번: 2016116457
이름: 박범진
과제명: 로또 번호 생성 프로그램
'''

import random

def create_lotto_number():
    purchase_number = 1
    random_num = random.randint(1, 45)
    while purchase_number != 0:
        purchase_number = int(input("로또를 몇장 구매하시겠습니까? "))
        if purchase_number == 0:
            print("종료합니다.")
            break
        print("로또 번호")
        for i in range(purchase_number):
            print("[ %d ]: " % (i+1), end=" ")
            for j in range(6):
                random_num = random.randint(1, 45)
                print("%2s" % str(random_num), end=" ")
            print()

create_lotto_number()

