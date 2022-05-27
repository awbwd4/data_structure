class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)  # 1부터 시작할 예정
        self.heap_array.append(data)

    # 루트노드가 자식노드랑 위치를 변경해야하는가를 판단
    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1

        # case1: 왼쪽 자식 노드도 없을 때
        if left_child_popped_idx >= len(self.heap_array):
            return False
        # case2: 오른쪽 자식 노드만 없을 때 (완전이진트리라는 것을 유의하자)
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return True  # 자식노드가 더 크니까 바꿔줘야함
            else:
                return False
        # case3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
        else:
            # 자식노드끼리 비교
            if (
                self.heap_array[left_child_popped_idx]
                > self.heap_array[right_child_popped_idx]
            ):
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    return True  # 자식노드가 더 크다면 바꿔줘야함
                else:
                    return False
            else:
                if (
                    self.heap_array[popped_idx]
                    < self.heap_array[right_child_popped_idx]
                ):
                    return True  # 자식노드가 더 크다면 바꿔줘야함
                else:
                    return False

    def pop(self):
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]  # 루트노드를 최하단 노드로 변경
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            # case2: 오른쪽 자식 노드만 없을 때
            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    (
                        self.heap_array[popped_idx],
                        self.heap_array[left_child_popped_idx],
                    ) = (
                        self.heap_array[left_child_popped_idx],
                        self.heap_array[popped_idx],
                    )
                    popped_idx = left_child_popped_idx

            # case3: 왼쪽, 오른쪽 자식 노드 모두 있을 때
            else:
                # 자식노드끼리 비교
                if (
                    self.heap_array[left_child_popped_idx]
                    > self.heap_array[right_child_popped_idx]
                ):
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
                            self.heap_array[right_child_popped_idx],
                            self.heap_array[popped_idx],
                        )
                        popped_idx = right_child_popped_idx

        return returned_data

    # 현재 노드가 상위노드와 바꿔야하는지를 판단
    def move_up(self, inserted_idx):
        if inserted_idx <= 1:  # 루트노드면 바꿀 노드가 없다.
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 1:  # 방어코드
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)  # 일단 완전 이진트리로 만든다
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):  # 현재노드를 상위노드와 바꿔야한다고 판단했다면
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = (
                self.heap_array[parent_idx],
                self.heap_array[inserted_idx],
            )
            inserted_idx = parent_idx
        return True


heap = Heap(15)
heap.insert(10)
heap.insert(20)
heap.insert(11)

print(heap.heap_array)  # 확인 [None,20,15,11,10]
print(heap.pop())  # 20
print(heap.heap_array)  # 확인 [None,15,11,10]
