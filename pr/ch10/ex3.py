#Exercise 3: Write a program that reads a file and prints the letters
#in decreasing order of frequency. Your program should convert all the
#input to lower case and only count the letters a-z. Your program should
#not count spaces, digits, punctuation, or anything other than the letters
#a-z. Find text samples from several different languages and see how
#letter frequency varies between languages. Compare your results with
#the tables at https://wikipedia.org/wiki/Letter_frequencies.

import string
fn = 'I want to be an engineer\\@ currently I am a student'
fn = fn.translate(str.maketrans('','',string.punctuation))
fn = fn.lower()
lst = fn.split()
lst1 = list()
dt = dict()

for i in lst :
    dt[i] = dt.get(i, 0) + 1

for k,v in dt.items() :
    lst1.append((v,k))

for x,y in sorted(lst1, reverse=True) :
    print(y , x)
