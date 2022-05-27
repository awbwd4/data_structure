import random

list = []

for i in range(50):
    a = random.randint(1, 100)
    while a in list:
        a = random.randint(1, 100)
    list.append(a)


def insert_sort(list):
    for i in range(1, len(list)):
        for j in range(i, 0, -1):
            if list[j] < list[j - 1]:
                list[j], list[j - 1] = list[j - 1], list[j]
    return list


print(insert_sort(list))
