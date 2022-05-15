# The algorithm is extremely simple:
#
# gcd(a,b)={   a       ,  if b=0
#           gcd(b,a%b), otherwise }

def recursive_gcd(a,b):
    if b==0:
        return a
    else:
        return recursive_gcd(b,a%b)

def gcd(a,b):
    while b:
        a,b=b,a%b
    return a

def gcd_array(arr):
    hf=gcd(arr[0],arr[1])
    for i in range(2,len(arr)):
        hf=gcd(hf,arr[i])
    return hf

def gcd_extended(a,b):
    if b==0:
        return 1,0,a
    x,y,g=gcd_extended(b,a%b)
    return y,x-(a//b)*y,g

print(gcd_extended(30,12))

# Least common multiple
# lcm(a,b)=a*b/gcd(a,b)
def LCM(a,b):
    return (a/gcd(a,b))*b