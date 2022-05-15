def a_power_b(a,b):
    if b==0:
        return 0
    else:
        res=1
        while(b>0):
            if b&1:
                res=res*a
            a=a*a
            b>>=1
        return res


# Effective computation of large exponents modulo a number
def Modulo_a_power_b(a,b,m):
    if b==0:
        return 1
    else:
        res=1
        while(b>0):
            if b&1:
                res=(res*a)%m
            a=(a*a)%m
            b>>=1
        return res




print( a_power_b(2,13))
print(Modulo_a_power_b(2,33,100000))



