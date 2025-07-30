# A simple if statement
cars = ['audi', 'bmw', 'subaru', 'toyota']
for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())


# Conditional Tests: 
"""
This is an expression that can be evaluated as True or False. This is the heart of every if statement. Python uses the values True and False to decide whether the code in an if statement should be executed. If a conditional test evaluates to True, Python executes the code following the if statement. If the test evaluates to False, Python ignores the code following the if statement.
"""

# Checking for equality: 
"""
This checks whether the value of a variable is equal to the value of interest. 
>>> car = 'bmw' : sets the value of car to 'bmw' using a single equal sign
>>> car == 'bmw' :  checks whether the value of car is 'bmw' using a double equal sign (==). This equality operator returns True if the values on the left and right side of the operator match, and False if they don’t match. 
True: The values in this example match, so Python returns True.

>>> car = 'audi': Sets the value of car to 'audi'
>>> car == 'bmw': checks whether the value of car is 'audi'
False: The values is this example don't match, so Python returns False
"""

# Ignoring Case When Checking for Equality
"""
Testing for equality is case sensitive in Python. For example, two values with different capitalization are not considered equal:
>>> car = 'Audi'
>>> car == 'audi'
False

If case matters, this behavior is advantageous. But if case doesn’t matter and instead you just want to test the value of a variable, you can convert the 
variable’s value to lowercase before doing the comparison:
>>> car = 'Audi'
>>> car.lower() == 'audi'
True

This test would return True no matter how the value 'Audi' is formatted because the test is now case insensitive. The lower() function doesn’t change 
the value that was originally stored in car, so you can do this kind of comparison without affecting the original variable:
>>> car
'Audi'
"""
