def a_star(start_node, goal_node):
    open_set = set([start_node])
    closed_set = set()
    g = {start_node: 0}
    parents = {start_node: start_node}

    while open_set:
        current_node = min(open_set, key=lambda node: g[node] + heuristic(node))
        
        if current_node == goal_node:
            path = []
            while current_node != start_node:
                path.append(current_node)
                current_node = parents[current_node]
            path.append(start_node)
            path.reverse()
            print('Path found:', path)
            return path
        
        open_set.remove(current_node)
        closed_set.add(current_node)

        for neighbor, weight in get_neighbors(current_node):
            if neighbor in closed_set:
                continue
            tentative_g = g[current_node] + weight
            if neighbor not in open_set or tentative_g < g[neighbor]:
                g[neighbor] = tentative_g
                parents[neighbor] = current_node
                open_set.add(neighbor)
    
    print('Path does not exist!')
    return None

def get_neighbors(node):
    return Graph_nodes.get(node, [])

def heuristic(node):
    H_dist = {
        'A': 11, 'B': 6, 'C': 99,
        'D': 1, 'E': 7, 'G': 0,
    }
    return H_dist.get(node, float('inf'))

Graph_nodes = {
    'A': [('B', 2), ('E', 3)],
    'B': [('A', 2), ('C', 1), ('G', 9)],
    'C': [('B', 1)],
    'D': [('E', 6), ('G', 1)],
    'E': [('A', 3), ('D', 6)],
    'G': [('B', 9), ('D', 1)]
}

a_star('A', 'G')


"""

Output:
Path found: ['A', 'E', 'D', 'G']

"""