fname = input("Enter file name: ")
fh = open(fname)

counts = dict()
names = list()
Hour = list()
lst = list()
for line in fh:
    if line.startswith('From') :
       words = line.rstrip()
       words = line.split()

       if len(words) == 7 :
           w = words[5]
           names.append(w)

#extractinh hours, minutes and seconds
for h in names:
    hours = h.split()

#extracting only hours
    for t in hours:
        time = t.split(':')
        H = time[0]
        Hour.append(H)

# creating dictionary
for n in Hour:
    counts[n] = counts.get(n,0) + 1

# creating tuples from the dictionary
for n,count in counts.items():
    hord = (n,count)
    lst.append(hord)

# sorting
lst = sorted(lst)

# printing counts, sorted by hour
for count,n in lst:
    print(count,n)
