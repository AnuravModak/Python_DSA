from numpy import array

def identifier(s):
    delimiters=[",",";"," "]
    brackets=["[","]","(",")"]
    tk=0
    token=[]
    letter=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    digit=[str(i) for i in range(0,10)]
    if s[0] in letter:
        for i in range(1,len(s)):
            if s[i] in letter or s[i] in digit or s[i]=="_" or s[i] in brackets :
                tk+=1
    if tk+1==len(s):
        return True
    else: 
        return False

def select(s):
    if identifier(s):
        if "[" in s and "]" in s:
            print("array")
        elif ")" in s and "(" in s:
            print("function")
        else:
            print("variable")
    else:
        print("not a identifier")




if __name__=="__main__":
    s=input("enter string: ")
    select(s)