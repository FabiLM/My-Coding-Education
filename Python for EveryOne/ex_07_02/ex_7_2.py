fname = input("Enter file name: ")
# verifying files exists
try:
   fh = open(fname)
except:
    print('File cannot be opened.', fname)
    quit()
# counting number of X-DSPAM-Confidence appears
count = 0
for text in fh:
    if text.startswith('X-DSPAM-Confidence:') :
       count = count + 1
       #print(count)
# searching
fh = open(fname)
totval = 0
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        #print(line)
        number = line.find(':')
        #print(number)
        piece = line[number+2:]
        #print(piece)
        value = float(piece)
        #print(value)
        totval = totval + value
#print(totval)
avtotval = totval / count
print("Average spam confidence:",avtotval)
