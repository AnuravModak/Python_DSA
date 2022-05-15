# arr1=[]
# def tic_tac_toe(arr):
#     count_X=0
#     count_O=0
#     count_empty=0
#     d_X=0
#     d_O=0
#     won_X=0
#     won_O=0
#     # counting operation
#     for i in range(3):
#         if arr[i][0]=='X':
#             count_X+=1
#         if arr[i][1]=='X':
#             count_X+=1
#         if arr[i][1]=='X':
#             count_X+=1
#
#         if arr[i][0]=='O':
#             count_O+=1
#         if arr[i][1]=='O':
#             count_O+=1
#         if arr[i][2]=='O':
#             count_O+=1
#
#         if arr[i][0]=='_':
#             count_empty+=1
#         if arr[i][1]=='_':
#             count_empty+=1
#         if arr[i][2]=='_':
#             count_empty+=1
#     # row operation
#     for i in range(2):
#         if arr[i][0]=='X' and arr[i][1]=='X' and arr[i][2]=='X':
#             won_X+=1
#         if arr[i][0]=='O' and arr[i][1]=='O' and arr[i][2]=='O':
#             won_O+=1
#
#     # column operation
#
#     for i in range(3):
#         if arr[0][i]=='O' and arr[1][i]=='O' and arr[2][i]=='O':
#             won_O+=1
#         if arr[0][i]=='X' and arr[1][i]=='X' and arr[2][i]=='X':
#             won_X+=1
#
#     # left diagonal operation
#     for i in range(3):
#         if arr[i][i]=='X':
#             d_X+=1
#         if arr[i][i]=='O':
#             d_O+=1
#     if d_X==3:
#         won_X+=1
#     if d_O==3:
#         won_O+=1
#     # print(d_X,d_O)
#     d_X=0
#     d_O=0
#     # right diagonal
#     u=0
#     for i in range(2,-1,-1):
#         # print(arr[u][i])
#         if arr[u][i]=="X":
#             d_X+=1
#         if arr[u][i]=="O":
#             d_O+=1
#         u+=1
#     if d_X == 3:
#         won_X += 1
#     if d_O == 3:
#         won_O += 1
#     # print(d_X, d_O,won_X,won_O)
#
#     # base condition
#     # print(count_X,count_O)
#     # print(won_O,won_X)
#     if count_X == count_O+1 or count_O==count_X:
#         if (won_X==1 and won_O==0) :
#             print("1")
#         if (won_O==1 and won_X==0) :
#             print("1")
#         if (won_O==0 and won_X==0) and count_empty==0:
#             print("1")
#         #_______________________________________________
#
#         if won_X>0 and won_O>0:
#             print("3")
#         if won_X>1 or won_O>1:
#             print("3")
#         #_________________________________________________
#
#         if (won_X==0 and won_O==0) and count_empty>0:
#             print("2")
#
#     else:
#         print("3")
#
# for i in range(int(input())):
#     s1=input()
#     s2 = input()
#     s3 = input()
#     row1=list(s1)
#     row2 = list(s2)
#     row3 = list(s3)
#     arr1.append(row1)
#     arr1.append(row2)
#     arr1.append(row3)
#     tic_tac_toe(arr1)
#     arr1.clear()
#     row2.clear()
#     row1.clear()
#     row3.clear()




# 1
# XOX
# XXO
# O_O


# 1
# XXX
# OOO
# ___

# 1
# XOX
# OX_
# XO_

# 1
# XXX
# OXO
# OOX

# 1
# XXX
# XOO
# XOO

# arr1=[]
# def tic_tac_toe(arr):
#     count_X=0
#     count_O=0
#     count_empty=0
#     d_X=0
#     d_O=0
#     won_X=0
#     won_O=0
#     # counting operation
#     for i in range(3):
#         for j in range(3):
#             if arr[i][j]=='X':
#                 count_X+=1
#             elif arr[i][j]=='O':
#                 count_O+=1
#             else:
#                 count_empty+=1
#
#     # column operation
#     for i in range(3):
#         if arr[0][i]==arr[1][i] and arr[2][i]==arr[1][i]:
#             if arr[0][i]=='X':
#                 won_X+=1
#             elif arr[0][i]=='O':
#                 won_O+=1
#
#     # row operation
#
#     for i in range(3):
#         if arr[i][0] == arr[i][1] and arr[i][2] == arr[i][1]:
#             if arr[i][0] == 'X':
#                 won_X += 1
#             elif arr[i][0] == 'O':
#                 won_O += 1
#
#     if arr[0][0]==arr[1][1] and arr[2][2]==arr[1][1]:
#         if arr[0][0]=='X':
#             won_X+=1
#         elif arr[0][0]=="O":
#             won_O+=1
#     if arr[0][2]==arr[1][1] and arr[2][0]==arr[1][1]:
#         if arr[1][1]=='X':
#             won_X+=1
#         elif arr[1][1]=="O":
#             won_O+=1
#     # print(count_O, count_X, count_empty)
#     # print(won_X,won_O)
#     # print(count_empty)
#
#     # conditions:
#     if (won_X==1 and won_O==1) or (count_X-count_O<0) or (count_X-count_O>1):
#         print(3)
#     elif (count_X==0 and count_O==0 and count_empty==9):
#         print(2)
#     elif won_X==1 and won_O==0 and count_X>count_O:
#         print(1)
#     elif (won_X==0 and won_O==0 and count_X==count_O):
#         print(1)
#     elif(won_X==0 and won_O==0 and count_empty==0):
#         print(1)
#     elif (won_X==0 and won_O==0 and count_empty>0):
#         print(2)
#     else:
#         print(3)
#
#
#
#
# if __name__ == '__main__':
#     for i in range(int(input())):
#         s1 = input()
#         s2 = input()
#         s3 = input()
#         row1 = list(s1)
#         row2 = list(s2)
#         row3 = list(s3)
#         arr1.append(row1)
#         arr1.append(row2)
#         arr1.append(row3)
#         tic_tac_toe(arr1)
#         arr1.clear()
#         row2.clear()
#         row1.clear()
#         row3.clear()



#
t=int(input())
for i in range(t):
    cx=0
    co=0
    n=0
    l=[]

    for i in range(3):
        tic=input()
        l.append(tic)
    print(l[1][1])
    for i in range(3):
        for j in range(3):
            if l[i][j]=='X':
                cx+=1
            elif l[i][j]=="O":
                co+=1
            else:
                n+=1
    wx=0
    wo=0
    if l[0][0]=="X" and l[0][1]=='X' and l[0][2]=='X':
        wx=1
    if l[1][0]=="X" and l[1][1]=='X' and l[1][2]=='X':
        wx=1
    if l[2][0]=="X" and l[2][1]=='X' and l[2][2]=='X':
        wx=1
    if l[0][0]=="X" and l[1][0]=='X' and l[2][0]=='X':
        wx=1
    if l[0][1]=="X" and l[1][1]=='X' and l[2][1]=='X':
        wx=1
    if l[0][2]=="X" and l[1][2]=='X' and l[2][2]=='X':
        wx=1
    if l[0][0]=="X" and l[1][1]=='X' and l[2][2]=='X':
        wx=1
    if l[0][2]=="X" and l[1][1]=='X' and l[2][0]=='X':
        wx=1

    if l[0][0]=="O" and l[0][1]=='O' and l[0][2]=='O':
        wo=1
    if l[1][0]=="O" and l[1][1]=='O' and l[1][2]=='O':
        wo=1
    if l[2][0]=="O" and l[2][1]=='O' and l[2][2]=='O':
        wo=1
    if l[0][0]=="O" and l[1][0]=='O' and l[2][0]=='O':
        wo=1
    if l[0][1]=="O" and l[1][1]=='O' and l[2][1]=='O':
        wo=1
    if l[0][2]=="O" and l[1][2]=='O' and l[2][2]=='O':
        wo=1
    if l[0][0]=="O" and l[1][1]=='O' and l[2][2]=='O':
        wo=1
    if l[0][2]=="O" and l[1][1]=='O' and l[2][0]=='O':
        wo=1

    if (wx==1 and wo==1) or (cx-co<0) or (cx-co>1):
        print(3)
    elif (cx==0 and co==0 and n==9):
        print(2)
    elif wx==1 and wo==0 and cx>co:
        print(1)
    elif (wx==0 and wo==1 and cx==co):
        print(1)
    elif(wx==0 and wo==0 and n==0):
        print(1)
    elif (wx==0 and wo==0 and n>0):
        print(2)
    else:
        print(3)
