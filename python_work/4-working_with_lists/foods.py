# Copying a list: 
"""
To copy a list, you can make a slice that includes theentire original list by omitting the first index and the second index ([:]). This tells Python to make a slice that starts at the first item and ends with the last item, producing a copy of the entire list.
"""
#  We make a list of the foods we like called my_foods.
my_foods = ['pizza', 'falafel', 'carrot', 'cake']

# We make a new list called friend_foods. We make a copy of my_foods by asking for a slice of my_foods without specifying any indices and store the copy in friend_foods
friend_foods = my_foods[:]

# When we print each list, we see that they both contain the same foods:
print("My favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)

# To prove that we actually have two separate lists, we’ll add a new food to each list and show that each list keeps track of the appropriate person’s favorite foods:
my_foods.append('cannoli')  #  we add 'cannoli' to my_foods
friend_foods.append('ice cream') #  we add 'ice cream' to friend_foods
print("\nMy favorite foods are:")
print(my_foods)

print("\nMy friend's favorite foods are:")
print(friend_foods)