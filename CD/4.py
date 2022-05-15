def validprod(left,multiprod):
    validprodcutions=["+","*","/","-","(",")"]+[chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)]
    flag=[0]*len(multiprod)
    if left.islower() or left.isnumeric():
        flag=1
    for right in range(len(multiprod)):
        for i in multiprod[right]:
            if i not in validprodcutions:
                flag[right]=1
    i=0
    while i<len(flag):
        if flag[i]==1:
            multiprod.pop(i)
            flag.pop(i)
            i-=1
        i+=1
    return multiprod
production=(input().split("->"))
left=production[0]
multiprod=production[1].split("|")
multiprod=validprod(left,multiprod)
print(multiprod)
print("left: ",left)
print("right: ",multiprod)
print(len(multiprod))