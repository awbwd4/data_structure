test_case = int(input())

N, M = list(map(int, input().split(" ")))
queue = list(map(int, input().split(" ")))
queue = [(i, idx) for idx, i in enumerate(queue)]


print(queue)
