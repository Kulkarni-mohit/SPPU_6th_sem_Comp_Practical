from collections import defaultdict

class Graph:
    def __init__(self):
        """
        Initialize a graph using defaultdict for adjacency list representation.
        """
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """
        Add an edge to the graph.
        
        Args:
            u (int): Starting node of the edge.
            v (int): Ending node of the edge.
        """
        self.graph[u].append(v)

    def dfs(self, v):
        """
        Perform Depth First Search (DFS) starting from node v.
        
        Args:
            v (int): Starting node for DFS traversal.
        """
        visited = set()
        self.dfs_rec(v, visited)

    def dfs_rec(self, v, visited):
        """
        Recursive function to perform Depth First Search (DFS).
        
        Args:
            v (int): Current node for DFS traversal.
            visited (set): Set of visited nodes.
        """
        visited.add(v)
        print(v, end=' ')

        for neighbor in self.graph[v]:
            if neighbor not in visited:
                self.dfs_rec(neighbor, visited)

    def bfs(self, v):
        """
        Perform Breadth First Search (BFS) starting from node v.
        
        Args:
            v (int): Starting node for BFS traversal.
        """
        visited = set()
        queue = [v]
        visited.add(v)

        while queue:
            node = queue.pop(0)
            print(node, end=' ')

            for neighbor in self.graph[node]:
                if neighbor not in visited:
                    queue.append(neighbor)
                    visited.add(neighbor)

# Create a graph instance
g = Graph()

# Input number of nodes
n = int(input("Enter the number of nodes: "))

# Input edges
for i in range(n):
    u = int(input("Enter the starting node: "))
    v = int(input("Enter the ending node: "))
    g.add_edge(u, v)
    g.add_edge(v, u)  # Assuming the graph is undirected

# Ask user for traversal choice
choice = input("Enter 'bfs' for Breadth First Search or 'dfs' for Depth First Search: ")

# Input starting node for traversal
start_node = int(input("Enter the starting node for traversal: "))

# Perform traversal based on user choice
if choice == 'bfs':
    print("Breadth First Search (BFS):")
    g.bfs(start_node)
elif choice == 'dfs':
    print("Depth First Search (DFS):")
    g.dfs(start_node)
else:
    print("Invalid choice! Please enter 'bfs' or 'dfs'.")
