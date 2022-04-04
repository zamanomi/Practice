#Exercise 1: Revise a previous program as follows: Read and parse the
#“From” lines and pull out the addresses from the line. Count the number of messages from
#each person using a dictionary.
#After all the data has been read, print the person with the most commits
#by creating a list of (count, email) tuples from the dictionary. Then
#sort the list in reverse order and print out the person who has the most
#commits.

#Sample Line:
#From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008
#Enter a file name: mbox-short.txt
#cwen@iupui.edu 5
#Enter a file name: mbox.txt
#zqian@umich.edu 195

fh = input('Enter file name: ')

try:
    fname = open(fh)
except:
    print('Invalid file name.')
    quit()

lst = list()
lst1 = list()
lst2 = list()
dt = dict()

for line in fname :
    line = line.rstrip()
    if len(line) < 2 : continue
    words = line.split()
    if not words[0] == 'From' : continue
    else :
        lst.append(words[1])

for i in lst :
    dt[i] = dt.get(i, 0) + 1

for email,count in dt.items() :
    lst1.append((count, email))

lst1.sort(reverse=True)

for k,v in lst1 :
    lst2.append((v,k))

print(lst2[0])
