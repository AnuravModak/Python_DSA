# Time complexity:O(sqrt(n))
def primeFact(n):
    d=2
    len=0

    if n==1:
        fact=[2]
        expo=[0]
        return expo,fact
    fact = [0] * n
    expo = [0] * n

    while n>1 and d*d<=n:
        k=0
        while n%d==0:
            n=n//d
            k+=1
            # in this loop k is storing the power of that factorization for every number which is divisible....
        if k>0:
            len+=1
            fact[len]=d
            expo[len]=k
        d+=1
    # if after successive division a prime number is left then......
    # in this i have out expo[len]=1 because the number which be left will be a prime number
    if n>1:
        len+=1
        fact[len]=n
        expo[len]=1
    return expo,fact

# this function will return prime numbers and its highest power.......
# print(primeFact(60))
print(primeFact(20))
# print(primeFact(100))

