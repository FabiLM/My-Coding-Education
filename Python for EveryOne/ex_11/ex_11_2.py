import re

fname = input("Enter the file name:")
fh = open(fname)

#reading fh and extracting numbers
x = fh.read()
y = re.findall('[0-9]+',x)
#print(y)
#print(len(y))

# using REGEX
print (sum([int(value) for value in y]))
