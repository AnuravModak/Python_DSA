edge_list=list(list())
n,m=map(int,input().split())
for i in range(m):
    a,b,w=map(int,input().split())
    edge_list.append([a-1,b-1,w])
start=int(input("Enter the starting point: "))
def bellman_Ford_shortetst_path(edge_list,m,start=0):
    dist=[9999999]*n
    dist[start-1]=0
    for i in range(0,m-1):
        a=edge_list[i][0]
        b=edge_list[i][1]
        w=edge_list[i][2]
        dist[b]=min(dist[b],dist[a]+w)

    a=edge_list[m-1][0]
    b=edge_list[m-1][1]
    w=edge_list[m-1][2]
    c=min(dist[b],dist[a]+w)
    dist[b]=min(dist[b],dist[a]+w)
    if  c==dist[a]+w:
        print("Negative cycle exist")
    else:
        print("Negative cycle doesnt exist")
    return dist

# def check_negative_cycle(edge_list,n,start=0):
#     dist=bellman_Ford_shortetst_path(edge_list,n,start)
#





print(bellman_Ford_shortetst_path(edge_list,m,start))




# 4 5
# 2 4 1
# 1 3 5
# 1 2 3
# 2 3 2
# 3 4 -7