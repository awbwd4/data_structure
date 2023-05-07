import random

n = int(input())

data_list = random.sample(range(100), n)

print(data_list)

for i in range(len(data_list)-1):
    swap = False
    for j in range(len(data_list)-1-i):
        if data_list[j] > data_list[j+1]:
            data_list[j],data_list[j+1] = data_list[j+1], data_list[j]
            swap = True
    if not swap:
        break

print(data_list)
