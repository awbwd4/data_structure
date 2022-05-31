def quick_sort(list):
    if len(list) == 1:
        return

    pivot = list[0]

    left_list = []
    right_list = []
    merged_arr = []
    for i in range(1, len(list)):
        if list[i] < pivot:
            left_list.append(list[i])
        else:
            right_list.append(list[i])

    print("left : ", left_list)
    print("pivot : ", pivot)
    print("right : ", right_list)

    # merged_arr = left_list
    # merged_arr.append(pivot)
    # merged_arr += right_list
    # merged_arr = quick_sort(left_list)
    # # merged_arr.append(pivot)
    # merged_arr += quick_sort(right_list)

    merged_arr = quick_sort(left_list) + quick_sort(right_list)

    return merged_arr


list = [4, 2, 1, 5, 7, 3, 9, 10]
print(quick_sort(list))
