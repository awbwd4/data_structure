class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None


class NodeMgmt:

    head = None
    findNode = None

    def __init__(self):
        self.head = None

    def insertNode(self, data):
        ## case1 : node가 하나도 없을 때
        if self.head == None:
            self.head = Node(data)
        else:
            ## case2 : node가 하나 이상일 때.
            findNode = self.head
            while True:
                ## case2-1 : 현재 노드의 왼쪽으로 이동
                if data < findNode.value:
                    if findNode.left is not None:
                        findNode = findNode.left
                    else:
                        findNode.left = Node(data)
                        break
                ## case2-2 : 현재 노드의 오른쪽으로 이동
                else:
                    if findNode.right is not None:
                        findNode = findNode.right
                    else:
                        findNode.right = Node(data)
                        break
        return True

    def search(self, data):
        # case1 : node가 하나도 없을 때
        if self.head is None:
            return None
        # case1 : node가 하나 이상 있을 때
        else:
            findNode = self.head
            while findNode is not None:
                if findNode.value == data:
                    return findNode
                elif data < findNode.value:
                    findNode = findNode.left
                else:
                    findNode = findNode.right
            return findNode


t = NodeMgmt
print(dir(t))
t.head

t.insertNode(t, 3)
t.insertNode(t, 4)
t.insertNode(t, 5)
# t.search(t, 3)

print(t.findNode)
