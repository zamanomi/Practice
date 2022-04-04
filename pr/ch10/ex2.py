#Exercise 2: This program counts the distribution of the hour of the day
#for each of the messages. You can pull the hour from the “From” line
#by finding the time string and then splitting that string into parts using
#the colon character. Once you have accumulated the counts for each
#hour, print out the counts, one per line, sorted by hour as shown below.
#python timeofday.py

#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008

#Enter a file name: mbox-short.txt
#04 3
#06 1
#07 1
#09 2
#10 3
#11 6
#14 1
#15 2
#16 4
#17 2
#18 1
#19 1

fh = input('Enter file name: ')

try:
    fname = open(fh)
except:
    print('Invalid file name.')
    quit()

lst = list()
dt = dict()

for line in fname :
    line = line.rstrip()
    if len(line) < 2 : continue
    words = line.split()
    if not words[0] == 'From' : continue
    else :
        word = words[5]
        x = word.find(':')
        lst.append(word[:x])

for i in lst :
    dt[i] = dt.get(i, 0) + 1

for k,v in sorted(dt.items()) :
    print(k,v)
