#Exercise 5: This program records the domain name (instead of the
#address) where the message was sent from instead of who the mail came
#from (i.e., the whole email address). At the end of the program, print
#out the contents of your dictionary.
#python schoolcount.py
#Enter a file name: mbox-short.txt
#{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
#'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

fh = input('Enter file name: ')

try :
    fname= open(fh)
except:
    print('Unexpected file name.')
    quit()

lst = list()
dt = dict()
lst1 = list()

for line in fname :
    line = line.rstrip()
    if len(line) < 2 : continue
    words = line.split()
    if not words[0] == 'From': continue
    else :
        lst.append(words[1])

for i in lst :
    pos = i.find('@')
    lst1.append(i[pos + 1 :])

for k in lst1 :
    dt[k] = dt.get(k, 0) + 1

print(dt)
