n,k=[int(x) for x in input().split()]
factors=[]
for i in range(2,n):
    if n%i==0:
        factors.append(i)
    if len(factors)==k:
        break
# print(factors)
if len(factors)>k :
    print(factors[k])
if len(factors)==k:
    print(factors[len(factors)-1])

if len(factors)<k:
    print(1)





