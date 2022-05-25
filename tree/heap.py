from turtle import left


class MaximumHeap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)  # 인덱스 0은 버린다
        self.heap_array.append(data)  # 인덱스 1부터 시작

    # 현재노드가 자식 노드랑 위치를 변경해야 하는가 판단.
    # 즉 현재 노드를 아래로 이동해야 하는지
    # 최대힙이므로 부모노드 > 자식노드 이어야함.
    # 삭제(pop)시에 사용
    def move_down(self, popped_idx):
        left_child_popped_idx = popped_idx * 2
        right_child_popped_idx = popped_idx * 2 + 1
        # 왼쪽 자식노드 인덱스 번호 = 부모노드 인덱스 번호*2
        # 오른쪽 자식노드 인덱스 번호 = 부모노드 인덱스 번호*2+1

        # case 1 : 왼쪽 자식노드가 없을 경우
        # 즉, 자식이 전혀 없을 경우.
        if left_child_popped_idx >= len(self.heap_array):
            return False
        # case 2 : 오른쪽 자식노드만 없을 경우
        # 즉, 자식이 하나 있을 경우
        elif right_child_popped_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                return True  # 자식노드가 더 크므로 변경
            else:
                return False  # 바꿀 필요 없음
        # case 3 : 왼쪽, 오른쪽 자식노드가 둘 다 있을 경우
        else:
            # 자식노드끼리 비교
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

    # 루트노드를 꺼낸다.
    def pop(self):
        # 트리에 아무내용이 없을 경우
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]  # 최하단의 마지막 노드를 루트 노드로
        del self.heap_array[-1]

        popped_idx = 1  # 비교대상 노드가 루트일때는 인덱스 1
        while self.move_down(popped_idx):  # 더이상 위치를 변경할노드가 없을 경우 종료(False)
            left_child_popped_idx = popped_idx * 2
            right_child_popped_idx = popped_idx * 2 + 1

            # case 1 : 자식 노드가 없을경우 -> 반복문 시작도 안함
            # case 2 : 오른쪽 자식 노드만 없을 때
            if right_child_popped_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] < self.heap_array[left_child_popped_idx]:
                    # 왼쪽 자식 노드만 존재하고, 자식 노드가 더 클때 스위칭
                    (
                        self.heap_array[popped_idx],
                        self.heap_array[left_child_popped_idx],
                    ) = (
                        self.heap_array[left_child_popped_idx],
                        self.heap_array[popped_idx],
                    )
                    popped_idx = left_child_popped_idx

            # case 3 : 두개의 자식 노드가 다 있을 경우
            else:
                # 자식 노드끼리 크기 비교
                if (
                    self.heap_array[left_child_popped_idx]
                    < self.heap_array[right_child_popped_idx]
                ):
                    # 자식 노드가 더 클 경우 swap
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
                else:
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
        return returned_data

    # 현재 노드가 부모 노드와 위치를 변경해야 하는지 판단
    # 즉 현재 노드를 위로 이동해야 하는지
    # 최대힙이므로 부모노드 > 자식노드 이어야함.
    # 삽입(insert)시에 사용
    def move_up(self, inserted_idx):
        if inserted_idx <= 1:  # 루트노드면 안바꿔도 됨
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
            # 자식 노드가 부모노드보다 크면 swap 대상임
        else:
            False

    def insert(self, data):
        if len(self.heap_array) == 1:
            # 힙의 크기가 1 즉, 아직 생성이 안됐을 경우
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)  # 일단 삽입 먼저 하고 본다
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            # 부모노드와의 크기 비교, 더 이상 올리지 않아도 될 때 까지 반복
            # move_up 메서드에서는 올릴지 말지만 체크를 해준다
            # 따라서 변수 선언등은 여기에 다시 서술해줘야함.
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = (
                self.heap_array[parent_idx],
                self.heap_array[inserted_idx],
            )
            inserted_idx = parent_idx  # 비교대상을 한칸 위로 이동
        return True


heap = MaximumHeap(15)
print(heap.heap_array)

heap.insert(10)
print(heap.heap_array)
heap.insert(20)
print(heap.heap_array)
heap.insert(11)
print(heap.heap_array)


print(heap.pop())
print(heap.heap_array)
