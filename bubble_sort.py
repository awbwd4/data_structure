def bubbleSort(list):
    length = len(list)
    print("length : ", length)  # 5

    for i in range(0, length - 1):

        print("i : ", i)

        swap = False

        for j in range(0, length - 1 - i):

            # -i 를 해주지 않으면 불필요한 비교 연산을 또 수행하게 된다
            # 예들들면, i == 1 즉 , 첫 회전일때 배열의 가장 끝에는 가장 큰 수가 하나 생긴다
            # 그렇담 그 다음 연산에서는 배열의 마지막 수와 비교하는 연산은 할 필요가 없다.
            # 두번째 회전까지 끝났을 경우에는 배열의 끝 2개에는 가장 큰 수 2개가 있으므로
            # 이 2개의 숫자는 비교 연산 대상에서 제외된다.
            print("  j : ", j)
            if list[j] > list[j + 1]:
                list[j], list[j + 1] = list[j + 1], list[j]
                # 파이썬은 이런식으로 스위칭이 된다!
                swap = True
            print("    ", swap)

        if swap == False:  # 배열을 한번 스캔할때 바꾼 것이 없으면 더이상 회전을 그만하고 break함.
            break


#  반복문이 중첩이므로 O(n^2)이다.


def bubbleSort2(list):
    length = len(list)
    for i in range(0, length - 1):
        for j in range(0, length - 1):
            if list[j] > list[j + 1]:
                temp = list[j]
                list[j] = list[j + 1]
                list[j + 1] = temp


# list = [5, 1, 4, 2, 12, 8, 11, 10, 8]
list = [4, 2, 3]
print(bubbleSort(list))
