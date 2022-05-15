def is_prime(n):
    primes=[True]*(n+1)


    i=2
    while i*i<=n:
        if primes[i]:
            for a in range(i*i,n+1,i):
                primes[a]=False
        i+=1

    return primes
def check_prime(n):
    if n==2:
        return True
    if n==3:
        return True
    if n%2==0 or n%3==0:
        return False
    m=int(n**0.5)
    i=n

    for n in range(5,m+1,6):
        if i%n==0 or i%(n+2)==0:
            return False
    return True

def consecutive_prime_sum(n):
    y=is_prime(n)
    ts=[]
    for i in range(2,n+1):
        if y[i]:
            ts.append(i)
    print(ts)
    tes=ts.copy()
    # partial sum
    for i in range(1,len(ts)):
        if ts[i]<=n:
            ts[i]=ts[i]+ts[i-1]
    print(ts)
    ans=[]
    for i in ts:
        if i>2 and i<=n and check_prime(i):
            ans.append(i)
    return ans


print(consecutive_prime_sum(20))
# for i in range(1,100):
#     print(i,check_prime(i))


