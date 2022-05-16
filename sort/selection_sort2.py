# list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
# list = [7, 3, 4, 0, 2, 6, 8, 9, 1]
# list = [7, 3, 4, 0, 2, 6, 8, 9, 1]
list = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(list) - 1):
    min_index = i
    for j in range(i + 1, len(list)):
        if list[min_index] > list[j]:
            min_index = j
    list[i], list[min_index] = list[min_index], list[j]
    print(list)

print(list)
