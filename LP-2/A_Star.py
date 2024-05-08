# def aStar(start, end):
#     openSet = set([start])
#     closedSet = set()
#     g = {start:0}
#     parent = {start:start}

#     while openSet:
#         current = min(openSet, key= lambda node: g[node]+ heuristic(node))

#         if current == end:
#             v = []
#             while current!= start:
#                 v.append(current)
#                 current = parent[current]

#             v.append(start)
#             v.reverse()
#             print(v)

#             return True
        
#         openSet.remove(current)
#         closedSet.add(current)

#         for i, weight in graph[current]:
#             if i in closedSet:
#                 continue
#             temp_g = g[current]+weight

#             if i not in openSet or temp_g<g[i]:
#                 g[i]=temp_g
#                 parent[i] = current
#                 openSet.add(i)

#     print("Path not found")
#     return False

def heuristic(node):
    p = {'A': 11, 'B': 6, 'C': 13,
        'D': 1, 'E': 7, 'G': 0,}
    return p.get(node)


graph = {
    "A": [['B',2], ['E',3]],
    'B':[['A',2], ['C',1], ['G',9]],
    'C':[['B',1]],
    'D':[['E',6],['G',1]],
    'E':[['A',3], ['D',6]],
    'G':[["B",9],["D",1]]
}

# aStar('D','A')


















def a_star(start,end):
    openset = set([start])
    closedset = set()
    g  = {start:0}
    parent = {start:start}

    while openset:
        current = min(openset, key= lambda node: g[node]+ heuristic(node))

        if current == end:
            a=[]
            while current!=start:
                a.append(current)
                current = parent[current]
            a.append(start)
            a.reverse()
            print(a)
            return True
        
        openset.remove(current)
        closedset.add(current)

        for i,weight in graph[current]:
            if i in closedset:
                continue
            temp_g = g[current]+weight

            if i not in openset or temp_g< g[i]:
                openset.add(i)
                parent[i] = current
                g[i]= temp_g

    print("No path found")
    return False


a_star('C','G')