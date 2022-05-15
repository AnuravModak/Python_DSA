#type "MODEQ" in codechef to get question and its test cases
res=[]
fin=[]
for i in range(int(input())):
    n,m=[int(x) for x in input().split()]
    b=n
    while(b>=2):
        y=m-(m%b)
        
        b-=1


# 3
# 3 5
# 3 6
# 3 10