# def dfs(adj_list,visited,start,path):
#     if visited[start]:
#         return
#     if adj_list[start]==0:
#         return path
#     visited[start]=True
#     path=path+[start]
#     # print(path)
#     for i in adj_list[start]:
#         # y=dfs(adj_list,visited,i,path)
#         y=dfs(adj_list,visited,i,path)
#         if y and len(y)>0:
#             print(y)
#
#
#     return path
def dfs(adj_list,visited,start):
    if visited[start]:
        return
    visited[start]=True
    print(start,end=" ")
    for i in adj_list[start]:
        dfs(adj_list,visited,i)

if __name__ == '__main__':
    routes=[
        [1,3],
        [3,2],
        [3,4],
        [2,8],
        [5,6],
        [6,7],
        [7,5],
        [7,7]

    ]
    # routes=[
    #     [1,3],
    #     [3,4],
    #     [4,5],
    #     [5,2],
    #     [2,1]
    # ]
    visited={}
    for i in routes:
        visited[i[0]]=False
        visited[i[1]] = False
    # print(visited)

    adj_list={}
    for i in visited:
        adj_list[i]=[]
    for i in routes:
        adj_list[i[0]].append(i[1])
    print(adj_list)
    for i in adj_list:
        if not visited[i]:
            dfs(adj_list,visited,i)



