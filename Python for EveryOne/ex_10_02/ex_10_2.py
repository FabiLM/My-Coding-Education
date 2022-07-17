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
       #print(words)
       if len(words) == 7 :
           w = words[5]
           #print(w)
           names.append(w)
#print(names)
#extractinh hours, minutes and seconds
for h in names:
    hours = h.split()
    #print(hours)
#extracting only hours
    for t in hours:
        time = t.split(':')
        #print(time)
        H = time[0]
        #print(H)
        Hour.append(H)
#print(Hour)
# creating dictionary
for n in Hour:
    counts[n] = counts.get(n,0) + 1
#print(counts)
# creating tuples from the dictionary
for n,count in counts.items():
    hord = (n,count)
    lst.append(hord)
    #print(hord)
# sorting
lst = sorted(lst)
#print(lst)
# printing counts, sorted by hour
for count,n in lst:
    print(count,n)
