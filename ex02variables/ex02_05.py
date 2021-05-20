# Exercise 5: Write a program which prompts the user for a Celsius tem-
# perature, convert the temperature to Fahrenheit, and print out the
# converted temperature.

celcius = input("Enter the temperature in celcius: ")

fahrenheit = int(celcius) / 5 * 9 + 32

print("Your fahrenheit temperature is: " + str(int(fahrenheit)))