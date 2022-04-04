#Exercise 3: Write a program to read through a mail log, build a histogram using a dictionary
#to count how many messages have come from each email address, and print the dictionary.
#Enter file name: mbox-short.txt
#{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
#'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
#'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
#'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
#'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
#'ray@media.berkeley.edu': 1}

fh = input('Enter file name: ')
try :
    fname = open(fh)
except :
    print('Invalid file name: ', fh)
    quit()

lst = list()
dt = dict()

for line in fname :
    line =line.rstrip()
    words = line.split()
    if len(line) < 2 : continue
    if not words[0] == 'From' : continue
    else :
        lst.append(words[1])

for i in lst :
    dt[i] = dt.get(i, 0) + 1

print(dt)
