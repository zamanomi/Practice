#Write a program to prompt the user to entaer a string and a word to count in the string.
#Create a function.
def countwords(st,w):
    count = 0
    for i in st:
        if i == w:
            count = count+1
    return count
st1 = input('Enter the String: ')
w1 = input('Enter the word to count: ')
c = countwords(st1,w1)
print(w1, 'is repeated',c,'times in the string.')
