list = [1, 2, 3, 4, 5]
i = len(list) - 1


def sum(i):
    if i == 0:
        return list[0]
    return list[i] + sum(i - 1)


sum = sum(i)
print(sum)


def sum2(list):
    if len(list) == 1:
        return list[0]
    return list[0] + sum2(list[1 : len(list)])


print(list[1 : len(list)])

print(sum2(list))
