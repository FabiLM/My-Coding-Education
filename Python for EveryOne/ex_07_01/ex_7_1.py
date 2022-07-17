fname = input("Enter the file name: ")

try:
    fh = open(fname)
except:
    print('File cannot be opened:', fname)
    quit()

ifh = fh.read()
uifh = ifh.upper()

for line in uifh:
    line = line.rstrip()
    
print(uifh)
