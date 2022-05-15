# Given two string or array, say s1 and s2,
# find the minimum substring in s1 where any anagram of "s2" is present
a=["t","o","m","a","t","t","s","a","t","a"]
# a=["t","o","m","a","t","t","a","a","t","a"]

# a=["t","a","t","t","s","a","t","a"]

b=["t","t","a"]
def solve(arr,b):
    dict={}
    for i in b:
        if i in dict:
            dict[i]+=1
        else:
            dict[i]=1
    dict1=dict.copy()
    count=0

    i=0
    j=0
    m=[0]*(len(a)+1)

    while j<len(arr):

        if arr[j] in dict:
            dict[arr[j]]-=1
            if dict[arr[j]]==0:
                count+=1
        if count==len(dict):
            count=sum(list(dict.values()))
            while count<0:
                i+=1
                if dict[arr[i-1]] in dict:
                    count+=1
            if len(arr[i:j + 1])<len(m):
                m=arr[i:j + 1].copy()
            i=j
            count=0
            dict=dict1.copy()
            if arr[j] in dict:
                dict[arr[j]]-=1

        j+=1
    return m

print(solve(a,b))





