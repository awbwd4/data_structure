# n,m을 공백을 기준으로 구분하여 입력받기
n, m = map(int, input().split())

# 2차원 리스트의 맵정보 받기
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))


def dfs(a, b, cnt):
    # 종료조건
    if a == n - 1 and b == m - 1:
        print("graph[%d][%d]" % (a, b))
        return cnt

    if a <= -1 or a >= n or b <= -1 or b >= m:
        return

    # 진행조건
    if graph[a][b] == 1:
        print("graph[%d][%d]" % (a, b))
        graph[a][b] = 0
        cnt += 1
        print(cnt)
        dfs(a, b + 1, cnt)  # 우
        dfs(a, b - 1, cnt)  # 좌
        dfs(a - 1, b, cnt)  # 상
        dfs(a + 1, b, cnt)  # 하
        return cnt
    else:
        return


count = 0

for i in range(0, n):  # 1 2 3 4
    print("i : [%d]" % i)
    for j in range(0, m):
        print(" j : [%d]" % j)  # 1 2 3 4
        # if dfs(i, j, count) == True:
        #     count += 1
        # else:
        #     count = 0
        print("result", dfs(i, j, count))
        # print("count [%d]" % count)
