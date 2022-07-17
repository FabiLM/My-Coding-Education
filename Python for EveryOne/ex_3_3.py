r = input("Enter range: ")
try:
   fr = float(r)
except:
    print("ops, need to be a number")
if fr < 0 :
    print("Error")
    quit()
if fr > 1 :
    print("Error")
    quit()
elif fr >=  0.9 :
    print("Grade: A ")
elif fr >= 0.8 :
    print("Grade: B")
elif fr >= 0.7 :
    print("Grade: C")
elif fr >= 0.6 :
    print("Grade: D")
elif fr < 0.6 :
    print("Grade: F")
