#Exercise 2: Rewrite your pay program using try and except so that your
#program handles non-numeric input gracefully by printing a message
#and exiting the program. The following shows two executions of the
#program:
#Enter Hours: 20
#Enter Rate: nine
#Error, please enter numeric input
#Enter Hours: forty
#Error, please enter numeric input
hr = input('Enter hours: ')
ra = input('Enter rate/hour: ')
pay = 1
try:
    hr = float(hr)
    ra = float(ra)
    if hr <= 40 :
        pay = hr * ra
    else :
        pay = ((hr - 40) * (ra * 1.5)) + (40 * ra)
    print('Pay:', pay)
except:
    print('Error, one of the inputs is a non numeric value.')
