adj_matrix=list(list())
lis=[]
n,m=map(int,input().split())
lis=[0]*n
for i in range(n):
    adj_matrix.append(list(lis))
# print(adj_matrix)

for i in range(m):
    a,b,w=map(int,input().split())
    if adj_matrix[a-1][b-1]==0:
        adj_matrix[a-1][b-1]=w
    if adj_matrix[b-1][a-1]==0:
        adj_matrix[b-1][a-1]=w

start=int(input("Enter starting point"))

def dijkstra_shortest_path(adj_matrix,start,n):
    dist=[9999999999]*n
    visited=[False]*n
    dist[start-1]=0
    k=0
    for i in range(0,n):
        k=0
        if i==0 and (start-1)!=0:
            i=start-1
            k+=1
        if i==start-1 and (start-1)!=0 and k==0:
            i=0
        for j in range(0,n):
            if adj_matrix[i][j]>0:
                if dist[i]+adj_matrix[i][j]<=dist[j]:
                    dist[j]=dist[i]+adj_matrix[i][j]

        visited[i]=True
    print(dist,visited)

dijkstra_shortest_path(adj_matrix,start,n)



#
# 5 6
# 1 5 1
# 1 4 9
# 5 4 2
# 1 2 5
# 2 3 2
# 3 4 2

# 5 6
# 1 5 1
# 1 4 9
# 5 4 2
# 1 2 5
# 2 3 2
# 3 4 6










