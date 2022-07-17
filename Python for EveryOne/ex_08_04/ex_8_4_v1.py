fname = input("Enter file name: ")
fh = open(fname)

count = 0
lst = list()

for line in fh:
    count = count + 1
    word = line.split()
    lst = lst + list(word)
    lst.sort()

mylst = lst
mylst = list(dict.fromkeys(mylst))

print(mylst)
