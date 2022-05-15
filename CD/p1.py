#program to read string and find all vowels and consonents

string= input("enter a string ")
#abcde
l=list(string)
lstv=[]
lstc=[]
for i in l:
  if i=='a' or i=='e' or i=='o' or i=='i' or i=='u' :
    print(i,"is a vowel")
    lstv.append(i)
  else:
    print(i,"is a consonant")
    lstc.append(i)
print(set(lstv),"are vowels in the string")
print(set(lstc),"are consonants in the string")