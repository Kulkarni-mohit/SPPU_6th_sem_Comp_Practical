from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addedge(self,u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def bfs(self,n):
        queue = [n]
        visited = set()
        visited.add(n)
        
        while queue:
            i = queue.pop(0)
            print(i, end=" ")

            for j in self.graph[i]:
                if j not in visited:
                    visited.add(j)
                    queue.append(j)


n = int(input("Enter no of nodes: "))

g = Graph()

for i in range(n):
    u=int(input("Starting: "))
    v = int(input("End: "))

    g.addedge(u,v)

g.bfs(0)