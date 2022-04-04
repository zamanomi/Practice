#Exercise 2: Write a program to look for lines of the form:
#New Revision: 39772
#Extract the number from each of the lines using a regular expression
#and the findall() method. Compute the average of the numbers and
#print out the average as an integer.
#Enter file:mbox.txt
#38549
#Enter file:mbox-short.txt
#39756

import re
fh = input('Enter file name: ')
try :
    fname = open(fh)
except :
    print('Invalid file name.')
    quit()

lst = list()
for line in fname:
    line = line.rstrip()
    num = re.findall('^N.+on: ([0-9]+)' , line)
    lst = lst + num
#print(lst)
add = 0
for i in lst :
    i = int(i)
    add = add + i

print(int(add/len(lst)))
