def quick_sort(array, start, end):
    # 원소가 1개인 경우 종료
    if start >= end:
        return

    pivot = start  # 피봇은 첫번째 원소
    left = start + 1  # 피봇의 다음부터 시작
    right = end

    # left와 right가 엇갈리기 전까지 반복한다.
    while left <= right:
        # 피봇보다 큰 데이터를 찾을 때 까지 반복
        while left <= end and array[left] <= array[pivot]:
            left += 1
            print(left, end)

        # 피봇보다 작은 데이터를 찾을 때 까지 반복
        while right > start and array[right] >= array[pivot]:
            right -= 1

        # 엇갈렸으면 작은 데이터와 pivot 스와핑
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            # 엇갈리지 않았으면, 작은데이터와 큰 데이터간 교체
            array[left], array[right] = array[right], array[left]

    # 분할 이후 왼쪽과 오른쪽 부분에서 각각 다시 퀵소트 수행
    quick_sort(array, start, right - 1)
    quick_sort(array, right + 1, end)
