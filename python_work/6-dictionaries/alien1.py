# Nesting
# A List of dictionaries
"""The alien_0 dictionary contains a variety of information about one alien,but it has no room to store information about a second alien, much less a screen full of aliens. How can you manage a fleet of aliens? One way is to make a list of aliens in which each alien is a dictionary of information about that alien. For example, the following code builds a list of three aliens:
"""
# We first create three dictionaries, each representing a different alien
alien_0 = {'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points':10}
alien_2 = {'color': 'red', 'points': 15}

# we pack each of these dictionaries into a list called aliens
aliens = [alien_0, alien_1, alien_2]

# Finally, weloop through the list and print out each alien:
for alien in aliens:
    print(alien)

print("-----------------------------------------------")

"""
A more realistic example would involve more than three aliens with code that automatically generates each alien. In the following example weuse range() to create a fleet of 30 aliens:
"""
# Make an empty list for storing aliens:
aliens = []

# Make 30 green aliens
for alien_number in range(30):
    new_alien = {'color': 'green', 'points': 5, 'speed':'slow'}
    aliens.append(new_alien)

# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("-----------------------------------------------")

# Show how many aliens have been created
print(" Total number of aliens: " + str(len(aliens)))

# Changing the first three aliens to yellow, medium speed aliens, worth 10 points each
# Make an empty list of aliens:
aliens = []

# Make 30 green aliens
for alien_number in range(0,30):
    new_alien = {'color': 'green', 'speed':'slow', 'points':5}
    aliens.append(new_alien)

for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
# Show the first 5 aliens:
for alien in aliens[:5]:
    print(alien)
print("-------------------------------------------------------")