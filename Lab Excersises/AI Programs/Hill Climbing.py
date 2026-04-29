def hill_climbing(graph, start, h_values):
    current = start

    while True:
        print(f"At node {current} (Value: {h_values[current]})")

        neighbors = graph.get(current, [])
        if not neighbors:
            break

        next_node = max(neighbors, key=lambda node: h_values[node])

        if h_values[next_node] <= h_values[current]:
            break

        current = next_node

    return current

nodes = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [], 'E': [], 'F': []
}

heights = {'A': 1, 'B': 5, 'C': 3, 'D': 4, 'E': 8, 'F': 2}

hill_climbing(nodes, 'A', heights)