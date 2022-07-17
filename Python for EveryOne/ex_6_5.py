text = "X-DSPAM-Confidence:    0.8475"

number = text.find('0.8475')
print(number)

nb = text[number:]
fnb = float(nb)

print(fnb)
