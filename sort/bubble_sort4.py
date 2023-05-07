import random
n = int(input())

data_list = random.sample(range(100, n))

# n = int(input())
array = list()

for i in range(n):
    array.append(int(input()))


for i in range(len(array)-1):
    switch = False
    for j in range(len(array)-i-1):
        if array[j] > array[j+1]:
            array[j],array[j+1] = array[j+1],array[j]
            switch = True
    if not switch:
        break

print(array)