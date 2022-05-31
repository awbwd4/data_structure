import random


def split(list):
    if len(list) == 1:
        return list
    # 반으로 쪼개기
    mid = int(len(list) // 2)
    list_left = list[0:mid]
    list_right = list[mid : int(len(list))]
    print("list1 : ", list_left)
    print("list2 : ", list_right)
    return True


def mergeSplitFunc(list):
    if len(list) == 1:
        print(list[0])
        return list
    # 반으로 쪼개기
    mid = int(len(list) // 2)
    list_left = mergeSplitFunc(list[0:mid])
    list_right = mergeSplitFunc(list[mid : len(list)])

    print("left ", list_left)
    print("right ", list_right)

    return merge(list_left, list_right)


def merge(list1, list2):
    result = []
    i = 0
    j = 0
    while i < len(list1) and j < len(list2):
        if list1[i] < list2[j]:
            result.append(list1[i])
            i += 1
        else:
            result.append(list2[j])
            j += 1

    while i < len(list1):
        result.append(list1[i])
        i += 1

    while j < len(list2):
        result.append(list2[j])
        j += 1
    print("     merge result : ", result)
    return result


list1 = [1, 2, 4, 7, 10, 11]
list2 = [5, 5, 7, 9]

# list = [4, 1, 2, 7, 11, 12, 5, 7, 5, 9]

list = []

for i in range(100):
    a = random.randint(0, 99)
    list.append(a)


# print(merge(list1, list2))

mergeSplitFunc(list)
