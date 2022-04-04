#Write a program to prompt the user to enter numeric values to find the biggest and the
#smallest number. The program must stop and display the result as soon as the user enters 'done'/'Done'/'DONE'
#'Invalid input.' this message must be displayed if the user enters undesirable input.
mx = None
mn = None
while True :
    x = input('Enter the Number: ')
    if x == 'done' or x == 'DONE' or x == 'Done' :
        break
    try :
        x = int(x)
    except :
        print('Invalid input.')
        print('Enter a numeric value like 15, 25, 10, 3,etc.')
        continue
    if mx is None or mx < x :
        mx = x
    elif mn is None or mn > x :
        mn = x
print('Maximum number is:', mx)
print('Minimum number is:', mn)
