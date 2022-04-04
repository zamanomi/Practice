#Scraping Numbers from HTML using BeautifulSoup In this assignment you will write a Python
#program similar to http://www.py4e.com/code3/urllink2.py. The program will use urllib to read
#the HTML from the data files below, and parse the data, extracting numbers and compute the sum
#of the numbers in the file.

#We provide two files for this assignment. One is a sample file where we give you the sum for
#your testing and the other is the actual data you need to process for the assignment.

#Sample data: http://py4e-data.dr-chuck.net/comments_42.html (Sum=2553)
#Actual data: http://py4e-data.dr-chuck.net/comments_1484174.html (Sum ends with 28)
#You do not need to save these files to your folder since your program will read the data
#directly from the URL. Note: Each student will have a distinct data url for the assignment - so
#only use your own data url for analysis.

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import re
fname = urllib.request.urlopen('http://py4e-data.dr-chuck.net/comments_1479960.html').read()
#print(fname)

file = BeautifulSoup(fname, 'html.parser')
#print(file)
sum = 0
nums= file('span')
#print(nums)
for i in nums :
    i = str(i)
    x = re.findall('[0-9]+', i)
    for p in x :
        p = int(p)
        sum  = sum + p
print(sum)
