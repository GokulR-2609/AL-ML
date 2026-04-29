from queue import PriorityQueue

def a_star(graph, start, goal, h):
    pq = PriorityQueue()
    pq.put((h[start], 0, start, [start]))
    visited = {}

    while not pq.empty():
        f, g, current, path = pq.get()

        if current == goal:
            return path, g

        for neighbor, cost in graph.get(current, {}).items():
            new_g = g + cost

            if neighbor not in visited or new_g < visited[neighbor]:
                visited[neighbor] = new_g
                new_f = new_g + h[neighbor]
                pq.put((new_f, new_g, neighbor, path + [neighbor]))

    return None, float('inf')

graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 5},
    'C': {'D': 1},
    'D': {}
}

h = {'A': 10, 'B': 6, 'C': 2, 'D': 0}

a_star(graph, 'A', 'D', h)