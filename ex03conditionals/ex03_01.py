# Exercise 1: Rewrite your pay computation to give the employee 1.5 times the hourly rate for hours worked above 40 hours.

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

hours = int(input("Enter Hours: "))
rate = int(input("Enter Rate: "))

if hours > 40:
  hr = 40
  habove = hours - hr
  pay = float(hr * rate) + (habove * rate * 1.5)
  print("Pay: " + str(pay))
else:
  pay = float(hours * rate)
  print("Pay: " + str(pay))