def square_free_nos(n):
    if n%2==0:
        n=n//2
    if n%2==0:
        return False
    m=int(n**0.5)
    for i in range(3,m+1):
        if n%i==0:
            n=n//i
        if n%i==0:
            return False
    return True
print(square_free_nos(20))