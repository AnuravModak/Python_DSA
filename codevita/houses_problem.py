arr=list(map(int,input().split()))
sum1=0
for i in range(0,len(arr),2):
    sum1+=arr[i]
sum2=0
for i in range(1,len(arr),2):
    sum2+=arr[i]
print(max(sum2,sum1))

# 6 7 1 3 8 2 5