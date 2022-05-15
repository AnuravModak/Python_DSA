def validprod(left,right):
    validprodcutions=["+","/","-","*"]+[chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)]
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
# taking production input
production=(input().split("->"))
# storing valid terminals
validterminals=[chr(i) for i in range(97,123)]
l=production[0]
r=production[1]
print(r)

# declaring set to have unique values
count=set()
if validprod(l,r):
    for i in r[0]:
        if i in validterminals:
            count.add(i)
            print(count)
print(len(count)," terminals in productions rae given as follows ",production[0]+"->"+production[1])