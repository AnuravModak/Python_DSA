for i in range(int(input())):
    # x,y,n=[int(x) for x in input().split()]
    x=int(input())
    y=int(input())

    n=int(input())

    if y==0:
        print(1%n)
    if x==0:
        print("0")
    else:
        res=1
        while(y>0):
            if (y&1):
                res=(res*x)%n
            x=(x*x)%n
            y>>=1
        print(res)




