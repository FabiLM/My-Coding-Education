def computepay():
    try:
        fhr = float(hr)
        frt = float(rt)
    except:
        print("Error, it need to be a number.")
    if fhr > 40:
        Rt = frt * 1.5
        pay = 40 * frt + (fhr - 40)* Rt
        return pay
    else :
        pay = fhr * frt
        return pay
hr = input("Enter Hours: ")
rt = input("Enter rate: ")
p = computepay()
print("Pay", p)
