#program to compare 2 sentences based on len of string

s1=input("Enter input string 1 : ")
print(s1)
s2=input("Enter input string 2 : ")
print(s2)
if len(s1)>len(s2):
    print("S1 is longer than S2")
else:
    print("S2 is longer than S1")