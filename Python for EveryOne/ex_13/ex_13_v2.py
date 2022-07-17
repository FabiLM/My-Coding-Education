import xml.etree.ElementTree as ET
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter-')
xml = urllib.request.urlopen(url,context=ctx)

lst = list()
data = xml.read()
print("Retrieved",len(data),"characters")
#print(data.decode())
tree = ET.fromstring(data)
lst = tree.findall('comments/comment')
print('Comment count:',len(lst))

soma = 0
count = 0
for item in lst:
    #print('Name',item.find('name').text)
    x = item.find('count').text
    #print(x)
    ix = int(x)
    #print(ix)
    soma = soma + ix
    count = count + 1
print('Soma',soma)
