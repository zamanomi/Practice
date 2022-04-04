#9.4 Write a program to read through the mbox-short.txt and figure out who has sent the
#greatest number of mail messages. The program looks for 'From ' lines and takes the second
#word of those lines as the person who sent the mail. The program creates a Python dictionary
#that maps the sender's mail address to a count of the number of times they appear in the file.
#After the dictionary is produced, the program reads through the dictionary using a maximum
#loop to find the most prolific committer.

# OUTPUT-: cwen@iupui.edu 5

fh = input('Enter file name: ')
fname = open(fh)
st = list()
dnr = dict()
for line in fname:
    line = line.rstrip()
    words = line.split()
    #print(words)
    if len(words) < 2 : continue
    if words[0] == 'From' :
        #print(words)
        st.append(words[1])
for email in st:
    dnr[email] = dnr.get(email,0) + 1
bigname = None
bigcount = None
for key,val in dnr.items():
    if bigcount is None or bigcount < val:
        bigcount = val
        bigname = key
print(bigname, bigcount)
