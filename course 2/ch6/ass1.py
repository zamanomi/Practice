#Exercise 5: Take the following Python code that stores a string:
#str = 'X-DSPAM-Confidence:0.8475'
#Use find and string slicing to extract the portion of the string after the
#colon character and then use the float function to convert the extracted
#string into a floating point number.
x = 'X-DSPAM-Confidence:  0.8475'
pos = x.find(':')
y = x[pos+1:]
y = y.lstrip()
f = float(y)
print(f)
