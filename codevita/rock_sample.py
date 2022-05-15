n,r=[int(x) for x in input().split()]
m=list(map(int,input().split()))
m.sort()
arr=list(list())
final=[]
for ra in range(r):
    a,b=[int(x) for x in input().split()]
    arr.append([a,b])
    count=0
    for i in range(n):
        if m[i]<=b and m[i]>=a:
            count+=1
    final.append(count)


for i in final:
    print(i, end=" ")


