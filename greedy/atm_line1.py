array = [3, 1, 4, 3, 2]


def min_wait_time(array):
    new_array = [0] * len(array)
    total_sum = 0

    array.sort()

    for i in range(len(new_array)):
        if i == 0:
            new_array[i] = array[i]
            print(new_array)
            continue
        time = new_array[i - 1] + array[i]
        new_array[i] = time

    total_sum = sum(new_array)

    return total_sum


print(min_wait_time(array=array))
