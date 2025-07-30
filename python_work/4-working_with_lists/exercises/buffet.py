"""
4-13. Buffet: A buffet-style restaurant offers only five basic foods . Think of five simple foods, and store them in a tuple .
 •	Use a for loop to print each food the restaurant offers .
 •	Try to modify one of the items, and make sure that Python rejects the change .
 •	The restaurant changes its menu, replacing two of the items with different foods . Add a block of code that rewrites the tuple, and then use a for loop to print each of the items on the revised menu 
"""
# List of simple foods at Migingo Annex Hotel
foods = ('tripes', 'fish', 'chicken', 'beef', 'pork')

# Printing the foods using a for loop
for food in foods:
    print(food)

# Try modifying and Python should reject the change
# foods[2] = 'omena'
# print(foods) 
# Rejects reasigning the omena in the Tuple

# Rewriting the tuple to match the restaurant's changes
foods = ('tripes', 'fish', 'chicken', 'ofulu', 'omena')

# Printing the updated foods at Migingo Annex Hotel using a for loop
for food in foods:
    print(food)
