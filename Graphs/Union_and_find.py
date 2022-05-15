# edge_list=[[1,2],[2,3],[3,1]]
edge_list=[[5,6],[1,2],[3,6],[1,5],[2,3],[2,5],[4,6],[3,4]]
n=6
link=[]
for i in range(n):
    link.append(-1)
size=[1]*n

def find(x):
    if link[x-1]==-1:
        return x
    # if link[x]==-1 then it means that it is the representative node
    return find(link[x-1])
def unite(a,b):
    a1=a
    b1=b
    a=find(a)
    b=find(b)
    if a==b:
        print("Cycle detected at the edge ({},{})".format(a1,b1))
    else:
        if size[a-1]<size[b-1]:
            a,b=b,a
        size[a-1]+=size[b-1]
        link[b-1]=a
for i in edge_list:
    unite(i[0],i[1])
    print(i[0],i[1])
    print(link,size)
    print()

print("Final link: {} and size: {}".format(link,size))
print("Number of nodes in minimum spanning tree will be:",max(size))


    

