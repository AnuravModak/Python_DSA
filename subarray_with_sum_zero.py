from collections import Counter
arr=[1, 4, -2, -2, 5, -4, 3]
prefix_sum=[]
sum=0
for i in arr:
    sum+=i
    prefix_sum.append(sum)
print(prefix_sum)
print(Counter(prefix_sum))
for i in Counter(prefix_sum):
    if Counter(prefix_sum)[i]>1 or i==0:
        print("True")
        break
