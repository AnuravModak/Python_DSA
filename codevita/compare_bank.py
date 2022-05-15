n=int(input())
tenure=int(input())
bank=[0]*2
for i in range(2):

    s=0
    for j in range(int(input())):
        time,roi=[float(x) for x in input().split()]
        yy=(1+roi)**(time*12)
        y=1/yy
        emi=(n*roi)/(1-1/(y))
        s+=emi
    bank[i]=s
if bank[0]<bank[1]:
    print("Bank A")
else:
    print("Bank B")




