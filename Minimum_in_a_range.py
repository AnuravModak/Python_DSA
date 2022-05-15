arr=[1,3,4,8,6,7,4,2]
res=[]
def mins(arr,a,b):
    if a==b+1 or b==a+1:
        # print(1)
        return min(arr[a],arr[b])
    if a==b:
        return arr[a]
    w=(b-a+1)//2
    print(w)
    minimum=min(mins(arr,a,a+w-1),mins(arr,a+w,b))
    return minimum
print(mins(arr,2,6))

# Complexity is O(log(range))..so lets assume k=range, then O(log(k)) and log(k)=constant => O(1)
