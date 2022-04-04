#10.2 Write a program to read through the mbox-short.txt and figure out the distribution by
#hour of the day for each of the messages. You can pull the hour out from the 'From ' line by
#finding the time and then splitting the string a second time using a colon.

#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

#Once you have accumulated the counts for each hour, print out the counts, sorted by hour as
#shown below.
fh = input('Enter file name: ')
try :
    fname = open(fh)
except :
    print('Invalid input.')
    quit()
dt = dict()
lst = list()
time = list()
srt = list()
for line in fname:
    line = line.rstrip()
    words = line.split()
    if len(words) < 2 : continue
    if not words[0] == 'From' : continue
    else :
        lst.append(words[5])
#print(lst)
for i in lst:
    p = i.find(':')
    time.append(i[:p])
#print(time)
for count in time:
    dt[count] = dt.get(count, 0) + 1
#print(dt)
srt = dt.items()
for y,k in sorted(srt):
    print(y,k)
