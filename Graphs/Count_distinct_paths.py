adj_list = {1: [2, 4], 2: [3, 6], 3: [6], 4: [5], 5: [2], 6: []}
start = 1
end = 6
distinct=[]

def distinct_path(adj_list, start, end, path=[]):
    path = path + [start]

    if start == end:
        return path

    if start not in adj_list:
        return None

    for node in adj_list[start]:
        if node not in path:
            sp = distinct_path(adj_list, node, end, path)
            if sp not in distinct and not sp == None:
                distinct.append(sp)




distinct_path(adj_list, start, end)
print(distinct)
