n = int(input())

# array = [0 for i in range(n+1)]
array = [0]*(n+1)

array[1] = 1
array[2] = 2

for i in range(3,n+1):
    array[i] = array[i-1]+array[i-2]


print(array[int(input())]%1007)
