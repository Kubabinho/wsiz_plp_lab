from collections import deque


def bfsPath(graph, start, end):
    queue = deque([start])

    visited = set()

    while queue:
        path = queue.popleft()
        node = path[-1]

        if node == end:
            return path
        if node not in visited:
            for neighbor in graph(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)
    return None


graph = {'A': ['B', 'C', 'F'],
         'B': ['A', 'C', 'D'],
         'C': ['A', 'B', 'D', 'F', 'E'],
         'D': ['B', 'C'],
         'E': ['C'],
         'F': ['A', 'C']}

print(bfsPath(graph, 'A', 'B'))