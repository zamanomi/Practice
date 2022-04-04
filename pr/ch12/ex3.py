#Exercise 3: Use urllib to replicate the previous exercise of (1) retrieving
#the document from a URL, (2) displaying up to 3000 characters, and
#(3) counting the overall number of characters in the document. Don’t
#worry about the headers for this exercise, simply show the first 3000
#characters of the document contents

import urllib.request, urllib.parse, urllib.error
file = urllib.request.urlopen('http://data.pr4e.org/intro-short.txt')

length = 0
for line in file :
    if length >= 3000 : break
    length += len(line.decode())
    print(line.decode())
print(length)
