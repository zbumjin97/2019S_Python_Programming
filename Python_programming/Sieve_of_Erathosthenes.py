'''
학번: 2016116457
이름: 박범진
과제명: 에라토스테네스의 체
'''


def main():
    num_list = []
    for i in range(99):
        num_list.append(i + 2)
    print_original(num_list)
    remove_number(num_list, 2)
    remove_number(num_list, 3)
    remove_number(num_list, 5)
    remove_number(num_list, 7)
    print_list(num_list)


def print_original(num_list):
    print("Original number =>")
    for i in range(99):
        print("{0:4s}".format(str(num_list[i])), end="")
        if i % 10 == 9:
            print()
    print()


def remove_number(num_list, num):
    print("Remove {0}'s multiple numbers".format(num))
    for i in range(99):
        if (i + 2) % num == 0 and i != num - 2:
            num_list[i] = 'X'
        print("{0:4s}".format(str(num_list[i])), end="")
        if i % 10 == 9:
            print()
    print()
    return num_list


def print_list(num_list):
    print("Prime numbers:")
    for i in range(99):
        print("{0:4s}".format(str(num_list[i])), end="")
        if i % 10 == 9:
            print()
    print()


main()
