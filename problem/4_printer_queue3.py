total_test = int(input())

for i in range(total_test):
    n, m = list(map(int, input().split(" ")))
    queue = list(map(int, input().split(" ")))
    queue = [(i, idx) for idx, i in enumerate(queue)]

    print("최초 큐 : ", queue)

    count = 0  # 출력 횟수

    while True:
        # 맨 앞에 있는 문서가 가중치가 제일 큰 문서일 경우 : 출력
        # 맨 앞의 문서의 가중치가 큐에서 가장 큰 경우 : 출력
        if queue[0][0] == max(queue, key=lambda x: x[0])[0]:
            count += 1
            if queue[0][1] == m:  # 지금 출력되는 문서가 내가 찾던 문서일 경우 - 종료
                print(count)
                break
            else:
                queue.pop(0)  # 지금 출력되는 문서가 내가 찾던 문서가 아닐 경우 : pop 후 진행
        # 아닐경우 : 맨 앞의 문서를 뒤로 보낸다.
        else:
            queue.append(queue.pop(0))
