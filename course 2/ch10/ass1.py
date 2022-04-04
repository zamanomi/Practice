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
print(sorted([(x,y) for k,v in dt.items()]))
