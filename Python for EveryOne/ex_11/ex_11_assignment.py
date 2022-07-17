import re

fname = input("Enter the file name:")
fh = open(fname)

#reading fh and extracting numbers
x = fh.read()
y = re.findall('[0-9]+',x)

#converting string in intenger and adding
soma = 0
for num in y:
    inum = int(num)
    soma = soma + inum
print(soma)
