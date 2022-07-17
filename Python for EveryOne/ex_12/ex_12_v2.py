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
count = input('Enter count:')
# Retrieve all of the anchor tags

lst = list()
tags = soup('a')
for tag in tags:
    x = tag.get('href', None)
    lst.append(x)
#print(lst)
print("Enter this URL:", lst[17])
