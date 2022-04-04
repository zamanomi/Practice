#Write a program to calculate gross pay. the rate is 10.5 per hour upto 40 hours.
#after fourty hours the rate is 1.5 times the original rate for each extra hour.
try :
    d = input('Enter Hours: ')
    d = float(d)
    y = input('Enter Rate/hour: ')
    y = float(y)
    def computepay(h,r) :
        if h <= 40 :
            p = h * r
            return p
        else :
            z = (h - 40) * (r * 1.5)
            p = (40 * r) + z
            return p
    print('Pay: ', computepay(d,y))
except :
    print('Invalid input, enter numeric values.')
