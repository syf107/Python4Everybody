# Exercise 1: Revise a previous program as follows: Read and parse the “From” lines and pull out the addresses from the line. Count the number of messages from each person using a dictionary.

# After all the data has been read, print the person with the most commits by creating a list of (count, email) tuples from the dictionary. Then sort the list in reverse order and print out the person who has the most commits.


try:
    name = input("Please enter your file name: ")
    fhand = open(name)
except:
    print("The file doesn't exist")
    exit()

counts = dict()
for line in fhand:
    words = line.split()
    if len(words) == 0 or words[0] != "From": continue
    word = words[1]
    if word not in counts:
        counts[word] = 1
    else:
        counts[word] += 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

amount, email = lst[0]

print(email, amount)