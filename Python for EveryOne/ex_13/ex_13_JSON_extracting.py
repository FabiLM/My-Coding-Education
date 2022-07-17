import json
import urllib.request, urllib.parse, urllib.error
from urllib.request import urlopen
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# extracting & treating data from url
url = input('Enter-')
java = urllib.request.urlopen(url,context=ctx)
data = java.read().decode()

# creating dictionary by using json
js = json.loads(data)

# extracting & creating a list x from js
x = js['comments']

# extracting dictionary items embedded in a list
new_list = [i["count"] for i in x]


# adding the numbers
print("Sum:",sum(new_list))
