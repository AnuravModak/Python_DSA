# cook your dish here
t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    s = str(input())
    temp_ans=[False]*k
    for i in range(k):
        if s[i]==s[i+1]:
            temp_ans[i]=True
    # print(temp_ans)
    ans_arr=[]
    count=0
    for i in temp_ans:
        if not i:
            count+=1
    a=count
    for i in range(k,n-1):
        temp=temp_ans.pop(0)
        if not temp:
            count-=1
        if s[i]!=s[i+1]:
            temp_ans.append(False)
            count+=1
        else:
            temp_ans.append(True)
        a+=count
    print(a)

# 1
# 6 3
# aabbcc