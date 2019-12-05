# 2019S_Python_Programming
2019학년도 여름학기 파이선 프로그래밍


---
### dice.py
* 주사위를 던져서 각 면이 나오는 횟수 및 확률을 구하는 프로그램을 작성하시오.
* - 화면상에서 주사위를 던질 회수를 입력하면 그 회수만큼 for 문장을 이용하여 반복하
면서 랜덤하게 1에서 6까지의 숫자 생성한다.
* - 최소 100회 이상 주사위를 던질 숫자를 입력하고, 100회 보다 작은 수를 입력하는 경
우 프로그램을 종료함
* - 주사위를 던지는 횟수가 많아질 수록 각 면이 나오는 확률이 1/6 (약 0.167)이 되는지
확인 하시오. (확률 계산은 소수점 3자리까지 계산)


---
### lotto.py
* 로또 번호 생성 프로그램
* 로또 번호는 1에서 45까지 총 45개의 숫자 중에서 6개의 숫자로 구성되어 있다.
* 구입할 로또 개수를 입력 받고, 해당 개수 만큼 로또 번호를 생성함:
* - random_num = randint(시작숫자, 마지막 숫자) 사용
* 랜덤하게 생성된 각 숫자는 문자열로 변환하여 아래와 같이 문자열을 생성함
* - 문자열 변환함수: str(숫자)
* - 문자열 자리수: “%2s” % 문자열
* 개수 입력에서 0을 입력할 때까지 반복함 (while문 사용)
* 중첩 for 문장 사용
* - 구매 개수 만큼 반복하기 위한 for문
* - 6개의 숫자를 랜덤 생성하기 위한 for문


---
### vendingmachine.py
* 커피 자판기 프로그램
* 화면상에 메뉴를 출력함 (종료를 선택할 때까지 반복, while문 사용)
* - 1. 블랙커피, 2: 프림커피, 3: 설탕프림 커피, 4: 재고현황, 5: 종료
* - 커피 가격은 모두 300원으로 동일함
* 초기 자판기 상황
* - 자판기 동전: 10000원 (모두 100원짜리 100개 보유)
* - 물: 1000ml
* - 커피: 500g, 프림: 500g, 설탕: 500g, 종이컵 30개
* 메뉴에 따른 커피, 설탕, 프림 소모량
* - 블랙커피: 커피 30g + 물 100ml
* - 프림커피: 커피 15g + 프림 15g + 물 100ml
* - 설탕커피: 커피 10g + 프림 10g + 설탕 10g + 물 100ml
* 재고현황
* - 커피 재고량, 프림 재고량, 설탕 재고량, 컵 재고량, 잔여 물용량 출력
* - 잔돈 현황 출력 (입출금 관리)


---
### Class_4 (2019.05.09)
* Graphic User Interface
* BorderLayout, FlowLayout, GridLayout, etc.
* Label, TextField, and Button


---
### Class_5 (2019.05.16)
* Event-driven Programming
* Lambda Expression
* Mouse & MouseMotion Event Listener


---
### Class_6 (2019.05.23)
* File Input/Output
* Byte Stream & Character Stream
* File Object Serialization


---
### Class_7 (2019.05.30)
* Inheritance of Thread Class
* Implementation of Runnable Interface
* Synchronization
