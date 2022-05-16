# list = list(map(int, input()))


list = [7, 3, 4, 0, 2, 6, 8, 9, 1]

min = list[0]

for i in range(len(list)):
    print("[%i]" % i)
    min = list[i]
    for j in range(i, len(list)):
        if min > list[j]:
            min = list[j]
            min_index = j
            print("      min[%d]  , min_index[%d] " % (min, min_index))
    list[i], list[min_index] = list[j], list[min_index]
    print("     ", list)
print(list)
