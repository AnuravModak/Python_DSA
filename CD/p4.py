sf = (input("Enter file name: "))
cf = (input("Enter Name of file to be copied in : "))

file = open(sf,"r")
texts = file.read()
file.close()
print("sf closed!")
print()

file1 = open(cf,"w")
for s in texts:
    f1.write(s)
f1.close()
print("cf closed!")
print()

print("\nFile Copied Successfully!")