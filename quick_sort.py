"""나누고 정렬하기"""


def quickSort(list, begin, end):

    i = 0

    def sort(list, begin, end):
        if begin < end:  # 종료조건
            p = partition(list, begin, end)
            quickSort(list, begin, p - 1)
            quickSort(list, p + 1, end)

    def partition(list, begin, end):

        l = begin
        r = end
        pivot = (begin + end) / 2

        i += 1

        print("\n 퀵정렬 %d 단계 : pivot = %d" % i, list[pivot])

        while l < r:  # L과 R이 서로 만날때까지 반복
            while list[l] < list[pivot] and l < r:
                l += 1  # 피봇보다 크거나 같은것을 찾음.
            while list[r] >= list[pivot] and l < r:
                r -= 1  # 피봇보다 작은것을 찾음.
            if l < r:
                # l이 피봇보다 크거나 같은것을 찾고
                # r이 피봇보다 작은것을 찾은경우
                # 두 값을 스위칭함.
                list[l], list[r] = list[r], list[l]

        # L과 R 이 만나면, 피봇과 R을 스위칭함
        list[pivot], list[r] = list[r], list[pivot]

        # L을 리턴
        # 다음 부분집합 소팅의 기준점이 됨.
        return l

    return sort


list = [69, 10, 30, 2, 16, 8, 31, 22]


print(quickSort(list, 0, 7))

print(list)
