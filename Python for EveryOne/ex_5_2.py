largest = None
smallest = None
while True:
    val = input('Enter a number: ')
    if val =='done' :
        break
    try:
        ival = int(val)
    except:
        print('Invalid input')
        continue
    if smallest is None :
        smallest  = ival
    elif ival < smallest :
        smallest = ival
    if largest is None :
        largest = ival
    elif ival > largest:
        largest = ival

print('Maximum is', largest)
print('Minimum is', smallest)
