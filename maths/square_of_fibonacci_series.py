def fibonacci(n):
    if n==0:
        return 0
    F=[[1,1],[1,0]]
    power(F,n-1)
    return F[0][0]

def squares(F):
    pass

def multiply(F, M):
    x = (F[0][0] * M[0][0] +
         F[0][1] * M[1][0])
    y = (F[0][0] * M[0][1] +
         F[0][1] * M[1][1])
    z = (F[1][0] * M[0][0] +
         F[1][1] * M[1][0])
    w = (F[1][0] * M[0][1] +
         F[1][1] * M[1][1])

    F[0][0] = x
    F[0][1] = y
    F[1][0] = z
    F[1][1] = w
    # sum=1
    # sum+=x**2
    # print(x,y)
    # print(F)
    return [w**2,y**2,x**2]
# def power(F,n,res=[]):
#     if n==0 or n==1:
#         return
#     power(F,n//2,res)
#     sum=0
#
#     y=multiply(F,F)
#     res.append(y)
#     M=[[1,1],[1,0]]
#     if n%2!=0:
#         y=multiply(F,M)
#         res.append(y)
#     print(res)

def power(F,n):
    res=[]
    pes=[]
    M = [[1, 1], [1, 0]]
    while n>1:
        n=n//2
        y = multiply(F, F)

        res.append(y)
        if n % 2 != 0:
            y1 = multiply(F, M)

            res.append(y1)


    print(res)
    sum_of_squares=0
    c=0
    print(len(res))
    for i in res:
        if c%2==0:
            print(i[:2])
            sum_of_squares+=i[0]+i[1]

        elif not c%2==0 :
            print(i[1:])
            print(c)
            sum_of_squares+=sum(i[1:])

        c+=1

    print("Sum of squares:",sum_of_squares)




if __name__ == '__main__':
    print(fibonacci(9))

