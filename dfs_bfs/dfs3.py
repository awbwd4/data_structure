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


def dfs(graph, start_node):
    visited, need_visit = list(), list()
    # 일반적으로는 앞으로 방문해야 할 need_visit은 스택으로 구현
    # 리스트의 메서드를 이용해 스택처럼 쓴다
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        # 후입 선출로 가져옴.
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited


print(dfs(graph, "A"))
