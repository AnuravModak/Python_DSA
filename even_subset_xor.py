def brian_algo(n):
    count=0
    while n:
        n=n&(n-1)
        count+=1
    return count

for _ in range(int(input())):
    n=int(input())
    count=0
    i=1
    ans=[]
    while count<n:
        c=brian_algo(i)
        if c%2==0:
            ans.append(i)
            count+=1
        i+=1
    for i in ans:
        print(i,end=" ")

