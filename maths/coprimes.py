def isAcoprimeB(a,b):
    if a**(b-1)%b==1:
        return True
    return False
print(isAcoprimeB(10,17))