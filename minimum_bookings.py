# A = [ 1, 2, 3 ]
# B = [ 2, 3, 4 ]
# K=1

A = [ 17, 0, 45, 11, 16, 43, 15, 42, 2, 41, 0, 27, 37, 25, 17, 42, 24, 23, 11, 4, 29, 39, 6, 10, 42, 16, 17, 39, 1 ]
B =[ 25, 24, 52, 51, 26, 46, 25, 45, 9, 51, 49, 48, 51, 66, 65, 57, 69, 43, 50, 9, 32, 55, 10, 58, 62, 46, 19, 87, 12 ]
K = 16


# A = [ 13, 14, 36, 19, 44, 1, 45, 4, 48, 23, 32, 16, 37, 44, 47, 28, 8, 47, 4, 31, 25, 48, 49, 12, 7, 8 ]
# B = [ 28, 27, 61, 34, 73, 18, 50, 5, 86, 28, 34, 32, 75, 45, 68, 65, 35, 91, 13, 76, 60, 90, 67, 22, 51, 53 ]
# K=23
A.sort()
B.sort()
print(A)
print(B)
d=A+B
d.sort()
# METHOD-1--------------------------------
dict1={}
for i in d:
    dict1[i]=0
for i in B:
    dict1[i]-=1
for i in A:
    dict1[i]+=1
cum=[]
for i in dict1:
    cum.append(dict1[i])
print(cum)
for i in range(1,len(cum)):
    cum[i]=cum[i]+cum[i-1]
print(cum)
if max(cum)<=K:
    print(True)
else:
    print(False)
# METHOD-1--------------------------------


# METHOD-2--------------------------------
for i in range(len(A)-K):
    if B[i]>A[i+K]:
        print(False)
        break
    else:
        print(True)
        break
# METHOD-2--------------------------------