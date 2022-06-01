# 탐색하고자하는 그래프를 딕셔너리로
# key에는 노드, 밸류는 인접 노드를 리스트 타입으로 연결
# 방문 여부는 list로
from collections import deque
import queue

graph = {
    "A": ["B"],
    "B": ["A", "C", "H"],
    "C": ["B", "D"],
    "D": ["C", "E", "G"],
    "E": ["D", "F"],
    "F": ["E"],
    "G": ["D"],
    "H": ["B", "I", "J", "M"],
    "I": ["H"],
    "J": ["H", "K"],
    "K": ["J", "L"],
    "L": ["K"],
    "M": ["H"],
}


def bfs(graph, start_node):
    visited = list()
    queue = deque()

    queue.append(start_node)

    while queue:
        node = queue.popleft()

        if node not in visited:
            visited.append(node)
            queue.extend(graph[node])
    return visited


# print(bfs(graph, "A"))


queue = deque()
queue.extend(graph["B"])
# node = queue.popleft()
print(queue.popleft())
# print(node)


dq = deque("love")
dq.append("m")
dq.popleft()

dq.extend("you")

print(dq)
