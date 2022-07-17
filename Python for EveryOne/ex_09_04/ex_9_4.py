fname = input("Enter file name: ")
fh = open(fname)

counts = dict()
names = list()
bigcount = None
bigword = None

for line in fh:
    if line.startswith('From') :
       words = line.rstrip()
       words = line.split()
       if len(words) == 7 :
           w = words[1]
           names.append(w)

for n in names:
    counts[n] = counts.get(n,0) + 1

for n,count in counts.items():
    if bigcount is None or count > bigcount :
        bigcount = count
        bigword = n
        
print(bigword,bigcount)
