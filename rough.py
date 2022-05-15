def maximizeArray( arr1, arr2, n):
    arr3 = arr1 + arr2
    arr3 = list(dict.fromkeys(arr3))
    arr3.sort(reverse=True)
    temp = {}
    for i in range(n):
        temp[arr3[i]] = 0
    for i in range(len(arr2)):
        if arr2[i] in temp and temp[arr2[i]]==0:
            temp[arr2[i]] = i+1
    print(arr3)
    r_temp={}
    for i in temp:
        if temp[i]>0:
            r_temp[i]=temp[i]
    r_temp = sorted(r_temp.items(), key=lambda x: x[1])
    # print(r_temp)
    ans=[]
    for i in r_temp:
        ans.append(i[0])
    # print(ans)
    r_temp.clear()
    r_temp={}
    # print(temp)
    for i in range(len(arr1)):
        if arr1[i] in temp and temp[arr1[i]]==0:
            temp[arr1[i]]+=1
            r_temp[arr1[i]]=i+1
    r_temp=sorted(r_temp.items(),key=lambda x:x[1])
    # print(r_temp)
    for i in r_temp:
        ans.append(i[0])
    return ans



print(maximizeArray([8 ,8 ,4, 3, 1 ,4 ,9],[2, 0, 6, 8, 9 ,2, 6],7))