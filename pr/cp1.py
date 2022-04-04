hr = input('Enter hours: ')
try :
    hr = float(hr)
except :
    print('Error, hour is a non numeric value.')
    quit()
ra = input('Enter rate/hour: ')
try :
    ra = float(ra)
except :
    print('Error, rate is a non numeric value.')
    quit()
pay = 1
hr = float(hr)
ra = float(ra)
if hr <= 40 :
    pay = hr * ra
else :
    pay = ((hr - 40) * (ra * 1.5)) + (40 * ra)
print('Pay:', pay)
