n = 5
array = [3, 1, 4, 3, 2]

minimum = 0


array.sort()


for index in range(n):
    for index2 in range(index + 1):
        minimum += array[index2]

print(minimum)
