#Exercise 1: Write a program which repeatedly reads numbers until the
#user enters “done”. Once “done” is entered, print out the total, count,
#and average of the numbers. If the user enters anything other than a
#number, detect their mistake using try and except and print an error
#message and skip to the next number.
#5.9. EXERCISES 65
#Enter a number: 4
#Enter a number: 5
#Enter a number: bad data
#Invalid input
#Enter a number: 7
#Enter a number: done
#16 3 5.333333333333333
ad = 0
co = 0
av = 0
while True :
    x = input('Enter the number: ')
    if x == 'done' or x == 'DONE' or x == 'Done' :
        break
    try :
        x = int(x)
    except :
        print('Invalid input')
        print('Only numeric values are accepted.')
        continue
    ad = ad + x
    co = co + 1
    av = ad / co
print('Number of input:', co)
print('Addition of the numbers:', ad)
print('Average:', av)
print('Thank you')
