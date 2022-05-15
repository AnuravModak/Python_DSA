arr=["a","b","a","a","a","b","b","a","a","a","b","a","a","b","a"]

def count_anagram(s1,s2):
    i=0
    j=len(s2)-1
    dict={}
    dict1={}
    for i1 in s2:
        if i1 not in dict:
            dict[i1]=1
        else:
            dict[i1]+=1
    res=[]
    dict1=dict.copy()

    while j<(len(s1)):
        for a in s1[i:j+1]:
            if a in dict:
                if dict[a]>0:
                    dict[a]-=1
                else:
                    break
            else:
                break

        s=sum(list(dict.values()))
        if s==0:
            res.append(s1[i:j+1])
        i += 1
        j += 1
        dict=dict1.copy()
    return res

print(count_anagram(arr,["a","b","a","b"]))











