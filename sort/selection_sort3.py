import random

list = []
for i in range(50):
    a = random.randint(1, 100)
    while a in list:
        a = random.randint(1, 100)
    list.append(a)


def selection_sort(list):
    for i in range(len(list)):
        min = list[i]
        for j in range(i, len(list) - 1):
            if min > list[j + 1]:
                min, list[j + 1] = list[j + 1], min
        list[i] = min
    return list


print(selection_sort(list))
