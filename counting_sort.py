arr=[3, 4, 1 ]
n=len(arr)
maximum=max(arr)

def Counting_sort(a,n,k):
    b=[]
    b=a.copy()
    c=[]
    c=[0]*(k+1)
    print(c)
    for j in range(n):
        c[a[j]]=c[a[j]]+1
    print(c)
    for i in range(1,k):
        c[i]=c[i]+c[i-1]
    print(c)
    for j in range(n-1,-1,-1):
        b[c[a[j]]]=a[j]
        c[a[j]]=c[a[j]]-1
    print(c)
    return max(c)
print(Counting_sort(arr,n,maximum))

