def binary_search(arr,k):
    n=len(arr)
    start=0
    end=n-1
    while  start<end:
        mid=(start+end)//2
        if arr[mid]==k:
            return arr[mid]
        if arr[mid]<k:
            end=mid-1
        if arr[mid]>k:
            start=mid+1
    return -1

if __name__ == '__main__':
    numbers = {0:["zero",2],1: ["one", 2], 2: ["two", 1], 3: ["three", 2], 4: ["four", 2], 5: ["five", 2], 6: ["six", 1],
               7: ["seven", 2],
               8: ["eight", 2], 9: ["nine", 2], 10: ["ten", 1], 11: ["eleven", 3], 12: ["twelve"], 13: ["thirteen", 3],
               14: ["fourteen", 4],
               15: ["fifteen", 3], 16: ["sixteen", 3], 17: ["seventeen", 3], 18: ["eighteen", 4], 19: ["nineteen", 4],
               20: ["twenty", 1],
               30: ["thirty", 1], 40: ["forty", 1], 50: ["fifty", 1], 60: ["sixty", 1], 70: ["seventy", 2],
               80: ["eighty", 2], 90: ["ninety", 2],
               100: ["hundred", 2]}

    n=int(input())
    arr=list(map(int,input().split()))
    count_vowel = 0
    for i in arr:
        j=str(i)
        if len(j)==1:
            count_vowel+=numbers[i][1]
        elif i%10==0:
            count_vowel+=numbers[i][1]
        else:
            if i>10 and i<=19 and len(j)==2:
                count_vowel+=numbers[i][1]
            elif len(j)==2:
                num1=int(j[0])*10
                num2=int(j[1])
                count_vowel+=numbers[num1][1]
                count_vowel+=numbers[num2][1]
    print(count_vowel)
    count_pairs=0
    if count_vowel>100:
        print("greater 100")
    else:

        #now we will use hashmap to do it in constant time
        hash_map={}
        for i in range(len(arr)):
            t=count_vowel-arr[i]
            if t in hash_map:
                count_pairs+=1

            # storing index...in ur dictionary...

            hash_map[arr[i]]=i

        if count_pairs==0:
            print("zero")
        elif count_pairs>0 and count_vowel<=9:
            print(numbers[count_pairs][0])
        elif count_pairs>9 and count_vowel<=19:
            print(numbers[count_pairs][0])
        elif count_pairs%10==0:
            print(numbers[count_pairs][0])
        else:
            j=str(count_pairs)
            num1 = int(j[0]) * 10
            num2 = int(j[1])
            space=" "
            s=numbers[num1][0]+space+numbers[num2][0]
            print(s)


























