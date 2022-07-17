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

# searching
fh = open(fname)
totval = 0
for line in fh:
    if line.startswith('X-DSPAM-Confidence:'):
        number = line.find(':')
        piece = line[number+2:]
        value = float(piece)
        totval = totval + value

avtotval = totval / count
print("Average spam confidence:",avtotval)
