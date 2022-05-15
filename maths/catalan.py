def catalan_recursive(n):
    if n<=1:
        return 1
    res=0
    for i in range(n):
        res+= catalan_recursive(n)*catalan_recursive(n-i-1)
    return res

def catalan_DP(n):
    arr=[]
    arr.append(1)
    arr.append(1)
    for i in range(2,n+1):
        arr.append(0)
        for j in range(i):
            arr[i]+=arr[j]*arr[i-j-1]
    return arr[n]
def binomialCoefficient(n,r):
    if r>n-r:
        r=n-r
    res=1
    for i in  range(r):
        res=res*(n-i)
        res=res/(i+1)
    return res

def catalan(n):
    c=binomialCoefficient(2*n,n)
    return c/(n+1)

for i in range(int(input("Enter value of n:"))):
    print(int(catalan(i)))

