import re
file = input("Enter file name. ")
try :
    fname = open(file)
except :
    print("Invalid file name.")
    quit()
#print(fname.read())
dt = dict()
lst = list()
for line in fname :
    line = line.lower()
    lst1 = re.findall('[a-z]', line)
    lst += lst1

for k in lst :
    dt[k] = dt.get(k, 0) + 1
for l,m in sorted(dt.items()) :
    print(l,m)
