# Exercise 2: This program counts the distribution of the hour of the day for each of the messages. You can pull the hour from the “From” line by finding the time string and then splitting that string into parts using the colon character. Once you have accumulated the counts for each hour, print out the counts, one per line, sorted by hour as shown below.

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
    time = words[5].split(":")
    hour = time[0]
    if hour not in counts:
        counts[hour] = 1
    else:
        counts[hour] += 1

# make it in tuple to be arranged
lst = list()
for hour, message in list(counts.items()):
    lst.append((hour, message))

# sorting lst
lst.sort()

# iterate to print all lst
for a, b in lst:
    print(a, b)