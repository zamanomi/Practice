#7.2 Write a program that prompts for a file name, then opens that file and reads through
#the file, looking for lines of the form:
#X-DSPAM-Confidence:    0.8475
#Count these lines and extract the floating point values from each of the lines and compute
# the average of those values and produce an output as shown below. Do not use the
#sum() function or a variable named sum in your solution.
#You can download the sample data at http://www.py4e.com/code3/mbox-short.txt
#when you are testing below enter mbox-short.txt as the file name.
fn = input('Enter file name: ')
fname = open(fn)
count = 0
addi = 0
av = 0
for line in fname :
    if not 'X-DSPAM-Confidence:' in line : #if line.find('X-DSPAM-Confidence:') == -1 / you can also put affirmative condition and remove the continue command.
        continue
    count = count + 1
    pos = line.find(':')
    val = line[pos+1 :]
    val = val.lstrip()
    val = float(val)
    addi = addi + val
av = addi/count
print('Average spam confidence:', av)
