def quick_sort(array, start, end):
    # 종료조건 : 원소가 하나인 경우에 종료, 원소가 하나인 경우에는 start == end 가 된다.
    if start >= end:
        return

    pivot = start  # 호어법에 따라 피벗은 배열의 첫번째 원소이다.
    left = start + 1  # pivot보다 큰 값을 찾을 left
    right = end  # pivot 보다 작은 값을 찾을 right

    while left <= right:
        # 두개의 기준위치가 엇갈릴때까지 반복한다.
        # 즉 left == right일 때에도 이 반복문 수행
        while left <= end and array[left] <= array[pivot]:
            # left가 맨 끝으로 갈때까지
            # 해당 값이 피봇 값보다 클때까지(같은거 안됨)
            # 즉, left가 맨 끝으로 가거나 혹은 pivot보다 큰 값을 만난다면 멈춤
            # and 조건이므로 하나라도 된다면 멈춤
            left += 1  # left 오른쪽으로 이동
        while right > start and array[right] >= array[pivot]:
            # right가 맨 앞으로 갈때까지...는 아니고 pivot의 바로 앞으로 갈때까지
            # right의 데이터 값이 피봇 값보다 작을때까지(같은거 안됨)
            # 즉, right가 피봇 바로 앞까지 가거나 혹은 pivot 보다 작은 값을 만난다면 멈춤
            # and 조건이므로 하나라도 된다면 멈춤
            right -= 1

        if left > right:  # 엇갈렸다면? 작은데이터와 피벗 교체(피벗 위치 확정)
            # left는 피벗보다 큰 값, right는 피벗보다 작은 값을 찾으므로
            # right와 교체하면 된다.
            # 엇갈렸으므로 이 전체 반복문은 종료된다.
            array[pivot], array[right] = array[right], array[pivot]
        else:
            # 엇갈리지 않았다면? left값과 right값 교체(피벗 위치 확정x)
            # 엇갈리지 않았으므로 이 전체 반복문은 계속 진행된다.
            array[left], array[right] = array[right], array[left]

        # 분할 된 이후(pivot위치가 교체+확정된 이후) 발생한 양측의 배열로 다시 정렬 수행
        quick_sort(array, start, right - 1)
        quick_sort(array, right + 1, end)


array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]


quick_sort(array, 0, len(array) - 1)
print(array)
