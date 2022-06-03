import heapq

queue = []

heapq.heappush(queue, [2, "A"])
heapq.heappush(queue, [5, "B"])
heapq.heappush(queue, [1, "C"])
heapq.heappush(queue, [7, "D"])
# queue라는 리스트에 heap형태로 데이터를 넣음

print(queue)
for index in range(len(queue)):
    print(heapq.heappop(queue))
