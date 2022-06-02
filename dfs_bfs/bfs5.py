graph = dict()

graph["A"] = ["B", "C"]
graph["B"] = ["A", "D"]
graph["C"] = ["A", "G", "H", "I"]
graph["D"] = ["B", "E", "F"]
graph["E"] = ["D"]
graph["F"] = ["D"]
graph["G"] = ["C"]
graph["H"] = ["C"]
graph["I"] = ["C", "J"]
graph["J"] = ["I"]


def bfs(graph, start_node):
    visited = list()
    need_visit = list()  # 큐를 안쓰고 리스트의 함수를 가지고 구현

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(0)  # 리스트에도 pop이 있다!!!!
        # pop(0) : 큐처럼 딱 선입선출이 됨.
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited


print(bfs(graph, "A"))
