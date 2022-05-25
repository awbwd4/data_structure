class Node:
    def __init__(self, value):
        self.value = value
        self.left = self.right = None


class BST:
    def __init__(self, root):
        self.root = root

    def insert(self, value):
        self.current_node = self.root
        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.root

        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        # 삭제할 노드 탐색
        self.current_node = self.root  # 삭제할 노드
        self.parent = self.root  # 삭제할 노드의 부모노드

        # 일단 해당 노드가 있는지 찾는다.
        while self.current_node:
            if self.current_node.value == value:
                searched = True
                break
            # 왼쪽 이동
            elif value < self.current_node.value:
                self.parent = self.current_node
                self.current_node = self.current_node.left
                # 비교대상 변경
            # 오른쪽 이동.
            else:
                self.parent = self.current_node
                self.current_node = self.current_node.right

        if searched == False:
            print("삭제 대상 없음.")
            return False

        # 해당 노드를 찾음, 삭제

        # case 0 : 삭제할 노드가 헤드이며, 헤드만 있는 트리인 경우
        if (
            self.root == self.current_node
            and self.current_node.right == None
            and self.current_node.left
        ):
            self.root = None

        # case 1 : 삭제할 노드가 리프 노드인 경우
        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None

        # case 2 : chile node가 한개인 노드 삭제
        # 왼쪽 : 부모 노드가 손자 노드를 바라보도록한다.
        ### case 2-1 : 왼쪽 노드만 갖고 있는 경우
        if self.current_node.left != None and self.current_node.right == None:
            # 삭제될 노드가 parent의 오른쪽? or 왼쪽?
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.rignt = self.current_node.left
        ## case 2-2 : 오른쪽 노드만 갖고 있는 경우
        elif self.current_node.left == None and self.current_node.right != None:
            # 삭제될 노드가 parent의 오른쪽? or 왼쪽?
            if value < self.parent.value:  # 왼쪽
                self.parent.left = self.current_node.right
            else:  # 오른쪽
                self.parent.right = self.current_node.right

        # case3 : 삭제할 노드가 두개의 자식을 갖고 있을 경우
        # ****: 삭제할 노드의 오른쪽 자식 중 가장 작은 값을 parent노드가 가리키게 한다.
        if self.current_node.left != None and self.current_node.right != None:
            ## case3-1 : 삭제할 노드가 부모 노드의 왼쪽인 경우
            if value < self.parent.value:
                # change_node : 삭제될 노드를 대체할 작은 노드
                # change_node_parent : 삭제될 노드를 대체할 작은 노드의 부모노드 위치.
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right

                # 가장 작은 값은 반드시 left에 존재, 일단 트리의 left끝으로 이동.
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left

                ### case 3-1-1 : 삭제할 노드의 가장 작은 자식(가장 왼쪽)에게 자식이 있을 때
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                ### case 3-1-1 : 삭제할 노드의 가장 작은 자식(가장 왼쪽)에게 자식이 없을 때
                else:
                    self.change_node_parent.left = None

                # 위로 올리기
                self.parent.left = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.current_node.left

            ## case3-2 : 삭제할 노드가 부모 노드의 오른쪽인 경우
            else:
                # change_node : 삭제될 노드를 대체할 가장 작은 노드
                # change_node_parent :  삭제될 노드를 대체할 가장 작은 노드의 부모노드
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                # 가장 작은 노드까지 이동
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                # case 3-2-2 : 가장 작은노드의 우측에 자식 노드가 있을 경우
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                # case 3-2-1 : 가장 작은노드의 우측에 자식 노드가 없을 경우
                else:
                    self.change_node_parent = None

                # 위로 이동
                self.parent.right = self.change_node
                self.change_node.right = self.current_node.right
                self.change_node.left = self.parent.left


# head = Node(1)
# BST = BST(head)
# BST.insert(2)
# BST.insert(3)

# print(BST.search(1))


import random

bst_nums = set()  # set 컬렉션으로 중복 방지함.
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0, 999))

# print(bst_nums)
# 선택된 100개의 숫자를 이진드리에 입력,
# 루트노드는 일부러 500으로 지정

head = Node(500)
bt = BST(head)
for num in bst_nums:
    bt.insert(num)

# 검색
for num in bst_nums:
    if bt.search(num) == False:
        print("Search Failed!!!!!", num)
    else:
        if num % 100 == 0:
            print(num)


# 입력한 100개의 숫자 중 10개의 숫자 랜덤 선택
delete_nums = set()
bst_nums = list(bst_nums)  # 인덱스로 접근하기 위해 list타입으로 변형
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0, 99)])

print(delete_nums)

# 선택한 10개의 숫자 삭제
for del_num in delete_nums:
    if bt.delete(del_num) == False:
        print("delete False!!!!", del_num)
