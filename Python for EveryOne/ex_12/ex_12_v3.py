import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")
#print(soup)
#count = input('Enter count:')
# Retrieve all of the anchor tags
count = 0
lst = list()
tags = soup('a')
for tag in tags:
    x = tag.get('href', None)
    lst.append(x)

#print(lst)
#print("This is the last:", lst[2])
lista = list()
for count >= 0 or count < 4:
   url = lst[2]
   html = urllib.request.urlopen(url, context=ctx).read()
   soup = BeautifulSoup(html, "html.parser")
counti = 1
for tag in tags:
    x = tag.get('href', None)
    lista.append(x)
    counti = counti + 1
print(lista[2])
print(counti)

    #print('URL:', tag.get('href', None))
