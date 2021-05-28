# Exercise 3: Write a program to read through a mail log, build a his-
# togram using a dictionary to count how many messages have come from
# each email address, and print the dictionary.
# Enter file name: mbox-short.txt
# {'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
# 'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
# 'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
# 'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
# 'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
# 'ray@media.berkeley.edu': 1}

try:
    name = input("Please input your file name: ")
    handle = open(name)
except:
    print("Your name file does not exist")
    exit()


counts = dict()
for line in handle:
    splitted_line = line.split()
    if len(splitted_line) == 0 or splitted_line[0] != "From": continue
    email = splitted_line[1]
    counts[email] = counts.get(email, 0) + 1

print(counts)