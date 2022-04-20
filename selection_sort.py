"""선택 정렬"""


def selectionSort(list):

    for i in range(len(list) - 1):

        print("i : ", i)
        # 가장 작은 값의 위치. 기준위치
        min_index = i

        print(" -min_index : ", min_index)
        # 리스트의 값을 하나하나 보면서
        # 가장 작은 값을 찾는다.

        for j in range(i + 1, len(list)):

            print("      --j : ", j)

            if list[min_index] > list[j]:

                # 더 작은 값을 발견하면, min_inde의 위치를 바꿔줌바꿔줌
                print("       ---list[j] : ", list[j])
                print("       ---list[min_index] : ", list[min_index])
                min_index = j
                ### 1번째 배열의 값이 0번째 배열의 값보다 작을 경우
                ### min_index는 0 -> 1로 바뀜.

        list[i], list[min_index] = list[min_index], list[i]

    return list


# print(selectionSort(list))


def selectionSort1(list):

    print(list)
    for i in range(len(list) - 1):
        print("i : [%i]" % i)
        print("list:", list)
        print("list[i] : ", list[i])
        min_index = i

        for j in range(i + 1, len(list)):
            if list[min_index] > list[j]:
                min_index = j
                print("     list[min_index] : ", list[min_index])

        list[i], list[min_index] = list[min_index], list[i]
        print("         list : ", list)

    return list


list = [64, 25, 12, 22, 11]
print(selectionSort1(list))
