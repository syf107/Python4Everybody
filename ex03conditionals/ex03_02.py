# Exercise 2: Rewrite your pay program using try and except so that your program handles non-numeric input gracefully by printing a message and exiting the program. The following shows two executions of the program:

# Enter Hours: 20
# Enter Rate: nine
# Error, please enter numeric input

# Enter Hours: forty
# Error, please enter numeric input

try:
  hours = input("Enter Hours: ")
  int_hr = int(hours)
  rate = input("Enter Rate: ")
  int_rate = int(rate)
except:
  print("Error, Please enter numeric input")
  quit()