'''
학번: 2016116457
이름: 박범진
2. Tongue Twister 문장 분석
'''


def print_split():
    message = "Peter Piper picked a peck of pickled peppers. A peck of pickled peppers Peter Piper picked."
    print("Original String:", message)
    msg_list = ""
    for word in message:
        if word != ".":
            msg_list += word
    msg_list = sorted(msg_list.split())
    print("Split String:", msg_list)
    print()
    return msg_list


def convert_dict(msg_list):
    msg_dict = dict()
    i = 0
    while i < len(msg_list):
        cnt = 1
        for j in range(1, 3):
            if i + j < len(msg_list):
                if msg_list[i + j] == msg_list[i]:
                    cnt += 1
                else:
                    break
        msg_dict[msg_list[i]] = cnt
        i += cnt
    return msg_dict


def repeat_word(msg_dict):
    print("단어 반복 회수 분석: ")
    for item in msg_dict:
        print(item, ":", msg_dict[item])
    print()


def convert_set_dict(msg_list):
    print("<<< Convert List -> Set -> Dictionary>>>")
    msg_set = set(msg_list)
    print("List to Set:", msg_set)
    return msg_set


def main():
    msg_list = print_split()
    print("<<< Convert List to Dictionary >>>")
    msg_dict = convert_dict(msg_list)
    print("List to Dict:", msg_dict)
    repeat_word(msg_dict)
    msg_set = convert_set_dict(msg_list)
    print("Set to Dict:", convert_dict(list(msg_set)))


main()
