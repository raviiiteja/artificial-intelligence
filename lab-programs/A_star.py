import heapq

def a_star(graph, heuristic, start, goal):
    priority_queue = []
    heapq.heappush(priority_queue, (0, start))

    g_cost = {start: 0}
    parent = {start: None}

    while priority_queue:
        current_f, current = heapq.heappop(priority_queue)

        if current == goal:
            break

        for neighbor, cost in graph[current]:
            new_g = g_cost[current] + cost

            if neighbor not in g_cost or new_g < g_cost[neighbor]:
                g_cost[neighbor] = new_g
                f = new_g + heuristic[neighbor]
                heapq.heappush(priority_queue, (f, neighbor))
                parent[neighbor] = current

    path = []
    node = goal

    while node is not None:
        path.append(node)
        node = parent[node]

    path.reverse()

    print("Shortest Path:", " -> ".join(path))
    print("Total Cost:", g_cost[goal])

graph = {
    'A': [('B', 1), ('C', 4)],
    'B': [('D', 2), ('E', 5)],
    'C': [('F', 3)],
    'D': [('G', 5)],
    'E': [('G', 2)],
    'F': [('G', 1)],
    'G': []
}

heuristic = {
    'A': 7,
    'B': 6,
    'C': 4,
    'D': 4,
    'E': 2,
    'F': 1,
    'G': 0
}
a_star(graph, heuristic, 'A', 'G')