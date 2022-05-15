arr=[]
for i in range(3):
    arr.append(input())
cx=0
co=0
# print(arr)
# for i in arr:
#     print(i)
def findwincol(arr,p):
    c1=False
    c2=False
    c3=False
    if arr[0][0]==p and arr[1][0]==p and arr[2][0]==p:
        c1=True
    if arr[0][1]==p and arr[1][1]==p and arr[2][1]==p:
        c2=True
    if arr[0][2]==p and arr[1][2]==p and arr[2][2]==p:
        c3=True
    return c1 or c2 or c3

def findwindiag(arr,p):
    d1=False
    d2=False
    if arr[0][0]==p and arr[1][1]==p and arr[2][2]==p:
        d1=True
    if arr[0][2]==p and arr[1][1]==p and arr[2][0]==p:
        d1=True
    return d1 or d2
def findwinrow(arr,p):
    r1=False
    r2=False
    r3=False
    if arr[0].count(p)==3:
        r1=True
    if arr[1].count(p)==3:
        r2=True
    if arr[2].count(p)==3:
        r3=True
    return r1 or r2 or r3

for i in arr:
    cx=cx+i.count("X")
    co=co+i.count("O")
# print(cx,co)
if cx==co or cx==co+1:
    x1=findwincol(arr,"X")
    x2=findwindiag(arr,"X")
    x3=findwinrow(arr,"X")
    xwin= x1 or x2 or x3
    # print(x1,x2,x3,xwin)

    y1 = findwincol(arr, "O")
    y2 = findwindiag(arr, "O")
    y3 = findwinrow(arr, "O")
    ywin = y1 or y2 or y3
    # print(y1,y2,y3,ywin)


    if xwin and ywin:
        print("NO")
    elif xwin and not ywin:
        if cx<=co:
            print("NO")
        else:
            print("YES")
    elif ywin and not xwin:
        if cx==co+1:
            print("NO")
        else:
            print("YES")
    elif (not ywin )and (not xwin):
        if cx==co or cx==co+1:
            print("YES")
        else:
            print("NO")
    else:
        print("YES")

else:
    print("NO")

# X__
# XO_
# XOO

# X__
# XO_
# XO_

# X__
# OOO
# XX_

# XOO
# OXO
# OOX