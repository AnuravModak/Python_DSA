for _ in range(int(input())):
    n,m=map(int, input().split())
    ar=list(map(int,input().split()))
    b=list(map(int,input().split()))
    time=0
    arr=ar.copy()
    steps=0
    c=0
    # res = []
    for i in range(len(b)):
        if  b[i]!=1:
            if arr[b[i]-1] == 1 and arr[0] == 1 and c<len(b):
                print(0,end=" ")
                c+=1
            if (not arr[b[i]-1] == 1) or (arr[0] != 1):
                steps = 0
                for a in range(b[i]-1, 0, -1):
                    steps += 1
                    if arr[a-1] == 1:
                        arr[b[i] - 1] = steps
                        break

                if arr[b[i]-1]==0 and c<len(b):
                    print(-1,end=" ")
                    c+=1
                steps = 0

                if b[i]<len(ar):
                    for a in range(b[i]+1, len(arr)+1):
                        steps += 1
                        if arr[a-1] == 2:
                            if arr[b[i] - 1] > steps:
                                arr[b[i] - 1] = steps

                if c<len(b):
                    print(arr[b[i] - 1], end=" ")
                    c +=1

                # res.append(arr[b[i]-1])
        else:
            if c==0:
                c+=1
                print(0,end=" ")
    print()






