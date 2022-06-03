import heapq

mygraph = {
    "A": {"B": 8, "C": 1, "D": 2},
    "B": {},
    "C": {"B": 5, "D": 2},
    "D": {"E": 3, "F": 5},
    "E": {"F": 1},
    "F": {"A": 5},
}


def dijkstra(graph, start):
    distances = {node: float("inf") for node in graph}
    # 거리를 기록하는 딕셔너리 형태.
    distances[start] = 0  # 스타트 노드는 자기자신이므로 거리는 0

    queue = []  # queue라는 리스트에 heap형태로 데이터를 넣음

    heapq.heappush(queue, [distances[start], start])

    # 노드의 이름이 아니라, 여기에서는 노드간의 거리를 키값으로 씀.

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue
        # 힙에서 꺼낸 노드까지의 거리가 리스트에 저장된 길이보다 길 경우
        # 아래의 작업을 수행할 필요 없음.

        for adjacent, weight in graph[current_node].items():
            # 해당 노드의 근접 노드들과 거리

            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                # 새로 계산된 거리가 기존에 저장된 거리보다 짧을 경우
                # 거리 저장값을 업데이트함.
                heapq.heappush(queue, [distance, adjacent])
                # 거리 저장값이 업데이트 된 노드는 힙에도 업데이트를 해준다.

    return distances


distances = {node: float("inf") for node in mygraph}

print(distances)


print(dijkstra(mygraph, "A"))
