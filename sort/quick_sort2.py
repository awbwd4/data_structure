import random

n = int(input())

array = random.sample(range(100), n)



def quick_sort(array):
    if len(array) <= 1:
        return array
    
    pivot = array[0]
    
    left = [item for item in array[1:] if item < pivot]
    right = [item for item in array[1:] if item >= pivot]

    return quick_sort(left)+[pivot]+quick_sort(right)


print(quick_sort(array))