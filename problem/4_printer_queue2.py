n, m = list(map(int, input().split(" ")))
queue = list(map(int, input().split(" ")))
queue = [(i, idx) for idx, i in enumerate(queue)]


# queue = []
print(queue)


# for idx, i in enumerate(queue):
#     print(idx, i)


count = 0  # 출력 횟수

print(max(queue, key=lambda x: x[0]))
print(max(queue, key=lambda x: x[0])[0])
print(queue[0][0])

while True:
    if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
        # 제일 첫번째에 있는 가중치값(queue[0][0])이 큐에서 가장 큰 가중치 값이라면
        count += 1  # 출력 1회 증가
        if queue[0][1] == m:  # 제일 첫번째에 있는 문서가 원하던 순서의 문서였을 경우
            print(count)
            break
        else:
            queue.pop(0)  # 가중치 값이 제일 큰 첫번째 문서 pop
    else:
        # 앞에 있던걸 뒤로 보낸다.
        queue.append(queue.pop(0))
