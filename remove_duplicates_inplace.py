

a = [1,1,1,3,4,5,5,5,5,7,7,7,9,9]

def removeDuplicates( a):
    count=0
    for i in range(len(a) - 1, 0, -1):
        if a[i] == a[i - 1]:
            count+=1
            if count>1:
                del a[i]
        else:
            count=0


    return a









print(removeDuplicates(a))