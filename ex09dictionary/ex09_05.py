# Exercise 5: This program records the domain name (instead of the
# address) where the message was sent from instead of who the mail came
# from (i.e., the whole email address). At the end of the program, print
# out the contents of your dictionary.
# python schoolcount.py
# Enter a file name: mbox-short.txt
# {'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
# 'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

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
    email = splitted_line[1].split('@')[1]
    counts[email] = counts.get(email, 0) + 1

print(counts)