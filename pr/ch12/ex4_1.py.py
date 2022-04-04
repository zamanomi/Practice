import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

#url = input('Enter - ')
#url = 'https://docs.python.org'
url = 'http://py4e-data.dr-chuck.net/comments_1484174.html'
html = urllib.request.urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, 'html.parser')


# Retrieve all of the anchor tags
tags = soup('p')
count = 0
for tag in tags:
    count += 1
print(count)
