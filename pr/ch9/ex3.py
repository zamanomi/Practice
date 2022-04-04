#Exercise 4: Add code to the above program to figure out who has the
#most messages in the file. After all the data has been read and the dictionary has been
#created, look through the dictionary using a maximum
#loop (see Chapter 5: Maximum and minimum loops) to find who has
#the most messages and print how many messages the person has.
#Enter a file name: mbox-short.txt
#cwen@iupui.edu 5
#Enter a file name: mbox.txt
#zqian@umich.edu 195

print('A program to find the the person that sent the most of the mails.')

fh = input('Enter file name: ')

try :
    fname = open(fh)
except :
    print('File can not be opened.')
    quit()

lst = list()
dt = dict()

for line in fname :
    line = line.rstrip()
    if len(line) < 2 : continue
    words = line.split()
    if not words[0]  =='From': continue
    else :
        lst.append(words[1])

for i in lst :
    dt[i] = dt.get(i, 0) + 1

mxmc = None
mxm = None

for k,v in dt.items() :
    if mxmc is None or mxmc < v :
        mxmc = v
        mxm = k

print(mxm, mxmc)
