fname = input("Enter file name: ")
fh = open(fname)
count = 0
lw = None
for line in fh:
    if line.startswith('From') :
       word = line.split()
       #print(word)
       lw = (len(word))
       if lw == 7 :
           email = word[1]
           print(email)
           count = count + 1
print("There were",count,"lines in the file with From as the first word")
