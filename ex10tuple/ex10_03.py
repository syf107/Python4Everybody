# Exercise 3: Write a program that reads a file and prints the letters
# in decreasing order of frequency. Your program should convert all the
# input to lower case and only count the letters a-z. Your program should
# not count spaces, digits, punctuation, or anything other than the letters
# a-z. Find text samples from several different languages and see how
# letter frequency varies between languages. Compare your results with
# the tables at https://wikipedia.org/wiki/Letter_frequencies.

import string
import re

try:
    name = input("Please enter your file name: ")
    fhand = open(name)
except:
    print("The file doesn't exist")
    exit()
    
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            if letter.isalpha():
                if letter not in counts:
                    counts[letter] = 1
                else:
                    counts[letter] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst:
    # atoz = re.search(r"[a-z]", key)
    # if atoz:
        print(val, key)

# Code: http://www.py4e.com/code3/count3.py
