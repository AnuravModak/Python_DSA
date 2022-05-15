def solve(arr):
    tempL=arr[0]
    tempR=arr[-1]
    maxL=[tempL]
    maxR=[tempR]
    for  i in range(1,len(arr)):
        tempL=max(tempL,arr[i])
        maxL.append(tempL)
    for i in range(len(arr)-2,-1,-1):
        tempR=max(tempR,arr[i])
        maxR.append(tempR)

    # now lets find maximum water level at each index
    water=[]
    for i in range(len(arr)):
        water.append(min(maxR[i],maxL[i]))

    # now lets find actual water level at each index
    for i in range(len(water)):
        water[i]=abs(water[i]-arr[i])
    return sum(water)

def rain_wter_no_space(arr):
    temp_L=-99999099
    temp_R=-99999999
    m=len(arr)-1
    s=0

    for i in range(0,len(arr)):
        temp_L=max(temp_L,arr[i])
        temp_R=max(temp_R,arr[m-i])
        t=min(temp_L,temp_R)
        t=abs(t-arr[i])
        s+=t
    return s




print(solve([3,0,0,2,0,4]))
print(rain_wter_no_space([3,0,0,2,0,4,6,8,2,0]))
print(rain_wter_no_space([3,0,0,2,0,4]))

