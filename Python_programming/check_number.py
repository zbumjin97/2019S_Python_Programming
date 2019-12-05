'''
학번: 2016116457
이름: 박범진
주민등록번호 정상 판별 프로그램
'''


class CheckNum:
    def __init__(self, num):
        self.num = num

    def input_num(self):
        self.num = input("주민등록번호를 숫자만 입력하세요: ")
        if len(self.num) > 13:
            print("주민등록번호가 13자리 보다 큽니다. 다시 입력하세요.")
            return False
        elif len(self.num) < 13:
            print("입력된 숫자의 자리수가 13자리 이하입니다. 다시 입력하세요")
            return False
        elif "-" in self.num:
            print("-를 빼고 다시 입력하세요.")
            return False
        elif " " in self.num:
            print("공백 문자가 포함되었습니다. 다시 입력하세요.")
            return False
        else:
            for item in self.num:
                if item.isalpha():
                    print("알파벳 문자가 포함되었습니다. 다시 입력하세요.")
                    return False
            return True

    def distinguish(self):
        error_check = 2*int(self.num[0]) + 3*int(self.num[1]) + 4*int(self.num[2]) + 5*int(self.num[3])\
                     + 6*int(self.num[4]) + 7*int(self.num[5]) + 8*int(self.num[6]) + 9*int(self.num[7])\
                     + 2*int(self.num[8]) + 3*int(self.num[9]) + 4*int(self.num[10]) + 5*int(self.num[11])
        if int(self.num[12]) != (11 - error_check % 11) % 10:
            print("불법 생성된 주민등록번호입니다.")
            return False
        return True

    def is_correct(self):
        print("정상적인 주민등록번호입니다.")
        age = 2019 - int("19" + self.num[0] + self.num[1])
        if age < 19:
            print("성인 인증이 실패하였습니다.")
            return False
        local = int(self.num[7] + self.num[8])
        if 0 <= local <= 8:
            location = "서울"
        elif 9 <= local <= 12:
            location = "부산"
        elif 13 <= local <= 15:
            location = "인천"
        elif 16 <= local <= 25:
            location = "경기"
        elif 26 <= local <= 34:
            location = "강원"
        elif 35 <= local <= 47:
            location = "충청"
        elif 48 <= local <= 66:
            location = "전라"
        elif 67 <= local <= 91:
            location = "경상"
        elif 92 <= local <= 95:
            location = "제주"
        else:
            print("출생지 인증이 실패하였습니다.")
            return False
        birth = ""
        for i in range(6):
            birth += self.num[i]
        print("성인 인증이 되었습니다. 나이", age, "세")
        print("주민등록번호:", self.num)
        print("생년월일:", birth)
        print("출생지:", location)


myNum = CheckNum("")
while True:
    if myNum.input_num():
        if myNum.distinguish():
            myNum.is_correct()
        break
