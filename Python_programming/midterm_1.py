'''
학번: 2016116457
이름: 박범진
1. 패스워드 검사 프로그램
'''


def input_password():
    password = input("패스워드를 입력하시오: ")
    while True:
        numAlpha = 0
        numDigit = 0
        numSpace = 0
        for word in password:
            if word.isalpha():
                numAlpha += 1
            elif word.isdigit():
                numDigit += 1
            elif word.isspace():
                numSpace += 1
        if numAlpha == 8 and numDigit == 2 and numSpace == 0:
            print("패스워드가 정상입니다.")
            break
        else:
            print("잘못된 패스워드입니다. 다시 입력하세요")
            print("알파벳 개수: " + str(numAlpha))
            print("숫자 개수: " + str(numDigit))
            print("공백 개수: " + str(numSpace))
        password = input("패스워드를 다시 입력하시오: ")


input_password()
