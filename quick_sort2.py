def quick_sort(list, start, end):
    if start >= end:
        return  # 종료조건. 원소가 1개 이하인 경우.

    pivot = start
