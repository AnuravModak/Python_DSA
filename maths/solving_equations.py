def gcd_extended(a,b):
    if b==0:
        return 1,0,a
    x,y,gcd=gcd_extended(b,a%b)
    return y,x-(a//b)*y,gcd
def solve_eqns(x,y,c):
    a,b,c1=gcd_extended(x,y)
    constant_factor=c//(x*a+y*b)
    return constant_factor*a,constant_factor*b,c

print(solve_eqns(39,15,12))