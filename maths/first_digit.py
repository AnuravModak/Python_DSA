# here we will look how to find first digit and also number if digits....
import math
i=int(input())
x=int(math.log(i,10))
print(x+1,"is the number of digits you have entered")
f=i/math.pow(10,x)
print(int(f))