st=input("Enter a string:")
nt=[]
for i in st:
    if i.isupper() and i not in nt:
        nt.append(i)
print(nt)