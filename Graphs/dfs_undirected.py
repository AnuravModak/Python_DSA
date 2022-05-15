def dfs(adj_list,visited,parent=-1):
    for i in visited:
        visited[i]=0

    def traversal(start,prev):
        visited[start]=True
        for i in adj_list[start]:
            if not visited[i]:
                y=traversal(i,start)
                if y:
                    return y
            elif i!=prev:
                return True
        return False
    for i in adj_list:
        if not visited[i]:
            y=traversal(i,-1)
            if y:
                return y
    return False












if __name__ == '__main__':

    routes = [
        [1, 3],
        [3, 2],
        [3, 4],
        [2, 8],
        [5, 6],

        [7, 5]

    ]
    # routes=[
    #     [1,3],
    #     [3,4],
    #     [4,5],
    #     [5,2],
    #     [2,1]
    # ]
    visited = {}
    for i in routes:
        visited[i[0]] = False
        visited[i[1]] = False
    # print(visited)

    adj_list = {}
    for i in visited:
        adj_list[i] = []
    for i in routes:
        adj_list[i[0]].append(i[1])
        adj_list[i[1]].append(i[0])
    print(adj_list)

    print(dfs(adj_list,visited))
