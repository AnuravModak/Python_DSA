adj_list={1:[2,4],2:[3,6],3:[6],4:[5],5:[2],6:[]}
start=1
end=6

def shortest_path(adj_list,start,end,path=[]):
    path=path+[start]
    if start==end:
        return path
    if start not in adj_list:
        return None
    shrt_path=None
    for node in adj_list[start]:
        if node not in path:
            sp=shortest_path(adj_list,node,end,path)
            if sp:
                if shrt_path is None or len(sp)<len(shrt_path):
                    shrt_path=sp
    return shrt_path
print(shortest_path(adj_list,start,end))



