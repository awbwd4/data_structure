from collections import deque
import queue

graph = {
    "a": ["b", "c"],
    "b": ["a", "c"],
    "c": ["a", "g", "h", "i"],
    "d": ["b", "e", "f"],
    "e": ["d"],
    "f": ["d"],
    "g": ["c"],
    "h": ["c"],
    "i": ["c", "j"],
    "j": ["i"],
}
# print(graph[1].keys())

visited = []


# def bfs(graph, start, visitied):

#     queue = deque(graph[1])


need_queue = deque("a")
# need_queue.append("2")print(need_queue.popleft())
print(need_queue.popleft())
