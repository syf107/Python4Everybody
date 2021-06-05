# Exercise 2: Write a program to look for lines of the form:

# New Revision: 39772

# Extract the number from each of the lines using a regular expression and the findall() method. Compute the average of the numbers and print out the average as an integer.

# Enter file:mbox.txt
# 38549

# Enter file:mbox-short.txt
# 39756

import re

filename = input("Enter file: ")
hand = open(filename)

amount = 0
total = 0

for line in hand:
    line = line.rstrip()
    x = re.findall("^New [A-Za-z]+: ([0-9]+)", line)
    if len(x) > 0:
        amount += 1
        total += int(x[0])

print(total//amount)