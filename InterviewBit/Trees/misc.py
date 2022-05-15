B = [
    [1, 2],
    [1, 3],
    [1, 4],
    [3, 5],
    [4, 6]
]
adj_list=dict()
for i ,j in B:
    if i not in adj_list and j not in adj_list:
        adj_list[i]=[j]
        adj_list[j]=[]
    elif i in adj_list and j not in adj_list:
        adj_list[i].append(j)
        adj_list[j]=[]
    elif i in adj_list and j in adj_list:
        adj_list[i].append(j)

print(adj_list)
