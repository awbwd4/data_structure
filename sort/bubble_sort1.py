# list = [4, 3, 10, 9, 11]
list = [1, 3, 9, 2]


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
        for j in range(0, i - 1):
            if list[j] > list[j + 1]:
                swap(list[j], list[j + 1])
                count += 1
                print(list)


def swap(a, b):
    a, b = b, a


bubble_sort2(list)
print(list)
