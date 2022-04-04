#Calculator
add = 0
sub = 0
ml = 1
di = 1
while True :
    x = input('Enter the number: ')
    if x == 'done' :
        break
    try :
        x = int(x)
    except :
        print('Invalid Input.')
        continue
    add = add + x
    sub = x - sub
    ml = ml * x
    di = x / di
print('Make your choice.')
print('1-Addition')
print('2-Substraction')
print('3-Multiplication')
print('4-Division')
c = input('Enter your choice.')
try :
    c = int(c)
except :
    print('Invalid input')
if c == 1 :
    print('Addition:', add)
elif c == 2 :
    print('Substraction:', sub)
elif c == 3 :
    print('Multiplication:', ml)
elif c == 4 :
    print('Division:', di)
else :
    print('Invalid choice.')
