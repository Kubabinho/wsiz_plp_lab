from collections import deque
from typing import Dict, List, Optional
from functools import reduce



def bfs(graph: Dict[str, List[str]], start: str, goal: str) -> Optional[List[str]]:
    queue = deque([(start, [start])])

    def process_queue(q: deque):
        if not q:
            return None

        current, path = q.popleft()

        if current == goal:
            return path

        new_states = [(neighbor, path + [neighbor]) for neighbor in graph.get(current, []) if neighbor not in path]
        return process_queue(q + deque(new_states))

    return process_queue(queue)

def optimize_tasks_procedural(tasks: List[Dict[str, int]]) -> Dict[str, any]:
    tasks.sort(key=lambda task: task['time'])

    total_waiting_time = 0
    current_time = 0
    order = []

    for task in tasks:
        current_time += task['time']
        total_waiting_time += current_time
        order.append(task['name'])

    return {
        "order": order,
        "total_waiting_time": total_waiting_time
    }


def optimize_tasks_functional(tasks: List[Dict[str, int]]) -> Dict[str, any]:
    sorted_tasks = sorted(tasks, key=lambda task: task['time'])
    def calculate_waiting_time(acc, task):
        acc["current_time"] += task['time']
        acc["total_waiting_time"] += acc["current_time"]
        acc["order"].append(task['name'])
        return acc

    result = reduce(
        calculate_waiting_time,
        sorted_tasks,
        {"current_time": 0, "total_waiting_time": 0, "order": []}
    )

    return {
        "order": result["order"],
        "total_waiting_time": result["total_waiting_time"]
    }

tasks_example = [
    {"name": "Task1", "time": 3, "reward": 10},
    {"name": "Task2", "time": 1, "reward": 20},
    {"name": "Task3", "time": 2, "reward": 15}
]

procedural_result = optimize_tasks_procedural(tasks_example)
print("Proceduralnie:", procedural_result)

functional_result = optimize_tasks_functional(tasks_example)
print("Funkcyjnie:", functional_result)

graph_example = {
    "A": ["B", "C"],
    "B": ["A", "D", "E"],
    "C": ["A", "F"],
    "D": ["B"],
    "E": ["B", "F"],
    "F": ["C", "E"]
}

start_vertex = "A"
goal_vertex = "F"
shortest_path = bfs(graph_example, start_vertex, goal_vertex)
print("Najkrótsza ścieżka:", shortest_path)
