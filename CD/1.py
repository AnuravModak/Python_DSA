production=(input().split("->"))
validprodcutions=["+"]+[chr(i) for i in range(65,91)]+[chr(i) for i in range(97,123)]
left=production[0]
right=production[1:]
flag=0
if left.islower() or left.isnumeric():
    flag=1
for i in right[0]:
    if i not in validprodcutions:
        flag=1
if flag==1:
    print("Not valid")
else:
    print("valid")