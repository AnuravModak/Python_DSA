# c=input()
# symbols = {'`','~','!','@','#','$','%','^','&','*','(',')','_','-','+','=','{','[','}','}','|',
# ':',';','"','<',',','>','.','?','/'}
# arr=[]
# for i in c:
#     if i not in symbols:
#         arr.append(i)
# for i in arr:
#     print(i,end=" ")
# valid productions:
# c=input()
# sarr=c.split("->")
# # print(sarr)
# if ord(sarr[0])<=90:
#     stemp=sarr[1].split("/")
#     if len(stemp)==0:
#         print("Valid")
#     else:
#         valid=True
#         for i in stemp:
#             i.strip()
#             if len(i)==0:
#                 print("not valid")
#                 valid=False
#                 break
#         if valid:
#             print("It is a valid production")
#
#
# else:
#     print("Not valid")
# eliminate left recursion.......
# c=input()
# arr=c.split("->")
# rhs=arr[1].split("|")
# # print(rhs)
# beta=""
# ans=""
# for i in rhs:
#     if len(i)==1:
#         beta=i
# # print(beta)
# alpha=None
# ans=[]
# for i in rhs:
#     if not i.islower() :
#         if i[0]==arr[0] and len(i)!=1:
#             alpha=i[1:]
#             if "{}->{}{}'".format(arr[0],beta,arr[0]) not in ans:
#                 ans.append("{}->{}{}'".format(arr[0],beta,arr[0]))
#
#             if "{}'->{}{}|epsilon".format(arr[0],alpha,arr[0]) not in ans:
#                 ans.append("{}'->{}{}|epsilon".format(arr[0],alpha,arr[0]))
#
# for i in ans:
#     print(i)

# A->Aa|Ab|d
arr=[0,0,0,0,0,0,0]
for i in range(1,len(arr)-1):
    for j in range(i,len(arr)-1,i):
        arr[j]+=1
print(arr)