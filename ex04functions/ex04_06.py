# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime and create a function called computepay which takes two parameters (hours and rate).

# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0

def computepay(hours, rate):
  if hours > 40:
    hr = 40
    habove = hours - hr
    pay = float(hr * rate) + (habove * rate * 1.5)
    return print("Pay: " + str(pay))
  else:
    pay = float(hours * rate)
    return print("Pay: " + str(pay))

hours = int(input("Enter Hours: "))
rate = int(input("Enter Rate: "))


computepay(hours, rate)