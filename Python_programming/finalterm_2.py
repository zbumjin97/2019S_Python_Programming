'''
학번: 2016116457
이름: 박범진
2. dictionary 자료를 정렬하는 함수를 람다식을 이용하여 구현하시오.
'''


def dsort(dic, index, desc):
    if index == 0:
        dic = sorted(dic.items(), key=(lambda x: x[0]), reverse=desc)
    else:
        try:
            dic = sorted(dic.items(), key=(lambda x: x[1][index - 1]), reverse=desc)
        except IndexError:
            print('index:{0}는 존재하지 않아서 정렬을 무시합니다.'.format(index))
    return dict(dic)


dic1 = {'d': ('Peter', 40), 'b': ('Marie', 32), 'a': ('Luna', 49), 'c': ('John', 29)}
dic2 = {1: ('Java', 50, 'C'), 3: ('C++', 70, 'B'), 2: ('Python', 90, 'A'), 4: ('Android', 30, 'D')}
dic3 = {201901: ('Java', 50, 60, 10), 201802: ('Network', 40, 55, 5), 201801: ('Python', 35, 80, 15)}
dic1 = dsort(dic1, 3, False)
print("dic1 index 3: ", dic1)
# key 기준으로 정렬, True: 내림차순, False: 오름차순
dic1 = dsort(dic1, 0, False)
print("dic1 index 0: ", dic1)
# key 기준으로 정렬
dic1 = dsort(dic1, 1, True)
print("dic1 index 1: ", dic1)
# key 기준으로 정렬
dic1 = dsort(dic1, 2, False)
print("dic1 index 2: ", dic1)
print()
# dict2 정렬
dic2 = dsort(dic2, 0, False)
print("dic2 index 0: ", dic2)
dic2 = dsort(dic2, 2, False)
print("dic2 index 2: ", dic2)
dic2 = dsort(dic2, 3, False)
print("dic2 index 3: ", dic2)
dic2 = dsort(dic2, 4, False)
print("dic2 index 4: ", dic2)
print()
dic3 = dsort(dic3, 4, False)
print("dic3 index 4: ", dic3)
