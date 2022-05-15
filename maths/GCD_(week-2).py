def euclidean_gcd(a,b):
    if b==0:
        return a
    else:
        a1=a%b
        return euclidean_gcd(b,a1)
def lcm(a,b):
    return (a*b)//euclidean_gcd(a,b)

def fibonacci(n):
    fib=[0]*(n+1)
    fib[1]=1
    for i in range(2,n+1):
        fib[i]=fib[i-1]+fib[i-2]
    return sum(fib)

# def fibonacci_squares(n):
#     fib=fibonacci(n)
#     for i in range(len(fib)):
#         fib[i]=(fib[i]**2)%10
#     return sum(fib)%10


def fibonacci_squares(n):
    l1=0
    l2=1
    fib_sum=1
    for i in range(2,n+1):
        l=(l1 + l2)%10
        # print(l)
        fib_sum+=l
        l1=l2
        l2=l

    return (fib_sum%10)**2
def binary_search(arr,k,start,end):
    mid=(start+end)//2

    if start<=end:
        if arr[mid]==k:
            return True
        if k > arr[mid]:
            return binary_search(arr, k, mid + 1, end)
        elif k < arr[mid]:
            return binary_search(arr, k, start, mid - 1)

    else:
        return False





    




print(euclidean_gcd(28851538,1183019))
print(lcm(761457,614573))
print(fibonacci(14))
# print(fibonacci_squares(1234567890))
arr=[1,4,5,6,7,11,12,13,14,16,19,20]
print(binary_search(arr,18,0,len(arr)-1))

