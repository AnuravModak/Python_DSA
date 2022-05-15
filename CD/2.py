def validprod(left,right):
    validprodcutions=["+"]+[chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)]
    flag=0
    if left.islower() or left.isnumeric():
        flag=1
    for i in right[0]:
        if i not in validprodcutions:
            flag=1
    if flag==1:
        return False
    else:
        return True
production=(input().split("->"))
left=production[0]
right=production[1]
print(right)
count=set()
if validprod(left,right):
    for i in right[0]:
        if i.isupper():
            count.add(i)
print(len(count)," non terminals in productions ",production[0]+"->"+production[1])
