#finding how many times a character is repeating itself.

file = input("Enter file name: ")
try :
    fname= open(file)
except:
    print('Invalid file name.')
    quit()

dt = dict()
for line in fname :
    line = line.lower()
    for word in line :
        for count in word :
            dt[count] = dt.get(count, 0) + 1
#print(dt)
print("Sorted in terms of characters.")
for k,v in sorted(dt.items()) :
    print(k,v)
print("")
print("")
lst = list()
print("Sorted in terms of number of occurences.")
for p,o in dt.items() :
    lst.append((o,p))
#print(sorted(lst))
for l,m in sorted(lst):
    print(m,l)
