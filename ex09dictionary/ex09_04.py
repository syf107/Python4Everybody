# Exercise 4: Add code to the above program to figure out who has the
# most messages in the file. After all the data has been read and the dic-
# tionary has been created, look through the dictionary using a maximum
# loop (see Chapter 5: Maximum and minimum loops) to find who has
# the most messages and print how many messages the person has.
# Enter a file name: mbox-short.txt
# cwen@iupui.edu 5
# Enter a file name: mbox.txt
# zqian@umich.edu 195

# try the name of file.
try:
    name = input("Please input your file name: ")
    handle = open(name)

# if the file doesn't exist, exit.
except:
    print("Your name file does not exist")
    exit()


# create a variable for email.
counts = dict()

# iteration for each line in text file.
for line in handle:
    splitted_line = line.split()
    if len(splitted_line) == 0 or splitted_line[0] != "From": continue
    email = splitted_line[1]
    counts[email] = counts.get(email, 0) + 1

biggest_email = None
biggest_number = None

for key in counts:
    if biggest_number == None or counts[key] > biggest_number:
        biggest_email = key
        biggest_number = counts[key]

print(biggest_email, biggest_number)