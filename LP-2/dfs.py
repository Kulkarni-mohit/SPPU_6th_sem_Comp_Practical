# from collections import defaultdict

# class Graph():
#     def __init__(self):
#         self.graph = defaultdict(list)

#     def addedge(self, u,v):
#         self.graph[u].append(v)
#         self.graph[v].append(u)

#     def dfs(self,v):
#         visited = set()

#         self.dfsrec(v,visited)

#     def dfsrec(self,v,visited):
#         visited.add(v)

#         print(v, end=" ")

#         for i in self.graph[v]:
#             if i not in visited:
#                 self.dfsrec(i,visited)


# n = int(input("Enter no of nodes: "))

# g = Graph()

# for i in range(n):
#     u=int(input("Starting: "))
#     v = int(input("End: "))

#     g.addedge(u,v)

# g.dfs(0)



from collections import defaultdict

class Graph():
    def __init__(self):
        self.graph = defaultdict(list)

    def addedge(self, u,v):
        self.graph[u].append(v)
        self.graph[v].append(u)

    def dfs(self,n):
        visited = set()

        self.dfsrec(visited,n)

    def dfsrec(self,visited,n):
        visited.add(n)
        print(n,end=" ")

        for i in self.graph[n]:
            if i not in visited:
                self.dfsrec(visited,i)


n = int(input("Enter no of nodes: "))

g = Graph()

for i in range(n):
    u=int(input("Starting: "))
    v = int(input("End: "))

    g.addedge(u,v)

g.dfs(0)