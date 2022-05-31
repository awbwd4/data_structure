def binary_search(list, start, end, data):

    if start == end and list[start] != data:
        return -1

    mid = int((start + end) / 2)
    print("mid : [%d]", list[mid])
    if list[mid] == data:
        return mid
    elif list[mid] < data:
        return binary_search(list, mid + 1, end, data)
    else:
        return binary_search(list, start, mid, data)


list = [2, 3, 8, 9, 10, 11, 12, 14, 15, 19]

print(binary_search(list, 0, len(list) - 1, 19))
print(binary_search(list, 0, len(list) - 1, 13))
