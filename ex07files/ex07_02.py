# Exercise 2: Write a program to prompt for a file name, and then read
# through the file and look for lines of the form:
# X-DSPAM-Confidence: 0.8475
# When you encounter a line that starts with “X-DSPAM-Confidence:”
# pull apart the line to extract the floating-point number on the line.
# Count these lines and then compute the total of the spam confidence
# values from these lines. When you reach the end of the file, print out
# the average spam confidence.
# 90 CHAPTER 7. FILES
# Enter the file name: mbox.txt
# Average spam confidence: 0.894128046745
# Enter the file name: mbox-short.txt
# Average spam confidence: 0.750718518519
# Test your file on the mbox.txt and mbox-short.txt files.

# ask the file name
fname = input('Enter your file name: ')

# put the file name into variable
fhand = open(fname)

# make the variable for total number and count.
total = 0
count = 0
length = len("X-DSPAM-Confidence:") + 2

# iterate each line in the file name
for line in fhand:
    
    # if the file start with “X-DSPAM-Confidence:”, 
    if line.startswith("X-DSPAM-Confidence:"):
        
        # get the number, change it into int.
        value = float(line[length:])
        
        # put the number into total variable and count.
        total = total + value
        count = count + 1

print("Average spam confidence:", total/count)