'''
학번: 2016116457
이름: 박범진
RandomIntList 클래스 구현
'''

import random


class RandomIntList(list):
    def __init__(self, start, end):
        self.start = start
        self.end = end
        for i in range(self.start, self.end + 1):
            self.append(random.randint(self.start, self.end))

    def __repr__(self):
        text = ""
        arraytext = "["
        for i in range(len(self)):
            text += "[%2d]" % i
        for i in range(len(self)):
            arraytext += "%2d" % self[i]
            if i != len(self) - 1:
                arraytext += ", "
        arraytext += "]"
        return "%s\n%s" % (text, arraytext)

    def replace(self, old, new):
        cnt = 0
        for i in range(len(self)):
            if self[i] == old:
                self[i] = new
                cnt += 1
        if cnt == 0:
            print("%d가 리스트에 없습니다." % old)
        else:
            print("%d개의 %d가 %d로 교체되었습니다." % (cnt, old, new))

    def dremove(self):
        cnt = 0
        for i in range(len(self)):
            for j in range(i + 1, len(self)):
                if self[i] == self[j]:
                    self[i] = " "
                    cnt += 1
                    break
        for i in range(len(self)):
            if " " in self:
                self.remove(" ")
        self.end -= cnt

    def removeall(self, x):
        cnt = 0
        for i in range(len(self)):
            if x in self:
                self.remove(x)
                cnt += 1
        self.end -= cnt
        if cnt == 0:
            print("%d가 리스트에 없습니다." % x)
        else:
            print("%d를 %d개 삭제하였습니다." % (x, cnt))


def main():
    main_text = input("RandomIntList 생성(시작과 끝을 입력하세요): ")
    start = int(main_text.split()[0])
    end = int(main_text.split()[1])
    random_list = RandomIntList(start, end)
    while True:
        print(random_list)
        print()
        print("RandomIntList 테스트")
        print("1. 리스트 출력")
        print("2. replace(old, new)")
        print("3. dremove(): 중복 item 제거")
        print("4. removeall(x): 모든 x 삭제")
        print("5. 종료")
        select = int(input("메뉴를 선택하세요: "))
        if select == 1:
            continue
        elif select == 2:
            text = input("교체할 숫자 (old, new) 입력(공백 구분): ")
            old = int(text.split()[0])
            new = int(text.split()[1])
            random_list.replace(old, new)
        elif select == 3:
            random_list.dremove()
        elif select == 4:
            removal = int(input("삭제할 숫자를 입력하세요: "))
            random_list.removeall(removal)
        elif select == 5:
            break


main()

