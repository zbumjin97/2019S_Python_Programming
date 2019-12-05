'''
학번: 2016116457
이름: 박범진
과제명: 카드게임
'''


import random

card_number = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
card_suit = ["♠", "♥", "♣", "◆"]


def calculate_score(list):
    player = 0
    for i in range(len(list)):
        if list[i][0] == "♣":
            player += 4 * list[i][1]
        elif card[i][0] == "♠":
            player += 3 * list[i][1]
        elif card[i][0] == "◆":
            player += 2 * list[i][1]
        elif card[i][0] == "♥":
            player += 1 * list[i][1]
    return player


card = []
for i in range(4):
    for j in range(13):
        card.append(tuple([card_suit[i], card_number[j]]))


print("초기 카드 생성")
for i in range(52):
    print(card[i], end="")
    if i % 13 == 12:
        print()

print("Shuffle Card")
random.shuffle(card)
for i in range(len(card_suit) * len(card_number)):
    print("('"+card[i][0]+"', "+str(card[i][1])+") ", end="")
    if i % len(card_number) == len(card_number) - 1:
        print()

print("Dealing three cards")
random.shuffle(card)

p1 = []
p2 = []
for i in range(6):
    if i % 2 == 0:
        p1.append(card[-i-1])
    else:
        p2.append(card[-i-1])

print("Player1:", p1)
print("Player2:", p2)
score_p1 = calculate_score(p1)
score_p2 = calculate_score(p2)
print("Player1:", score_p1, ", Player2:", score_p2)
if score_p1 > score_p2:
    print("Player1 Win")
elif score_p1 < score_p2:
    print("Player2 Win")
else:
    print("Draw")
