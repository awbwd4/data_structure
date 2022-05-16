from collections import deque

n, m = map(int, input().split())

# # 2차원 리스트의 맵 정보 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

# 방문여부
# visited = [[False] * m] * n ##이경우 n개의 [[False]*m]은 모두 같은 배열로 인식됨
visited = [[False] * m for _ in range(n)]

# 방향
da = [-1, 1, 0, 0]
db = [0, 0, -1, 1]

# queue = deque()
# queue.append((0, 0))

# a, b = queue.popleft()

# # print(queue.popleft())
# print(a, b)


def bfs():

    print("n : %d m : %d" % (n, m))
    # queue 생성
    queue = deque()
    # queue에 첫 값 넣기
    queue.append((0, 0))

    print(visited)
    print("==================")

    # 큐에 값이 있을 경우
    while queue:

        a, b = queue.popleft()
        print("이동기준좌표 [%d %d]" % (a, b))
        visited[a][b] = True  # 방문여부 체크
        print(visited)

        for i in range(4):  # 4방향 탐색
            na = a + da[i]
            nb = b + db[i]
            print("  ", na, " ", nb)

            # 이동하지 않는 조건
            if graph[na][nb] == 0:
                print("         1.필터링된 na nb : ", na, " ", nb)
                continuegit
            if na < 0 or na >= n or nb < 0 or nb >= m:
                # graph[0][3]
                print("         2.필터링된 na nb : ", na, " ", nb)
                continue
            if visited[na][nb] == True:
                print("         3.필터링된 na nb : ", na, " ", nb)
                continue
            # 이동시 그래프 리스트에 해당 노드까지의 이동 거리를 입력
            graph[na][nb] = graph[a][b] + 1
            queue.append((na, nb))  # 이동 좌표를 큐에 입력

    return graph[n - 1][m - 1]


print(bfs())
