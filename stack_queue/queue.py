from collections import deque

# queue구현을 위해 deque라이브러리 사용.
# 리스트보다 deque라이브러리 쓰는게 시간복잡도가 덜 나옴
queue = deque()

# 5, 2, 3, 7, 삭제, 1, 4, 삭제

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()  # right아님 left임
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()  # 역순으로 바꾸기
print(queue)
