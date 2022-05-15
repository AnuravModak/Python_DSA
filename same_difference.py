# You are given an array a of n integers. Count the number of pairs of in
# dices (i,j) such that i<j and aj−ai=j−i.for _ in range(int(input())):
for _ in range(int(input())):
    n=int(input())
    l=list(map(int,input().split()))
    ans=0
    d=dict()
    res=[]
    count=0
    for i in range(n):
        tem=l[i]-i

        if tem>=0:
            res.append(tem)
            if d.get(tem) == None:
                d[tem] = 1
                count += 1

            else:
                d[tem] += 1
                count += 1

    print(d)
    print(count)
    print(res)
#     print(res)


# 1
# 3
# 1 2 3