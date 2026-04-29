from queue import PriorityQueue

def best_first_search(graph, start, goal, h_values):
    pq = PriorityQueue()
    pq.put((h_values[start], start))
    visited = {start}

    while not pq.empty():
        score, current = pq.get()
        print(f"Visiting: {current}")

        if current == goal:
            return "Goal Reached!"

        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                pq.put((h_values[neighbor], neighbor))

    return "Path not found"

nodes = {'A': ['B', 'C'], 'B': ['D'], 'C': ['G'], 'D': [], 'G': []}
h = {'A': 10, 'B': 5, 'C': 2, 'D': 4, 'G': 0}

best_first_search(nodes, 'A', 'G', h)