import re
def valid(s):
    n = len(s)
    r = re.compile('[@_!#$%^&*()<>?/\|}{~:]')
    if r.search(s) != None:
        return False
        
    if (((ord(s[0]) >= ord('a') and ord(s[0]) <= ord('z')) or (ord(s[0]) >= ord('A') and ord(s[0]) <= ord('Z')) or
          ord(s[0]) == ord('_')) == False):
        return False
    for i in range(1, n):
        if (((ord(s[i]) >= ord('a') and ord(s[i]) <= ord('z')) or (ord(s[i]) >= ord('A') and ord(s[i]) <= ord('Z')) or
             (ord(s[i]) >= ord('0') and ord(s[i]) <= ord('9')) or ord(str[i]) == ord('_')) == False):
            return False
    return True
if __name__ == "__main__" :
    s = input("Enter a string: ")
    out = valid(s)
    if out is True:
        print(s," is Valid")
    else:
        print(s," is Invalid")
