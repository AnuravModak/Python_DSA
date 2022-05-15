def BFS(adj_list,visited):
    stack=[]


    def traversal(start):
        if visited[start]:
            return
        visited[start]=True
        print(start,end=" ")

    for io in adj_list:
        stack.append(io)
        while len(stack) > 0:
            i = stack.pop(0)
            if not visited[i]:
                print(i, end=" ")
                visited[i] = True
            for j in adj_list[i]:
                if not visited[j]:
                    traversal(j)
                    stack.append(j)




def iscyclic(adj_list,visited):


if __name__ == '__main__':
    routes=[
        [1,3],
        [3,2],
        [3,4],
        [2,8],
        [5,6],
        [6,7],
        [7,5],
        [1,9],
        [9,10]
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
    BFS(adj_list,visited)
