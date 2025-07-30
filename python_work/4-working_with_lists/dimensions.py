# Tuples
dimensions = (200, 50) #  We define the tuple dimensions using parentheses instead of square brackets.
# we print each element in the tuple individually, using the same syntax we’ve been using to access elements in a list:
print(dimensions[0]) # 200
print(dimensions[1]) # 50

# Let’s see what happens if we try to change one of the items in the tuple dimensions:
dimensions[0] = 250

"""
The code at u tries to change the value of the first dimension, but Python returns a type error. Basically, because we’re trying to alter a tuple, which can’t be done to that type of object, Python tells us we can’t assign a new value to an item in a tuple:
 Traceback (most recent call last):
  File "dimensions.py", line 3, in <module>
    dimensions[0] = 250
 TypeError: 'tuple' object does not support item assignment
"""