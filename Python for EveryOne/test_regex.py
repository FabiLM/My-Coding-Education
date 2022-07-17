import re

s = 'ACAABAACAAAB'

result = re.findall('A{1,2}', s)
L = len(result)

print(L)
