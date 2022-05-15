def recursive_LCS(x,y,n,m):
    if n==0 or m==0:
        return 0
    elif x[n-1]==y[m-1]:
        return 1+(recursive_LCS(x,y,n-1,m-1))
    else:
        return max(recursive_LCS(x,y,n-1,m),recursive_LCS(x,y,n,m-1))

def memoization_LCS(x,y,n,m,t):
    if n==0 or m==0:
        return 0
    elif t[n][m]!=-1:
        return t[n][m]
    elif x[n-1]==y[m-1]:
        return 1+(memoization_LCS(x,y,n-1,m-1,t))
    elif not x[n-1]==y[m-1]:
        return max(memoization_LCS(x,y,n-1,m,t),memoization_LCS(x,y,n,m-1,t))

def topdown_LCS(x,y,n,m,t):
    if n==0 or m==0:
        return 0
    for i in range(1,len(x)+1):
        for j in range(1,len(y)+1):
            if x[i-1]==y[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    return t

def print_LCS(x,y,n,m,l):
    n=len(x)
    m=len(y)
    ans=[]
    t=topdown_LCS(x,y,n,m,l)
    while n>0 and m>0:
        if x[n-1]==y[m-1]:
            ans.append(x[n-1])
            n=n-1
            m=m-1
        else:
            up=t[n-1][m]
            left=t[n][m-1]
            m1=max(up,left)
            if m1==up:
                n=n-1
            else:
                m=m-1
    print(n,m)
    print(ans[::-1])




if __name__ == '__main__':
    x="abcdefrg"
    y="abcdtgh"

    # recusrive
    print(recursive_LCS(x,y,len(x),len(y)))

    # memoization
    arr=list(list())
    lis=[-1]*(len(y)+1)
    for i in range(len(x)+1):
        arr.append(list(lis))
    print(memoization_LCS(x,y,len(x),len(y),arr))


    # top-down
    t=list(list())
    lis = [-1] * (len(y) + 1)
    for i in range(len(x) + 1):
        t.append(list(lis))
    for i in range(len(x)+1):
        t[i][0]=0
    for j in range(len(y)+1):
        t[0][j]=0
    # print(topdown_LCS(x,y,len(x),len(y),t))

    print(print_LCS(x,y,len(x),len(y),t))







