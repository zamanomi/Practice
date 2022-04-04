# Exercise 1: Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.
def chop(t) :
    del t[0]
    del t[-1]

lst =''
def middle(s) :
    del s[0]
    del s[-1]
    return s
ss = [1,2,3,4,5,6,7,8,9]
ss1 = [1,2,3,4,5,6,7,8,9]
print(chop(ss1))
print(middle(ss))
