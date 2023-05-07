import random

n = int(input())

array = random.sample(range(100), n)



def quick_sort(array:list):
    if len(array) <= 1 : return array

    left, right = list(), list()
    
    pivot = array[0]

    for i in range(1, len(array)):
        if array[i] > pivot : 
            right.append(array[i])
        else : 
            left.append(array[i])

    return quick_sort(left)+[pivot]+quick_sort(right)




print(quick_sort(array))



