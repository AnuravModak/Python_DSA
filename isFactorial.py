# The factorial of a number n is defined as n! = n * (n - 1) * (n - 2) * ... * 1.
# Given a positive integer a, return n such that n! = a. If there is no integer n that is a factorial, then return -1.(Inverse factorial)
def isFactorial(n):
    i=1
    m=1
    while i<=n:
        if n%i==0:
            m=m*i
        if n%i!=0:
            if m==n:
                return i
            else:
                return -1
        if m == n:
            return i
        i = i + 1
    if m==n:
        return n
    else:
        return -1
if __name__ == '__main__':
    print(isFactorial(120))

    a = input("Enter a string: ")
    res = [a[i:j]
           for i in range(len(a))
           for j in range(i + 1, len(a) + 1)]
    print(res)
    a = list(list())
    fin = []
    for i in res:
        a.append(sorted(i))
    for i in a:
        if a.count(i) > 1:
            fin.append(i)
    # print(fin)
    f = []
    for i in res:
        if sorted(i) in fin:
            f.append(i)
    f.sort()
    print(f)


