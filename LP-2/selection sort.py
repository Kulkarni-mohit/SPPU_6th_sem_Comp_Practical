l = [50,41,2,70,100]

# for i in range(len(l)):
#     min_idx = i
#     for j in range(i+1,len(l)):
#         if l[min_idx]>l[j]:
#             min_idx=j

#     l[i],l[min_idx] = l[min_idx],l[i]

print(l)
























for i in range(len(l)):
    min_idx = i
    for j in range(i+1,len(l)):
        if l[min_idx]>l[j]:
            min_idx = j

    l[min_idx], l[i] = l[i], l[min_idx]

print(l)


graph = {
    "A": [['B',2], ['E',3]],
    'B':[['A',2], ['C',1], ['G',9]],
    'C':[['B',1]],
    'D':[['E',6],['G',1]],
    'E':[['A',3], ['D',6]],
    'G':[["B",9],["D",1]]
}