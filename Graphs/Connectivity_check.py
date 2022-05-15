adj_list={1:[2,4],2:[1,3],3:[2,6],4:[1,5],5:[4],6:[3],7:[8],8:[7],9:[10,11],10:[11],11:[10],12:[]}
# adj_list={1:[2,4],2:[5,3],3:[2,6],4:[1],5:[2,6],6:[5,3]}
# adj_list={1:[2,4],2:[1,3,4],3:[2,6],4:[1,5],5:[4],6:[3]}
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

def Components_in_graph(adj_list,visited,comp=[]):
    for i in range(len(visited)):
        if not visited[i]:
            p,visited=dfs(adj_list,visited,[],i+1)
            comp.append(p)
    print("Components are: ",comp)



# print("Depth First Search: ",dfs(adj_list,visited))

p,v=dfs(adj_list,visited)
# print(p,v)
if len(p)==len(adj_list):
    print("Connected")
else:
    print("Not connected")
    comp = []
    comp.append(p)
    Components_in_graph(adj_list, visited, comp)
    print("Number of Components present is: ",len(comp))



























