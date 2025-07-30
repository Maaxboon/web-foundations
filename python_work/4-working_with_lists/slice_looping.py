# Looping through a slice
"""
You can use a slice in a for loop if you want to loop through a subset of the elements in a list. In the next example we loop through the first three players and print their names as part of a simple roster:
"""
players = ['charles', 'martina', 'michael', 'florence', 'eli']

print("Here are the first three players of my team:")
for player in players[:3]:
    print(player.title()) # Instead of looping through the entire list of players, Python loops through only the first three names:

print("Here is the last player in my team:")
for player in players[-1:]:
    print(player.title())

print(players[-1].title() + " is the last player in my team")