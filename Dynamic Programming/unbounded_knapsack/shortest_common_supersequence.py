def LCS(x,y,n,m,t):
    if n==0 or m==0:
        return 0
    for i in range(1,n+1):
        for j in range(1,m+1):
            if x[i-1]==y[j-1]:
                t[i][j]=1+t[i-1][j-1]
            else:
                t[i][j]=max(t[i-1][j],t[i][j-1])
    # return t[n][m] # return this you are implementing hortest_common_sequence
    return t

def shortest_common_subsequence(x,y,n,m,t):
    return len(x)+len(y)-LCS(x,y,n,m,t)

def print_shortest_common_subsequence(x,y,n,m,t):
    k=LCS(x,y,n,m,t)
    i=n
    j=m
    ans=[]
    while i>0 and j>0:
        if x[i-1]==y[j-1]:
            ans.append(x[i-1])
            i=i-1
            j=j-1
        else:
            if t[i-1][j]>t[i][j-1]:
                ans.append(x[i-1])
                i = i - 1
            else:
                ans.append(y[j - 1])
                j = j - 1

    while i>0:
        ans.append(x[i-1])
        i-=1
    while j>0:
        ans.append(y[j-1])
        j-=1
    return ans[::-1]

if __name__ == '__main__':
    x="Geekekubj"
    y="ekekunb"
    t=[[0]*(len(y)+1) for i in range(len(x)+1)]
    print(print_shortest_common_subsequence(x,y,len(x),len(y),t))

