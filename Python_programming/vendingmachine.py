'''
학번: 2016116457
이름: 박범진
과제명: 커피 자판기 프로그램
'''


def show_menu():
    print("------------------------------------")
    print("        커피 자판기 (300원)")
    print("1. 블랙 커피")
    print("2. 프림 커피")
    print("3. 설탕 프림 커피")
    print("4. 재고 현황")
    print("5. 종료")
    choice = int(input("메뉴를 선택하세요: "))
    return choice


def exit_program():
    print("---------------------------")
    print("커피 자판기 동작을 종료합니다.")
    print("---------------------------")


def provide_coffee(insert):
    money = 10000
    water = 1000
    coffee = 500
    prim = 500
    sugar = 500
    cup = 30
    while insert >= 300:
        choice = show_menu()
        if choice == 1:
            if water >= 100 and coffee >= 30 and cup >= 1:
                insert -= 300
                money += 300
                water -= 100
                coffee -= 30
                cup -= 1
                print("블랙 커피를 선택하셨습니다. 잔돈:", insert)
            else:
                print("재고가 부족해서 종료합니다.")
                break
        elif choice == 2:
            if water >= 100 and coffee >= 15 and prim >= 15 and cup >= 1:
                insert -= 300
                money += 300
                water -= 100
                coffee -= 15
                prim -= 15
                cup -= 1
                print("프림 커피를 선택하셨습니다. 잔돈:", insert)
            else:
                print("재고가 부족해서 종료합니다.")
                break
        elif choice == 3:
            if water >= 100 and coffee >= 10 and prim >= 10 and sugar >= 10 and cup >= 1:
                insert -= 300
                money += 300
                water -= 100
                coffee -= 10
                prim -= 10
                sugar -= 10
                cup -= 1
                print("설탕 프림 커피를 선택하셨습니다. 잔돈:", insert)
            else:
                print("재고가 부족해서 종료합니다.")
                break
        elif choice == 4:
            print("------------------------------------")
            print("재고 현황:")
            print("커피:", coffee, "g, 프림:", prim, "g, 설탕:", sugar, "g")
            print("물:", water, "ml, 종이컵:", cup, "개")
            print("자판기 남은 돈:", money, "원, 잔돈 현황:", insert, "원")
        elif choice == 5:
            break
        else:
            print("메뉴를 다시 선택하세요.")
        if insert < 300:
            print("잔돈이 부족해서 종료합니다.")
            break
    return insert


def main():
    insert = int(input("동전을 투입하세요: "))
    if insert >= 300:
        provide_coffee(insert)
        exit_program()
    else:
        print("돈이 부족합니다 ", insert, "원:")
        exit_program()


main()
