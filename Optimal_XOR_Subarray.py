# Find a subarray  such that the bitwise XOR of all the numbers in the range [1,N] is maximized.
# Print any subarray of these numbers that maximize the XOR.
for i in range(1):
    # n,k=map(int,input().split())
    # arr=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
    arr=[3,7,15,10]
    for i in range(1,len(arr)+1):
        arr.append(i)
    res = []
    fin=[]
    fin1=[]
    dict={}
    for i in range(len(arr) - 1):
        u=arr[i] ^ arr[i + 1]
        maxi = max(u, arr[i + 1])
        res.append(maxi)
        if maxi not in dict:
            dict[maxi]=[arr[i],arr[i+1]]
        else:
            dict[maxi] = [arr[i], arr[i + 1]]

    max_xor = max(res)
    print(max_xor,len(res))
    print(res)
    # print(res)
    # print(fin)
    # print(dict)
    print(dict[max(dict.keys())])
    # print(15^16)
    # print(15^3)