fname = input('Enter your file name: ')
if fname == "na na boo boo":
    print("NA NA BOO BOO TO YOU - You have been punk'd")
    quit()
try:
    fhand = open(fname)
except:
    print("The file", fname, 'cannot be opened.')
    exit()
    
count = 0
for line in fhand:
    if line.startswith("Subject:"):
        count = count + 1

print("There were", count, "subject lines in", fname)