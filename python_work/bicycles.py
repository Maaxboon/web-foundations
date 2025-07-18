# Accessing elements in a list
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles[0]) # prints the first item

print(bicycles[0].title()) # using string methods on a list: capitalizes Trek

# Index Positions Start at 0, Not 1
"""
Python considers the first item in a list to be at position 0, not position 1.
The second item in a list has an index of 1. Using this simple counting system, you can get any element you want from a list by subtracting one from its position in the list. For instance, to access the fourth item in a list, you request the item at index 3.
"""
# The following asks for the bicycles at index 1 and index 3:

#  This code returns the second and fourth bicycles in the list:
print(bicycles[1]) # cannondale
print(bicycles[3]) # specialized

# Python has a special syntax for accessing the last element in a list. By asking for the item at index -1, Python always returns the last item in the list:

print(bicycles[-1]) #specialized

# Using individual values from a list
message = "My first bicycle was a " + bicycles[0].title() + "."
print(message) # My first bicycle was a Trek.