edge_list=[[5,6],[1,2],[3,6],[1,5],[2,3],[2,5],[4,6],[3,4]]
#  this is an edge list arranged in increasing order of their weights....
n=6
link=[]
for i in range(n):
    link.append(-1)
size=[1]*n
visited=[False]*n

minimum_spanning_tree=[]

def find(x):
    if link[x-1]==-1:
        return x
    return find(link[x-1])

def unite(a,b):
    a1=a
    b1=b
    a=find(a)
    b=find(b)
    if not a==b:
        if size[a - 1] < size[b - 1]:
            a, b = b, a
        size[a - 1] += size[b - 1]
        link[b - 1] = a
        if not visited[a-1]:
            minimum_spanning_tree.append(a)
            visited[a-1]=True
        if not visited[b-1]:
            minimum_spanning_tree.append(b)
            visited[b-1]=True
for i in edge_list:
    unite(i[0],i[1])
print(minimum_spanning_tree)




