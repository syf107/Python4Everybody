# Exercise 1: Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.

def chop(li):
    li.pop(0)
    li.pop(-1)

def middle(li):
    return li [1:-1]


eusian = [1, 2, 3, 4, 5, 6]
print(chop(eusian))
print(middle(eusian))