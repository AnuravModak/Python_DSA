def tokens(s):
    delimeters=[",",";"," ","+","-","/",")","("]
    token=[]
    c=0
    for i in range(len(s)):
        if s[i] in delimeters:
            token.append(s[c:i])
            token.append(s[i])
            c=i+1
    token.append(s[c:])
    return token

if __name__=="__main__":
    op=["+","-","/","*","++","--","%","==","!=","<",">","<=",">=","&&","||","="]
    sym=["="]
    s=input("enter the string: ")
    token=tokens(s)
    output=[]
    for i in token:
        if i in op:
            output.append("<op, "+i+" >")
        elif i in sym:
            output.append("<sym, "+i+" >")
        else:
            output.append("<id, "+i+" >")
    for i in output:
        print(i,end=" ")