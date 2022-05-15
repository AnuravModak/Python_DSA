adj_list={1:[2,4],2:[5,3],3:[2,6],4:[1],5:[2,6],6:[5,3]}
visited=[False]*len(adj_list)

# print(visited)
def dfs(adj_list,visited,path=[],i=1):
    if visited[i-1]:
        return
    visited[i - 1] = True
    path.append(i)
    # print(visited)
    for a in adj_list[i]:
        dfs(adj_list, visited, path, a)
        # print(path,visited)  # to get time-complexity
    # print(path,visited)
    return path,visited

print("Depth First Search: ",dfs(adj_list,visited))
visited=[False]*len(adj_list)

def BFS(adj_list,visited,i=1):
    visit=[]
    visit.append(i)
    path=[]
    path.append(i)
    while(len(path)<len(adj_list)):
        if not visited[i - 1]:
            visited[i - 1] = True
            for a in adj_list[i]:
                if not visited[a - 1]:
                    path.append(a)
                    visit.append(a)
            visit.pop(0)
            if len(visit) > 0:
                i = visit[0]
        else:
            visit.pop(0)


    return path,visited,







print("Breadth First Seacrh: ",BFS(adj_list,visited))
# so seeing the outpur u will be quite sure that we dont need to travel every node in order to get BFS
# I only need one parent node to get the remaining child node.
