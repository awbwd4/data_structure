from collections import deque


def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        v = queue.popleft()
        print(v)
        for i in graph[v]:
            if visited[i] != True:
                queue.append(i)
                visited[i] = True


graph = [
    [],  # 0
    [2, 3, 8],  # 1
    [1, 7],  # 2
    [4, 5],  # 3
    [3, 5],  # 4
    [3, 4],  # 5
    [7],  # 6
    [6, 8],  # 7
    [5, 7],  # 8
]

visited = [False] * 9


bfs(graph, 1, visited)
