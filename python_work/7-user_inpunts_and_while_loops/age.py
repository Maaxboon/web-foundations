# Using int() to accept numerical input
"""
When you use the input() function, Python interprets everything the user 
enters as a string. Consider the following interpreter session, which asks for 
the user’s age:
"""

age = int(input("How old are you? "))
print(age)
print(type(age))
print(age >= 18)