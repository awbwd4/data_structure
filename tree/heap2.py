class MaximumHeap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)  # 인덱스0은 미사용
        self.heap_array.append(data)  # 인덱스1부터 시작

    # 루트노드가 자식노드와 위치를 변경해야 하는지 확인
    # 삭제에 사용
    # 최대힙이므로 부모노드 >> 자식 노드
    # 자식노드와 비교하여 작을 경우에는 아래로 이동.
    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1

        # case 1 : 왼쪽 노드도 없을때, 즉, 자식노드가 전혀 없을 때.
        if left_child_popped_idx >= len(self.heap_array):
            return False
        # case 2 :  왼쪽 자식 노드는 있으나, 오른쪽 자식노드는 없을 때.
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return True
            else:
                return False
        # case 3 : 자식 노드가 둘 다 있는 경우
        else:
            if (
                self.heap_array[left_child_popped_idx]
                > self.heap_array[right_child_popped_idx]
            ):
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    return True
                else:
                    return False
            else:
                if (
                    self.heap_array[popped_idx]
                    < self.heap_array[right_child_popped_idx]
                ):
                    return True
                else:
                    return False

    # 힙에서 값 제거(pop)시 항상 최상단 노드를 제거함.
    # 최대 힙이므로 루트 노드에는 항상 가장 큰 값이 있어야하는데
    # 루트노드 제거 후에는 먼저 가장 나중에 삽입된 노드가 루트노드로 이동한다
    # 그 뒤 자식 노드들과 크기 비교.
    # 자식 노드 중 큰것과 비교하여 자식노드 > 이동되는 노드인 경우
    # 아래로 내려감.
    def pop(self):
        # 빈 트리일 경우
        if len(self.heap_array) <= 1:
            return None

        #
        # 힙에서 값 제거(pop)시 항상 최상단 노드를 제거함.
        returned_data = self.heap_array[1]
        # 루트노드 제거 후에는 먼저 가장 나중에 삽입된 노드가 루트노드로 이동한다
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1

        # 그 뒤 자식 노드들과 크기 비교.
        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            # case1 : 자식노드가 하나도 없는 경우
            # case 2 : 자식 노드가 왼쪽만 있는 경우
            if right_child_popped_idx >= len(self.heap_array):
                # 왼쪽 자식 노드와 크기 비교
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    (
                        self.heap_array[popped_idx],
                        self.heap_array[left_child_popped_idx],
                    ) = (
                        self.heap_array[left_child_popped_idx],
                        self.heap_array[popped_idx],
                    )
                    popped_idx = left_child_popped_idx
            # case 3 : 자식 노드가 둘 다 있는 경우
            else:
                # 자식 노드끼리 크기 비교 후
                if (
                    self.heap_array[left_child_popped_idx]
                    > self.heap_array[right_child_popped_idx]
                ):
                    # 그 중 큰 노드와 크기 비교
                    if (
                        self.heap_array[popped_idx]
                        < self.heap_array[left_child_popped_idx]
                    ):
                        (
                            self.heap_array[popped_idx],
                            self.heap_array[left_child_popped_idx],
                        ) = (
                            self.heap_array[left_child_popped_idx],
                            self.heap_array[popped_idx],
                        )
                        popped_idx = left_child_popped_idx

                else:
                    if (
                        self.heap_array[popped_idx]
                        < self.heap_array[right_child_popped_idx]
                    ):
                        (
                            self.heap_array[popped_idx],
                            self.heap_array[right_child_popped_idx],
                        ) = (
                            self.heap_array[left_child_popped_idx],
                            self.heap_array[popped_idx],
                        )
                        popped_idx = right_child_popped_idx
        return returned_data

        pass

    # 삽입시 사용
    # 삽입시 삽입된 노드는 일단 힙의 가장 끝에 삽입된다.
    # 그 뒤 부모 노드와 비교하여 부모 노드와 변경되어야 하는지를 판단.
    # 최대힙이므로 "부모노드 < 삽입된 노드"인 경우 부모노드와 변경된다.
    # True이면 변경, False이면 그대로.
    def move_up(self, inserted_idx):
        if inserted_idx == 1:
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 1:  # 인덱스 0만 생성된 빈 트리인 경우
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = (
                self.heap_array[parent_idx],
                self.heap_array[inserted_idx],
            )  # 값도 바꾸고
            inserted_idx = parent_idx  # 인덱스도 바꿔준다.


heap = MaximumHeap(15)
heap.insert(10)
heap.insert(20)
heap.insert(11)

print(heap.heap_array)  # 확인 [None,20,15,11,10]
print(heap.pop())  # 20
print(heap.heap_array)  # 확인 [None,15,11,10]
