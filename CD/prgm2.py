def constant(s):
    digit=[str(i) for i in range(0,10)]
    decimal=0
    tk=0
    if s[0] in digit:
        for i in range(1,len(s)):
            if s[i] in digit :
                tk+=1
            elif s[i]=="." and decimal==0:
                decimal=1
                tk+=1
            else:
                break
    if tk+1==len(s):
        print(s," is a constant")
    else:
        print(s," is not a constant")

if __name__ == "__main__" :
    s = input("Enter input: ")
    constant(s)