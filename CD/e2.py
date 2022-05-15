st=input("Enter a production:")
flag=0
terminals=[]
non_terminals=[]
def isOpr(ch):
    if (ch=="+" or ch=="-" or ch=="/" or ch=="*" or ch=="%"):
        return True
    return False

def isSym(ch):
    if (ch==">" or ch=="<" or ch=="(" or ch==")"):
        return True
    return False
if st[0].isupper():
    terminals.append(st[0])
    if st[1]=="-" and st[2]==">":
        for i in range(3,len(st)):
            if st[i].isalpha():
                if st[i].isupper():
                    terminals.append(st[i])
                else:
                    non_terminals.append(st[i])
            elif isSym(st[i]) or isOpr(st[i]):
                non_terminals.append(st[i])
            else:
                flag=1
                break
        if flag==1:
            print("It is not a valid Production")
        else:
            a="".join(list(set(non_terminals)))
            b="".join(list(set(terminals)))
            print("It is a valid production!")
            print("terminals are:",b)
            print("non-terminals are:",a)
    else:
        print("Invalid Peoduction:")
else:
    print("It is a not a production")