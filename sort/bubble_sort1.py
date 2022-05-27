import random


# list = [4, 3, 10, 9, 11]
list = []
for i in range(50):
    a = random.randint(1, 100)
    while a in list:  # 생성한 난수가 list에 있는 숫자라면 계속 반복
        a = random.randint(1, 100)  # 위의 조건이 참이라면 난수를 다시 생성
    list.append(a)  # 위에서 중복에 걸리지 않은 숫자가 나올경우 리스트에 추가해줌.


def bubble_sort(list):
    while True:
        count = 0
        for i in range(0, len(list) - 1):
            if list[i] > list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
                count += 1
        print(list)
        if count == 0:
            break


def bubble_sort2(list):
    for i in range(0, len(list) - 1):
        count = 0
        for j in range(0, len(list) - i - 1):
            print(j)
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                count += 1
                print(list)
        if count == 0:
            break


def swap(a, b):
    a, b = b, a


bubble_sort2(list)
print(list)
