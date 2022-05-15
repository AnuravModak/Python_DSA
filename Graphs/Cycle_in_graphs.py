adj_list={1:[2,3],2:[3,4],3:[4],4:[2]}# DCG: Directed cyclic graph
# adj_list={1:[2,3],2:[3],3:[]}# DAG: Directed Acyclic graph

def DAG(adj_list,path=[],i=1):
    path=[]
    path.append(i)
    k=0
    while len(path)<=len(adj_list) and k<=len(adj_list):
        for a in adj_list[i]:
            path.append(a)
            i=a
        k+=1
    return path

path=DAG(adj_list)
print(path)
if len(path)>len(adj_list):
    print("Its not a Directed acyclic graph")
else:
    print("Its a Directed acyclic graph")



# cycle in undirected graph


# adj_list={1:[2,4],2:[1,3,4],3:[2,6],4:[1,5],5:[4],6:[3]}
# adj_list={1:[2,4],2:[1,3,5],3:[2,5],4:[1],5:[2,3]}
#
# adj_list={1:[2,4],2:[1,3,4],3:[2,6],4:[1,5],5:[4],6:[3]}
adj_list={1:[2,4],2:[1,3],3:[2,6],4:[1,5],5:[4],6:[3],7:[8],8:[7],9:[10,11],10:[11],11:[10],12:[]}
visited=[False]*len(adj_list)

adj_matrix=list(list())
lis=[]
lis=[0]*len(adj_list)
for i in range(len(adj_list)):
    adj_matrix.append(list(lis))
# print(adj_matrix)
for i in adj_list:
    for j in adj_list[i]:
        if adj_matrix[i-1][j-1]==0 and adj_matrix[j-1][i-1]==0:
            adj_matrix[i-1][j-1]=1
# print(adj_matrix)

edges=0
for i in range(len(adj_matrix)):
    for j in range(len(adj_matrix)):
        if adj_matrix[i][j]==1:
            edges+=1
print(edges)
if edges>=len(adj_list):
    print("Cycle exists")
else:
    print("Cycle doesnt exists")







# print(visited)
