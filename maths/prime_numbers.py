# find whether a number is prime or not.
def is_prime(n):
    if n==1:
        return False
    if n%2==0:
        return False
    if n%3==0:
        return False
    m=int(n**0.5)
    for i in range(5,m+1,6):
        if n%i==0 or n%(i+2)==0:
            return False
    return True
print(is_prime(14))

