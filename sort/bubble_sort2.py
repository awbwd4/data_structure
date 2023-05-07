n = int(input())
array = list()

for _ in range(n):
    array.append(int(input()))

print(array)


# for i in range(len(array)-1):

#     if array[i] > array[i+1]:
#         array[i], array[i+1] = array[i+1], array[i]

# print(array)


for i in range(len(array)-1):
    swap = False
    for j in range(len(array)-1-i):
        if array[j]>array[j+1]:
            swap = True
            array[j], array[j+1] = array[j+1], array[j]
    if not swap :
        break 


print(array)
