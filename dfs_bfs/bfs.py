from collections import deque
import queue

# bfs는 dfs와 달리 재귀 사용x, 메서드는 단 한번만 호출되며, queue와 while을 이용해 구현한다.
def bfs(graph, start, visited):

    # 첫번째 노드
    queue = deque([start])
    visited[start] = True

    # 큐에 넣고 빼고를 반복
    # 큐가 완전히 빌 때 까지 반복
    while queue:
        # 큐에 있는 노드를 꺼냄
        v = queue.popleft()  ##  꼭 popleft로 해야함.
        print(v)
        # 해당 노드의 인접 노드들 훑기
        for i in graph[v]:
            # 인접 노드들 중 방문하지 않은 노드가 있으면 그걸 큐에 놓기+방문여부 체크
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
