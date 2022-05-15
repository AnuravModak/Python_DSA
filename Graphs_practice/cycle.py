def iscyclic():
    visited

if __name__ == '__main__':
    # routes=[
    #     [1,3],
    #     [3, 2],
    #     [3,4],
    #     [5,6],
    #     [6,7],
    #     [7, 5]
    #
    #
    #
    # ]
    routes=[
        [5, 3],
        [3 ,1],
        [ 1 ,2],
        [2 ,4],
        [4 ,0]
    ]
    # routes = [
    #     [1, 3],
    #     [3, 2],
    #     [3, 4],
    #     [5, 6],
    #     [6, 7]
    #
    # ]
    visited={}
    adj_list={}
    for i in routes:
        visited[i[0]]=0
        adj_list[i[0]]=[]
        for j in i:
            visited[j]=0
            adj_list[j] = []
    print("visited:",visited)
    for i in routes:
        adj_list[i[0]].append(i[1])

    print("adj_list:",adj_list)
    print(iscyclic(6,adj_list))




