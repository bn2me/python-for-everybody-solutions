"""
Exercise  11.2: Write a program to look for lines of the form

'New Revision: 39771'

and extract the number from each of the lines using a regular expression and
the findall() method. Compute the average of the numbers and print out the
average.

Enter file:mbox.txt
38549.7949721

Enter file:mbox-short.txt
39756.9259259

Python for Everybody: Exploring Data Using Python 3
by Charles R. Severance

Solution by Jamison Lahman, June 4, 2017
"""
import re

fh = input('Enter File: ')
try:
    fhand = open(fh)
except:
    print('This file could not be opened, please try again.')
    exit()

sum = 0
count = 0
for line in fhand:
    line = line.rstrip()
    numbers = re.findall('^New Revision: ([0-9]+)', line) # for each valid number found, each one is added to the new list of 'numbers'
    for number in numbers:
        value = int(number)
        sum += value
        count += 1

average = sum / count
print(int(average))
