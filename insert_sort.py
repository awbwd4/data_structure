"""삽입정렬"""

# 배열의 두번째 값부터 시작해서, 바로 앞에 있는 값이 자기보다 크면 앞으로 이동


def insertSort(list):

    for i in range(1, len(list)):
        # 삽입정렬은 배열을 0번째 값부터 비교하는것이 아닌 1번째 값부터 비교한다.
        # 따라서 1부터 시작
        key = list[i]
        j = i - 1  # 비교대상이 되는 배열의 인덱스 번호
        print("key : ", key)

        while j >= 0 and key < list[j]:

            list[j + 1] = list[j]  # 비교대상이 되는 값을 한칸씩 뒤로 밀어줌
            print("   list 0 : ", list)
            j -= 1

        list[j + 1] = key
        print("   list 2 : ", list)


# list = [13, 12, 11, 6, 5]
list = [5, 6, 7, 8, 9]
insertSort(list)
