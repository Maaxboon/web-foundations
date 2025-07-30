# Tuples
dimensions = (200, 50) #  We define the tuple dimensions using parentheses instead of square brackets.
# we print each element in the tuple individually, using the same syntax we’ve been using to access elements in a list:
print(dimensions[0]) # 200
print(dimensions[1]) # 50

# Let’s see what happens if we try to change one of the items in the tuple dimensions:
# dimensions[0] = 250

"""
The code at u tries to change the value of the first dimension, but Python returns a type error. Basically, because we’re trying to alter a tuple, which can’t be done to that type of object, Python tells us we can’t assign a new value to an item in a tuple:
 Traceback (most recent call last):
  File "dimensions.py", line 3, in <module>
    dimensions[0] = 250
 TypeError: 'tuple' object does not support item assignment
"""

# Looping Through All Values in a Tuple: You can loop over all the values in a tuple using a for loop, just as you did with a list:
for dimension in dimensions:
    print(dimension) # Python returns all the elements in the tuple, just as it would for a list:

# Writing over a Tuples
"""
Although you can’t modify a tuple, you can assign a new value to a variable that holds a tuple. So if we wanted to change our dimensions, we could redefine the entire tuple:
"""

#  This block defines the original tuple and prints the initial dimensions
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

#  we store a new tuple in the variable dimensions.
dimensions = (400, 100)

# We then print the new dimensions at w. Python doesn’t raise any errors this time, because overwriting a variable is valid:
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

"""
Note: When compared with lists, tuples are simple data structures. Use them when you want to store a set of values that should not be changed throughout the life of a program.
"""
