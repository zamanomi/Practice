fh = input('Enter file name: ')
fname = open(fh)
word = list()
ext = list()
for line in fname :
    line = line.rstrip()
    y = line.split()
    word = word + y
for i in word :
    if i in ext :
        continue
    else:
        ext.append(i)
ext.sort()
print(ext)
