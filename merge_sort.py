# def mergeSort(nums: List[int]) -> List[int]:
def mergeSort(list_s):

    """분할"""

    length = len(list_s)

    if length == 1:
        return list_s

    mid = int(length / 2)  # 분할 기준

    print("mid : ", mid)

    left_nums = list_s[:mid]
    right_nums = list_s[mid:]

    sorted_left = mergeSort(left_nums)
    sorted_right = mergeSort(right_nums)

    """ 합병, 정렬하며 합병함"""

    sorted_nums = []  # 임시 저장될 배열
    idx_l = 0  # 왼쪽편 출발
    idx_r = 0  # 오른쪽편 출발

    while idx_l < len(sorted_left) or idx_r < len(
        sorted_right
    ):  # 합병하는 과정이며 또한 재귀의 종료조건이기도 하다.

        if idx_l == len(sorted_left):
            sorted_nums.append(sorted_right[idx_r])
            idx_r += 1
            continue
            # 왼쪽이 먼저 끝날 경우 오른쪽을 하나씩 sorted_nums배열에 넣어준다.
            # 왼쪽은 이미 끝났으므로 이 아래 로직은 더 할필요가 없다. 따라서 continue

        if idx_r == len(sorted_right):
            sorted_nums.append(sorted_left[idx_l])
            idx_l += 1
            continue
            # 오른쪽이 먼저 끝날 경우 오른쪽을 하나씩 sorted_nums배열에 넣어준다.
            # 오른쪽은 이미 끝났으므로 이 아래 로직은 더 할필요가 없다. 따라서 continue

        # 실제 병합처리.
        if sorted_left[idx_l] <= sorted_right[idx_r]:
            sorted_nums.append(sorted_left[idx_l])
            idx_l += 1
        else:
            sorted_nums.append(sorted_right[idx_r])
            idx_r += 1

    # nums = sorted_nums  # 임시 배열에 다 처리가 끝났으므로 원래의 nums 배열로 이동시켜줌.

    print(sorted_nums)
    return sorted_nums


# nums = [5, 7, 9, 9, 3, 1, 2, 4, 4]

# nums = [4, 1, 9, 5]
nums = [7, 3, 1, 5, 6, 4, 2]


# print(mergeSort(nums))

mergeSort(nums)
