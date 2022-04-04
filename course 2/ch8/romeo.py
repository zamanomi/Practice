#8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list
#of words using the split() method. The program should build a list of words. For each word on
#each line check to see if the word is already in the list and if not append it to the list.
#When the program completes, sort and print the resulting words in alphabetical order.
#You can download the sample data at
# http://www.py4e.com/code3/romeo.txt
fh = input('Enter file name: ')
fname = open(fh)
word = list()
for line in fname :
    line = line.rstrip()
    var = line.split()
    for i in var :
        if not i in word: # can make it affirmative and shift the continue coomand inside if
            word.append(i)
        else :
            continue
word.sort()
print(word)
