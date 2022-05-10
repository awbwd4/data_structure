graph = [
    [],  # 0
    [2, 6],  # 1
    [1, 3, 7],  # 2
    [2, 4, 8],  # 3
    [3, 5, 9],  # 4
    [4, 10],  # 5
    [1, 7, 11],  # 6
    [2, 6, 8, 12],  # 7
    [3, 7, 9, 13],  # 8
    [4, 8, 10, 14],  # 9
    [5, 9, 15],  # 10
    [6, 12, 16],  # 11
    [7, 11, 13, 17],  # 12
    [8, 12, 14, 18],  # 13
    [9, 13, 15, 19],  # 14
    [10, 14, 20],  # 15
    [11, 17],  # 16
    [12, 16, 18],  # 17
    [13, 17, 19],  # 18
    [14, 19, 20],  # 19
    [15, 19],  # 20
]

visited = [False] * 21
visited[0] = True
visited[3] = True
visited[4] = True
visited[9] = True
visited[10] = True
visited[11] = True
visited[12] = True
visited[13] = True
visited[14] = True
visited[15] = True
# visited[9, 10] = True
# visited[11:16] = True


def dfs(graph, v, visited):
    print(v)
    visited[v] = True
    for i in graph[v]:
        if visited[i] != True:
            dfs(graph, i, visited)


def count(graph, visited):
    cnt = 0
    for i in range(len(visited)):
        if visited[i] != True:
            dfs(graph, i, visited)
            cnt += 1
    print(cnt)


# print(visited)

count(graph, visited)
