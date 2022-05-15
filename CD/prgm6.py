def tokens(s):
    delimeters=[",",";"," ","+","-","/",")","(","="]
    token=[]
    c=0
    for i in range(len(s)):
        if s[i] in delimeters:
            # print(i)
            token.append(s[c:i])
            token.append(s[i])
            c=i+1
    token.append(s[c:])
    print(token)
if  __name__ == '__main__':
    s=tokens(input("enter string: "))