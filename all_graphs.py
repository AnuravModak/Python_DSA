class graph:
    def __init__(self,edges):
        self.edges=edges
        self.graph_dict={}
        for i in edges:
            if i[0] in self.graph_dict:
                self.graph_dict[i[0]].append(i[1])
            else:
                self.graph_dict[i[0]] = [i[1]]

    def get_paths(self,start,end,path=[]):
        path=path+[start]
        if start==end:
            return [path]
        if start not in self.graph_dict:
            return []
        local_path=[]
        for i in self.graph_dict[start]:
            if i not in path:
                new_paths = self.get_paths(i, end, path)
                if new_paths:
                    for i1 in new_paths:
                        local_path.append(i1)

        return local_path


    def isCyclic(self):
        keys = self.graph_dict.keys()
        visited = {}
        for i in keys:
            for j in i:
                visited[j]=Fla
                z
        def traversal(start,path=[]):
            if visited[start]:
                return True
            path=path+[start]
            visited[start]=True
            for i in self.graph_dict[start]:
                y=traversal(i,path)
                if y:
                    return True
            return False


        print(traversal(list(keys)[0]))



    def shortest_path(self,start,end,path=[]):

        # method-1

        # m=self.get_paths(start,end)
        # print(m)
        # mini=len(m[0])
        # ans=m[0]
        # for i in range(len(m)):
        #     if min(mini,len(m[i]))!=mini:
        #         mini=min(mini,len(m[i]))
        #         ans=m[i]
        # return ans


        path=path+[start]
        if start==end:
            return path
        if start not in self.graph_dict:
            return None
        shortest_path=None
        for i in self.graph_dict[start]:
            new_paths=self.shortest_path(i,end,path)
            if new_paths:
                if shortest_path is None or len(new_paths)<len(shortest_path):
                    shortest_path=new_paths.copy()
        return shortest_path




























if __name__ == '__main__':
    routes=[
        ("mumbai","paris"),
        ("mumbai","dubai"),
        ("paris","new york"),
        ("dubai","new york"),
        ("new york","toronto"),
        ("paris","dubai")
    ]
    # so first step is to make adjacency list
    adj_list={}
    for i in routes:
        if i[0] in adj_list:
            adj_list[i[0]].append(i[1])
        else:
            adj_list[i[0]]=[i[1]]
    # print(adj_list)
    # g1=graph(routes)
    #
    #
    # print(g1.get_paths("mumbai","new york"))
    # print(g1.shortest_path("mumbai","new york"))


    # part-2 : Iscyclic

    routes_1=[
        [1,3],

        [3,4]
    ]

    g2=graph(routes_1)
    print(g2.graph_dict)
    g2.isCyclic()