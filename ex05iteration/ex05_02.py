# Exercise 2: Write another program that prompts for a list of numbers as above and at the end prints out both the maximum and minimum of the numbers instead of the average.

# We will examine lists in more detail in a later chapter.↩︎

numberlist = []
count = 0
total = 0

while True:
    number = input("# Enter a number: ")
    if number == 'done':
        break
    try:
        new_number = int(number)
    except:
        print("# Invalid  input")
        continue
    
    count = count + 1
    total = total + new_number
    numberlist.append(new_number)

print("The total is ", total, "Amount number added are ", count)
print(f"Max number is {max(numberlist)}. The minimum number is {min(numberlist)}.")
