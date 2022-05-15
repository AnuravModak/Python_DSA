# Write a program to check the given identifier is a variable or array or function or structure.
x="[4,5,4]"
if x.isalpha():
    print("Alphabets")
elif x.isdigit():
    print("digit")
elif x.isnumeric():
    print("numeric")
elif x.isdecimal():
    print("float data")
else:
    print("Its an array")