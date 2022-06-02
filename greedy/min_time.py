list = [3, 1, 4, 3, 2]


def min_time(list):
    list.sort()
    total_time = 0
    time = 0
    for i in list:
        time += i
        total_time += time

    return total_time


def min_time2(list):
    list.sort()
    minimum = 0
    for i in range(len(list)):
        print(i)
        for j in range(i + 1):
            print("    ", list[j])
            minimum += list[j]
    return minimum


min_time2(list)


print(min_time(list))
