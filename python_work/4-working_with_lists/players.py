# Slicing a List
"""
To make a slice, you specify the index of the first and last elements you want to work with.The following example involves a list of players on a team:
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']

"""The code prints a slice of this list, which includes just the first three players. The output retains the structure of the list and includes the first three players in the list:"""
print(players[0:3])

"""
You can generate any subset of a list. For example, if you want the second, third, and fourth items in a list, you would start the slice at index 1 and end at index 4:
"""
print(players[1:4]) #  This time the slice starts with 'martina' and ends with 'florence':

# If you omit the first index in a slice, Python automatically starts your slice at the beginning of the list:
print(players[:4]) # Without a starting index, Python starts at the beginning of the list:

"""
A similar syntax works if you want a slice that includes the end of a list. For example, if you want all items from the third item through the last item, you can start with index 2 and omit the second index:
"""
print(players[2:]) # Python returns all items from the third item through the end of the list:

"""
This syntax allows you to output all of the elements from any point in your list to the end regardless of the length of the list. Recall that a negative index returns an element a certain distance from the end of a list; 
therefore, you can output any slice from the end of a list. For example, if we want to output the last three players on the roster, we can use the slice players[-3:]:
"""
print(players[-3:]) # This prints the names of the last three players and would continue to work as the list of players changes in size.
