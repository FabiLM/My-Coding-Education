fname = input('Enter the file name: ')
try:
    fhand = open(fname)
except:
    print('File cannot be opened:', fname)
    exit()
lst = list()
for line in fhand :
    word = line.split()
    for wd in word :
        if wd not in lst :
            lst.append(wd)
        else: continue
lst.sort()
print(lst)
