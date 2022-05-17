# 노드 생성하기
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


# 노드 객체 생성
n1 = Node(1)
n2 = Node(2)

# 노드와 노드 연결하기
n1.next = n2


print(n1.next)
