# A simple dictionary
"""
Consider a game featuring aliens that can have different colors and point values. This simple dictionary stores information about a particular alien:
"""
alien_0 = {'color' : 'green', 'points' : '5'}

print(alien_0['color'])
print(alien_0['points'])

# Working with dictionaries
"""
A dictionary in Python is a collection of key-value pairs. Each key is connected to a value, and you can use a key to access the value associated with that key. A key’s value can be a number, a string, a list, or even another dictionary. 
In fact, you can use any object that you can create in Python as a value in a dictionary.
In Python, a dictionary is wrapped in braces, {}, with a series of key-value pairs inside the braces.
A key-value pair is a set of values associated with each other. When you provide a key, Python returns the value associated with that key. Every key is connected to its value by a colon, and individual key-value pairs are separated by commas. You can store as many key-value pairs as you want in a dictionary.
The simplest dictionary has exactly one key-value pair, as shown in this modified version of the alien_0 dictionary:
alien_0 = {'color': 'green'}
"""

# Accessing values in a Dictionary
"""
To get the value associated with a key, give the name of the dictionary and then place the key inside a set of square brackets, as shown here:
alien_0 = {'color' : 'green'}
print(alien_0['color'])
"""

#  pulls the value associated with the key 'points' from the dictionary and  stores it in the variable new_points. .
new_points = alien_0['points']
print("\nYou just earned " + str(new_points) + " points!\n")

# Adding New Key-Value Pairs
"""
Dictionaries are dynamic structures, and you can add new key-value pairs to a dictionary at any time. For example, to add a new key-value pair, you would give the name of the dictionary followed by the new key in square brackets along with the new value.
"""
print(str(alien_0) + "\n")
# we add a new key-value pair to the dictionary: key 'x_position' and value 0.
alien_0['x_position'] = 0

# we add a new key-value pair to the dictionary: key 'y_position' and value 25.
alien_0['y_position'] = 25
print(alien_0)

# Starting with an Empty Dictionary
"""
It’s sometimes convenient, or even necessary, to start with an empty diction
ary and then add each new item to it. To start filling an empty dictionary, 
define a dictionary with an empty set of braces and then add each key-value 
pair on its own line. For example, here’s how to build the alien_0 dictionary 
using this approach:
"""

alien_0 = {}
# print(alien_0)
alien_0['color'] = 'red'
alien_0['points'] = 10

print("\n " + str(alien_0))

# Tracking the position of an alien that can move at different speeds
alien_2 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_2['x_position']))

# Move the alien to the right.
# Determine how far to move the alien based on its current speed.
if alien_2['speed'] == 'slow':
    x_increment = 1
elif alien_2['speed'] == 'medium':
    x_increment = 2
else:
    # This must be a fast alien
    x_increment = 3

# The new position is the old position plus the increment
alien_2['x_position'] = alien_2['x_position'] + x_increment

print("New x-position: " + str(alien_2['x_position']))

# Removing Key-Value pairs
"""
When you no longer need a piece of information that’s stored in a dictionary, you can use the del statement to completely remove a key-value pair. 
All del needs is the name of the dictionary and the key that you want to remove.
"""
# Removing key 'points' from alien_1 dictionary
alien_1 = {'color': 'green', 'points': '5'}
print(alien_1)

del alien_1['points']
print(alien_1)