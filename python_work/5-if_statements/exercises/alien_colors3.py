"""
5-5. Alien Colors #3: Turn your if-else chain from Exercise 5-4 into an if-elifelse chain .
 •	If the alien is green, print a message that the player earned 5 points .
 •	If the alien is yellow, print a message that the player earned 10 points .
 •	If the alien is red, print a message that the player earned 15 points .
 •	Write three versions of this program, making sure each message is printed for the appropriate color alien 
"""
# Version one: green
alien_color = 'green'
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15

print("You have earned " + str(points) + " points for shooting a " + alien_color + " alien.")

# Version Two: yellow
alien_color = 'yellow'
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15

print("You have earned " + str(points) + " points for shooting a " + alien_color + " alien.")

# Version Three: red
alien_color = 'red'
if alien_color == 'green':
    points = 5
elif alien_color == 'yellow':
    points = 10
else:
    points = 15

print("You have earned " + str(points) + " points for shooting a " + alien_color + " alien.")