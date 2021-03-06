# 노드 생성하기
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:

    # 생성자
    # 링크드리스트 객체가 최초 생성될 시 head에 첫 노드가 들어간다.
    def __init__(self, data):
        self.head = Node(data)

    # 헤더부터 탐색해서 뒤로 새로운 노드 추가하기
    def append(self, data):
        cur = self.head  # 현재위치(헤더의 위치)
        while cur.next is not None:
            # next가 있을 경우
            cur = cur.next
            # 다음 노드가 현재 노드가 된다
            # 맨 뒤로 직접 이동을 한 뒤에 노드가 추가됨!
            # 링크드 리스트에 노드를 추가할 때마다
            # 현재 추가되어있는 노드를 한바퀴 다 봐야함
        cur.next = Node(data)
        # 맨 마지막 노드의 포인터에 새로운 노드 객체의 주소 추가

    # 모든 노드 값 출력
    def print_all(self):
        cur = self.head
        # print(cur.data)
        while True:
            print(cur.data)
            if cur.next is None:
                break
            cur = cur.next

    # 특정 위치의 노드 리턴하기.
    def get_node(self, index):
        cnt = 0
        node = self.head
        while cnt < index:
            # 해당 인덱스가 될 때까지 계속 이동함.
            cnt += 1
            node = node.next
            # 인덱스의 -1에서 반복문이 멈춤
            # 직전 노드의 next를 node 변수로.
        return node

    # 노드 중간에 삽입하기
    def add_node1(self, index, value):
        insert_node = Node(value)
        if self.head is None:
            self.head = insert_node
        else:
            cur = self.head
            cnt = 0
            while cnt < index - 1:
                cnt += 1
                cur = cur.next
                # 넣을 위치의 직전 노드까지 왔음.
            temp = cur.next
            cur.next = insert_node
            insert_node.next = temp

    def add_node2(self, index, value):
        new_node = Node(value)
        # 맨 앞에 넣을 경우
        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return
        # 만들어둔 get_node 메서드 사용
        node = self.get_node(index - 1)  # 삽입될 위치 직전 노드를 찾음
        new_node.next = node.next  # 직전노드의 next를 새 노드의 next로
        node.next = new_node

    # 중간의 노드 제거하기
    def delete_node(self, index):
        # deleted = Node(value)
        if self.head is None:
            # self.head = insert_node
            pass
        else:
            cur = self.head
            prev = self.head
            cnt = 0
            while cnt < index:
                cnt += 1
                cur = cur.next
                # cur : 삭제될 노드
                if cnt == index - 1:
                    prev = cur  # 삭제될 노드의 직전 노드
            prev.next = cur.next

    # 중간의 노드 제거하기
    def delete_node1(self, index):
        pass
        # 삭제하려는게 첫번째일 경우
        if index == 0:
            self.head = self.head.next
        deleted_node = self.get_node(index)
        self.get_node(index - 1).next = deleted_node.next


list = LinkedList(1)

list.append(2)
list.append(3)
list.append(4)
list.append(5)

list.print_all()

print("=================")
print(list.get_node(3).data)
list.add_node2(3, 6)
list.print_all()
print("=================")
list.delete_node(20)
list.print_all()

print("낄낄")
print("빡세게 하소오 :)")
